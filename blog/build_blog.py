#!/usr/bin/env python3
"""Сборка блога petrsolovarov.ru из Markdown.

Запуск из корня репозитория или из blog/:  python blog/build_blog.py

Что делает:
  blog/content/*.md  ->  blog/<slug>/index.html   (статья по шаблону blog/template.html)
                     ->  blog/index.html          (лента с рубриками)
                     ->  blog/rss.xml
                     ->  sitemap.xml, robots.txt, llms.txt  (в корне сайта)
                     ->  блок «Последние статьи» на главной index.html (между маркерами BLOG:START / BLOG:END)

Frontmatter статьи (YAML-подмножество, парсится без внешних библиотек):
  title, description, slug, date, updated, cluster, type, cover, cover_alt,
  faq (список q/a), sources (список title/url), cta (одно предложение для блока «Как подключить»),
  draft: true  — статья собирается, но не попадает в ленту, sitemap, RSS и на главную.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

import markdown
from markdown.extensions.toc import TocExtension

ROOT = Path(__file__).resolve().parent.parent      # корень репозитория = корень сайта
BLOG = ROOT / "blog"
CONTENT = BLOG / "content"
TEMPLATE = BLOG / "template.html"
HOME = ROOT / "index.html"

SITE = "https://petrsolovarov.ru"
SITE_NAME = "Пётр Соловаров"
AUTHOR = {
    "name": "Пётр Соловаров",
    "url": SITE + "/",
    "image": SITE + "/photo_2025-10-16_22-35-32.jpg",
    "jobTitle": "Внедряю ИИ в бизнес: конвейеры контента, автоответы, базы знаний",
    "sameAs": ["https://t.me/solovarov", "https://t.me/solovarovp", "https://www.instagram.com/ii.systema/"],
}
TELEGRAM = "https://t.me/solovarov"
CHANNEL = "https://t.me/solovarovp"

# Кейсы: попадают в sitemap и в блок «Читать кейсы» под статьёй.
CASES = [
    {"url": "/iisystema/", "title": "Кейс ii.systema: медиа-конвейер на ИИ", "note": "44 ролика за 14 дней, 170 942 просмотра, воронка по кодовому слову"},
    {"url": "/vetctschool/", "title": "Кейс VetCTschool: голосовой чеклист для ветеринарных радиологов", "note": "4 622 заключения КТ стали проверяемой базой знаний"},
]

RU_MONTHS = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]

# ---------------------------------------------------------------- frontmatter

def _scalar(v: str):
    v = v.strip()
    if v == "" or v == "~" or v == "null":
        return None
    if v.lower() in ("true", "yes"):
        return True
    if v.lower() in ("false", "no"):
        return False
    if (v[0] == v[-1]) and v[0] in "\"'" and len(v) >= 2:
        return v[1:-1].replace('\\"', '"')
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [_scalar(x) for x in inner.split(",")] if inner else []
    return v


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Минимальный YAML: ключ: значение; списки `- ` из скаляров или из пар ключ: значение."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("frontmatter не закрыт")
    block = text[3:end].strip("\n").splitlines()
    body = text[end + 4:].lstrip("\n")
    meta: dict = {}
    key = None
    i = 0
    while i < len(block):
        line = block[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if not line.startswith((" ", "\t", "-")):
            k, _, v = line.partition(":")
            key = k.strip()
            v = v.strip()
            if v == "" or v == "|" or v == ">":
                if v in ("|", ">"):
                    lines = []
                    i += 1
                    while i < len(block) and (block[i].startswith("  ") or not block[i].strip()):
                        lines.append(block[i][2:] if block[i].startswith("  ") else "")
                        i += 1
                    meta[key] = ("\n" if v == "|" else " ").join(lines).strip()
                    continue
                meta[key] = None  # список или вложенность следом
            else:
                meta[key] = _scalar(v)
            i += 1
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            if not isinstance(meta.get(key), list):
                meta[key] = []
            item_text = stripped[2:]
            if ":" in item_text and not item_text.startswith(("\"", "'", "http")):
                item: dict = {}
                k, _, v = item_text.partition(":")
                item[k.strip()] = _scalar(v)
                indent = len(line) - len(line.lstrip())
                i += 1
                while i < len(block):
                    nxt = block[i]
                    ind = len(nxt) - len(nxt.lstrip())
                    if not nxt.strip() or ind <= indent or nxt.strip().startswith("- "):
                        break
                    k, _, v = nxt.strip().partition(":")
                    item[k.strip()] = _scalar(v)
                    i += 1
                meta[key].append(item)
                continue
            meta[key].append(_scalar(item_text))
        i += 1
    return meta, body


# ---------------------------------------------------------------- helpers

TRANSLIT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i", "й": "y",
    "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
    "х": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}


def slugify(value: str, separator: str = "-") -> str:
    value = value.lower()
    value = "".join(TRANSLIT.get(ch, ch) for ch in value)
    value = re.sub(r"[^a-z0-9]+", separator, value).strip(separator)
    return value[:60] or "section"


def ru_date(iso: str) -> str:
    d = dt.date.fromisoformat(str(iso))
    return f"{d.day} {RU_MONTHS[d.month - 1]} {d.year}"


def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)


def word_count(md_body: str, meta: dict) -> int:
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", md_body)
    text = re.sub(r"[#*`>|_\-\[\]()]", " ", text)
    for item in meta.get("faq") or []:
        text += " " + str(item.get("q", "")) + " " + str(item.get("a", ""))
    return len(re.findall(r"[А-Яа-яЁёA-Za-z0-9]+(?:[-’'][А-Яа-яЁёA-Za-z0-9]+)*", text))


def render(template: str, ctx: dict) -> str:
    def sub(m):
        key = m.group(1)
        if key not in ctx:
            raise KeyError(f"в шаблоне нет значения для {{{{{key}}}}}")
        return str(ctx[key])
    return re.sub(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}", sub, template)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"  записал {path.relative_to(ROOT).as_posix()}")


# ---------------------------------------------------------------- markdown

def md_to_html(body: str) -> tuple[str, list[tuple[str, str]]]:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html",
                    TocExtension(slugify=slugify, toc_depth="2-3", marker="")],
        output_format="html5",
    )
    out = md.convert(body)
    toc = [(t["id"], t["name"]) for t in md.toc_tokens]  # только H2
    out = figures(out)
    out = re.sub(r"<table>", '<div class="tablewrap"><table class="fix">', out)
    out = out.replace("</table>", "</table></div>")
    return out, toc


def figures(out: str) -> str:
    """<p><img ... title="подпись"></p> -> figure с рамкой и подписью, как в кейсах."""
    def repl(m):
        img = m.group(1)
        title = re.search(r'\stitle="([^"]*)"', img)
        caption = title.group(1) if title else ""
        img = re.sub(r'\stitle="[^"]*"', "", img)
        if "loading=" not in img:
            img = img.replace("<img ", '<img loading="lazy" decoding="async" ')
        cap = f"<figcaption>{caption}</figcaption>" if caption else ""
        return f'<figure class="shot"><div class="frame"><div class="bar"><i></i><i></i><i></i></div>{img}</div>{cap}</figure>'
    return re.sub(r"<p>(<img [^>]*>)</p>", repl, out)


# ---------------------------------------------------------------- articles

def load_articles() -> list[dict]:
    articles = []
    for path in sorted(CONTENT.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        for req in ("title", "description", "slug", "date", "cluster", "type"):
            if not meta.get(req):
                raise SystemExit(f"{path.name}: во frontmatter нет поля {req}")
        meta.setdefault("updated", meta["date"])
        meta.setdefault("faq", [])
        meta.setdefault("sources", [])
        meta.setdefault("cover", f"/blog/{meta['slug']}/img/cover.jpg")
        meta.setdefault("cover_alt", meta["title"])
        meta.setdefault("cta", "")
        meta.setdefault("draft", False)
        meta["url"] = f"/blog/{meta['slug']}/"
        meta["abs_url"] = SITE + meta["url"]
        meta["abs_cover"] = SITE + meta["cover"] if str(meta["cover"]).startswith("/") else meta["cover"]
        meta["body_md"] = body
        meta["words"] = word_count(body, meta)
        meta["minutes"] = max(1, round(meta["words"] / 180))
        meta["images"] = len(re.findall(r"!\[", body)) + 1  # + обложка
        meta["source_file"] = path
        articles.append(meta)
    articles.sort(key=lambda a: (str(a["date"]), a["slug"]), reverse=True)
    return articles


def json_ld(article: dict, faq_html_present: bool) -> str:
    person = {"@type": "Person", "@id": SITE + "/#person", **AUTHOR}
    graph = [
        {
            "@type": "Article",
            "@id": article["abs_url"] + "#article",
            "mainEntityOfPage": {"@type": "WebPage", "@id": article["abs_url"]},
            "headline": article["title"],
            "description": article["description"],
            "image": [article["abs_cover"]],
            "datePublished": str(article["date"]),
            "dateModified": str(article["updated"]),
            "inLanguage": "ru-RU",
            "wordCount": article["words"],
            "articleSection": article["cluster"],
            "author": {"@id": SITE + "/#person"},
            "publisher": {"@id": SITE + "/#person"},
            "isPartOf": {"@type": "Blog", "@id": SITE + "/blog/#blog", "name": "Блог Петра Соловарова"},
        },
        person,
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Главная", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Блог", "item": SITE + "/blog/"},
                {"@type": "ListItem", "position": 3, "name": article["title"], "item": article["abs_url"]},
            ],
        },
    ]
    if faq_html_present:
        graph.append({
            "@type": "FAQPage",
            "@id": article["abs_url"] + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
                for q in article["faq"]
            ],
        })
    data = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")


def build_article(article: dict, template: str, all_articles: list[dict]) -> None:
    body_html, toc = md_to_html(article["body_md"])

    toc_html = ""
    if toc:
        items = "".join(f'<li><a href="#{esc(i)}">{esc(n)}</a></li>' for i, n in toc)
        toc_html = f'<nav class="toc" aria-label="Оглавление"><div class="toc-t">В статье</div><ol>{items}</ol></nav>'

    faq_html = ""
    if article["faq"]:
        qs = "".join(
            f'<div class="qa"><h3 id="faq-{k}">{esc(q["q"])}</h3><p>{esc(q["a"])}</p></div>'
            for k, q in enumerate(article["faq"], 1)
        )
        faq_html = f'<section class="faq" id="faq"><h2>Частые вопросы</h2>{qs}</section>'

    sources_html = ""
    if article["sources"]:
        li = "".join(
            f'<li><a href="{esc(s["url"])}" rel="noopener">{esc(s["title"])}</a>' + (f' <span>{esc(s["note"])}</span>' if s.get("note") else "") + "</li>"
            for s in article["sources"]
        )
        sources_html = f'<section class="sources" id="sources"><h2>Источники</h2><ul>{li}</ul></section>'

    related = [a for a in all_articles if a["slug"] != article["slug"] and not a["draft"]][:3]
    related_html = ""
    if related:
        li = "".join(f'<li><a href="{esc(a["url"])}">{esc(a["title"])}</a><span>{esc(a["cluster"])} · {ru_date(a["date"])}</span></li>' for a in related)
        related_html = f'<section class="related"><h2>Ещё в блоге</h2><ul>{li}</ul></section>'

    cases_html = "".join(f'<li><a href="{esc(c["url"])}">{esc(c["title"])}</a><span>{esc(c["note"])}</span></li>' for c in CASES)

    updated_html = ""
    if str(article["updated"]) != str(article["date"]):
        updated_html = f' · обновлено <time datetime="{esc(article["updated"])}">{ru_date(article["updated"])}</time>'

    cta_lead = article["cta"] or "Я настраиваю систему, о которой рассказал выше, под вашу нишу, голос и площадки. Снимаете вы или ваш эксперт, остальное делает конвейер."

    ctx = {
        "title": esc(article["title"]),
        "description": esc(article["description"]),
        "url": esc(article["abs_url"]),
        "cover": esc(article["abs_cover"]),
        "cover_src": esc(article["cover"]),
        "cover_alt": esc(article["cover_alt"]),
        "cluster": esc(article["cluster"]),
        "type": esc(article["type"]),
        "date_iso": esc(article["date"]),
        "date_ru": ru_date(article["date"]),
        "updated_html": updated_html,
        "minutes": article["minutes"],
        "words": f"{article['words']:,}".replace(",", " "),
        "toc": toc_html,
        "body": body_html,
        "faq": faq_html,
        "sources": sources_html,
        "related": related_html,
        "cases": cases_html,
        "cta_lead": esc(cta_lead),
        "telegram": TELEGRAM,
        "channel": CHANNEL,
        "author_name": esc(AUTHOR["name"]),
        "author_image": esc(AUTHOR["image"]),
        "json_ld": json_ld(article, bool(faq_html)),
        "year": str(dt.date.today().year),
        "robots": '<meta name="robots" content="noindex,nofollow">' if article["draft"] else "",
    }
    write(BLOG / article["slug"] / "index.html", render(template, ctx))


# ---------------------------------------------------------------- blog index

def build_index(articles: list[dict], template: str) -> None:
    public = [a for a in articles if not a["draft"]]
    clusters: dict[str, list[dict]] = {}
    for a in public:
        clusters.setdefault(a["cluster"], []).append(a)

    cards = []
    for a in public:
        cards.append(
            f'<article class="card" data-cluster="{esc(slugify(a["cluster"]))}">'
            f'<a class="card-img" href="{esc(a["url"])}"><img src="{esc(a["cover"])}" alt="" loading="lazy" decoding="async" width="1200" height="630"></a>'
            f'<div class="card-b"><div class="card-m"><span>{esc(a["cluster"])}</span><time datetime="{esc(a["date"])}">{ru_date(a["date"])}</time><span>{a["minutes"]} мин</span></div>'
            f'<h2><a href="{esc(a["url"])}">{esc(a["title"])}</a></h2><p>{esc(a["description"])}</p></div></article>'
        )
    chips = '<a class="chip is-on" href="#all" data-f="all">Все</a>' + "".join(
        f'<a class="chip" href="#{esc(slugify(c))}" data-f="{esc(slugify(c))}">{esc(c)} <b>{len(items)}</b></a>' for c, items in clusters.items()
    )
    empty = "" if public else '<p class="empty">Первые статьи уже в работе. Пока посмотрите кейсы ниже.</p>'

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Blog", "@id": SITE + "/blog/#blog", "url": SITE + "/blog/", "name": "Блог Петра Соловарова",
             "description": "Статьи и инструкции про внедрение ИИ в бизнес: конвейеры контента, автоответы, базы знаний. Факты из своих проектов.",
             "inLanguage": "ru-RU", "author": {"@id": SITE + "/#person"},
             "blogPost": [{"@type": "BlogPosting", "@id": a["abs_url"] + "#article", "headline": a["title"], "url": a["abs_url"], "datePublished": str(a["date"])} for a in public]},
            {"@type": "Person", "@id": SITE + "/#person", **AUTHOR},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Главная", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Блог", "item": SITE + "/blog/"}]},
        ],
    }
    ctx = {
        "cards": "".join(cards) + empty,
        "chips": chips,
        "count": len(public),
        "cases": "".join(f'<li><a href="{esc(c["url"])}">{esc(c["title"])}</a><span>{esc(c["note"])}</span></li>' for c in CASES),
        "json_ld": json.dumps(ld, ensure_ascii=False, indent=1).replace("</", "<\\/"),
        "telegram": TELEGRAM,
        "channel": CHANNEL,
        "year": str(dt.date.today().year),
    }
    write(BLOG / "index.html", render(template, ctx))


# ---------------------------------------------------------------- feeds and robots

def build_sitemap(articles: list[dict]) -> None:
    today = dt.date.today().isoformat()
    rows = [("/", today, "weekly", "1.0"), ("/blog/", today, "daily", "0.9")]
    rows += [(c["url"], today, "monthly", "0.8") for c in CASES]
    rows += [(a["url"], str(a["updated"]), "monthly", "0.8") for a in articles if not a["draft"]]
    body = "".join(
        f"  <url><loc>{SITE}{loc}</loc><lastmod>{mod}</lastmod><changefreq>{freq}</changefreq><priority>{pr}</priority></url>\n"
        for loc, mod, freq, pr in rows
    )
    write(ROOT / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")


def build_robots() -> None:
    write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


def build_rss(articles: list[dict]) -> None:
    public = [a for a in articles if not a["draft"]]

    def rfc822(iso: str) -> str:
        d = dt.datetime.combine(dt.date.fromisoformat(str(iso)), dt.time(9, 0), tzinfo=dt.timezone(dt.timedelta(hours=3)))
        return d.strftime("%a, %d %b %Y %H:%M:%S %z")

    items = "".join(
        f"  <item>\n    <title>{esc(a['title'])}</title>\n    <link>{a['abs_url']}</link>\n    <guid isPermaLink=\"true\">{a['abs_url']}</guid>\n"
        f"    <pubDate>{rfc822(a['date'])}</pubDate>\n    <category>{esc(a['cluster'])}</category>\n    <description>{esc(a['description'])}</description>\n"
        f"    <enclosure url=\"{a['abs_cover']}\" type=\"image/jpeg\" length=\"0\"/>\n  </item>\n"
        for a in public
    )
    last = rfc822(public[0]["updated"]) if public else rfc822(dt.date.today().isoformat())
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n'
        f"  <title>Блог Петра Соловарова: ИИ в бизнесе</title>\n  <link>{SITE}/blog/</link>\n"
        f'  <atom:link href="{SITE}/blog/rss.xml" rel="self" type="application/rss+xml"/>\n'
        "  <description>Статьи и инструкции про внедрение ИИ в бизнес: конвейеры контента, автоответы, базы знаний. Факты из своих проектов.</description>\n"
        f"  <language>ru</language>\n  <lastBuildDate>{last}</lastBuildDate>\n{items}</channel>\n</rss>\n"
    )
    write(BLOG / "rss.xml", xml)


def build_llms(articles: list[dict]) -> None:
    public = [a for a in articles if not a["draft"]]
    lines = [
        "# Пётр Соловаров — petrsolovarov.ru",
        "",
        "> Внедряю ИИ в бизнес и показываю на своих проектах, как это работает: конвейер коротких роликов из одного человека, автоответы по кодовому слову, базы знаний из документов. Все цифры в статьях и кейсах взяты из моих систем и указаны с датой.",
        "",
        "Язык сайта: русский. Автор всех текстов: Пётр Соловаров. Связь: https://t.me/solovarov (слово «система» — бесплатный разбор 30 минут).",
        "",
        "## Статьи блога",
        "",
    ]
    lines += [f"- [{a['title']}]({a['abs_url']}): {a['description']}" for a in public]
    lines += ["", "## Кейсы", ""]
    lines += [f"- [{c['title']}]({SITE}{c['url']}): {c['note']}" for c in CASES]
    lines += ["", "## Служебные", "", f"- [RSS]({SITE}/blog/rss.xml)", f"- [Sitemap]({SITE}/sitemap.xml)", ""]
    write(ROOT / "llms.txt", "\n".join(lines))


# ---------------------------------------------------------------- homepage block

HOME_START = "<!-- BLOG:START -->"
HOME_END = "<!-- BLOG:END -->"


def home_cards(articles: list[dict]) -> str:
    public = [a for a in articles if not a["draft"]][:3]
    if not public:
        return '<p class="posts-empty">Первые статьи уже в работе. Загляните в <a href="/blog/">блог</a> через пару дней.</p>'
    out = []
    for a in public:
        out.append(
            f'<a class="post-card" href="{esc(a["url"])}">'
            f'<img class="post-cover" src="{esc(a["cover"])}" alt="" loading="lazy" decoding="async" width="1200" height="630">'
            f'<div class="post-body"><div class="post-meta"><span>{esc(a["cluster"])}</span><span>{ru_date(a["date"])}</span><span>{a["minutes"]} мин</span></div>'
            f'<h3 class="post-title">{esc(a["title"])}</h3><p class="post-desc">{esc(a["description"])}</p></div></a>'
        )
    return "".join(out)


def update_home(articles: list[dict]) -> None:
    if not HOME.exists():
        print("  главная не найдена, пропускаю")
        return
    text = HOME.read_text(encoding="utf-8")
    if HOME_START not in text or HOME_END not in text:
        print("  на главной нет маркеров BLOG:START/BLOG:END, блок «Последние статьи» не обновлён")
        return
    before, rest = text.split(HOME_START, 1)
    _, after = rest.split(HOME_END, 1)
    new = before + HOME_START + "\n" + home_cards(articles) + "\n                " + HOME_END + after
    if new != text:
        HOME.write_text(new, encoding="utf-8", newline="\n")
        print("  обновил блок «Последние статьи» на главной")
    else:
        print("  главная без изменений")


# ---------------------------------------------------------------- main

def main() -> int:
    print("Собираю блог…")
    template = TEMPLATE.read_text(encoding="utf-8")
    index_template = (BLOG / "template_index.html").read_text(encoding="utf-8")
    articles = load_articles()
    if not articles:
        print("  в blog/content нет статей")
    for a in articles:
        build_article(a, template, articles)
        print(f"    {a['slug']}: {a['words']} слов, {a['images']} картинок, {len(a['faq'])} вопросов FAQ" + (" (черновик)" if a["draft"] else ""))
    build_index(articles, index_template)
    build_sitemap(articles)
    build_robots()
    build_rss(articles)
    build_llms(articles)
    update_home(articles)
    print("Готово.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
