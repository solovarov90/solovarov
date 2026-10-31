---
title: Как запустить рекламу в Meta через Claude и Pipeboard без Ads Manager
cover_title: Реклама Meta через Claude без Ads Manager
description: Как настроить рекламу Meta через нейросеть: Claude с коннектором Pipeboard собрал мне кампании, креативы и лендинг с пикселем. Цифры за 2 дня и что сломалось.
slug: reklama-meta-cherez-claude-pipeboard
date: 2026-10-31
updated: 2026-10-31
cluster: Продажи и заявки
type: Кейс
cover: /blog/reklama-meta-cherez-claude-pipeboard/img/cover.jpg
cover_alt: Как настроить рекламу Meta через нейросеть Claude и коннектор Pipeboard без Ads Manager
cta: Я подключу Claude к твоему рекламному кабинету, соберу лендинг с пикселем и кодовыми словами и первую кампанию из твоих роликов. Включаешь рекламу ты сам, одним «да».
faq:
  - q: Может ли Claude списать лишние деньги с карты без моего ведома?
    a: У меня правило: Claude создаёт всё на паузе, а включает рекламу только после моего «да». Дневной бюджет кампании задаю и проверяю я, у меня это 300 000 ₫ в день. Карту и токены я ввожу сам, Claude их не видит.
  - q: Нужно ли оплачивать API Claude или достаточно обычной подписки?
    a: Мне хватило подписки. Коннектор Pipeboard подключается в claude.ai как обычный коннектор, и дальше вся работа идёт в чате. Отдельно я плачу только Pipeboard, когда бесплатных запросов перестало хватать.
  - q: Какие лимиты действуют на бесплатном тарифе Pipeboard?
    a: На странице тарифов Pipeboard на 31 октября 2026 года бесплатный план даёт 30 запросов к кабинету в неделю и 2 рекламных кабинета. Pro стоит 29,90 доллара в месяц, запросы без лимита, 3 кабинета, первые 7 дней бесплатно. Мне 30 запросов хватило на один день работы.
  - q: Почему привязка Instagram-аккаунта в Meta может отваливаться при настройке через ИИ?
    a: Объявление от имени Instagram-аккаунта можно сделать, только если аккаунт привязан к странице Facebook. У меня @ii.systema не был привязан, и рекламу из рилсов собрать не получалось. Я привязал его в приложении Instagram за минуту, а переподключать Pipeboard не понадобилось.
  - q: Как отслеживать конверсии, если лид засчитывается по клику в Telegram?
    a: Кнопка «Написать в Telegram» на лендинге отправляет событие Lead в пиксель Meta и цель в Метрику. У каждого объявления своя метка, и в личку человек приходит со своим кодовым словом, так я вижу, с какой рекламы он пришёл. 28 октября я перевёл лид на реальную подписку на канал, потому что клики оказались слишком дешёвыми.
  - q: Зачем использовать Claude для рекламы, если есть готовые автоправила в Facebook Ads?
    a: Автоправила включают и выключают то, что уже собрано. Claude собирает саму кампанию, пишет тексты, верстает креативы, ставит метки и читает статистику по моей просьбе. Автоправила можно оставить, они друг другу не мешают.
  - q: Сколько времени занимает запуск кампании через Claude?
    a: Первую кампанию с лендингом, пикселем и тремя креативами Claude собрал 27 октября 2026 года, в тот же день она пошла в показы. Вторую, из четырёх рилсов, он собрал 28 октября. От меня в обоих случаях были проверка и «да».
