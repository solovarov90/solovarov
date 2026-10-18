# Блог petrsolovarov.ru/blog/

Статьи лежат в `blog/content/<slug>.md` (Markdown + frontmatter), сайт собирается одной командой из корня репозитория:

```bash
python blog/build_blog.py
```

Что получается:

- `blog/<slug>/index.html` — статья по шаблону `blog/template.html` (крошки, автор и даты, оглавление, FAQ, источники, блок «Как подключить у вас», кейсы; JSON-LD Article + Person + FAQPage + BreadcrumbList, OG, canonical).
- `blog/index.html` — лента с рубриками (шаблон `blog/template_index.html`).
- `sitemap.xml`, `robots.txt`, `llms.txt` в корне сайта, `blog/rss.xml`.
- Блок «Последние статьи» на главной `index.html` между маркерами `<!-- BLOG:START -->` и `<!-- BLOG:END -->`.

## Новая статья

1. Создать `blog/content/<slug>.md`. Frontmatter: `title`, `description`, `slug`, `date`, `updated`, `cluster` (рубрика), `type`, `cover`, `cover_alt`, `cta`, `faq` (список `q`/`a`), `sources` (список `title`/`url`/`note`). `draft: true` прячет статью из ленты, sitemap, RSS и с главной (в самой странице ставится noindex).
2. Картинки: `![alt](/путь.jpg "подпись под снимком")` — подпись из title попадает в figcaption. Можно вставлять HTML-блоки из кейсов: `<ol class="flow">`, `<div class="figures">`, `<div class="proof">`.
3. Обложка 1200×630: `python blog/make_cover.py <slug>` (PIL, палитра сайта; `cover_title` во frontmatter задаёт короткий заголовок на обложке).
4. `python blog/build_blog.py`, посмотреть локально: `python -m http.server 8099` из корня и открыть `http://localhost:8099/blog/<slug>/`.
5. Коммит, push. Когда Netlify выложил, `python blog/indexnow.py` отправит новые адреса в Яндекс и Bing (ключ-файл `<ключ>.txt` в корне сайта уже создан; он должен быть выложен до первой отправки).

Правила текста: по-русски, от первого лица, просто, без канцелярита и «не только…, но и». Факты только из своих систем (Notion, кейсы), чужие — с внешней ссылкой. Ответ в первых 2–3 предложениях каждого раздела, H2 в форме вопросов, 5–8 вопросов в FAQ.
