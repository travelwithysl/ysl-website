# Tour feedback form: the YSL Travel Experience Evaluation Form, rebuilt as a mobile-first web page.
# Reached by a link or QR code sent at the end of each tour; not in the menu, not indexed.
# Prefill from the link: feedback.html?code=QH2611&leader=Tan&dep=2026-11-02&ret=2026-11-11

LEVELS = [('4', 'Excellent', '非常满意'), ('3', 'Good', '满意'), ('2', 'Average', '可接受'), ('1', 'Poor', '不满意')]

PEOPLE = [('leader', 'Tour leader', '领队', 'Please rate the tour leader.', '请对领队进行评分。'),
          ('guide', 'Local tour guide', '导游', 'Please rate the local tour guide.', '请对当地导游进行评分。')]
PEOPLE_CRIT = [('lead', 'Leadership ability', '领导才能'), ('attitude', 'Service attitude', '服务态度'), ('knowledge', 'Destination knowledge', '知识掌握')]
TOUR_CRIT = [('itinerary', 'Itinerary', '行程安排'), ('hotel', 'Hotel', '住宿安排'), ('meals', 'Meals', '餐式安排'),
             ('transport', 'Transportation', '交通安排'), ('driver', 'Driver', '司机服务')]
REASONS = [('advert', 'Advertisement', '广告宣传'), ('itinerary', 'Ideal itinerary', '心仪的行程'), ('date', 'Suitable departure date', '出发日期合适'),
           ('price', 'Competitive price', '价格合理'), ('brand', 'Strong brand recognition', '品牌认知度高'), ('service', 'Quality service', '服务良好'),
           ('referral', 'Recommended by family or friends', '亲友推荐')]
SOURCES = [('newspaper', 'Newspaper', '报纸'), ('fair', 'Travel fair', '旅游展'), ('social', 'Social media', '社交媒体'), ('friends', 'Friends and family', '亲友介绍')]


def zh(s):
    return f'<span class="zh" lang="zh-Hans">{s}</span>'


def rating_row(group, key, en, cn):
    name = f'{group}_{key}'
    opts = ''.join(
        f'<label class="rate"><input type="radio" name="{name}" value="{v}"><span><b>{e}</b>{zh(c)}</span></label>'
        for v, e, c in LEVELS)
    return f'<fieldset class="rate-row"><legend><b>{en}</b>{zh(cn)}</legend><div class="rate-opts">{opts}</div></fieldset>'


def chips(name, items, other=True):
    out = ''.join(f'<label class="chip"><input type="checkbox" name="{name}" value="{k}"><span>{e}{zh(c)}</span></label>' for k, e, c in items)
    if other:
        out += (f'<label class="chip"><input type="checkbox" name="{name}" value="other" data-other="{name}_other"><span>Other{zh("其它")}</span></label>'
                f'<div class="field other-field" id="{name}_other_wrap" hidden><label for="{name}_other">Please state {zh("请注明")}</label><input id="{name}_other" name="{name}_other"></div>')
    return f'<div class="chip-set">{out}</div>'


def section(num, en, cn, body, sub_en='', sub_cn=''):
    sub = f'<p class="fb-sub">{sub_en} {zh(sub_cn)}</p>' if sub_en else ''
    return f'''<section class="fb-sec rv"><header><span class="fb-num">{num:02d}</span><h2 class="h-m">{en} {zh(cn)}</h2>{sub}</header>{body}</section>'''