sources:
  - title: "Журнал изменений: Реклама Meta: Claude управляет кабинетом через Pipeboard"
    url: https://app.notion.com/p/Meta-Claude-Pipeboard-407dfdb14822816aa374f80ad22ce849
    note: подключение коннектора, правило «всё на паузе», лимит бесплатного плана и лид-формы, 27–28.10.2026
  - title: "Журнал изменений: Кампания «Внедрение ИИ — Лиды»"
    url: https://app.notion.com/p/Telegram-407dfdb1482281a1ac18db9c3de4ff29
    note: устройство лендинга и пикселя, цифры за 27–28.10.2026
  - title: "Журнал изменений: Рилсы ii.systema в рекламе: Instagram привязан к странице, 4 ролика"
    url: https://app.notion.com/p/ii-systema-Instagram-4-407dfdb1482281048faeca1dc647c77a
    note: привязка Instagram к странице и кампания из рилсов, 28.10.2026
  - title: "Журнал изменений: Креативы на фото Петра"
    url: https://app.notion.com/p/407dfdb14822817dbe57d7b3514a5f5f
    note: третья кампания на фото из фотобанка, 28.10.2026
  - title: Тарифы Pipeboard
    url: https://pipeboard.co/pricing
    note: лимиты бесплатного плана и цена Pro, проверено 31.10.2026
  - title: Условия лид-рекламы Meta
    url: https://www.facebook.com/ads/leadgen/tos
    note: страница, где администратор страницы принимает условия лид-форм
  - title: Кейс ii.systema на petrsolovarov.ru
    url: https://petrsolovarov.ru/iisystema/
    note: конвейер роликов, из которого взяты рилсы для рекламы
  - title: Пошаговая настройка MCP-коннектора Claude для Instagram
    url: https://app.notion.com/p/MCP-Claude-Instagram-3f6dfdb148228172a655c1a02fb08025
    note: материал к ролику о подключении Claude к аналитике Instagram, 21.10.2026
---

Запустить рекламу в Meta можно прямо из чата с Claude, не открывая Ads Manager: нейросеть подключается к рекламному кабинету через коннектор Pipeboard. Claude сам собирает кампанию, пишет тексты, верстает креативы и ставит таргетинг, а я проверяю и говорю «да». Так я запустил 27 октября 2026 года первую кампанию на свою услугу внедрения ИИ: за два дня она дала 40 нажатий на кнопку Telegram по 9 800 ₫ за каждое.

Ниже разбираю, как настроить рекламу Meta через нейросеть по шагам: что подключить, что Claude делает сам, как связать рекламу с лендингом и пикселем и что у меня сломалось за первые два дня. Все цифры взяты из моего журнала изменений в Notion за 27–28 октября.

## Что такое Pipeboard и как Claude получает доступ к кабинету Meta?

Pipeboard это коннектор, через который Claude получает доступ к рекламному кабинету Meta. Подключаешь его один раз, входишь через Facebook, и дальше Claude видит кампании, группы объявлений, креативы и статистику. Ads Manager при этом открывать не нужно.

Коннектор работает по протоколу MCP. Если по-простому, это розетка, через которую нейросеть берёт инструменты у другого сервиса. Claude не нажимает кнопки в кабинете за тебя. Он вызывает официальные команды Meta: «создай кампанию», «загрузи картинку», «покажи расход за вчера».

Что умеет связка, по моему журналу на 27 октября 2026 года:

- создавать кампании, группы объявлений, креативы и сами объявления;
- загружать картинки и делать объявления из уже вышедших постов Instagram;
- читать статистику и превью объявлений;
- менять бюджет, статус и метки ссылок.

