import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES
import feedback
import legal
import zh
from data import SERVICES, TOURS, BRANDS, MEMBERS, CONTACT, FAIRS, OPENINGS, QG, GD_TOURS, MON

# 'en' builds the English site into dist/, 'zh' the Simplified Chinese site into dist/zh/ (see zh.py)
LANG = 'en'
NO_ZH = {'feedback.html'}
SITE = 'https://www.ysltravel.com'  # official address: canonical links, sitemap and share images use it  # pages with no Chinese twin (the feedback form is already bilingual)

SRC = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(SRC, '..', 'dist')
MAIN_DIST = os.path.abspath(DIST)
read = lambda f: open(os.path.join(SRC, f), encoding='utf-8').read()

LOGO = read('logo.svg')
ICONS = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + read('icons.svg') + '</defs></svg>'
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 8h12M9 3l5 5-5 5"/></svg>'
ARROW_L = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 8H2M7 3L2 8l5 5"/></svg>'
DIAG = '<svg class="go" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12L12 4M5.5 4H12v6.5"/></svg>'
WA = 'Chat on WhatsApp'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:ital,wght@0,300..700;1,300..700&family=IBM+Plex+Mono:wght@400;500&display=swap">'

NAV = [('corporate.html', 'Corporate Travel'), ('tours.html', 'Holidays &amp; Tours'), ('services.html', 'Travel Services'), ('about.html', 'About'), ('journal.html', 'Journal')]

def nav(current):
    items = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<header class="site-nav">
  <div class="container">
    <a class="brand" href="index.html" aria-label="YSL Travel and Tours, home">{LOGO}<span>Travel &amp; Tours</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="navLinks" aria-label="Menu"><span></span><span></span><span></span></button>
    <ul class="nav-links" id="navLinks">
      {items}
      <li><a class="lang" href="__LANGSWITCH__" {'lang="en" hreflang="en">EN' if LANG == 'zh' else 'lang="zh-Hans" hreflang="zh-Hans">中文'}</a></li>
      <li><a class="nav-cta" href="contact.html"{" aria-current=\"page\"" if current == "contact.html" else ""}>Plan a trip</a></li>
    </ul>
  </div>
</header>'''

ASSOC = [('matta', 'MATTA, Malaysian Association of Tour and Travel Agents', 'https://www.matta.org.my/'),
         ('mita', 'MITA, Malaysian Inbound Tourism Association', 'https://www.mita.org.my/'),
         ('mica', 'MICA, Malaysia Inbound Chinese Association', ''),
         ('mcta', 'MCTA, Malaysian Chinese Tourism Association', '')]

def assoc_strip():
    items = ''.join((f'<li><a href="{u}" target="_blank" rel="noopener"><img src="assets/assoc-{k}.png" alt="{a}" loading="lazy"></a></li>' if u else f'<li><img src="assets/assoc-{k}.png" alt="{a}" loading="lazy"></li>') for k, a, u in ASSOC)
    return f'<aside class="assoc-strip" aria-label="Memberships"><div class="container"><span class="lbl">Proud member of</span><ul>{items}</ul></div></aside>'

def footer():
    return f'''{assoc_strip()}
<footer class="site-footer on-dark">
  <div class="container">
    <div class="foot-grid">
      <div class="foot-brand">{LOGO}<p>Travel services for individuals and companies, from Klang to the world since 2009.</p></div>
      <div><h4>Explore</h4><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)}<li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Visit us</h4><p style="margin:0">{CONTACT['address']}</p><p style="margin:12px 0 0">{CONTACT['hours']}</p></div>
      <div><h4>Get in touch</h4><ul><li>{CONTACT['phone']}</li><li><a href="https://wa.me/{CONTACT['wa']}" target="_blank" rel="noopener">WhatsApp {CONTACT['whatsapp']}</a></li><li>{CONTACT['email']}</li><li><a href="{CONTACT['facebook']}" target="_blank" rel="noopener">Facebook</a></li><li><a href="{CONTACT['instagram']}" target="_blank" rel="noopener">Instagram @ysltravel</a></li><li><a href="{CONTACT['maps']}" target="_blank" rel="noopener">Google Maps</a></li></ul></div>
    </div>
    <div class="foot-base">
      <span>&copy; 2026 YSL Travel &amp; Tours Sdn Bhd (877803-T) &nbsp; <span lang="zh-Hans">咏胜天下旅游有限公司</span></span>
      <span><a href="privacy.html">Privacy Notice</a> &nbsp; Licence KPL 6107 &nbsp; Member of MATTA, MITA, MICA and MCTA</span>
    </div>
  </div>
</footer>'''

def cta_band(title='Let’s plan your next trip.'):
    return f'''<section class="cta-band on-red" aria-labelledby="cta-h">
  <div class="container">
    <div>
      <p class="eyebrow">Talk to us</p>
      <h2 class="h-xl" id="cta-h">{title}</h2>
      <div class="btn-row" style="margin-top:36px"><a class="btn btn--white" href="contact.html">{WA}</a><a class="btn btn--line-light" href="tours.html">Browse tours</a></div>
    </div>
    <dl class="contact-quick">
      <div><dt>Call</dt><dd>{CONTACT['phone']}</dd></div>
      <div><dt>Email</dt><dd>{CONTACT['email']}</dd></div>
      <div><dt>Visit</dt><dd>Taman Klang Utama, Klang</dd></div>
    </dl>
  </div>
</section>'''

def tour_card(t, cls='ticket rv'):
    """Tour cards are tickets, after the YSL business card."""
    href = t.get('page', 'contact.html?tour=' + t['slug'])
    if t.get('img'):
        vis = f'<div class="media"><span class="pill">{t.get("dur", t["kind"])}</span><img src="assets/{t["img"]}" alt=""></div>'
    else:
        vis = f'<div class="slot" style="--c1:{t["c1"]};--c2:{t["c2"]}"><span class="pill">{t.get("dur", t["kind"])}</span><b>{t.get("short", t["region"])}</b><small>Tour photo to come</small></div>'
    return f'''<a class="{cls}" href="{href}" data-cat="{t['cat']}">{vis}<span class="t-body"><span class="t-route"><span><small>From</small>{t.get('origin', 'KUL')}</span><i>{MINI_PIN}</i><span><small>To</small>{t['iata']}</span></span><b class="t-title">{t['title']}</b><span class="t-line">{t['line']}</span><span class="t-dep"><span>Departs</span>{t['departs'] if t.get('departs') else '<span class="tbc">Months from YSL</span>'}</span></span><span class="t-stub"><span>{'Partner tour' if t.get('brand') else 'YSL Travel &amp; Tours'}</span><span>{'View' if t.get('page') else 'Enquire'} {ARROW}</span></span></a>'''

def post_card(p):
    if p.get('img'):
        vis = f'<div class="media"><img src="assets/{p['img']}" alt=""></div>'
    else:
        c1, c2, lab = p['slot']
        vis = f'<div class="media slot" style="--c1:{c1};--c2:{c2}"><b>{lab}</b><small>Photo to come</small></div>'
    return f'''<a class="post-card rv" href="{p['href']}" data-cat="{p['cat']}">{vis}<span class="tag">{p['cat_label']}</span><h3>{p['title']}</h3><p>{p['excerpt']}</p><span class="date">{p['date']}</span></a>'''

def page(fname, title, desc, body, current, home=False, extra_head='', extra_js='', og_image='assets/hero.jpg'):
    if LANG == 'zh':
        extra_head = '\n' + zh.FONTS + extra_head
        switch = '../' + fname
    else:
        switch = 'zh/' + (fname if fname not in NO_ZH else 'index.html')
    main = os.path.abspath(DIST) == MAIN_DIST  # not for the stand-alone feedback site
    path = '' if fname == 'index.html' else fname
    en_url, zh_url = f'{SITE}/{path}', f'{SITE}/zh/{path}'
    url = zh_url if LANG == 'zh' else en_url
    if main and fname not in NO_ZH and fname != '404.html':
        extra_head = (f'\n<link rel="canonical" href="{url}">\n<link rel="alternate" hreflang="en" href="{en_url}">'
                      f'\n<link rel="alternate" hreflang="zh-Hans" href="{zh_url}">\n<link rel="alternate" hreflang="x-default" href="{en_url}">') + extra_head
    if main:
        extra_head = ('\n<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n<link rel="icon" href="assets/favicon-32.png" sizes="32x32" type="image/png">'
                      '\n<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">') + extra_head
    og_abs = og_image if og_image.startswith('http') else f'{SITE}/{og_image}'
    head = f'''<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="YSL Travel &amp; Tours">
