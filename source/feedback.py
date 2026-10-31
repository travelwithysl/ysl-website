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
        <div class="field"><label for="fb-leader">Tour leader {z2}</label><input id="fb-leader" name="tour_leader" autocomplete="off" required></div>
        <div class="field"><label for="fb-dep">Departure date {z3}</label><input id="fb-dep" name="departure" type="date" required></div>
        <div class="field"><label for="fb-ret">Return date {z4}</label><input id="fb-ret" name="return" type="date" required></div>
      </div>'''.format(z1=zh('团号'), z2=zh('领队'), z3=zh('出发日期'), z4=zh('返回日期'))
    you = '''<div class="fields">
        <div class="field full"><label for="fb-name">Name {z1}</label><input id="fb-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="fb-tel">Contact number {z2}</label><input id="fb-tel" name="phone" type="tel" required autocomplete="tel" inputmode="tel"></div>
        <div class="field"><label for="fb-email">Email {z3} <span class="opt">(optional)</span></label><input id="fb-email" name="email" type="email" autocomplete="email"></div>
      </div><p class="fb-note">We use these details only to follow up on your feedback. {z4}</p>'''.format(
        z1=zh('姓名'), z2=zh('联络电话'), z3=zh('电邮（可选填）'), z4=zh('您的资料仅用于跟进您的意见。'))

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
      <div class="field full"><label for="fb-comments">Comments {zh('意见反馈')}</label><textarea id="fb-comments" name="comments" required placeholder="What did you enjoy most? What could we do better?"></textarea></div>'''
    secs.append(section(n, 'Overall', '整体满意度', overall)); n += 1
    times = ''.join(f'<label class="chip"><input type="radio" name="times" value="{v}"><span>{l}</span></label>' for v, l in
                    [('1', 'First trip'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5+', '5 or more')])
    secs.append(section(n, 'Travelling with YSL', '参团次数', f'<div class="chip-set">{times}</div>',
                        'How many times have you travelled with YSL Travel &amp; Tours?', '这是您第几次参加咏胜旅游组织的旅行团？')); n += 1
    secs.append(section(n, 'Why this tour', '选择原因', chips('reasons', REASONS),
                        'What made you choose this tour? Choose any that apply.', '请勾选您选择本次行程的原因（可多选）。')); n += 1
    secs.append(section(n, 'How you found us', '认识渠道', chips('source', SOURCES),
                        'How did you hear about YSL Travel &amp; Tours?', '您是通过哪种渠道认识我们的？')); n += 1
    secs.append(section(n, 'About you', '联络资料', you)); n += 1
    consent = f'''<div class="consent-box">
        <label class="tick"><input type="checkbox" name="testimonial_consent" value="yes"><span><b>Yes, YSL may quote my comments</b> on its website, social media and other marketing materials. {zh('我同意咏胜旅游在网站、社交媒体及其他宣传资料中引用我的意见。')}</span></label>
        <div class="credit" id="fb-credit" hidden>
          <p class="credit-q">How should we credit you? {zh('请选择署名方式：')}</p>
          <div class="chip-set">
            <label class="chip"><input type="radio" name="testimonial_credit" value="first name and initial" checked><span>First name and initial{zh('名字及姓氏首字母')}</span></label>
            <label class="chip"><input type="radio" name="testimonial_credit" value="full name"><span>Full name{zh('全名')}</span></label>
            <label class="chip"><input type="radio" name="testimonial_credit" value="anonymous"><span>Anonymously{zh('匿名')}</span></label>
          </div>
          <p class="fb-note">We may shorten your comments, but never change their meaning. You can withdraw this permission at any time. {zh('我们或会精简您的意见，但不会改变原意。您可随时撤回此同意。')}</p>
        </div>
        <p class="fb-note">Optional. Your feedback is just as welcome if you leave this unticked. {zh('此项可选，不勾选亦不影响提交。')}</p>
      </div>
      <div class="consent-box">
        <label class="tick"><input type="checkbox" name="privacy_consent" value="yes" required><span><b>I have read and agree to the Privacy Notice below.</b> {zh('我已阅读并同意以下隐私声明。')}</span></label>
        <details class="pdpa">
          <summary>Privacy Notice {zh('隐私声明')}</summary>
          <div class="pdpa-body">
            <p>YSL Travel &amp; Tours Sdn Bhd (877803-T) collects the details on this form, including your name, contact number, email and feedback, to follow up on your comments and to improve our tours and services. Only if you tick the box above will we use your comments in our marketing.</p>
            <p>Your information is used only by YSL Travel &amp; Tours. We do not sell it or share it with third parties, except service providers who store it for us under confidentiality. We keep it only as long as these purposes require.</p>
            <p>To access or correct your information, or to withdraw your consent, contact us at travelwithysl@gmail.com or 03-3290 3500. This notice is given under Malaysia’s Personal Data Protection Act 2010.</p>
            <p lang="zh-Hans" class="pdpa-zh">咏胜旅游有限公司（877803-T）收集本表格中的资料，包括您的姓名、联络电话、电邮及意见，用于跟进您的意见及改善我们的行程与服务。仅在您勾选上方选项时，我们才会将您的意见用于宣传。您的资料仅供咏胜旅游使用，我们不会出售或与第三方分享，但为我们储存资料并须保密的服务供应商除外。资料只保留至上述用途所需的期限。如需查阅或更正资料，或撤回同意，请联络 travelwithysl@gmail.com 或 03-3290 3500。本声明依据马来西亚《2010年个人资料保护法令》发出。</p>
          </div>
        </details>
      </div>'''
    secs.append(section(n, 'Your consent', '同意事项', consent))

    body = f'''{nav('')}
<main id="main">
{head_block([('index.html', 'Home'), (None, 'Tour feedback')], 'Tour feedback ' + zh('旅游体验评估'), 'How was <span class="nw"><em>your trip?</em></span>',
            'Thank you for travelling with us. This takes about three minutes, and every answer is read by our team. Please answer every question. ' + zh('感谢您参加咏胜旅游的行程。填写约需三分钟，每份意见都会由我们的团队细阅。请填写所有项目。'))}
<section class="section fb-wrap">
  <div class="container">
    <form class="fb-form" id="feedback" novalidate>
      {''.join(secs)}
      <div class="fb-submit rv">
        <p class="fb-err" id="fb-err" role="alert" hidden></p>
        <button class="btn btn--red" type="submit">Send feedback {zh('提交')}</button>
        <small>Your details are handled under our Privacy Notice above. {zh('您的资料将依据上方隐私声明处理。')}</small>
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
      var v = q.get(p[0]), el = form.elements[p[1]];
      if (!v) return;
      el.value = v;
      if (el.value) { el.readOnly = true; el.tabIndex = -1; el.closest('.field').classList.add('locked'); }
    });
    // tell people why they cannot change it
    if (form.querySelector('.field.locked')) {
      var n = document.createElement('p'); n.className = 'fb-note locked-note';
      n.innerHTML = 'Filled in by YSL for your tour. <span class="zh" lang="zh-Hans">\u6b64\u90e8\u5206\u5df2\u7531\u548f\u80dc\u65c5\u6e38\u4e3a\u60a8\u7684\u884c\u7a0b\u586b\u5199\u3002</span>';
      form.querySelector('.field.locked').closest('.fields').after(n);
    }
  } catch (e) {}
  // overall score readout
  var s = document.getElementById('fb-score'), out = document.getElementById('fb-score-out'), touched = false;
  function show() { out.innerHTML = (touched ? s.value : '\u2013') + '<small>/100</small>'; s.style.setProperty('--p', s.value + '%'); }
  s.addEventListener('input', function () { touched = true; show(); }); show();
  // "Other" reveals a text box
  form.addEventListener('input', function (e) { var m = e.target.closest('.fb-missing'); if (m) m.classList.remove('fb-missing'); });
  form.addEventListener('change', function (e) {
    var m = e.target.closest('.fb-missing'); if (m) m.classList.remove('fb-missing');
    if (e.target.name === 'testimonial_consent') document.getElementById('fb-credit').hidden = !e.target.checked;
    var t = e.target; if (!t.dataset || !t.dataset.other) return;
    var w = document.getElementById(t.dataset.other + '_wrap'); w.hidden = !t.checked; if (t.checked) w.querySelector('input').focus();
  });
  function collect() {
    var d = { submitted_at: new Date().toISOString(), page: location.href };
    new FormData(form).forEach(function (v, k) { if (d[k] !== undefined) d[k] = [].concat(d[k], v); else d[k] = v; });
    if (!touched) delete d.overall;
    if (!d.testimonial_consent) { d.testimonial_consent = 'no'; delete d.testimonial_credit; }
    if (!d.privacy_consent) d.privacy_consent = 'no';
    return d;
  }
  form.addEventListener('submit', function (e) {
    e.preventDefault(); err.hidden = true;
    var miss = [];
    form.querySelectorAll('.fb-missing').forEach(function (el) { el.classList.remove('fb-missing'); });
    function flag(el) { if (el && miss.indexOf(el) < 0) { el.classList.add('fb-missing'); miss.push(el); } }
    var E = form.elements;
    ['tour_code', 'tour_leader', 'departure', 'return'].forEach(function (k) { if (!E[k].value.trim()) flag(E[k].closest('.field')); });
    form.querySelectorAll('fieldset.rate-row').forEach(function (fs) { if (!fs.querySelector('input:checked')) flag(fs); });
    if (!touched) flag(s.closest('.score'));
    if (!E.comments.value.trim()) flag(E.comments.closest('.field'));
    if (!form.querySelector('input[name=times]:checked')) flag(form.querySelector('input[name=times]').closest('.chip-set'));
    ['reasons', 'source'].forEach(function (k) {
      var box = form.querySelector('input[name=' + k + ']').closest('.chip-set');
      if (!form.querySelector('input[name=' + k + ']:checked')) flag(box);
      else if (form.querySelector('input[name=' + k + '][value=other]:checked') && !E[k + '_other'].value.trim()) flag(E[k + '_other'].closest('.field'));
    });
    if (!E.name.value.trim()) flag(E.name.closest('.field'));
    if (!/^[+\d][\d\s-]{6,}$/.test(E.phone.value.trim())) flag(E.phone.closest('.field'));
    var em = E.email.value.trim(); if (em && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)) flag(E.email.closest('.field'));
    if (!E.privacy_consent.checked) flag(E.privacy_consent.closest('.consent-box'));
    if (miss.length) {
      err.textContent = 'Please complete the highlighted questions (' + miss.length + '). \u8bf7\u586b\u5199\u6807\u793a\u7684\u9879\u76ee\u3002';
      err.hidden = false; miss[0].scrollIntoView({ block: 'center', behavior: 'smooth' }); return;
    }
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