Я подключил Pipeboard в claude.ai по своей подписке. Похожую связку я уже делал для аналитики Instagram, там Claude через коннектор читает статистику роликов. Пошаговый гайд лежит в [материалах к роликам](https://video.petrsolovarov.ru/materials).

<!-- img: type=screenshot url=https://pipeboard.co/pricing caption="Тарифы Pipeboard: бесплатный план с 30 запросами в неделю и Pro без лимита, на 31 октября 2026 года." alt="pipeboard meta ads claude: тарифы коннектора" -->

![pipeboard meta ads claude: тарифы коннектора](/blog/reklama-meta-cherez-claude-pipeboard/img/screenshot-1.jpg "Тарифы Pipeboard: бесплатный план с 30 запросами в неделю и Pro без лимита, на 31 октября 2026 года.")


## Что нужно настроить до первого запуска рекламы через ИИ?

До первого запуска нужны пять вещей: рекламный кабинет Meta с картой, страница Facebook, привязанный к ней Instagram, лендинг с пикселем и правило, что Claude ничего не включает сам. Без последнего пункта я бы связку не запускал.

Пиксель это кусочек кода на сайте, который сообщает Meta, что человек сделал нужное действие: открыл страницу, нажал кнопку. По этим сигналам Meta учится показывать рекламу тем, кто похож на нажавших.

Чеклист перед стартом:

1. **Кабинет и оплата.** Карту и реквизиты вводишь сам. У меня кабинет считает в донгах (VND), отсюда значок ₫ во всех цифрах статьи.
2. **Страница Facebook.** От её имени идут объявления. Она же принимает условия лид-рекламы, если хочешь формы прямо в Meta.
3. **Instagram, привязанный к странице.** Без этого объявления из рилсов не собрать, на этом я споткнулся, подробности ниже.
4. **Лендинг с пикселем.** У меня это страница [petrsolovarov.ru/ai/](/ai/) с политикой конфиденциальности, пиксель стоит на всём сайте.
5. **Правило паузы.** Claude создаёт всё на паузе. Включение только по моему «да». Токены и пароли ввожу я, Claude их не видит.

Правило паузы записано у меня в журнале изменений с первого дня, 27 октября 2026 года. Оно снимает главный страх: нейросеть не потратит деньги без тебя, потому что кнопку включения нажимаешь ты.

## Как Claude сам собирает кампании, группы объявлений и креативы?

Я пишу задачу словами, Claude предлагает структуру кампании, я её поправляю, и он собирает всё в кабинете на паузе. Тексты объявлений и сами картинки он тоже делает сам. Мне остаётся посмотреть превью и сказать «да».

Как это выглядело на первой кампании «Внедрение ИИ — Лиды» 27 октября:

1. **Задача.** Я написал, что продаю внедрение ИИ, веду людей на лендинг /ai/ и хочу, чтобы они писали мне в Telegram.
2. **Аудитория.** Claude предложил русскоязычных людей в 14 странах, 25–55 лет, с интересами ИИ, CRM, автоматизация и владельцы бизнеса. Бюджет 300 000 ₫ в день на всю кампанию.
3. **Креативы.** Три картинки 1080×1350 по моим кейсам: «Ночной бот», «Контент-завод» (это конвейер [ii.systema](/iisystema/)) и «База знаний» (кейс [VetCTschool](/vetctschool/)). Claude сверстал их как html-страницы и снял скриншотом, поэтому шрифты и цифры на них ровные.
4. **Тексты и метки.** К каждому объявлению свой текст и своя метка в ссылке. Метка это хвост адреса вроде `utm_content=night_bot`, по нему видно, с какого объявления пришёл человек.
5. **Проверка.** Claude показал превью, я посмотрел и включил.

<!-- img: type=scheme caption="Как Claude превращает короткий бриф в готовую черновую кампанию внутри Meta Ads через коннектор Pipeboard." alt="управление рекламой facebook через claude: создание кампании в чате" was="Компьютер Петра, claude.ai: диалог, где Claude через коннектор Pipeboard создаёт кампанию «Внедрение ИИ — Лиды» на паузе и показывает список объявлений с превью; номер кабинета и оплату закрыть" what="Текстовая задача в чате → Claude: подбор аудитории и бюджета → Claude: верстка креативов и UTM-меток → Превью объявлений в диалоге → Подтверждение от пользователя → Pipeboard API → Черновик кампании на паузе в Meta Ads" -->

<figure class="scheme">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="100%" role="img" aria-label="Схема: задача в чате, Claude подбирает аудиторию и бюджет, верстает креативы и метки, показывает превью, после подтверждения через Pipeboard API создаётся черновик кампании на паузе в Meta Ads">
  <title>Как Claude превращает короткий бриф в черновую кампанию в Meta Ads</title>
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M1 1 L9 5 L1 9 Z" fill="var(--line)" stroke="var(--line)" stroke-width="1" stroke-linejoin="round"/>
    </marker>
    <marker id="arrA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M1 1 L9 5 L1 9 Z" fill="var(--accent)" stroke="var(--accent)" stroke-width="1" stroke-linejoin="round"/>
    </marker>
  </defs>

  <!-- Стрелки -->
  <g fill="none" stroke="var(--line)" stroke-width="2.5" marker-end="url(#arr)">
    <line x1="268" y1="125" x2="319" y2="125"/>
    <line x1="573" y1="125" x2="624" y2="125"/>
    <line x1="878" y1="125" x2="929" y2="125"/>
    <line x1="1058" y1="210" x2="1058" y2="284"/>
    <line x1="933" y1="375" x2="882" y2="375"/>
  </g>
  <line x1="628" y1="375" x2="577" y2="375" fill="none" stroke="var(--accent)" stroke-width="3.5" marker-end="url(#arrA)"/>

  <!-- 1 -->
  <rect x="18" y="40" width="250" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <circle cx="52" cy="76" r="18" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
  <text x="52" y="83" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">1</text>
  <text x="80" y="82" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Я</text>
  <text x="42" y="130" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Задача в чате</text>
  <text x="42" y="164" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Продаю внедрение ИИ,</text>
  <text x="42" y="188" font-family="var(--font-body)" font-size="18" fill="var(--muted)">хочу заявки в Telegram</text>

  <!-- 2 -->
  <rect x="323" y="40" width="250" height="170" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <circle cx="357" cy="76" r="18" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
  <text x="357" y="83" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">2</text>
  <text x="385" y="82" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Claude</text>
  <text x="347" y="130" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Аудитория</text>
  <text x="347" y="164" font-family="var(--font-body)" font-size="18" fill="var(--muted)">14 стран, 25–55 лет,</text>
  <text x="347" y="188" font-family="var(--font-body)" font-size="18" fill="var(--muted)">300 000 ₫ в день</text>

  <!-- 3 -->
  <rect x="628" y="40" width="250" height="170" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <circle cx="662" cy="76" r="18" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
  <text x="662" y="83" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">3</text>
  <text x="690" y="82" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Claude</text>
  <text x="652" y="130" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Креативы</text>
  <text x="652" y="164" font-family="var(--font-body)" font-size="18" fill="var(--muted)">3 картинки 1080×1350,</text>
  <text x="652" y="188" font-family="var(--font-body)" font-size="18" fill="var(--muted)">своя метка в ссылке</text>

  <!-- 4 -->
  <rect x="933" y="40" width="250" height="170" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <circle cx="967" cy="76" r="18" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
  <text x="967" y="83" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">4</text>
  <text x="995" y="82" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Claude</text>
  <text x="957" y="130" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Превью</text>
  <text x="957" y="164" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Вижу, как будут</text>
  <text x="957" y="188" font-family="var(--font-body)" font-size="18" fill="var(--muted)">выглядеть объявления</text>

  <!-- 5 -->
  <rect x="933" y="290" width="250" height="170" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <circle cx="967" cy="326" r="18" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
  <text x="967" y="333" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">5</text>
  <text x="995" y="332" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Я</text>
  <text x="957" y="380" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Моё «да»</text>
  <text x="957" y="414" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Смотрю превью и</text>
  <text x="957" y="438" font-family="var(--font-body)" font-size="18" fill="var(--muted)">пишу «да»</text>

  <!-- 6 -->
  <rect x="628" y="290" width="250" height="170" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
  <circle cx="662" cy="326" r="18" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
  <text x="662" y="333" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">6</text>
  <text x="690" y="332" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Коннектор</text>
  <text x="652" y="380" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Pipeboard API</text>
  <text x="652" y="414" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Передаёт кампанию</text>
  <text x="652" y="438" font-family="var(--font-body)" font-size="18" fill="var(--muted)">в Meta</text>

  <!-- 7 -->
  <rect x="323" y="290" width="250" height="170" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="3"/>
  <circle cx="357" cy="326" r="18" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
  <text x="357" y="333" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--accent)">7</text>
  <text x="385" y="332" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Meta Ads</text>
  <text x="347" y="380" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Черновик</text>
  <text x="347" y="414" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Кампания на паузе,</text>
  <text x="347" y="438" font-family="var(--font-body)" font-size="18" fill="var(--muted)">включаю сам</text>
