---
title: Почему лимит Claude по подписке кончается к обеду и как растянуть его на день
cover_title: Почему лимит Claude кончается к обеду
description: "Почему Claude быстро тратит лимит по подписке Pro: длинный разговор каждый раз отправляется модели целиком. Короткие сессии, CLAUDE.md, --resume и резерв на API."
slug: pochemu-limit-claude-bystro-konchaetsya
date: 2026-10-31
updated: 2026-10-31
cluster: Инструменты
type: Инструкция
cover: /blog/pochemu-limit-claude-bystro-konchaetsya/img/cover.jpg
cover_alt: Почему лимит Claude по подписке быстро кончается и как его экономить, обложка статьи
cta: Я разберу, какие задачи в твоей работе стоит отдать ИИ, и соберу схему, где Claude, Gemini и резерв на API делят работу без лишних трат на лимиты и токены.
faq:
  - q: Через сколько часов сбрасывается лимит сообщений в Claude Pro?
    a: По справке Anthropic, лимит сессии в Pro сбрасывается каждые 5 часов, сверху действует ещё недельный лимит (проверено 31.10.2026). Окно считается от первого сообщения, а не по календарю. У меня 01.10.2026 монтаж встал на лимите и продолжился сам после сброса в 16:39.
  - q: Почему при коротких вопросах лимит заканчивается за несколько сообщений?
    a: Потому что короткий вопрос уходит модели вместе со всей историей разговора, файлами и инструкциями проекта. Справка Anthropic прямо пишет, что число сообщений зависит от длины текущего разговора и вложений. В длинном чате даже вопрос из трёх слов стоит дорого.
  - q: Теряется ли написанный код или контекст сессии при наступлении лимита?
    a: Файлы, которые агент уже записал на диск, остаются на месте. Сессия Claude Code тоже сохраняется, и после сброса её можно поднять командой claude --resume с id сессии. У меня так монтаж 01.10.2026 продолжился с шага 4 из 7 без повтора готовых шагов.
  - q: Как возобновить работу Claude Code без повторного выполнения команд?
    a: Запомни id сессии, его отдаёт claude -p --output-format json в поле session_id. После сброса лимита запусти claude -p с флагом --resume и этим id и напиши «продолжи». Claude помнит, что уже сделано, и идёт дальше с того места, где встал.
  - q: Стоит ли переходить с подписки за 20 долларов на API-ключ?
    a: Для ежедневной работы с агентом я остаюсь на подписке. По моему руководству по Claude на 04.10.2026, Pro стоит $20 в месяц, а агент за одну задачу читает десятки файлов, и по API это был бы счёт за каждый кусок текста. API у меня работает только резервом с жёстким дневным потолком.
  - q: Как безопасно настроить переключение на платный API при исчерпании лимита?
    a: Держи ключ в отдельной переменной, которую бот подставляет только при ошибке лимита, и поставь дневной потолок расходов. У моего мозг-бота с 28.10.2026 это $3 в сутки на Sonnet 5.5, дальше отвечает база знаний. Сам ключ ANTHROPIC_API_KEY в окружении постоянно держать нельзя, иначе Claude Code будет всегда платить по API.