<meta property="og:locale" content="{'zh_CN' if LANG == 'zh' else 'en_GB'}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_abs}">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
<link rel="stylesheet" href="assets/site.css">{extra_head}'''
    content = f'''{ICONS}
<a class="skip-link" href="#main" style="position:absolute;left:-9999px">Skip to content</a>
{body}
<script src="assets/site.js"></script>{extra_js}'''
    if home:
        html = head + '\n' + content
    else:
        html = f'''<!doctype html>
<html lang="{'zh-Hans' if LANG == 'zh' else 'en-GB'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{content}
</body>
</html>'''
    if LANG == 'zh':
        if home:
            html = '<html lang="zh-Hans">\n' + html
        html = zh.translate_html(html, fname)
        html = re.sub(r'(src|href|content)="assets/', r'\1="../assets/', html)
    html = html.replace('__LANGSWITCH__', switch)
    html = html.encode('ascii', 'xmlcharrefreplace').decode('ascii')
    out = os.path.join(DIST, 'zh') if LANG == 'zh' else DIST
    open(os.path.join(out, fname), 'w', encoding='utf-8').write(html)
    print('wrote', os.path.relpath(os.path.join(out, fname), DIST), len(html) // 1024, 'KB')

def head_block(crumb, eyebrow, title, lead, extra=''):
    crumbs = ''.join(f'<li><a href="{h}">{t}</a></li>' if h else f'<li aria-current="page">{t}</li>' for h, t in crumb)
    return f'''<section class="page-head">
  <div class="container">
    <ol class="crumbs">{crumbs}</ol>
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="h-xxl">{title}</h1>
    <p class="lead">{lead}</p>{extra}
  </div>
</section>'''

# ======================= HOME =======================
PIN = re.search(r'<g id="pinMark">(.*?)</g>', read('entrance.html'), re.S).group(1)
PIN_PATHS = re.findall(r'<path fill="([^"]+)" d="([^"]+)"/>', PIN)  # white silhouette, then the four horizons
MINI_PIN = '<svg viewBox="70 198 140 192" aria-hidden="true">' + PIN + '</svg>'

def horizon(bottom, top='transparent', cls=''):
    """Layered horizons from the YSL mark: orange, rust, red, deep red, then the next section's colour."""
    bands = [('#ed6723', 22), ('#be4027', 44), ('#e72629', 64), ('#bb2030', 82), (bottom, 98)]
    paths = ''.join(f'<path fill="{c}" d="M0,{y} C480,{y - 30} 960,{y - 30} 1440,{y} V122 H0 Z"/>' for c, y in bands)
    bg = '' if top == 'transparent' else f'<rect width="1440" height="122" fill="{top}"/>'
    return f'<svg class="horizon {cls}" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true">{bg}{paths}</svg>'

def sun_hero():
    o = OPENINGS[0]
    sil = PIN_PATHS[0][1]
    flds = ''.join(f'<path class="fld" fill="{c}" d="{d}"/>' for c, d in [PIN_PATHS[i] for i in (2, 3, 4, 1)])  # orange, rust, red, deep red
    fclip = ''.join(f'<path class="cf" d="{d}"/>' for c, d in PIN_PATHS[1:])
    img = f'assets/{o["img"]}'
    return f'''<section class="sun-hero playing" id="sunHero" aria-label="Welcome">
  <img class="photo" src="{img}" alt="">
  <svg class="sun" aria-hidden="true" preserveAspectRatio="none">
    <defs>
      <clipPath id="cSil" clipPathUnits="userSpaceOnUse"><path id="cSilU" d="{sil}"/></clipPath>
      <clipPath id="cFld" clipPathUnits="userSpaceOnUse">{fclip}</clipPath>
      <clipPath id="cIn" clipPathUnits="userSpaceOnUse"><path d="{sil}"/></clipPath>
    </defs>
    <image id="ph2" href="{img}" x="0" y="0" preserveAspectRatio="xMidYMid slice" clip-path="url(#cSil)"/>
    <g id="pinG"><path fill="#fff" d="{sil}"/></g>
    <image id="ph1" href="{img}" x="0" y="0" preserveAspectRatio="xMidYMid slice" clip-path="url(#cFld)" style="opacity:0"/>
    <g id="pinF"><g clip-path="url(#cIn)">{flds}</g></g>
  </svg>
  <div class="shade"></div>
  <div class="sun-copy">
    <div class="container">
      <div>
        <p class="eyebrow">From Klang. To the world.</p>
        <h1>Every journey<br> begins with a<br> <em>point<br> on the map.</em></h1>
        <p class="sub">From that first point to the flight home, <br>we plan every step.</p>
        <div class="btn-row"><a class="btn btn--white" href="tours.html">Explore tours</a><a class="btn btn--line-light" href="contact.html">Plan a trip</a></div>
      </div>
      <a class="boarding" href="{o['href']}">
        <span class="bp-main"><small>Now boarding &nbsp;{o['kind']}</small><span class="bp-route">KUL<i>{MINI_PIN}</i>{o['code']}</span><b>{o['tour']}</b></span>
        <span class="bp-stub">{ARROW}</span>
      </a>
    </div>
  </div>
  <button class="sun-replay" id="sunReplay" type="button">Replay</button>
  {horizon('#f7f1ea')}
</section>'''

def globe_hero():
    return f'''<section class="globe-hero playing" id="globeHero" aria-label="Welcome">
  <canvas class="globe" aria-hidden="true"></canvas>
  <div class="lm-beam" aria-hidden="true"></div>
  <svg class="lm-layer" aria-hidden="true"></svg>
  <div class="lm-pin" aria-hidden="true">{MINI_PIN}</div>
  <a class="lm-label" href="tours.html" tabindex="-1"><b></b><span></span><em></em></a>
  <div class="globe-copy">
    <div class="container"><div class="inner">
      <p class="eyebrow">From Klang. To the world.</p>
      <h1>Every journey<br> begins with a<br> <em>point<br> on the map.</em></h1>
      <p class="sub">From that first point to the flight home, <br>we plan every step.</p>
      <div class="btn-row"><a class="btn btn--white" href="tours.html">Explore tours</a><a class="btn btn--line-light" href="contact.html">Plan a trip</a></div>
    </div></div>
  </div>
  <button class="globe-replay" id="globeReplay" type="button">Replay</button>
</section>'''

def plan_band():
    return f'''<section class="plan-band" aria-labelledby="plan-h">
  <img class="bg" src="assets/hero.jpg" alt="">
  <div class="container">
    <p class="eyebrow eyebrow--plain">Your next point on the map.</p>
    <h2 id="plan-h">Where to next?</h2>
    <p class="lead">Tell us where, when and who is coming. A consultant replies within one working day.</p>
    <div class="btn-row" style="margin-top:32px"><a class="btn btn--white" href="contact.html">Plan a trip</a><a class="btn btn--line-light" href="contact.html">{WA}</a></div>
    <dl><div><dt>Call</dt><dd>{CONTACT['phone']}</dd></div><div><dt>Email</dt><dd>{CONTACT['email']}</dd></div><div><dt>Visit</dt><dd>Taman Klang Utama, Klang</dd></div></dl>
  </div>
</section>'''

def build_home():
    rail = ''.join(tour_card(t, 'ticket') for t in TOURS)
    brands = ''.join(f'<span class="b">{b}</span>' for b in BRANDS)
    members = ''.join(f'<li><b>{a}</b><span>{n}</span></li>' for a, n in MEMBERS)
    fairs = ''.join(f'<li><b>{n}</b><span>{d}</span></li>' for n, d in FAIRS)
    body = f'''{nav('index.html')}
<main id="main">
{globe_hero()}