</svg>
<figcaption>Как Claude превращает короткий бриф в готовую черновую кампанию внутри Meta Ads через коннектор Pipeboard.</figcaption>
</figure>


Как я формулирую задачу, чтобы Claude собрал кампанию с первого раза:

- **Что продаю и кому.** Одна фраза про услугу и одна про того, кто её покупает.
- **Куда веду.** Адрес лендинга и что на нём считается результатом: нажатие, заявка, подписка.
- **Из чего делать креативы.** Мои кейсы, ролики или фото, а не картинки из интернета.
- **Сколько тратить.** Дневной бюджет и на сколько дней тест.
- **Что нельзя.** Обещать результат в цифрах, называть конкурентов, включать без меня.

Последний пункт важнее остальных. Claude честно спросит, если чего-то не хватает, но границы лучше задать заранее. Тогда первое превью уже похоже на то, что ты хотел, и правок остаётся одна-две.

28 октября Claude собрал вторую кампанию, «Внедрение ИИ — Рилсы ii.systema». Он сам выбрал 4 моих рилса с самыми большими просмотрами за 90 дней и сделал объявления из самих постов. Так у рекламы сохраняются лайки и комментарии ролика, она выглядит живой. Самый большой из них, ролик про файл AGENTS.md, набрал к тому моменту 48 285 просмотров.

