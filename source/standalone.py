# Stand-alone feedback site for feedback.ysltravel.com, launched before the main website.
# Output: ../feedback-site/  (upload this folder to Cloudflare Pages)
import os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B
import feedback

OUT = os.path.join(B.SRC, '..', 'feedback-site')
MAIN_SITE = 'https://ysltravel.com'


def nav(_):
    return f'''<header class="site-nav">
  <div class="container">
    <a class="brand" href="{MAIN_SITE}" aria-label="YSL Travel and Tours">{B.LOGO}<span>Travel &amp; Tours</span></a>
    <a class="nav-cta" href="{MAIN_SITE}">ysltravel.com</a>
  </div>
</header>'''


def footer():
    C = B.CONTACT
    return f'''<footer class="site-footer on-dark">
  <div class="container">
    <div class="foot-grid">
      <div class="foot-brand">{B.LOGO}<p>Travel services for individuals and companies, from Klang to the world since 2009.</p></div>
      <div><h4>Visit us</h4><p style="margin:0">{C['address']}</p></div>
      <div><h4>Opening hours</h4><p style="margin:0">{C['hours']}</p></div>
      <div><h4>Get in touch</h4><ul><li>{C['phone']}</li><li>{C['email']}</li><li><a href="{C['facebook']}" target="_blank" rel="noopener">Facebook</a></li><li><a href="{MAIN_SITE}">ysltravel.com</a></li></ul></div>
    </div>
    <div class="foot-base">
      <span>&copy; 2026 YSL Travel &amp; Tours Sdn Bhd (877803-T) &nbsp; <span lang="zh-Hans">咏胜天下旅游有限公司</span></span>
      <span>Licence KPL 6107 &nbsp; Member of MATTA, MITA, MICA and MCTA</span>
    </div>
  </div>
</footer>'''


def head_block(crumb, eyebrow, title, lead, extra=''):
    return f'''<section class="page-head">
  <div class="container">
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="h-xxl">{title}</h1>
    <p class="lead">{lead}</p>{extra}
  </div>
</section>'''


def page_to(out):
    def page(fname, title, desc, body, current, home=False, extra_head='', extra_js=''):
        saved = B.DIST
        B.DIST = out
        try:
            B.page(fname, title, desc, body, current, home=False, extra_head=extra_head, extra_js=extra_js)
        finally:
            B.DIST = saved
    return page


