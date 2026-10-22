// Цели для Яндекс.Метрики и события для Google Analytics.
// Счётчики подключены в <head> страниц; здесь только отправка событий.
(function () {
    var YM_ID = 113666612;

    function send(name, params) {
        params = params || {};
        params.page = location.pathname;
        try { if (window.ym) ym(YM_ID, 'reachGoal', name, params); } catch (e) { }
        try { if (window.gtag) gtag('event', name, params); } catch (e) { }
    }

    document.addEventListener('click', function (e) {
        var el = e.target.closest ? e.target.closest('a, button') : null;
        if (!el) return;

        var card = el.closest('.project-card');
        var project = card ? card.getAttribute('data-project') : undefined;
        var href = el.getAttribute('href') || '';

        if (el.classList.contains('project-expand-btn')) {
            // считаем только раскрытие, не сворачивание
            if (card && !card.classList.contains('expanded')) send('case_expand', { project: project });
        } else if (el.classList.contains('project-link-btn')) {
            send('case_open', { project: project, href: href });
        } else if (el.classList.contains('back')) {
            send('back_home');
        } else if (href.indexOf('case.smart-posting.ru') !== -1) {
            send('case_site_click', { project: project });
        } else if (href.indexOf('t.me/') !== -1 && !el.hasAttribute('onclick')) {
            send('telegram_click', { target: href.replace(/^https?:\/\/t\.me\//, '').split('?')[0] });
        }
    }, { passive: true });

    // Глубина прокрутки: 50% и 90%, по одному разу за визит
    var sent = {};
    var ticking = false;

    function checkDepth() {
        ticking = false;
        var doc = document.documentElement;
        var max = doc.scrollHeight - window.innerHeight;
        if (max <= 0) return;
        var pct = (window.scrollY / max) * 100;
        [50, 90].forEach(function (mark) {
            if (pct >= mark && !sent[mark]) {
                sent[mark] = true;
                send('scroll_' + mark);
            }
        });
    }

    window.addEventListener('scroll', function () {
        if (!ticking) {
            ticking = true;
            requestAnimationFrame(checkDepth);
        }
    }, { passive: true });
})();