<section class="section section--ivory" id="next" aria-labelledby="tours-h" data-rail style="padding-top:clamp(40px,5vw,72px)">
  <div class="container">
    <div class="rail-head">
      <div><p class="eyebrow">Holidays &amp; Tours</p><h2 class="h-xl" id="tours-h">Where we’re <em>going next.</em></h2></div>
      <div style="display:flex;align-items:center;gap:24px"><a class="link-arrow" href="tours.html">All tours {ARROW}</a><div class="rail-ctrl"><button type="button" data-prev aria-label="Previous tours">{ARROW_L}</button><button type="button" data-next aria-label="Next tours">{ARROW}</button></div></div>
    </div>
    <div class="rail">{rail}</div>
    <div class="brand-strip rv"><span class="lbl">Tour brands we carry</span>{brands}<span class="more">and more</span></div>
    <nav class="svc-strip rv" aria-label="Travel services"><span class="lbl">Travel services</span><ul>{''.join(f'<li><a href="services.html#{k}"><svg aria-hidden="true"><use href="#ic-{i}"/></svg>{t}</a></li>' for k, i, t in [('air', 'air', 'Air tickets'), ('visa', 'visa', 'Visas'), ('insurance', 'ins', 'Travel insurance'), ('cruises', 'cruise', 'Cruises'), ('hotels', 'hotel', 'Hotels')])}</ul><a class="all" href="services.html">All services</a></nav>
  </div>
</section>

<section class="section section--ivory" aria-labelledby="proof-h" style="padding-top:0">
  <div class="container">
    <div class="proof rv">
      <div class="chapter-head" style="margin-bottom:clamp(28px,3vw,44px)"><div><p class="eyebrow">Why travel with YSL</p><h2 class="h-l" id="proof-h">Licensed, accredited and trusted since 2009.</h2></div><p class="lead">A registered, licensed travel agency and an active member of Malaysia’s travel associations.</p></div>
      <dl class="stats">
        <div><dt>Year founded</dt><dd class="num">2009</dd></div>
        <div><dt>Founder’s experience</dt><dd class="num">25+ yrs</dd></div>
        <div><dt>Corporate clients</dt><dd class="num">50+</dd></div>
        <div><dt>Industry associations</dt><dd class="num">4</dd></div>
      </dl>
      <div class="creds">
        <div class="cred">
          <h3 class="code">Licensed &amp; registered</h3>
          <ul class="legal"><li><b>KPL 6107</b><span>Travel agency licence, Ministry of Tourism, Arts and Culture Malaysia (MOTAC)</span></li><li><b>877803-T</b><span>YSL Travel &amp; Tours Sdn Bhd, registered with SSM</span></li></ul>
        </div>
        <div class="cred">
          <h3 class="code">Member of</h3>
          <ul class="badges">{members}</ul>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
{plan_band()}
{footer()}'''
    css = '<style>\n' + read('globe.css') + '\n</style>'
    js = '\n<script src="assets/landmarks.js"></script>\n<script>\n' + read('d3geo.min.js') + '\n' + read('land.js') + '\n' + read('landmarks.js') + '\n' + (zh.globe_js() if LANG == 'zh' else '') + read('globe.js') + '\n</script>'
    page('index.html', 'YSL Travel & Tours', 'YSL Travel & Tours: corporate travel, holidays and tours from Klang, Malaysia, since 2009.', body, 'index.html', home=True, extra_head='\n' + css, extra_js=js)

# ======================= CORPORATE & MICE =======================
def build_corporate():
    mice = [
        ('M', 'Meetings', 'Board retreats, management offsites and regional meetings, with the venue, rooms, AV and travel arranged as one package.',
         ['Venue sourcing and site inspections', 'Meeting rooms, AV and breakout spaces', 'Retreats in Malaysia and overseas']),
        ('I', 'Incentives', 'Reward trips for top performers, dealers and agents: an itinerary people work all year to qualify for.',
         ['Bespoke itineraries and exclusive experiences', 'Gala and awards nights', 'Wave departures for very large groups']),
        ('C', 'Conferences', 'Delegate travel and logistics for conventions and annual conferences, from registration to the closing dinner.',
         ['Delegate registration and rooming', 'Airport transfers in waves', 'Hospitality desks at the venue']),
        ('E', 'Exhibitions', 'Business delegations to trade fairs and expos abroad, and group travel for exhibitors and buyers.',
         ['Trade fair delegations', 'Business visas and invitations', 'Hotels close to the fairground']),
    ]
    mice_html = ''.join(f'''<li class="rv"><span class="mice-letter" aria-hidden="true">{l}</span><h3>{t}</h3><p>{d}</p><ul>{''.join(f'<li>{x}</li>' for x in li)}</ul></li>''' for l, t, d, li in mice)
    scale = [
        ('air', 'Group air', 'Seat blocks across several flights, charter options, group check-in and staggered departure waves.'),
        ('hotel', 'Hotel allocations', 'Room blocks in one hotel or spread across several, rooming lists, VIP upgrades and late changes handled.'),
        ('coach', 'Ground transport', 'Coaches numbered and colour-coded by group, each with its own tour leader and a lead coordinator on the ground.'),
        ('flag', 'The arrival', 'A branded welcome at the airport: YSL flags and signage, a hospitality desk, and coaches waiting in order.'),
        ('doc', 'Registration and documents', 'Online registration, passport and visa collection, group visas, insurance, and pre-departure briefings.'),
        ('gala', 'Gala and awards nights', 'Venue buyouts, themed dinners, stage, sound and lighting, and the awards ceremony run to the minute.'),
        ('spark', 'Experiences', 'Team-building, private tours, CSR activities and exclusive access that make the trip worth qualifying for.'),
        ('meal', 'Every guest’s needs', 'Halal and vegetarian meals, prayer times, mobility needs and multilingual guides, planned for from the start.'),
        ('headset', 'On-site command', 'A 24-hour hotline, daily briefings with the client, and contingency plans for weather, delays and illness.'),
        ('report', 'After the trip', 'A reconciled final account, a photo and video round-up, and a debrief to make the next one better.'),
    ]
    scale_html = ''.join(f'<li class="rv"><svg class="ic" aria-hidden="true"><use href="#ic-{ic}"/></svg><span class="code">{i + 1:02d}</span><b>{t}</b><p>{d}</p></li>' for i, (ic, t, d) in enumerate(scale))
    runway = [
        ('6 months before', 'Brief and budget', 'Purpose, group size, dates, budget per head and the experience you want people to come home with.'),
        ('5 months', 'Proposal and site inspection', 'Destination options with itemised quotations; we can visit the hotels and venues with you.'),
        ('4 months', 'Contract and blocks', 'Air seats and hotel rooms secured, deposits scheduled, the programme agreed day by day.'),
        ('3 to 1 months', 'Registration and documents', 'Participant registration, rooming, passports, visas, dietary needs and insurance.'),
        ('2 weeks', 'Pre-departure briefing', 'Final programme, coach and room assignments, packing notes and contacts for every traveller.'),
        ('On the trip', 'Operations', 'YSL on site from the airport onwards, with tour leaders on every coach and one lead coordinator.'),
        ('After', 'Report and reconciliation', 'Final account, feedback and a debrief with your team.'),
    ]
    runway_html = ''.join(f'<li class="rv"><span class="code">{w}</span><b>{t}</b><p>{d}</p></li>' for w, t, d in runway)
    local = [
        ('team', 'Team building', 'Facilitated games and challenges, indoors or outdoors, designed around what your team needs to work on.'),
        ('palm', 'Retreats and offsites', 'Resort stays with meeting space for planning sessions, strategy days and management retreats.'),
        ('cake', 'Annual dinners and family days', 'Venue, catering, stage and programme for the company dinner or a day out with families.'),
        ('leaf', 'CSR days', 'Community and environmental projects your team can do together, with transport and meals arranged.'),
        ('coach', 'Day trips and company outings', 'Coaches, guides and meals for a day out, from one bus to a convoy.'),
    ]
    local_html = ''.join(f'<li class="rv"><svg class="ic" aria-hidden="true"><use href="#ic-{ic}"/></svg><b>{t}</b><p>{d}</p></li>' for ic, t, d in local)
    places_html = ''.join(f'<span class="b">{p}</span>' for p in ['Langkawi', 'Penang', 'Genting Highlands', 'Cameron Highlands', 'Port Dickson', 'Desaru', 'Melaka', 'Sabah'])
    brief = ['Purpose of the trip, and who is going', 'Group size, even a range', 'Preferred dates or months', 'Budget per person', 'Destinations you have in mind', 'Any dietary, faith or accessibility needs']
    brief_html = ''.join(f'<li>{b}</li>' for b in brief)
    body = f'''{nav('corporate.html')}
