---
title: "Gemini Omni 1.2 Flash: что умеет новая модель и как применить её в бизнесе"
cover_title: Gemini Omni 1.2 Flash для бизнеса
description: "Gemini Omni 1.2 Flash делает и правит видео до 15 секунд со звуком за $0,07 в секунду. Разбираю, где модель полезна бизнесу, сколько стоит и чем отличается от обычной Gemini Flash."
slug: gemini-omni-1-2-flash-dlya-biznesa
date: 2026-11-07
updated: 2026-11-09
cluster: Инструменты
type: Новость → как применить
cover: /blog/gemini-omni-1-2-flash-dlya-biznesa/img/cover.jpg
cover_alt: Gemini Omni 1.2 Flash для бизнеса, обложка статьи о новой модели Google для видео
cta: Помогу понять, какие задачи в твоём деле отдать видеомодели, а какие обычной Gemini Flash, и соберу связку, которая работает каждый день без ручных кликов.
offers: [club, consult, build]
faq:
  - q: Чем Gemini Omni Flash отличается от обычной Gemini Flash?
    a: Omni 1.2 Flash делает и правит видео со звуком, роликами от 3 до 15 секунд. Обычная Flash работает с текстом и смотрит видео, чтобы описать его словами. По документации Google у Omni нет вызова функций и ответа строго в JSON, поэтому для разбора заявок и переписки она не годится.
  - q: Можно ли пользоваться Gemini Omni 1.2 Flash бесплатно в рабочих процессах?
    a: По API нет. На странице цен Google на 6 ноября 2026 у Omni 1.2 Flash бесплатного уровня нет, модель доступна только на платном. Обычные текстовые модели Flash бесплатный лимит имеют, у меня на нём с 30.09.2026 работал разбор роликов.
  - q: Как подключить Gemini API, находясь в России?
    a: Напрямую не выйдет. 02.11.2026 я проверял: Google AI Studio и Gemini API для России закрыты, ответ 403. В проекте VetCT я с 30.10.2026 отправляю запросы к Gemini через российский шлюз Polza.ai с оплатой в рублях, формат запросов остаётся гугловский.
  - q: Хватит ли возможностей Flash для ответов клиентам в поддержке?
    a: Текстовой Flash хватает на короткие типовые задачи. В проекте JE 3.0 я 05.11.2026 перевёл на gemini-flash-latest черновики ответов клиенту, алерты и благодарности. Там, где нужен большой контекст и долгий разговор, оставил Pro. Omni 1.2 Flash для поддержки не предназначена.
  - q: Почему модель Flash иногда теряет параметры при вызове инструментов?
    a: На длинных инструкциях облегчённые модели хуже держат формат. У меня 18.10.2026 flash-lite вызвал запись файла без пути к файлу, и весь прогон конвейера упал. Помог перевод этих шагов на более сильную gemini-3-flash-preview и проверка ответа перед выполнением.
  - q: Что выгоднее малому бизнесу, подписка на чат или Flash по ключу?
    a: Зависит от того, руками ли ты работаешь. Для разовых роликов и текстов удобнее подписка и приложение. Если задача повторяется каждый день и её запускает бот, выгоднее ключ с оплатой за запрос. Мой разбор одного ролика на платной Flash стоит около цента.
  - q: Сколько стоит один ролик на Gemini Omni 1.2 Flash?
    a: По ценам Google на 6 ноября 2026 секунда видео в 720p стоит около $0,07, значит 15 секунд выходят примерно в $1,05. Черновик в 360p стоит $0,023 в секунду, 4K около $0,21. Сразу закладывай несколько попыток на один удачный кадр.
