#!/usr/bin/env python3
"""Обложка статьи 1200×630 в палитре сайта (графит и золото), собирается PIL.

    python blog/make_cover.py <slug>            # заголовок берётся из frontmatter blog/content/<slug>.md
    python blog/make_cover.py <slug> --light    # светлый вариант

Результат: blog/<slug>/img/cover.jpg. Шрифты: Jost и Open Sans, если установлены, иначе Segoe UI.
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_blog import CONTENT, BLOG, parse_frontmatter  # noqa: E402

W, H = 1200, 630
DARK = {"bg": (18, 17, 14), "surface": (27, 25, 20), "fg": (239, 233, 220), "muted": (167, 159, 142), "line": (48, 44, 36), "accent": (232, 163, 61)}
LIGHT = {"bg": (246, 243, 238), "surface": (255, 255, 255), "fg": (26, 24, 20), "muted": (93, 87, 76), "line": (221, 214, 200), "accent": (138, 90, 0)}

FONT_DIRS = [Path("C:/Windows/Fonts"), Path.home() / "AppData/Local/Microsoft/Windows/Fonts"]


def font(names: list[str], size: int) -> ImageFont.FreeTypeFont:
    for n in names:
        for d in FONT_DIRS:
            p = d / n
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default(size)


def wrap(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make(slug: str, light: bool = False) -> Path:
    meta, _ = parse_frontmatter((CONTENT / f"{slug}.md").read_text(encoding="utf-8"))
    title = str(meta.get("cover_title") or meta["title"])
    kicker = f"{meta.get('type', 'Статья')} · {meta.get('cluster', '')}".strip(" ·")
    pal = LIGHT if light else DARK

    img = Image.new("RGB", (W, H), pal["bg"])
    d = ImageDraw.Draw(img)

    # тонкая сетка-«конвейер» справа: 8 узлов, как в кейсе
    x0, y0 = 860, 150
    for i in range(8):
        r, c = divmod(i, 2)
        x, y = x0 + c * 150, y0 + r * 92
        d.rounded_rectangle([x, y, x + 120, y + 62], radius=8, fill=pal["surface"], outline=pal["line"], width=2)
        d.text((x + 12, y + 10), str(i + 1), font=font(["Jost-SemiBold.ttf", "segoeuib.ttf"], 20), fill=pal["accent"])
        d.rectangle([x + 12, y + 42, x + 12 + 40 + (i % 3) * 18, y + 46], fill=pal["line"])
        if c == 0:
            d.line([x + 120, y + 31, x + 150, y + 31], fill=pal["line"], width=2)
        if r < 3:
            d.line([x + 60, y + 62, x + 60, y + 92], fill=pal["line"], width=2)

    # полоса-акцент слева
    d.rectangle([0, 0, 14, H], fill=pal["accent"])

    f_k = font(["Jost-SemiBold.ttf", "segoeuib.ttf"], 22)
    f_t = font(["Jost-Bold.ttf", "segoeuib.ttf"], 58)
    f_s = font(["OpenSans-Regular.ttf", "segoeui.ttf"], 24)
    f_b = font(["Jost-SemiBold.ttf", "segoeuib.ttf"], 24)

    d.text((70, 72), kicker.upper(), font=f_k, fill=pal["accent"], spacing=4)
    lines = wrap(d, title, f_t, 760)
    if len(lines) > 4:
        f_t = font(["Jost-Bold.ttf", "segoeuib.ttf"], 48)
        lines = wrap(d, title, f_t, 760)
    y = 126
    for ln in lines:
        d.text((70, y), ln, font=f_t, fill=pal["fg"])
        y += int(f_t.size * 1.18)

    # подчёркивание-маркер под последней строкой
    d.rectangle([70, y + 6, 70 + min(360, int(d.textlength(lines[-1], font=f_t))), y + 12], fill=pal["accent"])

    d.text((70, H - 96), "Пётр Соловаров", font=f_b, fill=pal["fg"])
    d.text((70, H - 62), "petrsolovarov.ru/blog", font=f_s, fill=pal["muted"])

    out = BLOG / slug / "img" / "cover.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"обложка: {out.relative_to(BLOG.parent).as_posix()} ({out.stat().st_size // 1024} КБ)")
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("укажи slug статьи")
    make(args[0], light="--light" in sys.argv)