<main id="main">
<section class="corp-hero on-dark">
  <img class="ch-bg" src="assets/mice-hero.jpg" alt="A corporate group arriving at a seaside venue, welcomed by a host">
  <div class="container">
    <div class="ch-copy">
      <ol class="crumbs"><li><a href="index.html">Home</a></li><li aria-current="page">Corporate Travel</li></ol>
      <p class="eyebrow">Corporate Travel &amp; MICE</p>
      <h1 class="h-xxl">Business travel and MICE, <em>at any scale.</em></h1>
      <p class="line">From a board retreat of twelve to an incentive of hundreds, one team plans, moves and looks after your people.</p>
      <div class="btn-row" style="margin-top:32px"><a class="btn btn--white" href="contact.html?type=corporate">Request a MICE proposal</a><a class="btn btn--line-light" href="#runway">How we plan it</a></div>
    </div>
  </div>
</section>

<section class="section" aria-label="YSL in numbers" style="padding-block:clamp(48px,6vw,80px)">
  <div class="container">
    <dl class="stats" style="margin-top:0;border-top:0;padding-top:0">
      <div><dt>Corporate travel since</dt><dd class="num">2009</dd></div>
      <div><dt>Corporate clients</dt><dd class="num">50+</dd></div>
      <div><dt>Largest single group</dt><dd class="num">300+</dd></div>
      <div><dt>MICE projects delivered</dt><dd class="num">100+</dd></div>
    </dl>
  </div>
</section>

<section class="section section--paper" aria-labelledby="mice-h">
  <div class="container">
    <div class="chapter-head"><div><p class="eyebrow">What we handle</p><h2 class="h-xl" id="mice-h">All four letters of MICE.</h2></div><p class="lead">Meetings, incentives, conferences and exhibitions, in Malaysia and overseas, planned and run by one team with one point of contact.</p></div>
    <ul class="mice-grid">{mice_html}</ul>
  </div>
</section>

<section class="section" aria-labelledby="scale-h">
  <div class="container">
    <div class="chapter-head"><div><p class="eyebrow">Built for big groups</p><h2 class="h-xl" id="scale-h">Hundreds of people, moving as one.</h2></div><p class="lead">A large programme succeeds on logistics nobody notices. These are the parts we take off your hands.</p></div>
    <ol class="scale-grid">{scale_html}</ol>
  </div>
</section>

<section class="section section--ink on-dark" id="runway" aria-labelledby="run-h">
  <div class="container">
    <div class="chapter-head"><div><p class="eyebrow">How a large programme runs</p><h2 class="h-xl" id="run-h">Six months, one plan.</h2></div><p class="lead">For large groups we recommend starting at least six months ahead, so the best flights, rooms and venues are still available.</p></div>
    <ol class="runway">{runway_html}</ol>
  </div>
</section>

<section class="section section--paper" aria-labelledby="lo-h">
  <div class="container">
    <div class="chapter-head"><div><p class="eyebrow">Local MICE</p><h2 class="h-xl" id="lo-h">Closer to home.</h2></div><p class="lead">Not every company event needs a passport. We plan team days, retreats and celebrations across Malaysia, with transport for everyone arranged.</p></div>
    <ul class="local-grid">{local_html}</ul>
    <div class="local-places rv"><span class="lbl">Popular for company groups</span>{places_html}</div>
  </div>
</section>

<section class="section section--ink on-dark" aria-labelledby="c-h">
  <div class="container corp corp--solo">
    <div class="rv">
      <p class="eyebrow">Why YSL</p>
      <h2 class="h-l" id="c-h">Trusted by more than 50 companies across the region.</h2>
      <ul class="proof-list">
        <li><span class="code">A</span><div><b>Since 2009</b><span>Led by a founder with more than 25 years in travel.</span></div></li>
        <li><span class="code">B</span><div><b>Licensed and accredited</b><span>KPL 6107, and members of MATTA, MITA, MICA and MCTA.</span></div></li>
        <li><span class="code">C</span><div><b>Clear quotations</b><span>Itemised proposals and a reconciled final account your finance team can sign off.</span></div></li>
      </ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="br-h">
  <div class="container split split--center">
    <div><p class="eyebrow">Start a proposal</p><h2 class="h-xl" id="br-h">Send us a brief.</h2><p class="lead" style="margin-top:20px">A rough brief is enough to start. We reply with options and an itemised quotation.</p><div class="btn-row" style="margin-top:32px"><a class="btn btn--red" href="contact.html?type=corporate">Request a MICE proposal</a><a class="btn btn--line-dark" href="contact.html">{WA}</a></div></div>
    <div class="brief-card rv"><p class="code" style="margin:0 0 14px">What to include</p><ol>{brief_html}</ol></div>
  </div>
</section>
</main>
{footer()}'''
    page('corporate.html', 'Corporate Travel & MICE | YSL Travel & Tours', 'Meetings, incentives, conferences and exhibitions at any scale: group air, hotels, coaches, gala nights and on-site teams from YSL Travel & Tours.', body, 'corporate.html')

# ======================= ABOUT =======================
def build_about():
    members = ''.join(f'<li><b>{a}</b><span>{n}</span></li>' for a, n in MEMBERS)
    body = f'''{nav('about.html')}
<main id="main">
{head_block([('index.html', 'Home'), (None, 'About')], 'About us', 'From Klang <span class="nw"><em>to the world</em>,</span><br> since 2009.', 'A licensed Malaysian travel agency planning holidays, group tours and business travel.')}
<section class="section">
  <div class="container split split--center">
    <figure class="portrait rv" style="margin:0"><img src="assets/team.jpg" alt="The YSL Travel &amp; Tours team at a travel fair"></figure>
    <div class="prose rv">
      <p class="eyebrow">Our story</p>
      <h2 class="h-l" style="margin-bottom:28px">Built on more than 25 years in travel.</h2>
      <p>YSL Travel &amp; Tours was founded in Klang, Selangor, in 2009. We arrange holidays, group tours and business travel for individuals, families and companies, and look after each trip from the first quote to the flight home.</p>
      <p>The company is led by a founder with more than 25 years in the travel industry. Behind every booking is a team of consultants and operations staff who know the destinations, the suppliers and the details that keep a trip running smoothly.</p>
      <p>Today we plan travel for families, schools and more than 50 companies and organisations.</p>
    </div>
  </div>
  <div class="container">
    <dl class="stats rv">
      <div><dt>Year founded</dt><dd class="num">2009</dd></div>
      <div><dt>Founder's experience</dt><dd class="num">25+ yrs</dd></div>
      <div><dt>Corporate clients</dt><dd class="num">50+</dd></div>
      <div><dt>Industry associations</dt><dd class="num">4</dd></div>
    </dl>
  </div>
</section>
<section class="section section--ink on-dark">
  <div class="container mv-grid">
    <div class="rv"><p class="eyebrow">Our mission</p><h2 class="h-l">Make good travel easy to reach.</h2><p style="margin-top:18px">We connect people with the places they want to see, and take care of the planning so they can enjoy the journey.</p></div>
    <div class="rv"><p class="eyebrow">Our vision</p><h2 class="h-l">Be the travel partner people trust most.</h2><p style="margin-top:18px">To keep growing with our clients, open new destinations, and help more people travel well.</p></div>
  </div>
</section>
<section class="section" aria-labelledby="mem-h">
  <div class="container">
    <div class="sec-head"><div><p class="eyebrow">Credentials</p><h2 class="h-l" id="mem-h">Licensed, registered and accredited.</h2><p class="muted" style="margin:18px 0 0;max-width:60ch">Licensed by the Ministry of Tourism, Arts and Culture Malaysia (KPL 6107) and registered with SSM as YSL Travel &amp; Tours Sdn Bhd (877803-T).</p></div></div>
    <ul class="member-grid rv">{members}</ul>
  </div>
