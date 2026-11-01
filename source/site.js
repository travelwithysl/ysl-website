/* Shared behaviour for every page: mobile menu, nav shadow, gentle reveals, tour rail, filters. */
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // mobile menu
  var btn = document.querySelector('.menu-btn'), links = document.getElementById('navLinks');
  if (btn && links) {
    function setMenu(open) {
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      links.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    }
    btn.addEventListener('click', function () { setMenu(btn.getAttribute('aria-expanded') !== 'true'); });
    links.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    addEventListener('resize', function () { if (innerWidth > 960) setMenu(false); });
  }

  // nav shadow once the page scrolls
  var nav = document.querySelector('.site-nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', scrollY > 8); };
    addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }

  // reveal: content is always visible; items below the fold rise slightly into place
  if (!reduce && 'IntersectionObserver' in window) {
    var items = [].slice.call(document.querySelectorAll('.rv'));
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.remove('rv-pending'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top > innerHeight) { el.classList.add('rv-pending'); io.observe(el); }
    });
  }

  // tour rail controls
  [].forEach.call(document.querySelectorAll('[data-rail]'), function (wrap) {
    var rail = wrap.querySelector('.rail'), prev = wrap.querySelector('[data-prev]'), next = wrap.querySelector('[data-next]');
    if (!rail || !prev || !next) return;
    function step() { var c = rail.children[0]; return c ? c.getBoundingClientRect().width + 24 : 300; }
    function update() {
      prev.disabled = rail.scrollLeft < 4;
      next.disabled = rail.scrollLeft + rail.clientWidth > rail.scrollWidth - 4;
    }
    prev.addEventListener('click', function () { rail.scrollBy({ left: -step(), behavior: reduce ? 'auto' : 'smooth' }); });
    next.addEventListener('click', function () { rail.scrollBy({ left: step(), behavior: reduce ? 'auto' : 'smooth' }); });
    rail.addEventListener('scroll', update, { passive: true }); addEventListener('resize', update); update();
  });

  // filter chips (tours, journal)
  [].forEach.call(document.querySelectorAll('[data-filter-group]'), function (group) {
    var target = document.getElementById(group.getAttribute('data-filter-group'));
    var empty = document.getElementById(group.getAttribute('data-filter-group') + 'Empty');
    var chips = group.querySelectorAll('button');
    [].forEach.call(chips, function (chip) {
      chip.addEventListener('click', function () {
        var f = chip.getAttribute('data-f'), shown = 0;
        [].forEach.call(chips, function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
        [].forEach.call(target.querySelectorAll('[data-cat]'), function (el) {
          var on = f === 'all' || el.getAttribute('data-cat').split(' ').indexOf(f) > -1;
          el.hidden = !on; if (on) shown++;
        });
        if (empty) empty.hidden = shown > 0;
      });
    });
  });

  // copy buttons
  [].forEach.call(document.querySelectorAll('[data-copy]'), function (b) {
    b.addEventListener('click', function () {
      var text = b.getAttribute('data-copy') || location.href.split('#')[0];
      var label = b.textContent;
      var done = function () { b.textContent = b.getAttribute('data-copied') || 'Copied'; setTimeout(function () { b.textContent = label; }, 1800); };
      try { navigator.clipboard.writeText(text).then(done, function () { b.textContent = text; }); } catch (e) { b.textContent = text; }
    });
  });
})();