sources:
  - title: Google Cloud Blog — Gemini Omni 1.2 Flash generally available
    url: https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available
    note: анонс 6 ноября 2026, длина до 15 секунд, цена на 30% ниже версии 1.1, SynthID, Google Vids
  - title: Документация Gemini Omni 1.2 Flash в Google Cloud
    url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-2-flash
    note: что модель умеет и чего не умеет, разрешения, форматы 16:9 и 9:16, ограничения
  - title: Цены Gemini API
    url: https://aistudio.google.com/docs/pricing
    note: цена за секунду по разрешениям, нет бесплатного уровня, перевод запросов 1.1 на 1.2 с 3 декабря 2026
  - title: Обсуждение на Hacker News
    url: https://news.ycombinator.com/item?id=50392118
    note: отзывы разработчиков, жалобы на оплату и кабинет AI Studio
  - title: AI-стек ii.systema, Gemini (gemini-3.6-flash)
    url: https://app.notion.com/p/Gemini-gemini-3-6-flash-3ebdfdb1482281f78aadfbb877945015
    note: разбор видео на бесплатном лимите, 30.09.2026
  - title: Журнал изменений ii.systema, разбор на платном Gemini
    url: https://app.notion.com/p/Gemini-3ebdfdb14822816293ebf92c09831bd4
    note: около 1 цента за ролик, 30.09.2026
  - title: Задача JE 3.0, перевод сценариев с Pro на Flash
    url: https://app.notion.com/p/LLM-je30-server-Flash-40fdfdb1482281dd845fd6c683367685
    note: какие сценарии ушли на gemini-flash-latest, 05.11.2026
  - title: Журнал изменений ii.systema, персонаж через Wan 2.2 на fal
    url: https://app.notion.com/p/Wan-2-2-Animate-Replace-40cdfdb1482281b1aeb0ea7dab76cbbf
    note: около $0,08 за секунду дубля в 720p, 02.11.2026
  - title: Журнал изменений ii.systema, доступ к ИИ из России
    url: https://app.notion.com/p/4-40cdfdb148228142bee8e436424039b4
    note: проверка 02.11.2026, AI Studio и Gemini API для РФ закрыты
  - title: Кейс VetCTschool
    url: https://petrsolovarov.ru/vetctschool/
    note: Gemini через Polza.ai с российского сервера, 30.10.2026
---