</section>
</main>
{cta_band()}
{footer()}'''
    page('about.html', 'About YSL Travel & Tours', 'Founded in Klang in 2009, YSL Travel & Tours plans holidays, group tours and business travel for families and companies. Licensed by MOTAC (KPL 6107).', body, 'about.html')

# ======================= SERVICES =======================
def build_services():
    navl = ''.join(f'<li><a href="#{s["slug"]}">{s["title"]}</a></li>' for s in SERVICES)
    blocks = ''.join(f'''<article class="svc-block" id="{s['slug']}"><svg class="ic" aria-hidden="true"><use href="#ic-{s['icon']}"/></svg><div><h2 class="h-l">{s['title']}</h2><p>{s['body']}</p><ul class="ticks">{''.join(f'<li>{i}</li>' for i in s['includes'])}</ul><a class="btn btn--line-dark" href="contact.html">Ask about {s['title'].lower()}</a></div></article>''' for s in SERVICES)
    body = f'''{nav('services.html')}
<main id="main">
{head_block([('index.html', 'Home'), (None, 'Services')], 'What we do', 'Everything between here and there.', 'Eight services under one roof, so one team can look after your whole trip, or your whole company’s.')}
<section class="section">
  <div class="container svc-layout">
    <nav class="svc-nav" aria-label="Services"><ul>{navl}</ul></nav>
    <div>{blocks}</div>
  </div>
</section>
</main>
{cta_band('Not sure what you need? Ask us.')}
{footer()}'''
    js = '''
<script>
(function () {
  var links = document.querySelectorAll('.svc-nav a'), map = {};
  [].forEach.call(links, function (a) { map[a.getAttribute('href').slice(1)] = a; });
  if (!('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { [].forEach.call(links, function (a) { a.classList.remove('active'); }); var a = map[e.target.id]; if (a) a.classList.add('active'); } });
  }, { rootMargin: '-35% 0px -60% 0px' });
  [].forEach.call(document.querySelectorAll('.svc-block'), function (b) { io.observe(b); });
})();
</script>'''
    page('services.html', 'Services | YSL Travel & Tours', 'Air tickets, tours, hotels, cruises, insurance, visas, incentive groups and coach hire.', body, 'services.html', extra_js=js)

# ======================= TOURS =======================
def build_tours():
    regions = [('all', 'All tours', '全部'), ('asia', 'Asia', '亚洲'), ('europe', 'Europe', '欧洲'), ('africa', 'Africa', '非洲'), ('oceania', 'Australia &amp; New Zealand', '澳洲与纽西兰')]
    chips = '<div class="chips" data-filter-group="tourGrid" role="group" aria-label="Filter tours by region">' + ''.join(
        f'<button type="button" data-f="{k}" aria-pressed="{"true" if k == "all" else "false"}">{z if LANG == "zh" else e}</button>' for k, e, z in regions) + '</div>'
    order = [k for k, _, _ in regions]
    cards = ''.join(tour_card(t) for t in sorted(TOURS, key=lambda t: (bool(t.get('brand')), order.index(t['cat']))))  # YSL's own tours first, then partner tours by region
    body = f'''{nav('tours.html')}
<main id="main">
{head_block([('index.html', 'Home'), (None, 'Holidays &amp; Tours')], 'Holidays &amp; Tours', 'Where will you go next?', 'Our own group tours, and signature group tours from Malaysia’s leading tour brands, all booked and looked after by YSL.', chips)}
<section class="section" aria-label="Tours" style="padding-top:clamp(40px,5vw,72px)">
  <div class="container">
    <div class="tour-grid" id="tourGrid">{cards}</div>
    <div class="brand-note rv"><p><b>Looking for something else?</b> We also book packages from {', '.join(BRANDS[:-1])} and {BRANDS[-1]}. Tell us where you want to go and we’ll compare options for you.</p><a class="btn btn--red" href="contact.html">{WA}</a></div>
  </div>
</section>
</main>
{cta_band()}
{footer()}'''
    page('tours.html', 'Tour Packages from Malaysia | YSL Travel & Tours', 'Group tour packages from Kuala Lumpur to China, Japan, Korea, Taiwan, Vietnam, Europe, Switzerland, Türkiye, Egypt, South Africa and New Zealand. YSL’s own group tours and partner tours, booked in Klang.', body, 'tours.html')

# ======================= PRIVACY NOTICE AND 404 =======================
def build_privacy():
    if LANG == 'zh':
        content = legal.sections(legal.ZH) + '<p class="muted">如中文版本与英文版本有出入，以英文版本为准。<a href="../privacy.html">英文及马来文版本</a></p>'
        updated = legal.UPDATED[1]
    else:
        content = legal.sections(legal.EN) + '<p class="muted">If there is any difference between versions of this notice, the English version prevails.</p><h2 id="bm" lang="ms" style="margin-top:56px">Notis Privasi (Bahasa Malaysia)</h2>' + f'<div lang="ms">{legal.sections(legal.MS)}</div>'
        updated = legal.UPDATED[0]
    T = dict(h='隐私声明', eb='2010年个人资料保护法令', upd='最后更新：', end='。', title='隐私声明 | YSL Travel & Tours', desc='YSL Travel & Tours 依据《2010年个人资料保护法令》收集、使用及保护个人资料的方式。') if LANG == 'zh' else dict(h='Privacy Notice', eb='Personal Data Protection Act 2010', upd='Last updated ', end='.', title='Privacy Notice | YSL Travel & Tours', desc='How YSL Travel & Tours collects, uses and protects personal data under the Personal Data Protection Act 2010.')
    body = f'''{nav('')}
<main id="main">
{head_block([('index.html', 'Home'), (None, T['h'])], T['eb'], T['h'], T['upd'] + updated + T['end'])}
<section class="section" style="padding-top:clamp(32px,4vw,56px)">
  <div class="container"><div class="article-body legal-body">{content}</div></div>
</section>
</main>
{footer()}'''
    page('privacy.html', T['title'], T['desc'], body, '')

def build_404():
    zhp = LANG == 'zh'
    T = dict(eb='找不到页面', h='这个页面<span class="nw">已经搬走了。</span>', lead='链接可能已过时，或页面已更改。看看我们的旅游配套，或告诉我们您想去哪里。', tours='浏览行程', contact='联络我们', title='找不到页面 | YSL Travel & Tours', desc='找不到此页面。') if zhp else dict(eb='Page not found', h='This page has <span class="nw"><em>moved on.</em></span>', lead='The link may be old, or the page may have changed. Try our tours, or tell us where you want to go.', tours='Browse tours', contact='Contact us', title='Page not found | YSL Travel & Tours', desc='This page could not be found.')
    body = f'''{nav('')}