def build(page, nav, head_block, footer, fname='feedback.html', extra_head=''):
    trip = '''<div class="fields">
        <div class="field"><label for="fb-code">Tour code {z1}</label><input id="fb-code" name="tour_code" required autocomplete="off" placeholder="For example, QH2611"></div>
        <div class="field"><label for="fb-leader">Tour leader {z2}</label><input id="fb-leader" name="tour_leader" autocomplete="off"></div>
        <div class="field"><label for="fb-dep">Departure date {z3}</label><input id="fb-dep" name="departure" type="date"></div>
        <div class="field"><label for="fb-ret">Return date {z4}</label><input id="fb-ret" name="return" type="date"></div>
      </div>'''.format(z1=zh('团号'), z2=zh('领队'), z3=zh('出发日期'), z4=zh('返回日期'))
    you = '''<div class="fields">
        <div class="field full"><label for="fb-name">Name {z1}</label><input id="fb-name" name="name" autocomplete="name"></div>
        <div class="field"><label for="fb-tel">Contact number {z2}</label><input id="fb-tel" name="phone" type="tel" autocomplete="tel" inputmode="tel"></div>
        <div class="field"><label for="fb-email">Email {z3}</label><input id="fb-email" name="email" type="email" autocomplete="email"></div>
      </div><p class="fb-note">You can leave this section blank to stay anonymous. Add your details only if you would like us to reply. {z4}</p>'''.format(
        z1=zh('姓名'), z2=zh('联络电话'), z3=zh('电邮'), z4=zh('此部分可留空以匿名提交；如需我们回复，请留下联络资料。'))

    secs = [section(1, 'Your trip', '您的行程', trip)]
    n = 2
    for g, en, cn, sen, scn in PEOPLE:
        secs.append(section(n, en, cn, ''.join(rating_row(g, k, e, c) for k, e, c in PEOPLE_CRIT), sen, scn)); n += 1
    secs.append(section(n, 'The tour', '旅程各项', ''.join(rating_row('tour', k, e, c) for k, e, c in TOUR_CRIT),
                        'Please rate each part of the tour.', '请对以下行程内容进行评分。')); n += 1
    overall = f'''<div class="score">
        <div class="score-top"><label for="fb-score">Overall rating {zh('整体评分')}</label><output id="fb-score-out" for="fb-score">–<small>/100</small></output></div>
        <input id="fb-score" name="overall" type="range" min="0" max="100" step="5" value="80" aria-describedby="fb-score-hint">
        <div class="score-scale" id="fb-score-hint"><span>Dissatisfied {zh('不满意')}</span><span>Satisfied {zh('满意')}</span></div>
      </div>
      <div class="field full"><label for="fb-comments">Comments {zh('意见反馈')}</label><textarea id="fb-comments" name="comments" placeholder="What did you enjoy most? What could we do better?"></textarea></div>'''
    secs.append(section(n, 'Overall', '整体满意度', overall)); n += 1
    times = ''.join(f'<label class="chip"><input type="radio" name="times" value="{v}"><span>{l}</span></label>' for v, l in
                    [('1', 'First trip'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5+', '5 or more')])
    secs.append(section(n, 'Travelling with YSL', '参团次数', f'<div class="chip-set">{times}</div>',
                        'How many times have you travelled with YSL Travel &amp; Tours?', '这是您第几次参加咏胜旅游组织的旅行团？')); n += 1
    secs.append(section(n, 'Why this tour', '选择原因', chips('reasons', REASONS),
                        'What made you choose this tour? Choose any that apply.', '请勾选您选择本次行程的原因（可多选）。')); n += 1
    secs.append(section(n, 'How you found us', '认识渠道', chips('source', SOURCES),
                        'How did you hear about YSL Travel &amp; Tours?', '您是通过哪种渠道认识我们的？')); n += 1
    secs.append(section(n, 'About you (optional)', '联络资料（可选填）', you))

    body = f'''{nav('')}
<main id="main">
{head_block([('index.html', 'Home'), (None, 'Tour feedback')], 'Tour feedback ' + zh('旅游体验评估'), 'How was <span class="nw"><em>your trip?</em></span>',
            'Thank you for travelling with us. This takes about three minutes, and every answer is read by our team. ' + zh('感谢您参加咏胜旅游的行程。填写约需三分钟，每份意见都会由我们的团队细阅。'))}
<section class="section fb-wrap">
  <div class="container">
    <form class="fb-form" id="feedback" novalidate>
      {''.join(secs)}
      <div class="fb-submit rv">
        <p class="fb-err" id="fb-err" role="alert" hidden></p>
        <button class="btn btn--red" type="submit">Send feedback {zh('提交')}</button>
        <small>Your answers go to the YSL Travel &amp; Tours team only. {zh('您的资料仅供咏胜旅游内部使用。')}</small>
      </div>
    </form>
    <div class="fb-done" id="fb-done" hidden tabindex="-1">
      <p class="eyebrow">Thank you {zh('谢谢')}</p>
      <h2 class="h-xl">Thank you for <em>your feedback.</em></h2>
      <p class="lead">It helps us look after every traveller a little better. If you enjoyed your trip, we would be grateful for a review. {zh('您的宝贵意见将帮助我们持续优化服务。若您喜欢这次旅程，诚邀您为我们留下评价。')}</p>
      <div class="btn-row" style="margin-top:28px"><a class="btn btn--red" href="https://g.page/r/CTdiPzG-FVF4EAE/review" target="_blank" rel="noopener">Review us on Google</a><a class="btn btn--line-dark" href="https://www.facebook.com/ysltravel/reviews" target="_blank" rel="noopener">Recommend us on Facebook</a></div>
      <p class="fb-note" id="fb-proto" hidden>Prototype: this response was not stored. It will be saved once the form is connected to YSL’s response sheet.</p>
    </div>
  </div>
</section>
</main>
{footer()}'''

    js = r'''
<script>
(function () {
  var ENDPOINT = window.YSL_FEEDBACK_ENDPOINT || ''; // set in config.js: the Google Apps Script web-app URL
  var form = document.getElementById('feedback'), done = document.getElementById('fb-done'), err = document.getElementById('fb-err');
  // prefill trip details from the link
  try {
    var q = new URLSearchParams(location.search);
    [['code', 'tour_code'], ['leader', 'tour_leader'], ['dep', 'departure'], ['ret', 'return']].forEach(function (p) {
      if (q.get(p[0])) form.elements[p[1]].value = q.get(p[0]);
    });
  } catch (e) {}
  // overall score readout
  var s = document.getElementById('fb-score'), out = document.getElementById('fb-score-out'), touched = false;
  function show() { out.innerHTML = (touched ? s.value : '–') + '<small>/100</small>'; s.style.setProperty('--p', s.value + '%'); }
  s.addEventListener('input', function () { touched = true; show(); }); show();
  // "Other" reveals a text box
  form.addEventListener('change', function (e) {
    var t = e.target; if (!t.dataset || !t.dataset.other) return;
    var w = document.getElementById(t.dataset.other + '_wrap'); w.hidden = !t.checked; if (t.checked) w.querySelector('input').focus();
  });
  function collect() {
    var d = { submitted_at: new Date().toISOString(), page: location.href };
    new FormData(form).forEach(function (v, k) { if (d[k] !== undefined) d[k] = [].concat(d[k], v); else d[k] = v; });
    if (!touched) delete d.overall;
    return d;
  }
  form.addEventListener('submit', function (e) {
    e.preventDefault(); err.hidden = true;
    var miss = [];
    if (!form.elements.tour_code.value.trim()) miss.push('tour code 团号');
    if (!touched) miss.push('overall rating 整体评分');
    if (miss.length) { err.textContent = 'Please add your ' + miss.join(' and ') + '.'; err.hidden = false; err.scrollIntoView({ block: 'center', behavior: 'smooth' }); return; }
    var data = collect(), btn = form.querySelector('button[type=submit]');
    function finish() { form.hidden = true; done.hidden = false; done.focus(); window.scrollTo(0, done.getBoundingClientRect().top + scrollY - 120); }
    if (!ENDPOINT) { document.getElementById('fb-proto').hidden = false; try { console.log('feedback', data); } catch (x) {} finish(); return; }
    btn.disabled = true;
    fetch(ENDPOINT, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(data) })
      .then(finish).catch(function () { btn.disabled = false; err.textContent = 'Sorry, something went wrong. Please try again, or message us on WhatsApp.'; err.hidden = false; });
  });
})();
</script>'''
    page(fname, 'Tour Feedback | YSL Travel & Tours', 'Tell us about your trip with YSL Travel & Tours.', body, '',
         extra_head='\n<meta name="robots" content="noindex">' + extra_head, extra_js=js)
