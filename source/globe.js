/* Home hero: a globe turns to the world's great landmarks; at each, the YSL pin plants and the landmark
   draws itself in warm light. The opening tour ends at KUL, then the globe keeps travelling slowly. */
(function () {
  var hero = document.getElementById('globeHero');
  if (!hero || !window.G) return;
  var canvas = hero.querySelector('canvas.globe'), ctx = canvas.getContext('2d');
  var layer = hero.querySelector('.lm-layer'), label = hero.querySelector('.lm-label');
  var pin = hero.querySelector('.lm-pin'), beam = hero.querySelector('.lm-beam');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var proj = G.geoOrthographic().clipAngle(90).precision(.6), path = G.geoPath(proj, ctx);
  var back = G.geoOrthographic().clipAngle(90).precision(.6).reflectX(true), bpath = G.geoPath(back, ctx), grat = G.geoGraticule10();
  var sphere = { type: 'Sphere' };
  var byId = {}; LANDMARKS.forEach(function (l) { byId[l.id] = l; });
  var INTRO = ['cdg', 'nav', 'dxb', 'kul'];
  var LOOP = ['dps', 'syd', 'hnd', 'icn', 'pek', 'dxb', 'cai', 'nav', 'fco', 'zrh', 'cdg', 'jfk', 'kul'];
  var W, H, R, CX, CY, DPR, LM, phone;
  // where each landmark leads: a tour that goes there, or an enquiry for that place
  // labels can be swapped per language (the Chinese site sets window.GLOBE_TEXT and translates LANDMARKS places)
  var TX = window.GLOBE_TEXT || { see: 'See tour', china: 'China tours', plan: 'Plan a trip' };
  var TO = {
    CDG: ['tour-gd-europe-legend.html', TX.see], ZRH: ['tour-gd-europe-legend.html', TX.see],
    NAV: ['tour-gd-turkiye.html', TX.see], HND: ['tour-gd-hokkaido.html', TX.see], PEK: ['tours.html', TX.china]
  };
  function linkFor(l) {
    if (l.home) return null;
    return TO[l.code] || ['contact.html?dest=' + encodeURIComponent(l.place), TX.plan];
  }
  var hover = false, lastNow = 0;
  label.addEventListener('mouseenter', function () { hover = true; });
  label.addEventListener('mouseleave', function () { hover = false; });
  label.addEventListener('focus', function () { hover = true; });
  label.addEventListener('blur', function () { hover = false; });

  // one SVG group per landmark, drawn by stroke
  LANDMARKS.forEach(function (l) {
    var g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    // Twain's own drawing when there is one (landmark-art.js), else the placeholder
    var art = window.LANDMARK_ART && LANDMARK_ART[l.code], ds = art || l.d;
    var span = art ? 1500 : 700, n = Math.max(1, ds.length - 1);
    g.setAttribute('class', art ? 'lm fine' : 'lm'); g.setAttribute('data-id', l.id);
    ['halo', 'line'].forEach(function (cls) {
      var sub = document.createElementNS('http://www.w3.org/2000/svg', 'g'); sub.setAttribute('class', cls);
      ds.forEach(function (d, i) {   // paths draw one after another, in the order they were drawn
        var p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        p.setAttribute('d', d); p.setAttribute('pathLength', '1');
        p.style.transitionDelay = 'calc(var(--span, ' + span + 'ms) * ' + (i / n).toFixed(4) + ')'; sub.appendChild(p);
      });
      g.appendChild(sub);
    });
    layer.appendChild(g); l.el = g;
  });

  function size() {
    W = hero.clientWidth; H = hero.clientHeight; DPR = Math.min(window.devicePixelRatio || 1, 2);
    phone = W < 760;
    canvas.width = W * DPR; canvas.height = H * DPR; canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
    if (phone) { R = Math.min(W * .62, H * .36); CX = W / 2; CY = H - R * .72; LM = Math.min(170, R * .72); }
    else { R = Math.min(H * .43, W * .28); CX = W * .70; CY = H * .53; LM = Math.min(250, R * .74); }
    proj.translate([CX, CY]).scale(R); back.translate([CX, CY]).scale(R);
    layer.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
  }

  // rotation state: [lambda, phi]
  var rot = [0, 0];
  function target(l) { return [-l.lon, -(l.lat - (phone ? 6 : 10))]; }
  function wrap(a) { return ((a + 540) % 360) - 180; }

  function draw() {
    proj.rotate([rot[0], rot[1], 0]);
    back.rotate([rot[0] + 180, -rot[1], 0]);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    ctx.clearRect(0, 0, W, H);
    // red light spilling from the globe into the dark
    var glow = ctx.createRadialGradient(CX, CY, R * .92, CX, CY, R * 1.55);
    glow.addColorStop(0, 'rgba(235,40,40,.55)'); glow.addColorStop(.35, 'rgba(200,25,30,.18)'); glow.addColorStop(1, 'rgba(200,25,30,0)');
    ctx.fillStyle = glow; ctx.beginPath(); ctx.arc(CX, CY, R * 1.55, 0, 7); ctx.fill();
    // the glass: deep red-black inside, lifting towards the rim
    var body = ctx.createRadialGradient(CX - R * .2, CY - R * .25, R * .05, CX, CY, R);
    body.addColorStop(0, '#3d070d'); body.addColorStop(.6, '#2a0409'); body.addColorStop(.88, '#5a0a12'); body.addColorStop(1, '#a3141c');
    ctx.beginPath(); path(sphere); ctx.fillStyle = body; ctx.fill();
    // the far side, seen through the glass
    ctx.beginPath(); bpath(grat); ctx.lineWidth = .7; ctx.strokeStyle = 'rgba(255,80,70,.12)'; ctx.stroke();
    ctx.beginPath(); bpath(LAND); ctx.fillStyle = 'rgba(255,70,60,.14)'; ctx.fill();
    // the near side: glowing grid, luminous land, bright coastlines
    ctx.beginPath(); path(grat); ctx.lineWidth = .8; ctx.strokeStyle = 'rgba(255,90,80,.42)'; ctx.stroke();
    var land = ctx.createRadialGradient(CX - R * .3, CY - R * .35, R * .1, CX, CY, R * 1.05);
    land.addColorStop(0, '#ff5a4e'); land.addColorStop(.6, '#e02a2c'); land.addColorStop(1, '#a8121b');
    ctx.beginPath(); path(LAND); ctx.fillStyle = land; ctx.fill();
    ctx.save(); ctx.shadowColor = 'rgba(255,90,70,.9)'; ctx.shadowBlur = 6;
    ctx.lineWidth = .9; ctx.strokeStyle = 'rgba(255,190,170,.85)'; ctx.stroke(); ctx.restore();
    // glass highlight and a burning rim
    var hi = ctx.createRadialGradient(CX - R * .38, CY - R * .45, 0, CX - R * .38, CY - R * .45, R * .6);
    hi.addColorStop(0, 'rgba(255,220,210,.22)'); hi.addColorStop(1, 'rgba(255,220,210,0)');
    ctx.beginPath(); path(sphere); ctx.fillStyle = hi; ctx.fill();
    var rim = ctx.createRadialGradient(CX, CY, R * .8, CX, CY, R);
    rim.addColorStop(0, 'rgba(255,60,50,0)'); rim.addColorStop(1, 'rgba(255,60,50,.5)');
    ctx.beginPath(); path(sphere); ctx.fillStyle = rim; ctx.fill();
    ctx.save(); ctx.shadowColor = 'rgba(255,50,40,1)'; ctx.shadowBlur = 24;
    ctx.beginPath(); path(sphere); ctx.lineWidth = 1.6; ctx.strokeStyle = 'rgba(255,140,120,.9)'; ctx.stroke(); ctx.restore();
  }

  // the current landmark: pin, beam, drawing and label follow its point on the globe
  var cur = null, curT0 = 0, fading = null, fadeT0 = 0;
  function pt(l) { return proj([l.lon, l.lat]); }
  function visible(l) { return G.geoDistance([l.lon, l.lat], [-rot[0], -rot[1]]) < 1.35; }
  function placeMark(now) {
    LANDMARKS.forEach(function (l) { if (l !== cur && l !== fading) l.el.style.opacity = 0; });
    if (fading) {
      var f = 1 - Math.min(1, (now - fadeT0) / 350);
      fading.el.style.opacity = f; if (f <= 0) { reset(fading.el); fading = null; } else posGroup(fading);
    }
    if (!cur || !visible(cur)) { pin.style.opacity = 0; beam.style.opacity = 0; label.style.opacity = 0; label.classList.remove('live'); return; }
    var p = pt(cur), t = now - curT0;
    var k = Math.min(1, t / 900), e = 1 - Math.pow(1 - k, 3);
    posGroup(cur);
    cur.el.style.opacity = 1;
    var drop = Math.max(0, 1 - t / 320);
    pin.style.opacity = Math.min(1, t / 160);
    pin.style.transform = 'translate(' + p[0].toFixed(1) + 'px,' + (p[1] - 40 * drop * drop).toFixed(1) + 'px)';
    beam.style.opacity = .9 * Math.min(1, t / 500);
    beam.style.transform = 'translate(' + p[0].toFixed(1) + 'px,' + (p[1] - (phone ? 44 : 52)).toFixed(1) + 'px) scaleY(' + (LM / 100).toFixed(3) + ')';
    var lo = Math.min(1, Math.max(0, (t - 450) / 400));
    label.style.opacity = lo; label.classList.toggle('live', lo > .6 && !!label.getAttribute('data-go'));
    label.style.transform = phone ? 'translate(' + (p[0] - label.offsetWidth / 2).toFixed(1) + 'px,' + (p[1] + 10).toFixed(1) + 'px)' : 'translate(' + (p[0] + 26).toFixed(1) + 'px,' + (p[1] - label.offsetHeight / 2 - 18).toFixed(1) + 'px)';
  }
  function posGroup(l) {
    var p = pt(l), s = LM / 120;
    l.el.setAttribute('transform', 'translate(' + (p[0] - 60 * s).toFixed(1) + ',' + (p[1] - (phone ? 48 : 56) - 110 * s).toFixed(1) + ') scale(' + s.toFixed(3) + ')');
  }
  function reset(el) { el.classList.add('reset'); el.classList.remove('on'); el.getBoundingClientRect(); el.classList.remove('reset'); }
  function show(l, now, instant) {
    if (cur && cur !== l) { fading = cur; fadeT0 = now; }
    cur = l; curT0 = now;
    reset(l.el);
    // the opening tour draws faster so each landmark is complete before the globe moves on
    var quick = mode === 'intro' && !l.home;
    l.el.style.setProperty('--span', quick ? '650ms' : '');
    l.el.style.setProperty('--seg', quick ? '.28s' : '');
    if (instant) { l.el.classList.add('reset', 'on'); l.el.getBoundingClientRect(); l.el.classList.remove('reset'); }
    else requestAnimationFrame(function () { l.el.classList.add('on'); });
    label.querySelector('b').textContent = l.code; label.querySelector('span').textContent = l.place;
    var go = linkFor(l);
    label.querySelector('em').textContent = go ? go[1] : '';
    if (go) { label.href = go[0]; label.setAttribute('data-go', '1'); label.setAttribute('aria-label', go[1] + ': ' + l.place); }
    else { label.removeAttribute('href'); label.removeAttribute('data-go'); label.removeAttribute('aria-label'); }
    hero.classList.toggle('at-home', !!l.home);
  }
  function hide(now) { if (cur) { fading = cur; fadeT0 = now; cur = null; } }

  // move the globe between destinations
  var seq = [], si = 0, segT0 = 0, from = null, to = null, mode = 'intro', MOVE = 1000, DWELL = 700, raf = 0, ready = false;
  function ease(t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function startSeg(now) {
    from = rot.slice(); var tg = target(byId[seq[si]]);
    to = [from[0] + wrap(tg[0] - from[0]), tg[1]];
    var dist = Math.hypot(to[0] - from[0], to[1] - from[1]);
    MOVE = mode === 'intro' ? (si === 0 ? 1200 : 950) : Math.max(1500, Math.min(2600, dist * 22));
    DWELL = mode === 'intro' ? (seq[si] === 'kul' ? 0 : 1500) : 2800;
    segT0 = now; hide(now);
  }
  function tick(now) {
    // hovering a landmark's link holds the globe there
    if (hover && cur && now - segT0 > MOVE) segT0 += now - (lastNow || now);
    lastNow = now;
    var t = now - segT0;
    if (t < MOVE) {
      var e = ease(t / MOVE);
      rot = [from[0] + (to[0] - from[0]) * e, from[1] + (to[1] - from[1]) * e];
    } else {
      if (cur !== byId[seq[si]]) show(byId[seq[si]], now);
      rot[0] = to[0] + (t - MOVE) * .0016; // the globe never quite stops
      if (t > MOVE + DWELL && !(mode === 'intro' && seq[si] === 'kul')) next(now);
      if (mode === 'intro' && seq[si] === 'kul' && t > MOVE + 300) { landed(); }
    }
    draw(); placeMark(now);
    raf = requestAnimationFrame(safe);
  }
  function safe(now) { try { tick(now); } catch (e) { cancelAnimationFrame(raf); hero.classList.add('open'); } }
  function next(now) {
    si++;
    if (si >= seq.length) { si = 0; }
    startSeg(now);
  }
  var loopTimer = 0;
  function landed() {
    if (ready) return; ready = true;
    hero.classList.remove('playing'); hero.classList.add('open');
    loopTimer = setTimeout(function () { mode = 'loop'; seq = LOOP; si = 0; startSeg(performance.now()); }, 3800);
  }
  function play() {
    clearTimeout(loopTimer); ready = false;
    hero.classList.remove('open'); hero.classList.add('playing');
    mode = 'intro'; seq = INTRO; si = 0;
    var first = target(byId.cdg); rot = [first[0] + 70, first[1] + 8];
    cur = null; fading = null;
    startSeg(performance.now());
    setTimeout(function () { hero.classList.add('copy-in'); }, 500);
  }
  function settle() { // straight to KUL, no tour
    clearTimeout(loopTimer); mode = 'intro'; seq = ['kul']; si = 0;
    rot = target(byId.kul); from = rot.slice(); to = rot.slice(); MOVE = 0; DWELL = 0; segT0 = performance.now() - 1;
    show(byId.kul, performance.now() - 2000, true); hero.classList.add('copy-in'); landed();
  }
  function preview(l) { // index.html#JFK: fly straight to one landmark and stay, for checking artwork
    clearTimeout(loopTimer); ready = true; hero.classList.remove('playing'); hero.classList.add('open', 'copy-in');
    mode = 'loop'; seq = [l.id]; si = 0; rot = [target(l)[0] + 40, target(l)[1]]; startSeg(performance.now()); DWELL = 1e9;
  }

  size();
  addEventListener('resize', function () { size(); });
  var replay = document.getElementById('globeReplay');
  if (replay) replay.addEventListener('click', function () { cancelAnimationFrame(raf); play(); raf = requestAnimationFrame(safe); });
  hero.addEventListener('click', function (e) { if (!ready && !e.target.closest('a,button')) { settle(); } });

  var seen = false;
  try { seen = sessionStorage.getItem('yslGlobe') === '1'; sessionStorage.setItem('yslGlobe', '1'); } catch (e) {}
  var hashL = LANDMARKS.filter(function (l) { return ('#' + l.code).toUpperCase() === location.hash.toUpperCase(); })[0];
  if (hashL) preview(hashL); else if (seen || reduce) settle(); else play();
  if (reduce) { draw(); placeMark(performance.now()); return; }
  raf = requestAnimationFrame(safe);
  // pause when the hero is off screen
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) {
    es.forEach(function (en) { cancelAnimationFrame(raf); if (en.isIntersecting) raf = requestAnimationFrame(safe); });
  }).observe(hero);
})();