<main id="main">
{head_block([('index.html', 'Home'), (None, '404')], T['eb'], T['h'], T['lead'], f'<div class="btn-row" style="margin-top:32px"><a class="btn btn--red" href="tours.html">{T["tours"]}</a><a class="btn btn--line-dark" href="contact.html">{T["contact"]}</a></div>')}
</main>
{footer()}'''
    page('404.html', T['title'], T['desc'], body, '', extra_head=f'<base href="{'/zh/' if zhp else '/'}">\n<meta name="robots" content="noindex">')

# ======================= DEPARTURE DATES =======================
DATE_NOTES = {'School holidays': '学校假期', 'Fully booked': '已满'}

def dates_block(q):
    """Departure dates grouped by month; q['date_notes'] can tag single dates (school holidays, fully booked)."""
    if not q.get('dates'):
        return ''
    notes = q.get('date_notes', {})
    by_month = {}
    for d in q['dates']:
        by_month.setdefault(d[:7], []).append(d)
    def day(d):
        n = notes.get(d)
        label = f'{int(d[8:])}日' if LANG == 'zh' else str(int(d[8:]))
        if n:
            label += f' <small class="dep-note">{DATE_NOTES[n] if LANG == "zh" else n}</small>'
        return label
    sep = '、' if LANG == 'zh' else ', '
    rows = ''.join(f'<li><span class="code">{f"{int(k[:4])}年{int(k[5:])}月" if LANG == "zh" else f"{MON[int(k[5:])]} {k[:4]}"}</span><span>{sep.join(day(d) for d in v)}</span></li>' for k, v in by_month.items())
    return f'''<h3 class="h-m" style="margin-bottom:8px">Departure dates</h3>
      <p class="muted" style="margin:0 0 18px;font-size:14px">Group departures from Kuala Lumpur. Ask us which dates still have seats.</p>
      <ul class="dep-dates" style="margin-bottom:64px">{rows}</ul>
      '''

# ======================= QINGHAI & GANSU =======================
def build_tour_qg():
    q = QG
    hl = ''.join(f'<li>{h}</li>' for h in q['highlights'])
    fl = ''.join(f'''<li><span class="code">{d}</span><b>{fn}</b><span class="fl-route">{a}<i></i>{z}</span><span>{t1} to {t2}</span><small>{via}</small></li>''' for d, fn, a, z, t1, t2, via in q['flights'])
    days = ''
    for i, d in enumerate(q['days']):
        pics = ''
        for key in ('img', 'img2'):
            if d.get(key):
                pos = f' style="object-position:{d[key][2]}"' if len(d[key]) > 2 else ''
                pics += f'<figure><img src="assets/{d[key][0]}" alt="{d[key][1]}"{pos}><figcaption>{d[key][1]}</figcaption></figure>'
        meals = f'<span class="meals" title="Meals included">{d["meals"]}</span>' if d['meals'] else ''
        extra = ''
        if d.get('meal'): extra += f'<p class="d-meta"><span>Featured meal</span>{d["meal"]}</p>'
        if d.get('hotel'): extra += f'<p class="d-meta"><span>Stay</span>{d["hotel"]}</p>'
        if d.get('note'): extra += f'<p class="d-note">{d["note"]}</p>'
        days += f'''<li class="day rv"><div class="d-num"><span>Day</span>{i + 1:02d}</div><div class="d-body"><h3>{d['t']}{meals}</h3>{''.join(f'<p>{x}</p>' for x in d['p'])}{extra}{f'<div class="d-pics n{pics.count("<figure>")}">{pics}</div>' if pics else ''}</div></li>'''
    feats = ''.join(f'<li class="rv"><img src="assets/{im}" alt=""><b>{t}</b><p>{x}</p></li>' for im, t, x in q['features'])
    inc = ''.join(f'<li>{x}</li>' for x in q['included'])
    exc = ''.join(f'<li>{x}</li>' for x in q['excluded'])
    body = f'''{nav('tours.html')}
<main id="main">
<section class="tour-hero on-dark">
  <img src="assets/qg-hero.jpg" alt="The banded ridges of the Zhangye Rainbow Mountains">
  <div class="container">
    <ol class="crumbs"><li><a href="index.html">Home</a></li><li><a href="tours.html">Holidays &amp; Tours</a></li><li aria-current="page">Qinghai &amp; Gansu</li></ol>
    <p class="eyebrow">China &nbsp; Group tour &nbsp; {q['duration']}</p>
    <h1 class="h-xxl">{q['title']}</h1>
    <p class="line">{f'<span lang="zh-Hans" class="zh">{q["zh"]}</span> ' if q.get('zh') else ''}{q['line']}</p>
  </div>
</section>
<section class="section">
  <div class="container tour-layout">
    <div>
      <p class="eyebrow">Overview</p>
      <h2 class="h-l" style="margin-bottom:24px">Along the Silk Road to the roof of the plateau.</h2>
      <p class="lead" style="margin-bottom:48px">Ten days from Lanzhou through the Hexi Corridor to Dunhuang, across the Qaidam Basin to the salt lakes, and on to Qinghai Lake and Xining. Painted mountains, desert caves of Buddhist art, a lake that mirrors the sky, and the food of the Northwest along the way.</p>
      <h3 class="h-m" style="margin-bottom:20px">Highlights</h3>
      <ul class="highlights" style="margin-bottom:56px">{hl}</ul>
      <h3 class="h-m" style="margin-bottom:8px">Flights</h3>
      <p class="muted" style="margin:0 0 18px;font-size:14px">China Eastern, tentative and subject to airline confirmation. One checked bag up to 23kg, through-checked to Lanzhou.</p>
      <ul class="flights" style="margin-bottom:64px">{fl}</ul>
      {dates_block(q)}<h3 class="h-m" style="margin-bottom:24px">Day by day</h3>
      <ol class="days">{days}</ol>
    </div>
    <aside class="facts-card" aria-label="Tour details">
      <dl>
        <div><dt>Duration</dt><dd>{q['duration']}</dd></div>
        <div><dt>Tour type</dt><dd>Group tour</dd></div>
        <div><dt>Route</dt><dd>Lanzhou to Lanzhou</dd></div>
        <div><dt>Airline</dt><dd>China Eastern</dd></div>
        <div><dt>Hotels</dt><dd>4-Diamond</dd></div>
        <div><dt>Departures</dt><dd>{q.get('departs') or 'Ask us'}</dd></div>
        <div><dt>Fares</dt><dd>Latest fares on request</dd></div>
      </dl>
      <a class="btn btn--red" href="contact.html">Enquire on WhatsApp</a>
      <a class="btn btn--line-dark" href="contact.html">Ask for fares and dates</a>
      <p class="facts-note">Need a visa or travel insurance for this trip? <a href="services.html#visa">We arrange both.</a></p>
    </aside>
  </div>
</section>
<section class="section section--paper" aria-labelledby="pk-h">
  <div class="container">
    <div class="chapter-head"><div><p class="eyebrow">The package</p><h2 class="h-l" id="pk-h">Comfort for the long roads of the Northwest.</h2></div></div>
    <ul class="qg-feats">{feats}</ul>
    <div class="inc-grid" style="margin-top:56px">
      <div><h3>Included</h3><ul>{inc}</ul></div>
      <div><h3>Not included</h3><ul>{exc}</ul></div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="more-h">
  <div class="container">
    <div class="rail-head"><div><p class="eyebrow">You might also like</p><h2 class="h-l" id="more-h">More journeys</h2></div><a class="link-arrow" href="tours.html">All tours {ARROW}</a></div>
    <div class="tour-grid">{''.join(tour_card(t) for t in [x for x in TOURS if x['slug'] != q['slug']][:3])}</div>
  </div>
</section>
</main>
{cta_band()}
{footer()}'''
    page(q['page'], 'Majestic Qinghai & Gansu | YSL Travel & Tours', '10-day group tour through Gansu and Qinghai: the Rainbow Mountains, Mogao Caves, Chaka Salt Lake and Qinghai Lake.', body, 'tours.html')

# ======================= GOLDEN DESTINATIONS TOURS =======================
def build_gd_tour(q):
    hl = ''.join(f'<li>{h}</li>' for h in q['highlights'])
    days = ''
    for i, d in enumerate(q['days']):
        meals = f'<span class="meals" title="Meals included">{d["meals"]}</span>' if d['meals'] else ''
        extra = ''
        if d.get('meal'): extra += f'<p class="d-meta"><span>Featured meal</span>{d["meal"]}</p>'
        if d.get('hotel'): extra += f'<p class="d-meta"><span>Stay</span>{d["hotel"]}</p>'
        if d.get('note'): extra += f'<p class="d-note">{d["note"]}</p>'
        days += f'''<li class="day rv"><div class="d-num"><span>Day</span>{i + 1:02d}</div><div class="d-body"><h3>{d['t']}{meals}</h3>{''.join(f'<p>{x}</p>' for x in d['p'])}{extra}</div></li>'''
    inc = ''.join(f'<li>{x}</li>' for x in q['included'])
    exc = ''.join(f'<li>{x}</li>' for x in q['excluded'])
    notes = f'<p class="d-note" style="margin-top:28px">{q["notes"]}</p>' if q.get('notes') else ''
    i = next((n for n, t in enumerate(TOURS) if t['slug'] == q['slug']), -1)
    me = TOURS[i] if i >= 0 else {}
    rest = TOURS[i + 1:] + TOURS[:max(i, 0)]  # the tours that follow this one first, so related links spread across pages
    others = ''.join(tour_card(t) for t in ([x for x in rest if x.get('cat') == me.get('cat')] + [x for x in rest if x.get('cat') != me.get('cat')])[:3])
    if q.get('hero'):
        hero = f'''<section class="tour-hero on-dark">
  <img src="assets/{q['hero']}" alt="{q['hero_alt']}">'''
    else:
        hero = f'''<section class="tour-hero slot-hero on-dark" style="--c1:{q['c1']};--c2:{q['c2']}">
  <span class="slot-note">Tour photo to come</span>'''
    dates = dates_block(q)
    body = f'''{nav('tours.html')}
