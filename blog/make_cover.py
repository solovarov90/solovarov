#!/usr/bin/env python3
"""Обложка статьи 1200×630 в палитре сайта (графит и золото), собирается PIL.

    python blog/make_cover.py <slug>            # заголовок берётся из frontmatter blog/content/<slug>.md
    python blog/make_cover.py <slug> --light    # светлый вариант

Результат: blog/<slug>/img/cover.jpg. Шрифты: Jost и Open Sans, если установлены, иначе Segoe UI.
Запасной вариант: по умолчанию обложку рисует нейросеть (SEO-штаб, gen_cover); здесь мотив справа зависит от type.
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


def motif(d: ImageDraw.ImageDraw, pal: dict, kind: str, slug: str) -> None:
    """Запасной мотив справа (когда обложку не нарисовала нейросеть): схема шагов, столбцы, сравнение, окно, вопрос."""
    seed = sum(ord(ch) for ch in slug)
    f_n = font(["Jost-SemiBold.ttf", "segoeuib.ttf"], 20)
    if kind == "Кейс":   # столбцы с золотым пиком
        heights = [60 + ((seed * (i + 3)) % 7) * 36 for i in range(7)]
        heights[seed % 7] = 330
        for i, h in enumerate(heights):
            x = 860 + i * 46
            d.rounded_rectangle([x, 510 - h, x + 32, 510], radius=4,
                                fill=pal["accent"] if h == 330 else pal["surface"], outline=pal["line"], width=2)
        d.line([850, 512, 1180, 512], fill=pal["line"], width=2)
    elif kind == "Сравнение":   # две колонки с галочками и прочерками
        for c in range(2):
            x = 860 + c * 160
            d.rounded_rectangle([x, 140, x + 140, 520], radius=10, fill=pal["surface"], outline=pal["line"], width=2)
            d.rectangle([x + 16, 160, x + 16 + 60 + c * 40, 166], fill=pal["accent"] if c else pal["line"])
            for r in range(6):
                y = 200 + r * 52
                ok = ((seed >> (r + c * 6)) & 1) == c
                d.ellipse([x + 16, y, x + 36, y + 20], fill=pal["accent"] if ok else pal["line"])
                d.rectangle([x + 48, y + 7, x + 48 + 50 + (r % 3) * 12, y + 13], fill=pal["line"])
    elif kind in ("Разбор инструмента", "Новость → как применить"):   # окно с кодом/строками
        d.rounded_rectangle([850, 130, 1190, 520], radius=10, fill=pal["surface"], outline=pal["line"], width=2)
        for i in range(3):
            d.ellipse([868 + i * 18, 146, 878 + i * 18, 156], fill=pal["line"])
        d.line([850, 170, 1190, 170], fill=pal["line"], width=2)
        for r in range(9):
            y = 192 + r * 34
            indent = (seed >> r) & 3
            d.rectangle([870 + indent * 22, y, 870 + indent * 22 + 70 + ((seed * (r + 1)) % 5) * 36, y + 8],
                        fill=pal["accent"] if r in (seed % 9, (seed // 3) % 9) else pal["line"])
    elif kind == "Ответ на вопрос":   # большой знак вопроса в круге и пузырь ответа
        d.ellipse([870, 150, 1150, 430], outline=pal["accent"], width=4)
        d.text((950, 170), "?", font=font(["Jost-Bold.ttf", "segoeuib.ttf"], 220), fill=pal["accent"])
        d.rounded_rectangle([900, 450, 1180, 520], radius=12, fill=pal["surface"], outline=pal["line"], width=2)
        d.rectangle([918, 470, 1100, 476], fill=pal["line"])
        d.rectangle([918, 490, 1040, 496], fill=pal["line"])
    else:   # Инструкция и прочее: сетка-«конвейер» из 8 узлов, как в кейсе
        x0, y0 = 860, 150
        for i in range(8):
            r, c = divmod(i, 2)
            x, y = x0 + c * 150, y0 + r * 92
            d.rounded_rectangle([x, y, x + 120, y + 62], radius=8, fill=pal["surface"], outline=pal["line"], width=2)
            d.text((x + 12, y + 10), str(i + 1), font=f_n, fill=pal["accent"])
            d.rectangle([x + 12, y + 42, x + 12 + 40 + ((i + seed) % 3) * 18, y + 46], fill=pal["line"])
            if c == 0:
                d.line([x + 120, y + 31, x + 150, y + 31], fill=pal["line"], width=2)
            if r < 3:
                d.line([x + 60, y + 62, x + 60, y + 92], fill=pal["line"], width=2)


def make(slug: str, light: bool = False) -> Path:
    meta, _ = parse_frontmatter((CONTENT / f"{slug}.md").read_text(encoding="utf-8"))
    title = str(meta.get("cover_title") or meta["title"])
    kicker = f"{meta.get('type', 'Статья')} · {meta.get('cluster', '')}".strip(" ·")
    pal = LIGHT if light else DARK

    img = Image.new("RGB", (W, H), pal["bg"])
    d = ImageDraw.Draw(img)

    # мотив справа — по типу статьи, мелкие вариации от slug (чтобы обложки не были одинаковыми)
    motif(d, pal, str(meta.get("type", "")), slug)

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