LINKS = r'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Feedback Link Maker | YSL Travel &amp; Tours</title>
__FONTS__
<link rel="stylesheet" href="assets/site.css">
<style>
.lm-wrap { max-width: 720px; }
.lm-out { margin-top: 32px; padding: 24px; background: #fff; border-radius: 20px; display: grid; grid-template-columns: 180px minmax(0, 1fr); gap: 24px; align-items: center; }
.lm-out code { display: block; font-family: var(--mono); font-size: 13px; word-break: break-all; background: var(--ivory); padding: 12px 14px; border-radius: 10px; }
#qr { width: 180px; height: 180px; }
#qr img, #qr canvas { width: 180px !important; height: 180px !important; }
@media (max-width: 600px) { .lm-out { grid-template-columns: minmax(0, 1fr); } }
</style>
</head>
<body>
__NAV__
<main id="main">
<section class="page-head"><div class="container">
  <p class="eyebrow">For tour leaders and staff</p>
  <h1 class="h-xxl">Feedback <em>link maker.</em></h1>
  <p class="lead">Fill in the departure details to make a link and QR code with the tour already filled in. Send the link on WhatsApp, or show the QR code on the coach on the last day.</p>
</div></section>
<section class="section" style="padding-top:48px"><div class="container lm-wrap">
  <form class="fields" id="lm" onsubmit="return false">
    <div class="field"><label for="code">Tour code</label><input id="code" placeholder="For example, QH2611" autocomplete="off"></div>
    <div class="field"><label for="leader">Tour leader</label><input id="leader" autocomplete="off"></div>
    <div class="field"><label for="dep">Departure date</label><input id="dep" type="date"></div>
    <div class="field"><label for="ret">Return date</label><input id="ret" type="date"></div>
  </form>
  <div class="lm-out">
    <div id="qr" aria-label="QR code for the feedback link"></div>
    <div>
      <code id="url"></code>
      <div class="btn-row" style="margin-top:16px">
        <button class="btn btn--red" type="button" id="copy">Copy link</button>
        <button class="btn btn--line-dark" type="button" id="dl">Download QR</button>
        <a class="btn btn--line-dark" id="wa" target="_blank" rel="noopener">Share on WhatsApp</a>
      </div>
    </div>
  </div>
</div></section>
</main>
<script src="assets/qrcode.js"></script>
<script>
(function () {
  var base = location.origin + '/', qrBox = document.getElementById('qr'), urlEl = document.getElementById('url'), qr = null;
  function make() {
    var p = new URLSearchParams();
    [['code', 'code'], ['leader', 'leader'], ['dep', 'dep'], ['ret', 'ret']].forEach(function (k) { var v = document.getElementById(k[0]).value.trim(); if (v) p.set(k[1], v); });
    var u = base + (p.toString() ? '?' + p.toString() : '');
    urlEl.textContent = u;
    document.getElementById('wa').href = 'https://wa.me/?text=' + encodeURIComponent('Thank you for travelling with YSL Travel & Tours! Please tell us about your trip (3 minutes): ' + u);
    var q = qrcode(0, 'M'); q.addData(u); q.make();
    var n = q.getModuleCount(), px = 12, m = 4, size = (n + m * 2) * px, c = document.createElement('canvas');
    c.width = c.height = size; var g = c.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, size, size); g.fillStyle = '#170407';
    for (var r = 0; r < n; r++) for (var k = 0; k < n; k++) if (q.isDark(r, k)) g.fillRect((k + m) * px, (r + m) * px, px, px);
    qrBox.innerHTML = ''; qrBox.appendChild(c);
  }
  document.getElementById('lm').addEventListener('input', make);
  document.getElementById('copy').addEventListener('click', function () {
    var b = this; navigator.clipboard.writeText(urlEl.textContent).then(function () { b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Copy link'; }, 1500); });
  });
  document.getElementById('dl').addEventListener('click', function () {
    var c = qrBox.querySelector('canvas');
    var a = document.createElement('a'); a.href = c.toDataURL('image/png');
    a.download = 'ysl-feedback-' + (document.getElementById('code').value.trim() || 'qr') + '.png'; a.click();
  });
  make();
})();
</script>
</body>
</html>'''

APPS_SCRIPT = r'''/**
 * YSL tour feedback -> Google Sheet
 * 1. Create a Google Sheet named "YSL Tour Feedback".
 * 2. Extensions > Apps Script. Delete what is there, paste this whole file, Save.
 * 3. Deploy > New deployment > type: Web app.
 *      Execute as: Me      Who has access: Anyone
 *    Deploy, authorise, then copy the Web app URL (ends in /exec).
 * 4. Paste that URL into config.js on the feedback site and re-upload.
 * Ratings are stored as numbers: 4 Excellent, 3 Good, 2 Average, 1 Poor.
 */
var COLUMNS = [
  'submitted_at', 'tour_code', 'tour_leader', 'departure', 'return',
  'leader_lead', 'leader_attitude', 'leader_knowledge',
  'guide_lead', 'guide_attitude', 'guide_knowledge',
  'tour_itinerary', 'tour_hotel', 'tour_meals', 'tour_transport', 'tour_driver',
  'overall', 'comments', 'times', 'reasons', 'reasons_other', 'source', 'source_other',
  'name', 'phone', 'email'
];

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(COLUMNS);
      sheet.setFrozenRows(1);
      sheet.getRange(1, 1, 1, COLUMNS.length).setFontWeight('bold');
    }
    var d = JSON.parse(e.postData.contents);
    var row = COLUMNS.map(function (k) {
      var v = d[k];
      if (v === undefined || v === null) return '';
      if (Array.isArray(v)) return v.join(', ');
      if (k === 'submitted_at') return new Date(v);
      return v;
    });
    sheet.appendRow(row);
    return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}