Gemini Omni 1.2 Flash это модель Google, которая делает и правит короткие видео со звуком: от 3 до 15 секунд, в разрешении от 360p до 4K. Для малого бизнеса это быстрый способ получить ролик о товаре, рекламную вставку или примерку без съёмки. Секунда видео в 720p стоит около $0,07 по [ценам Google](https://aistudio.google.com/docs/pricing) на 6 ноября 2026, бесплатного уровня в API у модели нет.

Важная оговорка сразу. В выдаче модель часто путают с обычной Gemini Flash, которая читает текст и смотрит видео. Это разные инструменты, и ниже я разбираю, куда ставить каждый.

## Чем Gemini Omni 1.2 Flash отличается от предыдущих версий?

Главное отличие от версии 1.1 в длине и цене. Ролик стал до 15 секунд вместо 10, а секунда видео подешевела на 30%. Об этом Google написал в [анонсе 6 ноября 2026](https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available).

Что ещё добавили:

- **Правку в разговоре.** Пишешь «поменяй товар», «сделай свет теплее», «сними с другого угла», и модель меняет только это, остальное сохраняет.
- **Речь и звук.** Диалоги звучат естественнее, губы точнее попадают в слова, есть шумы и музыка.
- **Точность по образцам.** До 10 картинок и до 3 видео в одном запросе, модель держится ближе к ним.
- **Форматы 16:9 и 9:16.** Вертикаль подходит сразу под Reels и Shorts.

Невидимая метка SynthID стоит на каждом ролике. С 3 декабря 2026 все запросы к версии 1.1 Google сам переводит на 1.2.

## Какие бизнес-задачи стоит отдать модели линейки Flash?

Omni 1.2 Flash отдавай короткое видео, обычной Flash отдавай чтение и разбор. Так задачи и делятся.

| Задача | Какая модель |
|---|---|
| Ролик о товаре, примерка, рекламная вставка до 15 секунд | Omni 1.2 Flash |
| Перекрасить фон, поменять товар в готовом ролике | Omni 1.2 Flash |
| Разобрать чужой ролик: хук, структура, монтаж | обычная Flash |
| Черновик ответа клиенту, алерт, короткая карточка | обычная Flash |
| Разговор с большим контекстом, загрузка базы знаний | Pro |

<!-- img: type=scheme what="три узла и стрелки задач: Omni 1.2 Flash (ролик о товаре, вставка, правка видео) ← задача → обычная Flash (разбор ролика, черновик ответа, алерт) → Pro (большой контекст, база знаний); подписать, что выбирать по типу задачи" caption="Как делить задачи между Omni 1.2 Flash, обычной Flash и Pro: видео делает одна модель, чтение и разбор другая." alt="gemini omni 1.2 flash и обычная gemini flash: какие задачи бизнеса отдать каждой" -->

<figure class="scheme">
<svg width="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" role="img" aria-label="Как делить задачи между Omni 1.2 Flash, обычной Flash и Pro: видео делает одна модель, чтение и разбор другая">
  <title>Как делить задачи между Omni 1.2 Flash, обычной Flash и Pro</title>
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/>
    </marker>
    <marker id="arrLine" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="var(--line)"/>
    </marker>
  </defs>

  <text x="600" y="48" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">Выбирай модель по типу задачи</text>

  <rect x="40" y="110" width="320" height="300" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="2"/>
  <text x="200" y="158" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="28" fill="var(--fg)">Omni 1.2 Flash</text>
  <text x="200" y="192" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">делает видео</text>
  <text x="70" y="248" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Ролик о товаре</text>
  <text x="70" y="288" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Рекламная вставка</text>
  <text x="70" y="328" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Правка готового видео</text>
  <text x="70" y="378" font-family="var(--font-body)" font-size="18" fill="var(--muted)">до 15 секунд</text>

  <rect x="440" y="110" width="320" height="300" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <text x="600" y="158" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="28" fill="var(--fg)">Обычная Flash</text>
  <text x="600" y="192" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">читает и разбирает</text>
  <text x="470" y="248" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Разбор ролика</text>
  <text x="470" y="288" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Черновик ответа клиенту</text>
  <text x="470" y="328" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Алерт, короткая карточка</text>

  <rect x="840" y="110" width="320" height="300" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <text x="1000" y="158" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="28" fill="var(--fg)">Pro</text>
  <text x="1000" y="192" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">держит много контекста</text>
  <text x="870" y="248" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Большой контекст</text>
  <text x="870" y="288" font-family="var(--font-body)" font-size="19" fill="var(--fg)">База знаний</text>
  <text x="870" y="328" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Долгий разговор</text>

  <line x1="364" y1="260" x2="436" y2="260" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr)" marker-start="url(#arr)"/>
  <line x1="764" y1="260" x2="836" y2="260" stroke="var(--line)" stroke-width="3" marker-end="url(#arrLine)"/>

  <circle cx="200" cy="470" r="16" fill="var(--accent)"/>
  <text x="200" y="477" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="19" fill="var(--surface)">1</text>
  <text x="228" y="477" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Нужно видео?</text>
  <circle cx="600" cy="470" r="16" fill="var(--accent)"/>
  <text x="600" y="477" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="19" fill="var(--surface)">2</text>
  <text x="628" y="477" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Нужен разбор?</text>
  <circle cx="900" cy="470" r="16" fill="var(--accent)"/>
  <text x="900" y="477" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="19" fill="var(--surface)">3</text>
  <text x="928" y="477" font-family="var(--font-body)" font-size="19" fill="var(--fg)">Много данных?</text>
</svg>
<figcaption>Как делить задачи между Omni 1.2 Flash, обычной Flash и Pro: видео делает одна модель, чтение и разбор другая.</figcaption>
</figure>


По [документации Google](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-2-flash) у Omni нет вызова функций, ответа строго в формате JSON и поиска. Это значит, что бот не сможет попросить её «разложи заявку по полям». Для этого есть текстовые модели.

## Как запустить генерацию видео через API без лишних затрат?

Делай черновики в 360p или 720p, а в 1080p или 4K переводи только удачный вариант. Это совет из самого анонса Google, и он прямо бьёт по счёту.

Порядок работы:

1. **Ключ на платном уровне.** Бесплатного у Omni 1.2 Flash нет, модель зовётся `gemini-omni-1.2-flash`.
2. **Сначала образцы.** Фото товара, логотипа, комнаты. Чем точнее образец, тем меньше попыток.
3. **Черновик в 360p.** Секунда стоит $0,023, ошибиться не жалко.
4. **Правки словами.** Меняешь одно за раз, а не генерируешь заново.
5. **Финал в нужном качестве.** Апскейл до 1080p или 4K той же моделью.

Если руками не хочется, модель доступна в Google Vids, а владельцы подписки Google AI Ultra делают ролики до 15 секунд в приложении Gemini.

## Сколько стоит работа модели при регулярных нагрузках?

Пятнадцатисекундный ролик в 720p стоит около $1,05, в 4K около $3,1. Цифры посчитаны по [ценам Gemini API](https://aistudio.google.com/docs/pricing) на 6 ноября 2026.

| Разрешение | Цена за секунду | Ролик 15 секунд |
|---|---|---|
| 360p | $0,023 | около $0,35 |
| 720p | около $0,07 | около $1,05 |
| 1080p | $0,104 | около $1,56 |
| 4K | $0,209 | около $3,14 |

Для сравнения из своего: замена человека на персонажа через Wan 2.2 на сервисе fal у меня стоит около $0,08 за секунду дубля в 720p ([журнал изменений, 02.11.2026](https://app.notion.com/p/Wan-2-2-Animate-Replace-40cdfdb1482281b1aeb0ea7dab76cbbf)). Порядок цен тот же. Считай не один ролик, а попытки: удачный кадр редко выходит с первого раза.

## Проверил на себе: где Flash работает идеально, а где ломается?

Omni 1.2 Flash я ещё не гонял: модель вышла 6 ноября. Обычную Flash использую каждый день в трёх проектах, и вот что вижу.

**Разбор видео.** С 30.09.2026 Gemini Flash смотрит чужие ролики целиком и описывает хук, структуру и монтаж ([AI-стек](https://app.notion.com/p/Gemini-gemini-3-6-flash-3ebdfdb1482281f78aadfbb877945015)). Бесплатного лимита на тяжёлые файлы не хватило, и в тот же день я перевёл разбор на платную Flash с низким разрешением видео: около 1 цента за ролик ([журнал](https://app.notion.com/p/Gemini-3ebdfdb14822816293ebf92c09831bd4)). Как это устроено целиком, писал в статье [«Почему ролик залетел»](/blog/pochemu-rolik-zaletel/).

**Счёт клиента.** В проекте JE 3.0 расходы за месяц на Gemini API и сервер вышли $46 вместе с двумя месяцами аренды (04.11.2026). Основную часть съедали алерты, которые запускаются каждые 5 минут на Pro. 05.11.2026 я перевёл на gemini-flash-latest алерты, карточки уснувших клиентов, черновики ответов и благодарности, а Pro оставил там, где нужен большой контекст ([задача](https://app.notion.com/p/LLM-je30-server-Flash-40fdfdb1482281dd845fd6c683367685)). Если ответ пришёл не в JSON, бот повторяет запрос один раз.

**Что сломалось.** 18.10.2026 в контентном конвейере проекта «Техномаг» модель flash-lite на длинной инструкции вызвала запись файла без пути. Весь прогон упал, отчёт не дошёл. Длинные шаги я перевёл на gemini-3-flash-preview.

Вывод простой: облегчённая модель хороша на коротких задачах и подводит на длинных инструкциях. Проверяй ответ перед тем, как бот его выполнит.

## Как подключить Gemini в России и не потерять доступ?

Напрямую из России Gemini API не работает. Я проверял 02.11.2026: Google AI Studio и API отвечают 403. На российском сервере проекта VetCT Gemini не ответил совсем ([кейс](/vetctschool/), 30.10.2026).

Рабочий путь у меня один: российский шлюз Polza.ai. С 30.10.2026 все запросы VetCT к Gemini идут через него, оплата в рублях, ключ передаётся тем же заголовком `x-goog-api-key`. Код почти не меняется, меняется только адрес. Есть ли там уже Omni 1.2 Flash, проверь перед подключением: у меня такого факта нет.

## Кому модель не подойдёт и где нужен полноценный Pro?

Omni 1.2 Flash не подойдёт, если тебе нужно разбирать переписку, считать, отвечать клиентам или вести долгий разговор. Это задачи текстовых моделей, а для длинного контекста нужна Pro.

Ещё три случая, когда стоит подождать:

- **Нужен ролик длиннее 15 секунд одним куском.** Продлевать можно, но шов останется твоей заботой.
- **Пакетная обработка.** Batch-режим для модели в Google Cloud не поддерживается.
- **Нет платной карты.** На HN разработчики больше всего жалуются как раз на оплату и кабинет AI Studio ([обсуждение](https://news.ycombinator.com/item?id=50392118)).

Если хочешь понять, какую рутину в твоём деле отдать видеомодели, а какую обычной Flash, напиши мне слово «система» в личку в Telegram: [t.me/solovarov](https://t.me/solovarov). Посмотрим на твои процессы и соберём связку без лишних расходов. Как такие связки работают у меня каждый день, видно в статье про [медиа-конвейер на ИИ](/blog/media-konveyer-na-ii/).