<main id="main">
{hero}
  <div class="container">
    <ol class="crumbs"><li><a href="index.html">Home</a></li><li><a href="tours.html">Holidays &amp; Tours</a></li><li aria-current="page">{q['region']}</li></ol>
    <p class="eyebrow">{q['region']} &nbsp; Group tour &nbsp; {q['duration']}</p>
    <h1 class="h-xxl">{q['title']}</h1>
    <p class="line">{f'<span lang="zh-Hans" class="zh">{q["zh"]}</span> ' if q.get('zh') else ''}{q['line']}</p>
  </div>
</section>
<section class="section">
  <div class="container tour-layout">
    <div>
      <p class="eyebrow">Overview</p>
      <h2 class="h-l" style="margin-bottom:24px">{q['head']}</h2>
      <p class="lead" style="margin-bottom:48px">{q['lead']}</p>
      <h3 class="h-m" style="margin-bottom:20px">Highlights</h3>
      <ul class="highlights" style="margin-bottom:56px">{hl}</ul>
      {dates}<h3 class="h-m" style="margin-bottom:24px">Day by day</h3>
      <ol class="days">{days}</ol>
    </div>
    <aside class="facts-card" aria-label="Tour details">
      <dl>
        <div><dt>Duration</dt><dd>{q['duration']}</dd></div>
        <div><dt>Tour type</dt><dd>Group tour</dd></div>
        <div><dt>Hotels</dt><dd>{q['hotels']}</dd></div>
        <div><dt>Departures</dt><dd>{q.get('departs') or 'Ask us'}</dd></div>
        <div><dt>Fares</dt><dd>Latest fares on request</dd></div>
        <div><dt>Tour by</dt><dd>{q.get('brand', 'Golden Destinations')}</dd></div>
      </dl>
      <a class="btn btn--red" href="contact.html?tour={q['slug']}">Enquire on WhatsApp</a>
      <a class="btn btn--line-dark" href="contact.html?tour={q['slug']}">Ask for fares and dates</a>
      <p class="facts-note">Need a visa or travel insurance for this trip? <a href="services.html#visa">We arrange both.</a></p>
    </aside>
  </div>
</section>
<section class="section section--paper" aria-labelledby="pk-h">
  <div class="container">
    <div class="chapter-head"><div><p class="eyebrow">The package</p><h2 class="h-l" id="pk-h">What’s included.</h2></div><p class="lead">Booked through YSL. We handle your booking, documents and questions from start to finish.</p></div>
    <div class="inc-grid">
      <div><h3>Included</h3><ul>{inc}</ul></div>
      <div><h3>Not included</h3><ul>{exc}</ul></div>
    </div>{notes}
    <p class="muted" style="margin:24px 0 0;font-size:13.5px">{'' if q.get('brand', '').startswith('YSL') else 'Operated by ' + q.get('brand', 'Golden Destinations') + '. '}{'Images are for illustration purposes only. ' if q.get('brand') == 'Apple Vacations' else ''}Itinerary order and hotels may change with local events, weather or availability. Fares, dates and the full itinerary are confirmed when you book.</p>
  </div>
</section>
<section class="section" aria-labelledby="more-h">
  <div class="container">
    <div class="rail-head"><div><p class="eyebrow">You might also like</p><h2 class="h-l" id="more-h">More journeys</h2></div><a class="link-arrow" href="tours.html">All tours {ARROW}</a></div>
    <div class="tour-grid">{others}</div>
  </div>
</section>
</main>
{cta_band()}
{footer()}'''
    name = (q.get('seo') or q['title']).replace('&amp;', '&')
    if LANG == 'zh':
        desc = f"{q['duration']}团体游，吉隆坡出发：{q['line']}" + (f"出发月份：{q['departs']}。" if q.get('departs') else '') + '团费欢迎询问，由 YSL Travel & Tours 代订。'
    else:
        desc = f"{q['duration']} group tour from Kuala Lumpur: {q['line']}" + (f" Departs {q['departs']}." if q.get('departs') else '') + ' Fares on request from YSL Travel & Tours.'
    page(q['page'], f"{name} | YSL Travel & Tours", desc, body, 'tours.html', og_image=f"assets/{q['hero']}" if q.get('hero') else 'assets/hero.jpg')

# ======================= JOURNAL =======================
def _by_date(a):
    import datetime
    return datetime.datetime.strptime(a.get('date_en', a['date']), '%d %B %Y')

def build_journal():
    posts = sorted(ARTICLES, key=_by_date, reverse=True)
    f, rest = posts[0], posts[1:]
    chips = '<div class="chips" data-filter-group="postGrid" role="group" aria-label="Filter stories">' + ''.join(
        f'<button type="button" data-f="{k}" aria-pressed="{"true" if k == "all" else "false"}">{l}</button>' for k, l in [('all', 'All stories'), ('dest', 'Destinations'), ('tips', 'Travel tips'), ('corp', 'Corporate travel')]) + '</div>'
    grid = ''.join(post_card(p) for p in rest)
    fvis = f'<div class="media"><img src="assets/{f['img']}" alt="{f['alt']}"></div>' if f.get('img') else f'<div class="media slot" style="--c1:{f['slot'][0]};--c2:{f['slot'][1]}"><b>{f['slot'][2]}</b><small>Photo to come</small></div>'
    body = f'''{nav('journal.html')}
<main id="main">
{head_block([('index.html', 'Home'), (None, 'Journal')], 'Journal', 'Stories from <span class="nw"><em>the road.</em></span>', 'Destination guides, travel tips and corporate travel advice from the YSL Travel &amp; Tours team.', chips)}
<section class="section">
  <div class="container">
    <a class="feature-post rv" href="{f['href']}" data-cat="{f['cat']}">{fvis}<div><span class="tag">{f['cat_label']}</span><h2 class="h-l">{f['title']}</h2><p>{f['lead']}</p><span class="link-arrow">Read the story {ARROW}</span></div></a>
    <div class="post-grid" id="postGrid">{grid}<p class="empty-note" id="postGridEmpty" hidden>No stories in this topic yet.</p></div>
  </div>
</section>
</main>
{footer()}'''
    page('journal.html', 'Journal | YSL Travel & Tours', 'Destination guides, travel tips and corporate travel advice from YSL Travel & Tours.', body, 'journal.html')

def build_article(a):
    others = [p for p in sorted(ARTICLES, key=_by_date, reverse=True) if p['slug'] != a['slug']]
    same = [p for p in others if p['cat'] == a['cat']]
    rel = ''.join(post_card(p) for p in (same + [p for p in others if p not in same])[:3])
    fig = f'<figure class="lead-figure" style="margin:0"><img src="assets/{a['img']}" alt="{a['alt']}"></figure>' if a.get('img') else f'<figure class="lead-figure" style="margin:0"><div class="slot lead-slot" style="--c1:{a['slot'][0]};--c2:{a['slot'][1]}"><b>{a['slot'][2]}</b><small>Photo to come</small></div></figure>'
    ct, ctext, chref, clabel = a['cta']
    body = f'''{nav('journal.html')}
<main id="main">
<article>
  <header class="article-head">
    <ol class="crumbs"><li><a href="index.html">Home</a></li><li><a href="journal.html">Journal</a></li><li aria-current="page">{a['cat_label']}</li></ol>
    <span class="tag">{a['cat_label']}</span>
    <h1 class="h-xl">{a['title']}</h1>
    <p class="lead">{a['lead']}</p>
    <div class="byline"><span>By the YSL team</span><span>{a['date']}</span><span>{a['read']}</span></div>
  </header>
  {fig}
  <div class="article-body">
    {a['body']}
    <div class="inline-cta on-dark"><h2 class="h-m">{ct}</h2><p>{ctext}</p><div class="btn-row"><a class="btn btn--white" href="{chref}">{clabel}</a><a class="btn btn--line-light" href="contact.html">{WA}</a></div></div>
    <div class="share-row"><span>Share this story</span><button type="button" data-copy="" data-copied="Copied">Copy link</button></div>
  </div>
</article>
<section class="section section--paper" aria-labelledby="rel-h">
  <div class="container"><div class="rail-head"><h2 class="h-l" id="rel-h">More from the journal</h2><a class="link-arrow" href="journal.html">All stories {ARROW}</a></div><div class="post-grid">{rel}</div></div>