В тот же день Claude сделал три креатива на моих фото из фотобанка и завёл под них отдельную кампанию, на паузе. Отдельную он предложил сам, и правильно: бюджет первой кампании делится между её объявлениями, и новая группа забрала бы деньги у той, что уже работала.

## Как связать рекламу с лендингом, пикселем и кодовыми словами?

Связка у меня такая: объявление ведёт на лендинг /ai/, кнопка «Написать в Telegram» отправляет событие в пиксель и открывает мою личку, а в личке человек пишет кодовое слово своего объявления. Так каждое сообщение в Telegram привязано к конкретной рекламе.

<!-- img: type=scheme what="объявление Meta (метка utm_content) → лендинг petrsolovarov.ru/ai/ → кнопка «Написать в Telegram» → событие Lead в пиксель Meta и цель в Метрике → личка t.me/solovarov с кодовым словом объявления → разговор; подписать стрелку от пикселя обратно к объявлению: «Meta учится на нажатиях»" caption="Путь человека от рекламы до лички: метка объявления превращается в кодовое слово, а пиксель сообщает Meta о каждом нажатии." alt="запуск таргета через нейросеть: схема реклама, лендинг, пиксель, Telegram" -->

<figure class="scheme">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600" width="100%" role="img" aria-label="Путь человека от рекламы до лички: объявление Meta, лендинг, кнопка в Telegram, пиксель и Метрика, личка с кодовым словом, разговор">
<title>Путь человека от рекламы до лички</title>
<defs>
<marker id="arrA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker>
<marker id="arrL" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--line)"/></marker>
</defs>

<g fill="none" stroke-width="3">
<path d="M350 110 H438" stroke="var(--accent)" marker-end="url(#arrA)"/>
<path d="M760 110 H848" stroke="var(--accent)" marker-end="url(#arrA)"/>
<path d="M1010 170 V248" stroke="var(--accent)" marker-end="url(#arrA)"/>
<path d="M1010 370 V438" stroke="var(--accent)" marker-end="url(#arrA)"/>
<path d="M920 170 V210 H600 V248" stroke="var(--line)" marker-end="url(#arrL)"/>
<path d="M440 310 H190 V172" stroke="var(--line)" stroke-dasharray="8 6" marker-end="url(#arrL)"/>
</g>