sources:
  - title: Справка Anthropic о лимитах тарифа Pro
    url: https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage
    note: окно сессии 5 часов, недельный лимит, зависимость от длины разговора и вложений; проверено 31.10.2026
  - title: "Anton Abyzov, Why Your AI Coding Agent Gets Exponentially More Expensive (DEV Community)"
    url: https://dev.to/aabyzov/why-your-ai-coding-agent-gets-exponentially-more-expensive-and-what-to-do-about-it-17jd
    note: формула квадратичного роста стоимости длинной сессии агента и доля чтения кэша 87% при 100 000 токенов
  - title: "Claude Code в Telegram: как запустить ИИ-агента на сервере по подписке"
    url: https://petrsolovarov.ru/blog/claude-code-sotrudnik-telegram/
    note: лимит на шаге 4 из 7, окна по 5 часов и недельная квота, общий пул чата и Claude Code, таблица расхода лимита
  - title: "Claude Code как сотрудник в Telegram: запуск ИИ-агента на сервере по подписке"
    url: https://petrsolovarov.ru/blog/claude-code-kak-sotrudnik-v-telegram/
    note: второй бот ii-seo с 18.10.2026, статья за 10–25 минут, очередь на одного Claude
  - title: "ИИ-штаб на сервере: как управлять Claude Code с телефона по подписке"
    url: https://petrsolovarov.ru/blog/upravlyat-claude-code-s-telefona/
    note: отдельная сессия на тему, правила в CLAUDE.md, таймаут на каждый запуск
  - title: "Журнал изменений: лимит Claude, бот сам ждёт и продолжает (01.10.2026)"
    url: https://app.notion.com/p/Claude-3ecdfdb14822811da1a8ecc18d22b69a
    note: три дубля продолжились сами после сброса лимита в 16:39
  - title: "Журнал изменений: монтаж можно продолжить после обрыва (01.10.2026)"
    url: https://app.notion.com/p/3ecdfdb148228177b8a3e58a3b2e1e1b
    note: REEL-4 упёрся в лимит на шаге 4 из 7, подготовка дубля около 16 минут
  - title: "Журнал изменений: кнопка «Запустить сейчас» в статусе монтажа (18.10.2026)"
    url: https://app.notion.com/p/KeyError-resume-3fddfdb148228133977ac4117a796892
    note: запуск до сброса лимита, после 3 попыток ошибка и кнопка «Продолжить»
  - title: "Журнал изменений: мозг-бот при лимите подписки отвечает через API (28.10.2026)"
    url: https://app.notion.com/p/API-Sonnet-5-5-3-407dfdb1482281308e0bf82edf98efa7
    note: резерв на claude-sonnet-5-5, потолок $3 в сутки, кредиты $100
  - title: "Журнал изменений: разбор референсов переведён на Gemini (30.09.2026)"
    url: https://app.notion.com/p/Gemini-Claude-3ebdfdb1482281c2a72be4a710e93239
    note: Claude тратит лимит только на разговор и сценарии
  - title: "Файл CLAUDE.md: 4 правила, которые убирают ошибки Claude"
    url: https://app.notion.com/p/CLAUDE-md-4-Claude-3eedfdb14822819797f9e49adb1744cc
    note: файл правил от 30 до 150 строк, материал к ролику на 03.10.2026
  - title: "Схема выбора моделей Claude и внедрения ИИ в бизнес"
    url: https://app.notion.com/p/Claude-3f6dfdb1482281a886d8daa5f156cca0
    note: модель под задачу и регулятор Effort, материал на 11.10.2026
  - title: "Инструкция по настройке полоски памяти в Claude Code"
    url: https://app.notion.com/p/Claude-Code-401dfdb1482281609ac5f8223ff7401c
    note: индикатор занятого контекста, команды /compact и /clear, материал на 22.10.2026
---

Лимит Claude по подписке быстро кончается из-за длины разговора: каждое новое сообщение уходит модели вместе со всей историей чата, файлами и инструкциями. Чем длиннее переписка, тем дороже каждый следующий вопрос, даже короткий. Чтобы подписки хватало на весь день, дроби работу на короткие сессии, держи правила в компактном файле и отдавай простую обработку другим моделям.

Я работаю на одной подписке Claude, и на ней живут сразу несколько ботов моего проекта ii.systema: монтаж роликов, SEO-штаб, мозг-бот. Ниже разбираю, куда уходит лимит, как продолжить работу после него без потерь и как я поставил резерв на API с потолком $3 в сутки.

## Почему лимит сообщений Claude Pro тает быстрее с каждым новым вопросом?

Потому что лимит считает объём текста, который модель прочитала, а количество сообщений тут вторично. В [справке Anthropic](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage) (проверено 31.10.2026) так и написано: число сообщений зависит от их длины, от размера приложенных файлов, от длины текущего разговора и от модели. Двадцатый вопрос в одном чате стоит в разы дороже первого.

Как это выглядит в жизни. Утром ты открываешь чат, кидаешь туда договор на 30 страниц и задаёшь вопрос. Потом уточняешь. Потом просишь переписать пункт. Каждое уточнение заставляет модель заново прочитать договор и всю переписку. К обеду ты отправил полтора десятка сообщений, а лимит уже на нуле.

Три вещи съедают лимит сильнее всего:

- **Длинная история.** Один чат на весь день вместо отдельного чата на каждую задачу.
- **Тяжёлые вложения.** Файлы, скриншоты и инструкции проекта прочитываются при каждом сообщении. В [моём материале про ассистентов в Claude](https://app.notion.com/p/5-Claude-3f4dfdb1482281729876fb278cf25948) на 09.10.2026 записано, что инструкции проекта подмешиваются в каждое сообщение, поэтому гигантские промпты быстро расходуют лимит. Промпт здесь это текст задания для нейросети.
- **Агентная работа.** Claude Code за одну задачу читает десятки файлов. По моему [руководству по Claude](https://petrsolovarov.ru/blog/claude-code-sotrudnik-telegram/) на 04.10.2026, чат на claude.ai и Claude Code тратят один общий пул. Утро в Claude Code, и вечером в чате лимита уже нет.

Отдельно про окна. Лимит в Pro считается окнами по 5 часов плюс общая недельная квота, это подтверждает справка Anthropic. Окно начинается с первого сообщения. Поэтому «к обеду кончился» обычно значит, что утреннее окно ты сжёг длинными разговорами, и новое откроется через пару часов.

## Как устроена механика контекстного окна и почему длинные диалоги сжигают квоту?

Контекстное окно это всё, что модель видит за один раз: твои правила, историю чата, файлы и новый вопрос. Модель не помнит прошлых сообщений сама. Программа каждый раз собирает эту стопку целиком и отправляет её заново. Поэтому расход растёт быстрее длины разговора.

На DEV Community есть хороший разбор от Антона Абызова, [почему агент для кода дорожает с каждым шагом](https://dev.to/aabyzov/why-your-ai-coding-agent-gets-exponentially-more-expensive-and-what-to-do-about-it-17jd). Логика простая: с каждым шагом растёт и длина контекста, и число вызовов. Перемножь одно на другое, и стоимость сессии растёт квадратично. По его подсчёту, на 100 000 токенов контекста чтение уже накопленной истории занимает около 87% всех расходов сессии. Токен это кусочек слова, в таких единицах модели считают текст.

<!-- img: type=scheme what="слева короткая сессия: правила + вопрос → ответ, маленькая стопка; справа длинная сессия: правила + 20 прошлых сообщений + файлы + новый вопрос → ответ, высокая стопка; подпись внизу: каждое сообщение отправляет модели всю стопку заново" caption="Короткий вопрос в длинном чате отправляет модели всю накопленную историю, поэтому стоит дороже первого." alt="почему claude быстро тратит лимит: схема роста контекста в длинном диалоге" -->

<figure class="scheme">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600" width="100%" role="img" aria-label="Схема: короткая сессия отправляет модели небольшую стопку, длинная отправляет высокую стопку с историей и файлами">
<title>Короткий и длинный чат: что модель получает с каждым сообщением</title>
<defs>
<marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
<path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/>
</marker>
</defs>

<text x="270" y="50" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">Короткая сессия</text>
<text x="870" y="50" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">Длинная сессия</text>

<line x1="600" y1="80" x2="600" y2="470" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 8"/>

<rect x="60" y="340" width="300" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<text x="210" y="378" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">Правила</text>
<rect x="60" y="406" width="300" height="60" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="2"/>
<text x="210" y="444" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">Новый вопрос</text>

<rect x="640" y="100" width="300" height="60" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<text x="790" y="138" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">Правила</text>
<rect x="640" y="166" width="300" height="100" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<text x="790" y="208" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">20 прошлых</text>
<text x="790" y="238" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">сообщений</text>
<rect x="640" y="272" width="300" height="60" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<text x="790" y="310" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">Файлы</text>
<rect x="640" y="338" width="300" height="60" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<text x="790" y="376" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">Новый вопрос</text>
<rect x="640" y="338" width="300" height="60" rx="10" fill="none" stroke="var(--accent)" stroke-width="2"/>

<text x="210" y="498" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">маленькая стопка</text>
<text x="790" y="428" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">высокая стопка</text>

<line x1="370" y1="370" x2="410" y2="370" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr)"/>
<line x1="950" y1="250" x2="1000" y2="250" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr)"/>

<rect x="420" y="340" width="150" height="60" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="2"/>
<text x="495" y="378" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">Ответ</text>

<rect x="1010" y="220" width="150" height="60" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="2"/>
<text x="1085" y="258" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">Ответ</text>

<text x="600" y="560" text-anchor="middle" font-family="var(--font-body)" font-size="19" fill="var(--muted)">Каждое сообщение отправляет модели всю стопку заново</text>
</svg>
<figcaption>Короткий вопрос в длинном чате отправляет модели всю накопленную историю, поэтому стоит дороже первого.</figcaption>
</figure>


Что из этого следует на практике:

1. **Одна задача, одна сессия.** Закончил задачу, открыл новый чат. Нужные выводы перенеси туда одним абзацем.
2. **Сжимай историю.** В Claude Code есть команда `/compact`: она сворачивает историю в краткую выжимку. Команда `/clear` открывает чистый разговор. Обе описаны в [моей инструкции к Claude Code](https://app.notion.com/p/Claude-Code-401dfdb1482281609ac5f8223ff7401c) на 22.10.2026.
3. **Следи за заполнением.** В той же инструкции есть полоска в строке состояния Claude Code: она показывает, какая часть контекста занята. Краснеет, значит пора сворачивать или начинать заново.
4. **Не тащи файл в каждое сообщение.** Положи его в папку проекта и дай агенту путь. Он прочитает нужное место, а не весь файл.

У меня в штабе на каждую тему Telegram-группы своя сессия Claude, и история одной темы не тянется в другую. Как это устроено, я разбирал в статье [«ИИ-штаб на сервере»](/blog/upravlyat-claude-code-s-telefona/).

## Сколько строк должно быть в файле правил CLAUDE.md, чтобы не перегружать память?

Держи файл правил в пределах 30–150 строк. Эту норму я записал в [материале про CLAUDE.md](https://app.notion.com/p/CLAUDE-md-4-Claude-3eedfdb14822819797f9e49adb1744cc) на 03.10.2026: если раздуть инструкции до сотен строк, модель начинает выборочно их игнорировать. CLAUDE.md это файл в папке проекта, который Claude Code читает в начале каждой сессии.

Короткий файл экономит дважды. Он читается в каждой сессии, значит каждая лишняя строка умножается на число запусков. И модель лучше держит пять ясных правил, чем пятьдесят размытых.

Как я сокращаю правила:

- **Наверху только общее.** Что за проект, где лежат базы, кто автор, чего делать нельзя.
- **Подробности в навыки.** Навык (скилл) это отдельная инструкция на одну задачу: разобрать ролик, написать статью. Claude подгружает её, только когда задача подходит. Правила статей блога лежат в навыке, и в разговоре про монтаж они лимит не тратят.
- **Правило глаголом.** «Пиши коротко» работает лучше, чем «Краткость изложения».
- **Одно правило на одну вещь.** Два противоречивых указания про концовку модель исполнит как попало.

В [материале](https://app.notion.com/p/CLAUDE-md-4-Claude-3eedfdb14822819797f9e49adb1744cc) есть готовый файл на четыре правила: без усложнений, без домыслов, без лишних правок, самопроверка. Для старта этого хватает. Дописывай строку, когда агент второй раз ошибся в одном и том же месте.

## Подписка за 20 долларов или платный API: что выгоднее для ежедневных задач?

Для ежедневной работы с агентом выгоднее подписка. По моему [руководству по Claude](https://petrsolovarov.ru/blog/claude-code-kak-sotrudnik-v-telegram/) на 04.10.2026, Pro стоит $20 в месяц или $17 при оплате за год, и Claude Code в неё входит. API это платный программный доступ к модели, где оплачивается каждый кусок прочитанного и написанного текста.

| | Подписка Pro | API по ключу |
|---|---|---|
| Как платишь | фиксированно в месяц | за каждый токен |
| Где упираешься | окно 5 часов и недельная квота | только в деньги |
| Длинная сессия агента | съедает окно, потом пауза | растёт счёт |
| Для чего у меня | вся основная работа ботов | резерв, когда подписка в лимите |

Агент за одну задачу читает много файлов, и по API длинная сессия превращается в заметный счёт. На подписке худшее, что случится, это пауза до сброса окна. Пауза у меня обрабатывается автоматически, об этом следующий раздел.

Есть и третий путь: часть работы вообще убрать с Claude. 30.09.2026 я [перевёл разбор чужих роликов на Gemini](https://app.notion.com/p/Gemini-Claude-3ebdfdb1482281c2a72be4a710e93239), и с тех пор Claude тратит лимит только на разговор и сценарии. Разбор одного ролика на платном Gemini flash стоит около цента, подробно в статье [«Почему ролик залетел»](/blog/pochemu-rolik-zaletel/). Правило простое: Claude берёт задачи, где нужно думать и писать, а смотреть видео, расшифровывать и раскладывать по полям могут модели дешевле.

Внутри Claude тоже есть выбор. В [схеме выбора моделей](https://app.notion.com/p/Claude-3f6dfdb1482281a886d8daa5f156cca0) на 11.10.2026 я раскладывал так: Haiku на проверку орфографии и сортировку, Sonnet на повседневную аналитику, Opus на сложные задачи. Там же регулятор Effort: на уровне Medium модель рассуждает короче и тратит меньше лимита, чем на High.

## Как настроить автоожидание сброса лимита и продолжить работу через флаг --resume?

Сохрани id сессии и после сброса подними её флагом `--resume`. Claude Code помнит, что уже сделал, и продолжает с того же места. Если задачи запускает бот, научи его ловить ошибку лимита, ставить задачу на паузу и самому перезапускать её после сброса.

Шаги для бота на `claude -p` (неинтерактивный режим: задача передаётся одной строкой, Claude выполняет её и печатает результат):

1. **Запускай с JSON-ответом.** `claude -p "задача" --output-format json`. В ответе есть поле `session_id`, сохрани его рядом с задачей на диск.
2. **Лови лимит.** Если ответ говорит о лимите, не считай задачу проваленной. Поставь ей статус «пауза» и запиши время продолжения.
3. **Жди сброса.** Окно Pro длится 5 часов. Бот раз в несколько минут проверяет время и будит задачу.
4. **Продолжай ту же сессию.** `claude -p "продолжи" --resume <session_id>`. Готовые шаги Claude не повторяет.
5. **Дай кнопку человеку.** «Продолжить» на случай, если автоповтор не сработал, и «Запустить сейчас», если лимит уже освободился раньше.
6. **Ограничь попытки.** Если лимит на самом деле не сброшен, задача упрётся в него снова. После нескольких неудач остановись и напиши в чат.

<!-- img: type=scheme caption="Схема работы бота: как автоматически ставить задачу на паузу при исчерпании лимита и продолжать сессию через --resume." alt="лимит claude закончился что делать: статус задачи на паузе до сброса лимита" was="Telegram, Штаб ii.systema, тема 🎞 Монтаж: статус монтажа на паузе из-за лимита Claude: «продолжу сам в ЧЧ:ММ» и кнопки «Запустить сейчас» и «Отменить монтаж»" what="Старт: claude -p с сохранением session_id → Проверка ответа: успех или лимит Claude? → Ветка лимита: статус «Пауза», сохранение таймера сброса (5 часов) → Ожидание: таймер бота ИЛИ нажатие кнопки «Запустить сейчас» в Telegram → Возобновление: claude -p --resume session_id → Завершение задачи" -->

<figure class="scheme">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" role="img" aria-label="Схема работы бота: задача ставится на паузу при исчерпании лимита Claude и продолжается через --resume">
<title>Как бот ставит задачу на паузу при лимите и продолжает сессию через --resume</title>
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--line)"/></marker>
<marker id="ahA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--accent)"/></marker>
</defs>

<g stroke="var(--line)" stroke-width="2" fill="none">
<line x1="340" y1="115" x2="448" y2="115" marker-end="url(#ah)"/>
<line x1="750" y1="115" x2="858" y2="115" marker-end="url(#ah)"/>
<line x1="600" y1="170" x2="600" y2="288" marker-end="url(#ah)"/>
<line x1="600" y1="400" x2="600" y2="518" marker-end="url(#ah)"/>
</g>
<g stroke="var(--accent)" stroke-width="3" fill="none">
<line x1="750" y1="575" x2="858" y2="575" marker-end="url(#ahA)"/>
<line x1="1010" y1="520" x2="1010" y2="172" marker-end="url(#ahA)"/>
</g>

<text x="805" y="98" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">успех</text>
<text x="614" y="236" font-family="var(--font-body)" font-size="18" fill="var(--muted)">лимит</text>
<text x="1024" y="350" font-family="var(--font-body)" font-size="18" fill="var(--muted)">продолжаем</text>
<text x="1024" y="374" font-family="var(--font-body)" font-size="18" fill="var(--muted)">ту же сессию</text>

<g>
<rect x="40" y="60" width="300" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="70" cy="95" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/>
<text x="70" y="102" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">1</text>
<text x="100" y="102" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Старт</text>
<text x="60" y="134" font-family="var(--font-body)" font-size="18" fill="var(--muted)">claude -p, ответ в JSON</text>
<text x="60" y="158" font-family="var(--font-body)" font-size="18" fill="var(--muted)">session_id — на диск</text>
</g>

<g>
<rect x="450" y="60" width="300" height="110" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="480" cy="95" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/>
<text x="480" y="102" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">2</text>
<text x="510" y="102" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Проверка ответа</text>
<text x="470" y="134" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Успех или лимит Claude?</text>
<text x="470" y="158" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Читаем текст ответа</text>
</g>

<g>
<rect x="860" y="60" width="300" height="110" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="890" cy="95" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/>
<text x="890" y="102" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">6</text>
<text x="920" y="102" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Готово</text>
<text x="880" y="134" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Задача завершена</text>
<text x="880" y="158" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Итог приходит в чат</text>
</g>

<g>
<rect x="450" y="290" width="300" height="110" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="480" cy="325" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/>
<text x="480" y="332" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">3</text>
<text x="510" y="332" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Пауза</text>
<text x="470" y="364" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Статус «Пауза»</text>
<text x="470" y="388" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Таймер сброса: 5 часов</text>
</g>

<g>
<rect x="450" y="520" width="300" height="110" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="480" cy="555" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/>
<text x="480" y="562" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">4</text>
<text x="510" y="562" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Ожидание</text>
<text x="470" y="594" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Таймер бота или кнопка</text>
<text x="470" y="618" font-family="var(--font-body)" font-size="18" fill="var(--muted)">«Запустить сейчас»</text>
</g>

<g>
<rect x="860" y="520" width="300" height="110" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="3"/>
<circle cx="890" cy="555" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/>
<text x="890" y="562" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">5</text>
<text x="920" y="562" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Возобновление</text>
<text x="880" y="594" font-family="var(--font-body)" font-size="18" fill="var(--muted)">claude -p --resume</text>
<text x="880" y="618" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Готовые шаги не повторяет</text>
</g>

<text x="40" y="560" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Лимит ещё не сброшен?</text>
<text x="40" y="584" font-family="var(--font-body)" font-size="18" fill="var(--muted)">После нескольких попыток</text>
<text x="40" y="608" font-family="var(--font-body)" font-size="18" fill="var(--muted)">стоп и сообщение в чат</text>
</svg>
<figcaption>Схема работы бота: как автоматически ставить задачу на паузу при исчерпании лимита и продолжать сессию через --resume.</figcaption>
</figure>


У меня последний шаг появился не сразу. 18.10.2026 я добавил в статус монтажа кнопку «Запустить сейчас»: раннер не ждёт сброса и продолжает ту же сессию. По [журналу изменений](https://app.notion.com/p/KeyError-resume-3fddfdb148228133977ac4117a796892), если лимит на самом деле не сброшен, после 3 попыток задача встаёт в ошибку и ждёт кнопки «Продолжить».

## Как настроить резервный шлюз на API с жёстким дневным лимитом расходов?

Резерв включается только на ошибке лимита и выключается потолком расходов за сутки. Бот повторяет тот же вызов `claude` с API-ключом, считает, сколько потратил за день, и при достижении потолка перестаёт ходить в API. Так ты платишь за паузы подписки, а не за всю работу.

Как это сделано у моего мозг-бота с 28.10.2026, по [журналу изменений](https://app.notion.com/p/API-Sonnet-5-5-3-407dfdb1482281308e0bf82edf98efa7):

1. **Основной вызов по подписке.** `claude -p` от пользователя бота, без ключа в окружении.
2. **Ключ лежит отдельно.** В переменной `API_FALLBACK_KEY`, на счёте в Console $100 кредитов. Бот подставляет его только в повторный вызов.
3. **Модель дешевле.** Резерв идёт на `claude-sonnet-5-5`.
4. **Потолок в сутки.** `API_DAY_LIMIT`, по умолчанию $3, сутки по Москве.
5. **После потолка.** Отвечает второй мозг, моя база знаний, без вызова модели.
6. **Видно расход.** Под ответом из резерва бот ставит пометку, сколько потратил.
7. **Тяжёлое не трогает.** Облачные задачи остаются на подписке и в резерв не уходят.

<!-- img: type=scheme what="узлы и стрелки: вопрос Петра → claude -p по подписке → ответ; ветка «лимит» → claude -p с API_FALLBACK_KEY на Sonnet 5.5 → проверка «потрачено за сутки меньше $3?» → да: ответ с пометкой о расходе; нет: ответ из второго мозга" caption="Резерв мозг-бота: API включается только на лимите подписки и выключается потолком $3 в сутки." alt="подписка claude или api что выгоднее: схема резерва на API с дневным потолком" -->

<figure class="scheme">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 620" width="100%" role="img" aria-label="Схема резерва мозг-бота: вопрос идёт по подписке, на лимите включается API на Sonnet 5.5, при расходе меньше 3 долларов в сутки приходит ответ с пометкой, иначе отвечает второй мозг">
  <title>Резерв мозг-бота: API включается только на лимите подписки и выключается потолком $3 в сутки</title>
  <defs>
    <marker id="arrLine" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="var(--line)"/>
    </marker>
    <marker id="arrAccent" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="var(--accent)"/>
    </marker>
  </defs>

  <!-- Ряд 1: обычный путь -->
  <rect x="40" y="40" width="280" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <text x="180" y="88" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">Вопрос Петра</text>
  <text x="180" y="122" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">пишу боту</text>

  <rect x="390" y="40" width="360" height="110" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <text x="570" y="88" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">claude -p по подписке</text>
  <text x="570" y="122" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">без ключа в окружении</text>

  <rect x="880" y="40" width="280" height="110" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <text x="1020" y="88" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">Ответ</text>
  <text x="1020" y="122" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">лимит ещё не кончился</text>

  <line x1="320" y1="95" x2="388" y2="95" stroke="var(--line)" stroke-width="3" marker-end="url(#arrLine)"/>
  <line x1="750" y1="95" x2="878" y2="95" stroke="var(--line)" stroke-width="3" marker-end="url(#arrLine)"/>

  <!-- Ветка лимита -->
  <line x1="570" y1="150" x2="570" y2="233" stroke="var(--accent)" stroke-width="4" marker-end="url(#arrAccent)"/>
  <text x="595" y="198" font-family="var(--font-body)" font-size="19" fill="var(--accent)">лимит подписки</text>

  <rect x="390" y="235" width="360" height="130" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="3"/>
  <text x="570" y="283" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">claude -p с ключом API</text>
  <text x="570" y="317" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">API_FALLBACK_KEY</text>
  <text x="570" y="342" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">модель Sonnet 5.5</text>

  <line x1="570" y1="365" x2="570" y2="448" stroke="var(--accent)" stroke-width="4" marker-end="url(#arrAccent)"/>

  <!-- Проверка потолка -->
  <rect x="390" y="450" width="360" height="140" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="3"/>
  <text x="570" y="508" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">Потрачено за сутки</text>
  <text x="570" y="544" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="26" fill="var(--fg)">меньше $3?</text>

  <!-- Да -->
  <line x1="750" y1="520" x2="878" y2="520" stroke="var(--accent)" stroke-width="4" marker-end="url(#arrAccent)"/>
  <text x="814" y="506" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--accent)">да</text>

  <rect x="880" y="450" width="280" height="140" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <text x="1020" y="498" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Ответ с пометкой</text>
  <text x="1020" y="534" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">сколько потрачено</text>
  <text x="1020" y="558" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">за этот ответ</text>

  <!-- Нет -->
  <line x1="390" y1="520" x2="322" y2="520" stroke="var(--line)" stroke-width="3" marker-end="url(#arrLine)"/>
  <text x="356" y="506" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="22" fill="var(--fg)">нет</text>

  <rect x="40" y="450" width="280" height="140" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <text x="180" y="498" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Второй мозг</text>
  <text x="180" y="534" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">отвечает база знаний,</text>
  <text x="180" y="558" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">модель не вызывается</text>
</svg>
<figcaption>Резерв мозг-бота: API включается только на лимите подписки и выключается потолком $3 в сутки.</figcaption>
</figure>


Главная ловушка тут одна. Переменная `ANTHROPIC_API_KEY` в окружении бота держится только на время резервного вызова. Справка Anthropic предупреждает: если ключ задан, Claude Code берёт его вместо подписки. Оставил его в `.bashrc`, и вся работа поехала в оплату по API. Об этом я подробно писал в [статье про Claude Code в Telegram](/blog/claude-code-sotrudnik-telegram/).

Удобный счётчик для потолка: с `--output-format json` Claude Code кладёт в ответ поле `total_cost_usd`. Документация уточняет, что это оценка на стороне программы, и счёт она не заменяет. Для дневного потолка этой оценки хватает.

## Проверил на себе: как конвейер ii.systema держит двух автономных агентов на одной подписке

На моём сервере штаба с 2 ядрами и 4 ГБ памяти по одной подписке работают бот роликов и, с 18.10.2026, SEO-штаб: служба `ii-seo` пишет статьи через `claude -p` на Opus 5.5 за 10–25 минут. В каждом боте стоит очередь на одного Claude, у каждого запуска таймаут. Эту статью тоже написал он.

Первый раз в лимит я упёрся 01.10.2026. Первый монтаж из чата, ролик REEL-4, встал на шаге 4 из 7. По [журналу изменений](https://app.notion.com/p/3ecdfdb148228177b8a3e58a3b2e1e1b), одна подготовка дубля заняла около 16 минут. Монтаж просто оборвался, и всё, что Claude успел решить, пропало бы при новом запуске.

В тот же день я добавил две вещи. Кнопку «Продолжить»: раннер поднимает ту же сессию через `--resume`, Claude помнит скилл, сценарий и решения и не повторяет готовые шаги. И автоожидание: при лимите очередь встаёт на паузу, в статусе пишется «продолжу сам в ЧЧ:ММ». По [журналу](https://app.notion.com/p/Claude-3ecdfdb14822811da1a8ecc18d22b69a), три дубля, REEL-9, 8 и 7, в тот день продолжились сами после сброса лимита в 16:39. Я в это время был занят другим.

<!-- img: type=terminal cmds="whoami ;; claude --version ;; claude auth status ;; systemctl is-active ii-shtab ;; systemctl is-active ii-seo" caption="Сервер штаба: два бота работают от одного пользователя и одной подписки Claude Pro, без API-ключа." alt="лимиты claude code на сервере: два бота на одной подписке Pro" -->

![лимиты claude code на сервере: два бота на одной подписке Pro](/blog/pochemu-limit-claude-bystro-konchaetsya/img/terminal-4.jpg "Сервер штаба: два бота работают от одного пользователя и одной подписки Claude Pro, без API-ключа.")


Как у меня распределён лимит сейчас:

| Задача | Где выполняется | Как бережёт лимит |
|---|---|---|
| Разбор чужих роликов | Gemini | лимит Claude не тратит совсем |
| Разговор в темах штаба | Claude по подписке | своя сессия на тему, правила в CLAUDE.md |
| Сценарии и статьи | Claude Opus 5.5 по подписке | по одной в очереди, таймаут |
| Монтаж | Claude на домашнем компьютере | пауза на лимите и `--resume` |
| Отбор тем из трендов | Claude ночью по расписанию | не делит дневное окно |
| Мозг-бот в лимите | API на Sonnet 5.5 | потолок $3 в сутки |

Что сломалось по дороге, честно:

- **Монтаж обрывался на лимите.** Лечится сохранённой сессией, автоожиданием и кнопкой «Продолжить».
- **Раннер падал при перезапуске во время паузы.** Ошибка в коде продолжения съела три автоповтора у REEL-61, ролик встал в ошибку. Исправил 18.10.2026, кнопка «Продолжить» осталась страховкой.
- **Два Claude сразу съели бы память сервера.** Очередь на одного, остальные задачи ждут.
- **Зависший запуск держал бы очередь вечно.** Таймаут убивает процесс, бот пишет в тему, что случилось.
- **Ночные задачи мешали бы дневным.** Отбор тем стоит на раннее утро, чтобы не делить одно окно лимита с работой.

Главный вывод из месяца работы: лимит подписки ты почувствуешь точно, если работаешь с агентом всерьёз. Тяжёлое у меня идёт по очереди и с автопродолжением, лёгкое отвечает сразу, а простая обработка вообще ушла с Claude. Вся система целиком описана в [кейсе ii.systema](/iisystema/).

## С чего начать, если лимит кончается уже сегодня?

Начни с трёх вещей, они не требуют кода. Открой отдельный чат на каждую задачу. Сократи инструкции проекта до одной страницы. Посмотри в настройках аккаунта, сколько осталось в текущем окне и в недельной квоте, справка Anthropic показывает там обе шкалы.

Дальше, если работаешь с Claude Code:

1. Перед длинной задачей сделай `/clear`, а посреди неё `/compact`.
2. Вынеси подробные правила из CLAUDE.md в навыки.
3. Простую обработку отдай модели дешевле: Haiku или Gemini.
4. Если задачи запускает бот, добавь сохранение сессии, паузу на лимите и `--resume`.
5. Резерв на API ставь последним и только с дневным потолком.

Если хочешь, чтобы ИИ работал на твой бизнес весь день, а не до обеда, напиши слово «система» мне в личку [t.me/solovarov](https://t.me/solovarov). Посмотрим, какие рутины в твоей работе можно автоматизировать и как выстроить схему без лишних трат на лимиты и токены.
