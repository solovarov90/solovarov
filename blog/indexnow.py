#!/usr/bin/env python3
"""IndexNow: сообщить Яндексу и Bing о новых и обновлённых страницах.

Запускать ПОСЛЕ `git push`, когда сайт уже обновился (Netlify выкладывает за ~1 минуту):
    python blog/indexnow.py            # отправить URL, которых ещё не было в blog/indexnow_state.json
    python blog/indexnow.py --all      # отправить все URL из sitemap.xml
    python blog/indexnow.py --dry-run  # показать, что ушло бы, ничего не отправлять
    python blog/indexnow.py URL [URL…] # отправить конкретные адреса

Ключ лежит в корне сайта файлом <ключ>.txt (его содержимое равно имени файла без .txt),
так требует протокол: https://www.indexnow.org/documentation. Файл создаётся при первом запуске
и должен быть закоммичен и выложен до отправки, иначе поисковики ответят 403/422.
"""
from __future__ import annotations

import json
import re
import secrets
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://petrsolovarov.ru"
HOST = "petrsolovarov.ru"
STATE = ROOT / "blog" / "indexnow_state.json"
ENDPOINTS = ["https://yandex.com/indexnow", "https://www.bing.com/indexnow"]


def load_key() -> str:
    for p in ROOT.glob("*.txt"):
        key = p.stem
        if re.fullmatch(r"[a-f0-9]{32}", key) and p.read_text(encoding="utf-8").strip() == key:
            return key
    key = secrets.token_hex(16)
    (ROOT / f"{key}.txt").write_text(key, encoding="utf-8", newline="\n")
    print(f"создал ключ-файл {key}.txt в корне сайта: закоммить и выложи его до первой отправки")
    return key


def sitemap_urls() -> list[str]:
    xml = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    return re.findall(r"<loc>(.*?)</loc>", xml)


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"submitted": {}}


def submit(urls: list[str], key: str, dry: bool) -> bool:
    payload = {"host": HOST, "key": key, "keyLocation": f"{SITE}/{key}.txt", "urlList": urls}
    ok = True
    for ep in ENDPOINTS:
        if dry:
            print(f"[dry-run] POST {ep}: {len(urls)} URL")
            continue
        req = urllib.request.Request(ep, data=json.dumps(payload).encode("utf-8"),
                                     headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"{ep}: HTTP {r.status} (200/202 = принято)")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            print(f"{ep}: HTTP {e.code} {body}")
            ok = ok and e.code in (200, 202)
        except Exception as e:  # сеть
            print(f"{ep}: ошибка {e}")
            ok = False
    return ok


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    send_all = "--all" in argv
    explicit = [a for a in argv if a.startswith("http")]
    key = load_key()
    state = load_state()
    all_urls = sitemap_urls()
    if explicit:
        urls = explicit
    elif send_all:
        urls = all_urls
    else:
        import datetime as dt
        lastmod = dict(re.findall(r"<loc>(.*?)</loc><lastmod>(.*?)</lastmod>", (ROOT / "sitemap.xml").read_text(encoding="utf-8")))
        urls = [u for u in all_urls if state["submitted"].get(u) != lastmod.get(u)]
    if not urls:
        print("новых или обновлённых URL нет")
        return 0
    print("отправляю:\n  " + "\n  ".join(urls))
    if submit(urls, key, dry) and not dry:
        lastmod = dict(re.findall(r"<loc>(.*?)</loc><lastmod>(.*?)</lastmod>", (ROOT / "sitemap.xml").read_text(encoding="utf-8")))
        for u in urls:
            state["submitted"][u] = lastmod.get(u, "")
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
        print(f"записал состояние в {STATE.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