<text x="760" y="200" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">событие Lead</text>
<text x="315" y="298" text-anchor="middle" font-family="var(--font-body)" font-size="18" fill="var(--muted)">Meta учится на нажатиях</text>

<g>
<rect x="30" y="50" width="320" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="64" cy="86" r="18" fill="var(--accent)"/>
<text x="64" y="93" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--surface)">1</text>
<text x="96" y="94" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Объявление Meta</text>
<text x="96" y="125" font-family="var(--font-body)" font-size="18" fill="var(--muted)">метка utm_content</text>
<text x="96" y="150" font-family="var(--font-body)" font-size="18" fill="var(--muted)">у каждого своя</text>
</g>

<g>
<rect x="440" y="50" width="320" height="120" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="474" cy="86" r="18" fill="var(--accent)"/>
<text x="474" y="93" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--surface)">2</text>
<text x="506" y="94" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Лендинг /ai/</text>
<text x="506" y="125" font-family="var(--font-body)" font-size="18" fill="var(--muted)">petrsolovarov.ru/ai/</text>
<text x="506" y="150" font-family="var(--font-body)" font-size="18" fill="var(--muted)">принимает метку</text>
</g>

<g>
<rect x="850" y="50" width="320" height="120" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="884" cy="86" r="18" fill="var(--accent)"/>
<text x="884" y="93" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--surface)">3</text>
<text x="916" y="94" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Кнопка в Telegram</text>
<text x="916" y="125" font-family="var(--font-body)" font-size="18" fill="var(--muted)">«Написать в Telegram»</text>
<text x="916" y="150" font-family="var(--font-body)" font-size="18" fill="var(--muted)">нажимает человек</text>
</g>

<g>
<rect x="440" y="250" width="320" height="120" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<text x="470" y="294" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Пиксель и Метрика</text>
<text x="470" y="325" font-family="var(--font-body)" font-size="18" fill="var(--muted)">событие Lead в пикселе</text>
<text x="470" y="350" font-family="var(--font-body)" font-size="18" fill="var(--muted)">цель в Метрике</text>
</g>

<g>
<rect x="850" y="250" width="320" height="120" rx="10" fill="var(--surface)" stroke="var(--accent)" stroke-width="2"/>
<circle cx="884" cy="286" r="18" fill="var(--accent)"/>
<text x="884" y="293" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--surface)">4</text>
<text x="916" y="294" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Личка в Telegram</text>
<text x="916" y="325" font-family="var(--font-body)" font-size="18" fill="var(--muted)">t.me/solovarov</text>
<text x="916" y="350" font-family="var(--font-body)" font-size="18" fill="var(--muted)">с кодовым словом</text>
</g>

<g>
<rect x="850" y="440" width="320" height="120" rx="10" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>
<circle cx="884" cy="476" r="18" fill="var(--accent)"/>
<text x="884" y="483" text-anchor="middle" font-family="var(--font-display)" font-weight="600" font-size="20" fill="var(--surface)">5</text>
<text x="916" y="484" font-family="var(--font-display)" font-weight="600" font-size="24" fill="var(--fg)">Разговор</text>
<text x="916" y="515" font-family="var(--font-body)" font-size="18" fill="var(--muted)">слово показывает,</text>
<text x="916" y="540" font-family="var(--font-body)" font-size="18" fill="var(--muted)">с какой рекламы пришёл</text>
</g>
</svg>
<figcaption>Путь человека от рекламы до лички: метка объявления превращается в кодовое слово, а пиксель сообщает Meta о каждом нажатии.</figcaption>
</figure>


Что где стоит, по журналу на 27 октября 2026 года:

- **Лид** это нажатие кнопки «Написать в Telegram». Оно отправляет событие Lead в пиксель, цель в Яндекс Метрику и Google Analytics и переводит человека в t.me/solovarov.
- **Кодовые слова** зависят от метки объявления: «бот24», «контент», «база», без метки «разбор». В личке сразу видно, какой креатив привёл человека.
- **Пиксель** стоит на всём сайте petrsolovarov.ru, поэтому одна настройка работает для всех кампаний.