'''

README = '''YSL TOUR FEEDBACK SITE  (feedback.ysltravel.com)
================================================

WHAT IS IN THIS FOLDER
  index.html        the feedback form (opens at feedback.ysltravel.com)
  links.html        link and QR maker for tour leaders (feedback.ysltravel.com/links)
  config.js         where the Google Sheet address goes (step B)
  assets/           styles and scripts
  _headers          keeps search engines away from the form
  google-apps-script.gs   paste into the response sheet (step B); not served

A. PUT IT ONLINE (Cloudflare Pages)
  1. dash.cloudflare.com > Workers & Pages > Create > Pages > Upload assets.
  2. Project name: ysl-feedback. Drag in THIS FOLDER (or the zip). Deploy.
     It is now live at ysl-feedback.pages.dev
  3. In the project: Custom domains > Set up a custom domain > feedback.ysltravel.com
     Cloudflare shows a CNAME record to add. Keep that tab open.
  4. Squarespace > Domains > ysltravel.com > DNS > Custom records > Add record:
        Host:  feedback
        Type:  CNAME
        Data:  ysl-feedback.pages.dev
     Do not change any other record (email and the current website keep working).
  5. Back in Cloudflare, wait for the domain to show Active (minutes to a few hours).
     HTTPS is set up automatically.

B. CONNECT THE GOOGLE SHEET (where responses go)
  1. Follow the steps at the top of google-apps-script.gs.
  2. Open config.js and paste the Web app URL between the quotes.
  3. Upload again: Cloudflare project > Create new deployment > drag the folder in.
  4. Test: fill in the form once, check the new row in the sheet.
  Until this is done, the form works but does not store answers (it says so on screen).

C. USING IT
  Open feedback.ysltravel.com/links, fill in the tour code, leader and dates,
  then copy the link for WhatsApp or download the QR code for the coach.
'''


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'assets'))
    css = ''.join(B.read(f) for f in ['site.css', 'pages.css', 'home.css', 'premium.css', 'type.css', 'red.css'])
    open(os.path.join(OUT, 'assets', 'site.css'), 'w', encoding='utf-8').write(css)
    open(os.path.join(OUT, 'assets', 'site.js'), 'w', encoding='utf-8').write(B.read('site.js'))
    shutil.copy(os.path.join(B.SRC, 'qrcode.js'), os.path.join(OUT, 'assets', 'qrcode.js'))
    feedback.build(page_to(OUT), nav, head_block, footer, fname='index.html',
                   extra_head='\n<script src="config.js"></script>')
    open(os.path.join(OUT, 'config.js'), 'w').write(
        "// Paste the Google Apps Script web-app URL between the quotes (see README).\n"
        "window.YSL_FEEDBACK_ENDPOINT = 'https://script.google.com/macros/s/AKfycbzOI8DvEP1TWT9p-qvFXi4zVEIdY6laByLnDyo3QAWCKD6zjr3Nwo-_TA0IEAobBo4K/exec';\n")
    links = LINKS.replace('__FONTS__', B.FONTS).replace('__NAV__', nav(''))
    open(os.path.join(OUT, 'links.html'), 'w', encoding='utf-8').write(links.encode('ascii', 'xmlcharrefreplace').decode('ascii'))
    open(os.path.join(OUT, '_headers'), 'w').write('/*\n  X-Robots-Tag: noindex\n')
    open(os.path.join(OUT, 'google-apps-script.gs'), 'w').write(APPS_SCRIPT)
    open(os.path.join(OUT, 'README.txt'), 'w').write(README)
    print('standalone written to', os.path.abspath(OUT))


if __name__ == '__main__':
    main()