</section>
</main>
{footer()}'''
    import html as _h
    page(a['href'], f"{_h.unescape(a.get('seo') or a['title'])} | YSL Travel & Tours", _h.unescape(re.sub('<[^>]+>', '', a['lead'])), body, 'journal.html', og_image=f"assets/{a['img']}" if a.get('img') else 'assets/hero.jpg')

# ======================= CONTACT =======================
def build_contact():
    opts = ''.join(f'<option>{s["title"]}</option>' for s in SERVICES)
    body = f'''{nav('contact.html')}
<main id="main">
{head_block([('index.html', 'Home'), (None, 'Contact')], 'Contact us', 'Let’s plan <em>your next trip.</em>', 'Message us on WhatsApp, call, or visit our office in Klang. We’d be glad to look after your travel, for business or for pleasure.')}
<section class="section">
  <div class="container contact-grid">
    <div class="rv">
      <dl class="detail-list">
        <div><dt>Office</dt><dd>{CONTACT['address']}</dd></div>
        <div><dt>Phone</dt><dd>{CONTACT['phone']}</dd></div>
        <div><dt>WhatsApp</dt><dd><a href="https://wa.me/{CONTACT['wa']}" target="_blank" rel="noopener">{CONTACT['whatsapp']}</a><br><small class="muted">We reply during office hours.</small></dd></div>
        <div><dt>Email</dt><dd>{CONTACT['email']}</dd></div>
        <div><dt>Opening hours</dt><dd>{CONTACT['hours']}</dd></div>
        <div><dt>Payment</dt><dd>Touch ’n Go eWallet accepted at our office</dd></div>
      </dl>
      <div class="btn-row" style="margin-top:32px"><a class="btn btn--line-dark" href="{CONTACT['maps']}" target="_blank" rel="noopener">Open in Google Maps</a></div>
    </div>
    <form class="form-card rv" id="enquiry" novalidate>
      <h2 class="h-m">Send us a trip enquiry</h2>
      <p>Fill in what you know. We’ll turn it into a WhatsApp message so you can send it in one tap.</p>
      <div class="fields">
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" placeholder="Name"></div>
        <div class="field"><label for="f-type">I’m interested in</label><select id="f-type" name="type">{opts}</select></div>
        <div class="field"><label for="f-dest">Destination</label><input id="f-dest" name="dest" placeholder="For example, Japan"></div>
        <div class="field"><label for="f-month">When</label><input id="f-month" name="month" placeholder="For example, March 2027"></div>
        <div class="field"><label for="f-pax">Number of travellers</label><input id="f-pax" name="pax" inputmode="numeric" placeholder="2"></div>
        <div class="field"><label for="f-co">Company (optional)</label><input id="f-co" name="co" autocomplete="organization" placeholder="For corporate trips"></div>
        <div class="field full"><label for="f-msg">Anything else?</label><textarea id="f-msg" name="msg" placeholder="Budget, hotel preferences, special requests"></textarea></div>
      </div>
      <p class="preview-label">Your message</p>
      <div class="preview" id="preview" aria-live="polite"></div>
      <div class="form-actions"><button class="btn btn--red" type="submit">Send on WhatsApp</button><small id="formNote">Opens WhatsApp with your message ready to send. See our <a href="privacy.html">Privacy Notice</a>.</small></div>
    </form>
  </div>
</section>
</main>
{footer()}'''
    js = '''
<script>
(function () {
  var WA_NUMBER = '__WA__'; // office WhatsApp line, digits only
  var T = __T__;
  var form = document.getElementById('enquiry'), prev = document.getElementById('preview'), note = document.getElementById('formNote');
  function msg() {
    var v = function (n) { return (form.elements[n].value || '').trim(); };
    var lines = [T.hello];
    lines.push(T.ask + (T.lower ? v('type').toLowerCase() : v('type')) + (v('dest') ? T.to + v('dest') : '') + T.stop);
    if (v('month')) lines.push(T.when + v('month'));
    if (v('pax')) lines.push(T.pax + v('pax'));
    if (v('co')) lines.push(T.co + v('co'));
    if (v('msg')) lines.push(v('msg'));
    lines.push(T.thanks + (v('name') ? T.sign + v('name') : '') + T.end);
    return lines.join('\\n');
  }
  function update() { prev.textContent = msg(); }
  // arriving from a tour or a landmark on the globe: fill in the destination
  try {
    var q = new URLSearchParams(location.search), NAMES = __NAMES__;
    var d = q.get('dest') || NAMES[q.get('tour')] || '';
    if (d && !form.elements.dest.value) form.elements.dest.value = d;
    if (q.get('tour')) form.elements.type.selectedIndex = __TOURIDX__; // enquiries from a tour page are about that tour
  } catch (e) {}
  form.addEventListener('input', update); update();
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!WA_NUMBER) { note.textContent = T.proto; return; }
    var a = document.createElement('a'); a.href = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(msg()); a.target = '_blank'; a.rel = 'noopener';
    document.body.appendChild(a); a.click(); a.remove();
  });
})();
</script>'''
    import json, html as _h
    js = js.replace('__WA__', CONTACT['wa'])
    js = js.replace('__TOURIDX__', str([s['slug'] for s in SERVICES].index('tours')))
    js = js.replace('__NAMES__', json.dumps({t['slug']: _h.unescape(t['title']) for t in TOURS}))
    js = js.replace('__T__', json.dumps(zh.CONTACT_JS if LANG == 'zh' else dict(
        hello='Hello YSL Travel & Tours,', ask='I\u2019d like to ask about ', lower=True, to=' to ', stop='.', when='When: ', pax='Travellers: ',
        co='Company: ', thanks='Thank you', sign=', ', end='.', proto='Prototype: the WhatsApp number will be added once YSL confirms it.')))
    page('contact.html', 'Contact | YSL Travel & Tours', 'Visit, call or message YSL Travel & Tours in Klang, Selangor.', body, 'contact.html', extra_js=js)

if __name__ == '__main__':
    os.makedirs(os.path.join(DIST, 'assets'), exist_ok=True)
    open(os.path.join(DIST, 'assets', 'site.css'), 'w', encoding='utf-8').write(read('site.css') + read('pages.css') + read('home.css') + read('premium.css') + read('type.css') + read('red.css') + read('zh.css'))
    open(os.path.join(DIST, 'assets', 'site.js'), 'w', encoding='utf-8').write(read('site.js'))
    open(os.path.join(DIST, 'assets', 'landmarks.js'), 'w', encoding='utf-8').write(read('landmark-art.js'))
    def build_pages():
        build_home(); build_corporate(); build_about(); build_services(); build_tours(); build_tour_qg(); [build_gd_tour(q) for q in GD_TOURS]; build_journal(); [build_article(a) for a in ARTICLES]; build_contact(); build_privacy(); build_404()
    build_pages()
    # Chinese site: same templates, Chinese content from zh.py, written to dist/zh/
    os.makedirs(os.path.join(DIST, 'zh'), exist_ok=True)
    LANG = 'zh'
    SERVICES, TOURS, CONTACT, MEMBERS, OPENINGS, QG, GD_TOURS, ARTICLES = zh.localise(SERVICES, TOURS, CONTACT, MEMBERS, OPENINGS, QG, GD_TOURS, ARTICLES)
    build_pages()
    zh.check(os.path.join(DIST, 'zh'))
    # sitemap.xml and robots.txt, from the pages just written (both languages, no 404)
    import datetime
    today = datetime.date.today().isoformat()
    pages = sorted(f for f in os.listdir(DIST) if f.endswith('.html') and f != '404.html' and os.path.exists(os.path.join(DIST, 'zh', f)))
    urls = []
    for f in pages:
        p = '' if f == 'index.html' else f
        alts = f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}/{p}"/><xhtml:link rel="alternate" hreflang="zh-Hans" href="{SITE}/zh/{p}"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/{p}"/>'
        for loc in (f'{SITE}/{p}', f'{SITE}/zh/{p}'):
            urls.append(f'  <url><loc>{loc}</loc><lastmod>{today}</lastmod>{alts}</url>')
    open(os.path.join(DIST, 'sitemap.xml'), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(urls) + '\n</urlset>\n')
    open(os.path.join(DIST, 'robots.txt'), 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    print('wrote sitemap.xml with', len(urls), 'URLs, and robots.txt')