Кодовое слово я взял из своих роликов. Там зритель пишет «система» в комментариях и получает инструкцию в директ, как это устроено, я разобрал в статье [про автоответ по кодовому слову](/blog/avtootvet-kodovoe-slovo/). В рекламе тот же приём работает в личке: человеку не надо объяснять, кто он и откуда, он просто пишет слово.

## Проверил на себе: кампания «Внедрение ИИ — Лиды», цена лида и поломки

За 27–28 октября 2026 года первая кампания потратила 391 606 ₫, это около 15 долларов. Она дала 372 клика и 40 лидов, один из них мой тестовый. Лид обошёлся примерно в 9 800 ₫.

<div class="figures">
<div><strong>40</strong><span>нажатий «Написать в Telegram» за 27–28 октября</span></div>
<div><strong>≈ 9 800 ₫</strong><span>за одно нажатие, около 15 долларов на все</span></div>
<div><strong>372</strong><span>клика при расходе 391 606 ₫</span></div>
<div><strong>12,5%</strong><span>кликабельность лучшего креатива «Ночной бот»</span></div>
</div>

Креативы отработали очень по-разному:

| Креатив | Расход | Лиды | Цена лида |
|---|---|---|---|
| Ночной бот | 357 591 ₫ | 38 | 9 410 ₫ |
| Контент-завод | остаток бюджета | 2 | 14 060 ₫ |
| База знаний | 5 896 ₫ | 0 | нет |

Почти весь бюджет Meta отдала «Ночному боту». У него 343 клика и кликабельность 12,5%, то есть из ста человек, увидевших объявление, кликнули двенадцать. Два других креатива Meta почти не показывала.

<!-- img: type=photo what="Пётр за ноутбуком в тёмном интерьере, работает с рекламой" caption="Так выглядит моя работа с рекламой: чат с Claude, превью объявлений и одно «да»." -->

![Так выглядит моя работа с рекламой: чат с Claude, превью объявлений и одно «да».](/blog/reklama-meta-cherez-claude-pipeboard/img/photo-4.jpg "Так выглядит моя работа с рекламой: чат с Claude, превью объявлений и одно «да».")


Теперь честно, что эти 40 лидов значат. Лид здесь это нажатие кнопки. Оплаты и даже сообщения за ним может не быть. Когда я сверил нажатия с личкой, оказалось, что писать доходят далеко не все. 28 октября я решил считать лидом реальную подписку на канал @solovarovp, потому что клик по кнопке давал дешёвые лиды, которые не равны разговорам. Сколько стоит подписка из рекламы, я напишу, когда наберётся неделя цифр.

Вывод для себя: дешёвый лид в отчёте Meta ещё ничего не говорит. Меряй то действие, после которого с человеком можно поговорить.

## Что сломалось: лимиты бесплатного Pipeboard, лид-формы и привязка Instagram?

За два дня сломались три вещи, и все три на стыках: лимит тарифа, условия лид-рекламы и привязка Instagram к странице. Ни одна не связана с самим Claude. Все три чинятся за минуты, если знать, где искать.

**1. Кончился бесплатный лимит Pipeboard.** Бесплатный план даёт 30 запросов к кабинету в неделю, по [странице тарифов](https://pipeboard.co/pricing) на 31 октября 2026 года. Каждое действие Claude в кабинете это запрос: создать группу, загрузить картинку, проверить статус. 28 октября лимит кончился посреди сборки кампании из рилсов, все запросы падали с ошибкой «weekly limit on your Free plan». Решение: Pro за 29,90 доллара в месяц, запросы без лимита, 3 кабинета, первые 7 дней бесплатно.

**2. Не создались лид-формы Meta.** Лид-форма это анкета внутри Facebook или Instagram, человек оставляет контакт, не уходя на сайт. Claude попробовал её создать и получил ошибку 1815089: страница не приняла [условия лид-рекламы](https://www.facebook.com/ads/leadgen/tos). Принимаются они на отдельной странице Meta от имени страницы, через коннектор этого не сделать. Я не стал разбираться в тот же день и перешёл на лид через пиксель на сайте. Для моей воронки это даже удобнее: человек сразу попадает в Telegram.

**3. Instagram не был привязан к странице.** Для объявлений из рилсов нужен Instagram-аккаунт, привязанный к странице Facebook. У меня @ii.systema висел отдельно, и Claude не мог сделать объявление из поста. Я привязал его в приложении Instagram: «Редактировать профиль» → «Страница» → «Подключить». Переподключать Pipeboard не понадобилось, Claude сразу увидел аккаунт.

Ещё одна вещь, которая поломкой не считается, но время съела. Два рилса из четырёх Meta одобрила сразу, а два ушли на проверку. Claude тут ничего не ускорит, проверку делает Meta.

Как это у меня закрыто:

- каждая поломка и решение записываются строкой в журнал изменений в Notion;
- правило паузы держит всё новое выключенным, пока я не проверю.

## Сколько стоит такая автоматизация таргета по сравнению с таргетологом?

Моя связка стоит подписку Claude и Pipeboard Pro за 29,90 доллара в месяц, плюс рекламный бюджет, который ты платишь Meta в любом случае. Первые 7 дней Pipeboard бесплатны, а для пробы хватит и бесплатного плана на 30 запросов в неделю.

Цен таргетологов я не собирал, поэтому сравню по работе, а не по деньгам:

| Что нужно сделать | Через Claude и Pipeboard | Руками в Ads Manager |
|---|---|---|
| Собрать кампанию и группы | пишешь задачу словами, Claude собирает | заполняешь формы сам или платишь специалисту |
| Креативы | Claude верстает картинки по твоим кейсам | дизайнер или Canva |
| Объявления из рилсов | Claude сам выбирает ролики по просмотрам | ищешь и добавляешь руками |
| Метки и кодовые слова | ставятся к каждому объявлению сразу | легко забыть |
| Отчёт | спрашиваешь в чате «что вчера» | открываешь кабинет и строишь отчёт |
| Решение включать | твоё «да» | твоё или специалиста |

Чего связка не заменяет: понимания, что ты продаёшь и кому. Claude соберёт кампанию за минуты, но оффер, лендинг и то, что считать лидом, решаешь ты. У меня самое важное решение двух дней, что клик не равен разговору, принял я сам, глядя на личку.

## Кому подходит запуск рекламы через Claude, а кому лучше остаться в Ads Manager?

Связка подходит тем, кто сам ведёт рекламу небольшим бюджетом и хочет запускать и проверять связки быстро: эксперт, студия, школа, клиника. Если у тебя десятки кампаний, отдельный отдел и сложные правила ставок, Ads Manager и живой специалист пока надёжнее.

Подходит, если:

- у тебя есть готовые материалы: ролики с просмотрами, кейсы, фото;
- лендинг и пиксель уже стоят или ты готов их поставить;
- ты хочешь сам говорить «да» каждой кампании;
- бюджет небольшой, и платить специалисту за каждую новую связку невыгодно.

Лучше остаться в Ads Manager, если:

- ты ни разу не запускал рекламу и не понимаешь, что такое цель кампании и пиксель, сначала разберись руками;
- у тебя ниша со строгой модерацией Meta, где каждое объявление приходится согласовывать вручную;
- в кабинете работает команда, и изменения из чата могут столкнуться с чужими.

Я пришёл к этой связке, потому что у меня уже был конвейер роликов. Как он устроен, я разобрал в статье [про медиа-конвейер на ИИ](/blog/media-konveyer-na-ii/). Ролики, которые набрали просмотры в органике, стали готовыми креативами, а Claude просто забрал из них лучшие.

Если хочешь автоматизировать рекламу и завязать заявки на ИИ без найма новых людей, напиши мне слово «система» в личку [t.me/solovarov](https://t.me/solovarov). Разберём твою воронку за 30 минут и наметим, как может выглядеть пилот.
