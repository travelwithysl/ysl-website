# Simplified Chinese site (dist/zh/). build.py renders every page with the same templates; for Chinese it
#  1. swaps the content (data.py, articles.py) for the Chinese overlays: SERVICES_ZH etc. below,
#     tours_zh.py (itineraries) and articles_zh.py (journal). Images, codes and links stay in data.py.
#  2. translates the template wording through UI below: exact English fragments of the rendered HTML -> Chinese.
#  3. checks the result: every UI entry must still match something (so an English edit in build.py that
#     breaks a match is caught), and no run of English words may be left on a Chinese page.
# When you change English wording in build.py, change the matching key here too; the build tells you which.
import html as _html, json, os, re, datetime
from tours_zh import QG_ZH, GD_ZH
from data import month_runs
from articles_zh import ARTICLES_ZH, CAT_LABEL_ZH

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@400;500&display=swap">'

# ---------------------------------------------------------------- content overlays
SERVICES_ZH = {
    'air': dict(title='机票预订', short='个人、团体、学生及劳工机票。',
        body='为各类旅客订机票：度假、商务出差、出国留学的学生，以及按合约出国工作的劳工。我们比较航空公司与航线，为团体预留座位，行程有变时也协助您处理。',
        includes=['个人及团体票价', '学生及劳工票价', '全服务航空与廉价航空', '特别协助，例如轮椅申请', '更改日期与重新订票']),
    'tours': dict(title='旅游配套', short='国内游、入境游及国际旅游团。',
        body='亚洲、欧洲及更远地区的团体游、国内短途假期，以及为访马旅客安排的入境游。我们按您的节奏、兴趣和预算配对行程，从第一份报价到回程航班，全程照顾。',
        includes=['资深领队带领的团体游', '自由行配套', '国内游及入境游', '私人及家庭定制行程', '知名旅游品牌的配套']),
    'hotels': dict(title='全球酒店', short='城市酒店与度假村，出发前确认。',
        body='城市酒店、度假村及适合家庭的住宿，出发前完成预订和确认；可单独预订，也可配搭旅游配套。',
        includes=['全球酒店与度假村', '团体及活动客房预留', '机票加酒店配套']),
    'cruises': dict(title='邮轮配套', short='从亚洲短程航线到地中海。',
        body='从区域内的短程航线，到长途的飞机加邮轮假期；机票、登船前的酒店和接送，都围绕您的航期安排妥当。',
        includes=['区域内短程航线', '前往欧洲及其他地区的飞机加邮轮假期', '为家庭及团体提供舱房建议']),
    'insurance': dict(title='旅游保险', short='随预订一并安排旅游保障。',
        body='旅游保险与您的预订一并安排，从付款当天起即受保障。',
        includes=['海外医疗保障', '行程延误与取消', '行李遗失或延误', '个人、家庭及团体计划']),
    'visa': dict(title='签证申请', short='证件检查与申请协助。',
        body='我们先查明目的地的入境要求，协助您准备证件，并一步步指导您完成申请，到了柜台不会有意外。',
        includes=['预订前确认签证要求', '准备申请文件', '申请及预约协助']),
    'incentive': dict(title='奖励旅游团', short='公司旅游、会议及奖励旅游。',
        body='奖励旅游、公司出游、会议及研讨会，从需求简报和预算到全员登机，全程由同一位专人负责。',
        includes=['奖励及表彰旅游', '公司出游及团队旅行', '会议、研讨会及活动', '全程专人负责']),
    'coach': dict(title='巴士租赁', short='团体专用豪华冷气巴士。',
        body='为旅游团、公司旅行、学校出游及各类活动提供豪华冷气巴士，司机经验丰富，熟悉路线。',
        includes=['各种人数的团体巴士', '机场及活动接送', '一日游及外州行程']),
    'transfer': dict(title='私人接送', short='私家车机场、酒店及市区接送。',
        body='配备司机的私家车或客货车，提供机场接送、酒店接驳及市内出行，马来西亚境内及海外皆可。可单独预订，也可加入任何行程，按您的航班时间安排。',
        includes=['机场接机及送机', '酒店及市区接送', '适合家庭及小团体的轿车与客货车', '马来西亚境内及海外']),
}

TOURS_ZH = {  # card text; GD titles and regions come from tours_zh.py so card and page always agree
    'qinghai-gansu': dict(region='中国', line='七彩丹霞、大漠沙丘与天空之镜盐湖'),
    'yunnan': dict(line='大理、泸沽湖、丽江、香格里拉与梅里雪山日照金山'),
    'gd-europe-legend': dict(line='巴黎、布鲁塞尔、阿姆斯特丹、莱茵河、蒂蒂湖、莱茵瀑布、苏黎世与琉森'),
    'gd-hokkaido': dict(short='北海道', line='登别、洞爷湖、小樽与札幌'),
    'gd-turkiye': dict(short='土耳其', line='伊斯坦布尔、恰纳卡莱、以弗所、棉花堡、科尼亚与卡帕多奇亚'),
    'gd-eastern-europe': dict(short='东欧', line='布达佩斯、布拉迪斯拉发、维也纳、哈尔施塔特、萨尔茨堡、克鲁姆洛夫与布拉格'),
    'gd-new-zealand': dict(short='纽西兰', line='南北两岛，从奥克兰到皇后镇'),
    'gd-south-africa': dict(short='南非', line='约翰内斯堡、开普敦、博茨瓦纳与维多利亚瀑布'),
    'gd-japan': dict(short='日本', line='浅草、富士山、高山、白川乡、京都与大阪'),
    'gd-korea': dict(short='韩国', line='南怡岛、雪岳山、Everland，穿韩服游景福宫'),
    'gd-taiwan': dict(short='台湾', line='野柳、九份、十分，礁溪温泉一晚，再游台北'),
    'gd-vietnam': dict(short='岘港', line='会安古镇、巴拿山黄金桥与顺化皇城'),
    'gd-switzerland-italy': dict(short='瑞士', line='少女峰、Glacier 3000、Golden Pass 观光列车、日内瓦湖与米兰'),
    'gd-egypt': dict(short='埃及', line='金字塔、阿布辛贝、尼罗河游船三晚、卢克索与亚历山大'),
    'ap-zhangjiajie': dict(short='张家界', line='砂岩峰林、峡谷玻璃桥、天门山与凤凰古城'),
    'ap-dongbei': dict(short='哈尔滨', line='雾凇、雪中温泉与哈尔滨冰雪大世界'),
    'ap-spain-portugal': dict(short='西班牙', line='波尔图、里斯本、塞维利亚、龙达、科尔多瓦、托莱多、马德里与巴塞罗那'),
    'ap-morocco': dict(short='摩洛哥', line='卡萨布兰卡、蓝色小镇舍夫沙万、菲斯、撒哈拉一夜与马拉喀什'),
    'ap-finland': dict(short='拉普兰', line='哈士奇、驯鹿、挪威帝王蟹与北极光'),
    'ap-australia': dict(short='澳洲', line='悉尼港、蓝山、大洋路与企鹅归巢'),
}

MEMBERS_ZH = {'MATTA': '马来西亚旅游代理商协会', 'MITA': '马来西亚入境旅游协会',
              'MICA': '马来西亚中国入境旅游协会', 'MCTA': '马来西亚华人旅游协会'}

HOURS_ZH = '星期一至五，上午9时至下午6时<br>星期六，上午9时至下午3时<br>星期日休息'

MEALS = {'B': '早', 'L': '午', 'D': '晚'}


def _dur(s):
    """'10 days, 8 nights' / '10D8N' -> '10天8晚'"""
    m = re.match(r'(\d+)\D+?(\d+)', s)
    return f'{m.group(1)}天{m.group(2)}晚'


def _day(en, z):
    d = dict(en)
    for k in ('t', 'p', 'hotel', 'note', 'meal'):
        if k in z:
            d[k] = z[k]
    d['meals'] = ' · '.join(MEALS[x] for x in en['meals'].split(', ')) if en['meals'] else ''
    for k, c in (('img', 'cap'), ('img2', 'cap2')):
        if en.get(k) and c in z:
            d[k] = (en[k][0], z[c]) + tuple(en[k][2:])
    return d


def _tour(en, z):
    q = dict(en)
    for k in ('title', 'region', 'line', 'hotels', 'head', 'lead', 'highlights', 'included', 'excluded', 'notes', 'flights', 'hero_alt', 'seo'):
        if k in z:
            q[k] = z[k]
    q['duration'] = z.get('duration') or _dur(en['duration'])
    if en.get('hero') and 'hero_alt' not in z:
        raise KeyError('missing Chinese hero_alt for ' + en['slug'])
    if en.get('dates'):
        q['departs'] = departs_zh(en['dates'])
    if en.get('notes') and 'notes' not in z:
        raise KeyError('missing Chinese notes for ' + en['slug'])
    assert len(z['days']) == len(en['days']), en['slug']
    q['days'] = [_day(a, b) for a, b in zip(en['days'], z['days'])]
    if 'features' in en:
        q['features'] = [(im, t, x) for (im, _, _), (t, x) in zip(en['features'], z['features'])]
    q['zh'] = ''
    return q


def departs_zh(dates):
    """Chinese twin of data.departs_en: '2027年2月', '2027年1月至9月', '2026年12月至2027年3月'"""
    out = []
    for (y1, m1), (y2, m2) in month_runs(dates):
        if (y1, m1) == (y2, m2):
            out.append(f'{y1}年{m1}月')
        elif y1 == y2:
            out.append(f'{y1}年{m1}月至{m2}月')
        else:
            out.append(f'{y1}年{m1}月至{y2}年{m2}月')
    return '、'.join(out)


def zh_date(s):
    d = datetime.datetime.strptime(s, '%d %B %Y')
    return f'{d.year}年{d.month}月{d.day}日'


def localise(SERVICES, TOURS, CONTACT, MEMBERS, OPENINGS, QG, GD_TOURS, ARTICLES):
    services = [{**s, **SERVICES_ZH[s['slug']]} for s in SERVICES]
    qg = _tour(QG, QG_ZH)
    gd = [_tour(q, GD_ZH[q['slug']]) for q in GD_TOURS]
    by = {q['slug']: q for q in gd + [qg]}
    tours = []
    for t in TOURS:
        z = dict(TOURS_ZH[t['slug']])
        if t['slug'] in by:
            for k in ('title', 'region'):
                if k not in z:
                    z[k] = by[t['slug']][k]
        z.setdefault('short', t.get('short') or z.get('title'))  # photo-placeholder label: a place, so Chinese; Europe Legend keeps its tour name
        if t.get('dates'):
            z['departs'] = departs_zh(t['dates'])
        tours.append({**t, **z, 'dur': _dur(t['dur']), 'kind': '团体游'})
    contact = {**CONTACT, 'hours': HOURS_ZH}
    members = [(a, MEMBERS_ZH[a]) for a, _ in MEMBERS]
    openings = [{**o, 'tour': '金山秘湖', 'kind': '团体游', 'place': '云南昆明'} for o in OPENINGS]
    articles = []
    for a in ARTICLES:
        z = ARTICLES_ZH[a['slug']]
        b = {**a, **{k: z[k] for k in ('title', 'lead', 'excerpt', 'read', 'alt', 'body', 'seo') if k in z}}
        b['cta'] = (z['cta'][0], z['cta'][1], a['cta'][2], z['cta'][2])
        if a.get('slot'):
            b['slot'] = (a['slot'][0], a['slot'][1], z['slot_label'])
        b['cat_label'] = CAT_LABEL_ZH[a['cat']]
        b['date_en'], b['date'] = a['date'], zh_date(a['date'])
        articles.append(b)
    return services, tours, contact, members, openings, qg, gd, articles


# ---------------------------------------------------------------- scripts
CONTACT_JS = dict(hello='您好，YSL Travel & Tours：', ask='我想咨询', lower=False, to='，目的地：', stop='。', when='出行时间：',
                  pax='人数：', co='公司：', thanks='谢谢！', sign=' ', end='', proto='原型阶段：WhatsApp 号码待 YSL 确认后加入。')

PLACES = {'JFK': '美国纽约', 'CDG': '法国巴黎', 'ZRH': '瑞士采尔马特', 'FCO': '意大利罗马', 'NAV': '土耳其卡帕多奇亚',
          'CAI': '埃及吉萨', 'DXB': '阿联酋迪拜', 'PEK': '中国长城', 'ICN': '韩国首尔', 'HND': '日本富士山',
          'DPS': '印尼巴厘岛', 'SYD': '澳洲悉尼', 'KUL': '马来西亚吉隆坡'}


def globe_js():
    """Runs between landmarks.js and globe.js on the Chinese home page (ASCII only: \\u escapes)."""
    return ('var PLACES_ZH = ' + json.dumps(PLACES) + ';\nLANDMARKS.forEach(function (l) { if (PLACES_ZH[l.code]) l.place = PLACES_ZH[l.code]; });\n'
            'window.GLOBE_TEXT = ' + json.dumps(dict(see='查看行程', china='中国旅游团', plan='规划行程')) + ';\n')


# ---------------------------------------------------------------- template wording
UI = {
  # page titles and descriptions
  'Corporate Travel & MICE | ': '商务旅游与 MICE | ',
  'About YSL Travel & Tours': '关于 YSL Travel & Tours',
  'Services | ': '旅游服务 | ',
  'Majestic Qinghai & Gansu | ': '大美青甘 | ',
  'Journal | ': '旅游札记 | ',
  'Contact | ': '联络我们 | ',
  'YSL Travel & Tours: corporate travel, holidays and tours from Klang, Malaysia, since 2009.': 'YSL Travel & Tours：自2009年起，从马来西亚巴生出发，提供商务旅游、假期与旅游团服务。',
  'Meetings, incentives, conferences and exhibitions at any scale: group air, hotels, coaches, gala nights and on-site teams from YSL Travel & Tours.': '会议、奖励旅游、研讨会与展览，规模不限：团体机票、酒店、巴士、晚宴及现场团队，由 YSL Travel & Tours 一手包办。',
  'Founded in Klang in 2009, YSL Travel & Tours plans holidays, group tours and business travel for families and companies. Licensed by MOTAC (KPL 6107).': 'YSL Travel & Tours 2009年创立于巴生，为家庭与企业安排假期、团体游及商务旅行。持有马来西亚旅游、艺术及文化部执照（KPL 6107）。',
  'Air tickets, tours, hotels, cruises, insurance, visas, incentive groups, coach hire and private transfers.': '机票、旅游配套、酒店、邮轮、保险、签证、奖励旅游团、巴士租赁及私人接送。',
  'Tour Packages from Malaysia | YSL Travel & Tours': '旅游配套，吉隆坡出发 | YSL Travel & Tours',
  'Group tour packages from Kuala Lumpur to China, Japan, Korea, Taiwan, Vietnam, Europe, Switzerland, Türkiye, Egypt, South Africa and New Zealand. YSL’s own group tours and partner tours, booked in Klang.': '吉隆坡出发的团体旅游配套：中国、日本、韩国、台湾、越南、欧洲、瑞士、土耳其、埃及、南非与纽西兰。YSL 自营团体游及合作伙伴团，在巴生预订。',
  '10-day group tour through Gansu and Qinghai: the Rainbow Mountains, Mogao Caves, Chaka Salt Lake and Qinghai Lake.': '甘肃、青海10天团体游：七彩丹霞、莫高窟、茶卡盐湖与青海湖。',
  'Destination guides, travel tips and corporate travel advice from YSL Travel & Tours.': 'YSL Travel & Tours 的目的地指南、旅行贴士与商务旅游建议。',
  'Visit, call or message YSL Travel & Tours in Klang, Selangor.': '到访、致电或留言给位于雪兰莪巴生的 YSL Travel & Tours。',

  # header and footer
  'Skip to content': '跳至内容',
  'aria-label="YSL Travel and Tours, home"': 'aria-label="YSL Travel &amp; Tours，首页"',
  'aria-label="Menu"': 'aria-label="菜单"',
  '>Corporate Travel</a>': '>商务旅游</a>',
  'Holidays &amp; Tours': '假期与旅游团',
  '>Travel Services</a>': '>旅游服务</a>',
  '>About</a>': '>关于我们</a>',
  '>Journal</a>': '>旅游札记</a>',
  '>Plan a trip</a>': '>规划行程</a>',
  '>Contact</a>': '>联络我们</a>',
  'Travel services for individuals and companies, from Klang to the world since 2009.': '自2009年起，从巴生出发，为个人与企业提供通往世界各地的旅游服务。',
  '<h4>Explore</h4>': '<h4>浏览</h4>',
  '<h4>Visit us</h4>': '<h4>欢迎到访</h4>',
  '<h4>Get in touch</h4>': '<h4>联络方式</h4>',
  '>Google Maps</a>': '>谷歌地图</a>',
  'Licence KPL 6107 &nbsp; Member of MATTA, MITA, MICA and MCTA': '旅行社执照 KPL 6107 &nbsp; MATTA、MITA、MICA 及 MCTA 会员',

  # shared blocks
  '<p class="eyebrow">Talk to us</p>': '<p class="eyebrow">联络我们</p>',
  'Let’s plan your next trip.': '一起规划您的下一段旅程。',
  'Not sure what you need? Ask us.': '不确定需要什么？问问我们。',
  'Chat on WhatsApp': 'WhatsApp 咨询',
  '>Browse tours</a>': '>浏览旅游团</a>',
  '<dt>Call</dt>': '<dt>电话</dt>',
  '<dt>Email</dt>': '<dt>电邮</dt>',
  '<dt>Visit</dt>': '<dt>地址</dt>',
  '<dd>Taman Klang Utama, Klang</dd>': '<dd>巴生 Taman Klang Utama</dd>',
  '<small>From</small>KUL': '<small>出发</small>KUL',
  '<small>To</small>': '<small>抵达</small>',
  '<span>Departs</span>': '<span>出发</span>',
  '<span>View <svg': '<span>查看 <svg',
  '<li><a href="index.html">Home</a></li>': '<li><a href="index.html">首页</a></li>',
  'All tours <svg': '全部旅游团 <svg',

  # home
  'aria-label="Welcome"': 'aria-label="欢迎"',
  'From Klang. To the world.': '自巴生，行天下。',
  '<h1>Every journey<br> begins with a<br> <em>point<br> on the map.</em></h1>': '<h1>千里之行，<br><em>始于图上一点。</em></h1>',
  '<p class="sub">From that first point to the flight home, <br>we plan every step.</p>': '<p class="sub">从启程到归途，<br>每一步，都为您安排。</p>',
  '>Explore tours</a>': '>探索旅游团</a>',
  '>Replay</button>': '>重播</button>',
  'Where we’re <em>going next.</em>': '我们的<em>下一站。</em>',
  'aria-label="Previous tours"': 'aria-label="上一组旅游团"',
  'aria-label="Next tours"': 'aria-label="下一组旅游团"',
  'Tour brands we carry': '合作旅游品牌',
  '>and more</span>': '>等更多品牌</span>',
  'aria-label="Travel services"': 'aria-label="旅游服务"',
  '<span class="lbl">Travel services</span>': '<span class="lbl">旅游服务</span>',
  '</svg>Air tickets</a>': '</svg>机票</a>',
  '</svg>Visas</a>': '</svg>签证</a>',
  '</svg>Travel insurance</a>': '</svg>旅游保险</a>',
  '</svg>Cruises</a>': '</svg>邮轮</a>',
  '</svg>Hotels</a>': '</svg>酒店</a>',
  '>All services</a>': '>全部服务</a>',
  'Why travel with YSL': '为何选择 YSL',
  '<p class="eyebrow">Why YSL</p>': '<p class="eyebrow">为何选择 YSL</p>',
  'Licensed, accredited and trusted since 2009.': '持牌经营，业界认可，自2009年起深受信赖。',
  'A registered, licensed travel agency and an active member of Malaysia’s travel associations.': '注册持牌旅行社，也是马来西亚多个旅游业协会的活跃会员。',
  '<dt>Year founded</dt>': '<dt>创立年份</dt>',
  '<dt>Founder’s experience</dt>': '<dt>创办人资历</dt>',
  "<dt>Founder's experience</dt>": '<dt>创办人资历</dt>',
  '<dt>Corporate clients</dt>': '<dt>企业客户</dt>',
  '<dt>Industry associations</dt>': '<dt>所属行业协会</dt>',
  '>25+ yrs</dd>': '>25年+</dd>',
  '<h3 class="code">Licensed &amp; registered</h3>': '<h3 class="code">持牌与注册</h3>',
  'Travel agency licence, Ministry of Tourism, Arts and Culture Malaysia (MOTAC)': '马来西亚旅游、艺术及文化部（MOTAC）颁发的旅行社执照',
  'YSL Travel &amp; Tours Sdn Bhd, registered with SSM': 'YSL Travel &amp; Tours Sdn Bhd，于马来西亚公司委员会（SSM）注册',
  '<h3 class="code">Member of</h3>': '<h3 class="code">所属协会</h3>',
  'Your next point on the map.': '您在地图上的下一个点。',
  '>Where to next?</h2>': '>下一站去哪里？</h2>',
  'Tell us where, when and who is coming. A consultant replies within one working day.': '告诉我们想去哪里、什么时候出发、有谁同行。旅游顾问会在一个工作日内回复您。',

  # corporate
  'alt="A corporate group arriving at a seaside venue, welcomed by a host"': 'alt="企业团体抵达海边会场，接待人员上前迎接"',
  '<li aria-current="page">Corporate Travel</li>': '<li aria-current="page">商务旅游</li>',
  'Corporate Travel &amp; MICE': '商务旅游与 MICE',
  'Business travel and MICE, <em>at any scale.</em>': '<span class="nw">商旅与 MICE，</span><br><span class="nw"><em>不拘规模。</em></span>',
  'From a board retreat of twelve to an incentive of hundreds, one team plans, moves and looks after your people.': '<span class="nw">小至十二人的董事会议，</span><span class="nw">大至数百人的奖励旅游，</span><span class="nw">同一团队，</span><span class="nw">从策划到归程，</span><span class="nw">全程照顾。</span>',
  '>Request a MICE proposal</a>': '>索取 MICE 方案</a>',
  '>How we plan it</a>': '>我们如何策划</a>',
  'aria-label="YSL in numbers"': 'aria-label="YSL 数据一览"',
  '<dt>Corporate travel since</dt>': '<dt>商务旅游服务始于</dt>',
  '<dt>Largest single group</dt>': '<dt>最大单一团体</dt>',
  '<dt>MICE projects delivered</dt>': '<dt>已完成 MICE 项目</dt>',
  '<p class="eyebrow">What we handle</p>': '<p class="eyebrow">服务范围</p>',
  'All four letters of MICE.': 'MICE 四大领域，全面包办。',
  'Meetings, incentives, conferences and exhibitions, in Malaysia and overseas, planned and run by one team with one point of contact.': '会议、奖励旅游、研讨会与展览，无论在马来西亚还是海外，都由同一个团队策划执行，专人负责。',
  '<h3>Meetings</h3>': '<h3>会议</h3>',
  'Board retreats, management offsites and regional meetings, with the venue, rooms, AV and travel arranged as one package.': '董事会外地会议、管理层外地会议及区域会议，场地、客房、视听设备与交通一并安排。',
  '<li>Venue sourcing and site inspections</li>': '<li>寻找场地及实地考察</li>',
  '<li>Meeting rooms, AV and breakout spaces</li>': '<li>会议室、视听设备及分组讨论空间</li>',
  '<li>Retreats in Malaysia and overseas</li>': '<li>马来西亚及海外的度假会议</li>',
  '<h3>Incentives</h3>': '<h3>奖励旅游</h3>',
  'Reward trips for top performers, dealers and agents: an itinerary people work all year to qualify for.': '犒赏优秀员工、经销商与代理的奖励之旅：一份值得大家努力一整年去争取的行程。',
  '<li>Bespoke itineraries and exclusive experiences</li>': '<li>量身定制的行程与专属体验</li>',
  '<li>Gala and awards nights</li>': '<li>晚宴及颁奖之夜</li>',
  '<li>Wave departures for very large groups</li>': '<li>超大型团体分批出发</li>',
  '<h3>Conferences</h3>': '<h3>研讨会</h3>',
  'Delegate travel and logistics for conventions and annual conferences, from registration to the closing dinner.': '大会及年度研讨会的代表出行与后勤，从报名登记到闭幕晚宴。',
  '<li>Delegate registration and rooming</li>': '<li>代表报名及分房</li>',
  '<li>Airport transfers in waves</li>': '<li>分批机场接送</li>',
  '<li>Hospitality desks at the venue</li>': '<li>会场接待柜台</li>',
  '<h3>Exhibitions</h3>': '<h3>展览</h3>',
  'Business delegations to trade fairs and expos abroad, and group travel for exhibitors and buyers.': '组织商务代表团参加海外商展与博览会，并为参展商和买家安排团体出行。',
  '<li>Trade fair delegations</li>': '<li>商展代表团</li>',
  '<li>Business visas and invitations</li>': '<li>商务签证及邀请函</li>',
  '<li>Hotels close to the fairground</li>': '<li>邻近展馆的酒店</li>',
  '<p class="eyebrow">Built for big groups</p>': '<p class="eyebrow">专为大型团体而设</p>',
  'Hundreds of people, moving as one.': '数百人同行，步调一致。',
  'A large programme succeeds on logistics nobody notices. These are the parts we take off your hands.': '大型活动的成功，靠的是没人注意到的后勤。以下这些，都交给我们。',
  '<b>Group air</b>': '<b>团体机票</b>',
  'Seat blocks across several flights, charter options, group check-in and staggered departure waves.': '跨多个航班预留座位、包机选择、团体办理登机及分批出发。',
  '<b>Hotel allocations</b>': '<b>酒店客房安排</b>',
  'Room blocks in one hotel or spread across several, rooming lists, VIP upgrades and late changes handled.': '集中一家或分散多家酒店的客房预留、分房名单、贵宾升级，临时更改也一并处理。',
  '<b>Ground transport</b>': '<b>地面交通</b>',
  'Coaches numbered and colour-coded by group, each with its own tour leader and a lead coordinator on the ground.': '巴士按组编号、以颜色区分，每辆车配一位领队，另有一位总协调在现场统筹。',
  '<b>The arrival</b>': '<b>抵达迎接</b>',
  'A branded welcome at the airport: YSL flags and signage, a hospitality desk, and coaches waiting in order.': '机场的专属迎接：YSL 旗帜与指示牌、接待柜台，巴士依序候车。',
  '<b>Registration and documents</b>': '<b>报名与证件</b>',
  'Online registration, passport and visa collection, group visas, insurance, and pre-departure briefings.': '网上报名、收集护照与签证资料、团体签证、保险及行前说明会。',
  '<b>Gala and awards nights</b>': '<b>晚宴与颁奖之夜</b>',
  'Venue buyouts, themed dinners, stage, sound and lighting, and the awards ceremony run to the minute.': '包场、主题晚宴、舞台音响灯光，颁奖典礼分秒不差。',
  '<b>Experiences</b>': '<b>特色体验</b>',
  'Team-building, private tours, CSR activities and exclusive access that make the trip worth qualifying for.': '团队建设、私人导览、企业社会责任活动及专属参观，让这趟旅程值得争取。',
  '<b>Every guest’s needs</b>': '<b>照顾每位来宾</b>',
  'Halal and vegetarian meals, prayer times, mobility needs and multilingual guides, planned for from the start.': '清真餐与素食、祈祷时间、行动不便者的需要及多语导游，从一开始就纳入规划。',
  '<b>On-site command</b>': '<b>现场指挥</b>',
  'A 24-hour hotline, daily briefings with the client, and contingency plans for weather, delays and illness.': '24小时热线、每日与客户简报，并为天气、延误和生病预备应变方案。',
  '<b>After the trip</b>': '<b>旅程结束后</b>',
  'A reconciled final account, a photo and video round-up, and a debrief to make the next one better.': '核对清楚的最终账目、照片与短片回顾，以及检讨会议，让下一次更好。',
  '<p class="eyebrow">How a large programme runs</p>': '<p class="eyebrow">大型活动如何进行</p>',
  'Six months, one plan.': '六个月，一个计划。',
  'For large groups we recommend starting at least six months ahead, so the best flights, rooms and venues are still available.': '大型团体建议至少提前六个月开始筹备，才能订到最好的航班、客房与场地。',
  '>6 months before</span>': '>出发前6个月</span>',
  '<b>Brief and budget</b>': '<b>需求与预算</b>',
  'Purpose, group size, dates, budget per head and the experience you want people to come home with.': '目的、人数、日期、每人预算，以及您希望大家带回家的体验。',
  '>5 months</span>': '>5个月前</span>',
  '<b>Proposal and site inspection</b>': '<b>方案与实地考察</b>',
  'Destination options with itemised quotations; we can visit the hotels and venues with you.': '附逐项报价的目的地方案；我们可陪同您实地考察酒店与场地。',
  '>4 months</span>': '>4个月前</span>',
  '<b>Contract and blocks</b>': '<b>签约与预留</b>',
  'Air seats and hotel rooms secured, deposits scheduled, the programme agreed day by day.': '确保机位与客房，排定订金时间表，逐日确认行程。',
  '>3 to 1 months</span>': '>3至1个月前</span>',
  'Participant registration, rooming, passports, visas, dietary needs and insurance.': '参加者报名、分房、护照、签证、饮食需要及保险。',
  '>2 weeks</span>': '>2个星期前</span>',
  '<b>Pre-departure briefing</b>': '<b>行前说明会</b>',
  'Final programme, coach and room assignments, packing notes and contacts for every traveller.': '最终行程、巴士与分房安排、行李须知，以及给每位旅客的联络资料。',
  '>On the trip</span>': '>旅程期间</span>',
  '<b>Operations</b>': '<b>现场执行</b>',
  'YSL on site from the airport onwards, with tour leaders on every coach and one lead coordinator.': 'YSL 团队从机场起全程在场，每辆巴士都有领队，另有一位总协调。',
  '>After</span>': '>结束后</span>',
  '<b>Report and reconciliation</b>': '<b>报告与结算</b>',
  'Final account, feedback and a debrief with your team.': '最终账目、意见反馈，并与您的团队检讨总结。',
  '<p class="eyebrow">Local MICE</p>': '<p class="eyebrow">国内 MICE</p>',
  'Closer to home.': '近在国内。',
  'Not every company event needs a passport. We plan team days, retreats and celebrations across Malaysia, with transport for everyone arranged.': '不是每个公司活动都需要护照。我们在马来西亚各地策划团队活动日、度假营和庆祝活动，全员交通一并安排。',
  '<b>Team building</b>': '<b>团队建设</b>',
  'Facilitated games and challenges, indoors or outdoors, designed around what your team needs to work on.': '由专人带领的室内或户外游戏与挑战，针对团队需要加强的方面而设计。',
  '<b>Retreats and offsites</b>': '<b>度假营与外地会议</b>',
  'Resort stays with meeting space for planning sessions, strategy days and management retreats.': '入住设有会议空间的度假村，进行规划会议、策略日及管理层度假会议。',
  '<b>Annual dinners and family days</b>': '<b>年度晚宴与家庭日</b>',
  'Venue, catering, stage and programme for the company dinner or a day out with families.': '公司晚宴或家庭日的场地、餐饮、舞台与节目安排。',
  '<b>CSR days</b>': '<b>企业社会责任日</b>',
  'Community and environmental projects your team can do together, with transport and meals arranged.': '团队可以一起参与的社区与环保项目，交通和餐食一并安排。',
  '<b>Day trips and company outings</b>': '<b>一日游与公司出游</b>',
  'Coaches, guides and meals for a day out, from one bus to a convoy.': '一日出游的巴士、导游与餐食，从一辆车到整个车队。',
  'Popular for company groups': '企业团体热门地点',
  '<span class="b">Langkawi</span>': '<span class="b">兰卡威</span>',
  '<span class="b">Penang</span>': '<span class="b">槟城</span>',
  '<span class="b">Genting Highlands</span>': '<span class="b">云顶高原</span>',
  '<span class="b">Cameron Highlands</span>': '<span class="b">金马仑高原</span>',
  '<span class="b">Port Dickson</span>': '<span class="b">波德申</span>',
  '<span class="b">Desaru</span>': '<span class="b">迪沙鲁</span>',
  '<span class="b">Melaka</span>': '<span class="b">马六甲</span>',
  '<span class="b">Sabah</span>': '<span class="b">沙巴</span>',
  'Trusted by more than 50 companies across the region.': '深受区域内50多家企业信赖。',
  '<b>Since 2009</b>': '<b>始于2009年</b>',
  'Led by a founder with more than 25 years in travel.': '由拥有逾25年旅游业经验的创办人领导。',
  '<b>Licensed and accredited</b>': '<b>持牌与认证</b>',
  'KPL 6107, and members of MATTA, MITA, MICA and MCTA.': '执照 KPL 6107，并为 MATTA、MITA、MICA 及 MCTA 会员。',
  '<b>Clear quotations</b>': '<b>报价清楚</b>',
  'Itemised proposals and a reconciled final account your finance team can sign off.': '逐项列明的方案，以及财务部门可直接核准的最终账目。',
  '<p class="eyebrow">Start a proposal</p>': '<p class="eyebrow">开始规划方案</p>',
  'Send us a brief.': '把需求告诉我们。',
  'A rough brief is enough to start. We reply with options and an itemised quotation.': '只需大概的需求就能开始，我们会回复几个方案和逐项报价。',
  'What to include': '需求可包括',
  '<li>Purpose of the trip, and who is going</li>': '<li>旅程目的，以及哪些人参加</li>',
  '<li>Group size, even a range</li>': '<li>人数，大约范围也可以</li>',
  '<li>Preferred dates or months</li>': '<li>希望的日期或月份</li>',
  '<li>Budget per person</li>': '<li>每人预算</li>',
  '<li>Destinations you have in mind</li>': '<li>心目中的目的地</li>',
  '<li>Any dietary, faith or accessibility needs</li>': '<li>饮食、宗教或无障碍方面的需要</li>',

  # about
  '<li aria-current="page">About</li>': '<li aria-current="page">关于我们</li>',
  '<p class="eyebrow">About us</p>': '<p class="eyebrow">关于我们</p>',
  'From Klang <span class="nw"><em>to the world</em>,</span><br> since 2009.': '从巴生<span class="nw"><em>到世界</em>，</span><br>始于2009年。',
  'A licensed Malaysian travel agency planning holidays, group tours and business travel.': '马来西亚持牌旅行社，专门安排假期、团体游与商务旅行。',
  'alt="The YSL Travel &amp; Tours team at a travel fair"': 'alt="YSL Travel &amp; Tours 团队在旅游展上"',
  '<p class="eyebrow">Our story</p>': '<p class="eyebrow">我们的故事</p>',
  'Built on more than 25 years in travel.': '<span class="nw">二十五年的行业历练，</span><span class="nw">都化作您旅途中的从容。</span>',
  'YSL Travel &amp; Tours was founded in Klang, Selangor, in 2009. We arrange holidays, group tours and business travel for individuals, families and companies, and look after each trip from the first quote to the flight home.': '2009年，YSL Travel &amp; Tours 在雪兰莪巴生成立。家庭出游、团体旅行、企业出差，我们从第一份报价开始跟进，直到您平安回家。',
  'The company is led by a founder with more than 25 years in the travel industry. Behind every booking is a team of consultants and operations staff who know the destinations, the suppliers and the details that keep a trip running smoothly.': '创办人在旅游业打拼逾二十五年。身边的顾问与执行团队熟悉各地目的地和合作伙伴，大小细节都替您打点妥当，让每一趟行程走得安稳。',
  'Today we plan travel for families, schools and more than 50 companies and organisations.': '今天，信任我们的不只是一个个家庭，还有学校，以及五十多家企业与机构。',
  '<p class="eyebrow">Our mission</p>': '<p class="eyebrow">我们的使命</p>',
  'Make good travel easy to reach.': '让好的旅行触手可及。',
  'We connect people with the places they want to see, and take care of the planning so they can enjoy the journey.': '我们带人们去想去的地方，并包办所有规划，让大家安心享受旅程。',
  '<p class="eyebrow">Our vision</p>': '<p class="eyebrow">我们的愿景</p>',
  'Be the travel partner people trust most.': '成为最受信赖的旅游伙伴。',
  'To keep growing with our clients, open new destinations, and help more people travel well.': '与客户一同成长，开拓新的目的地，帮助更多人好好旅行。',
  '<p class="eyebrow">Credentials</p>': '<p class="eyebrow">资质</p>',
  'Licensed, registered and accredited.': '持牌、注册、获认证。',
  'Licensed by the Ministry of Tourism, Arts and Culture Malaysia (KPL 6107) and registered with SSM as YSL Travel &amp; Tours Sdn Bhd (877803-T).': '持有马来西亚旅游、艺术及文化部执照（KPL 6107），并以 YSL Travel &amp; Tours Sdn Bhd（877803-T）名义于马来西亚公司委员会（SSM）注册。',

  # services
  '<li aria-current="page">Services</li>': '<li aria-current="page">旅游服务</li>',
  '<p class="eyebrow">What we do</p>': '<p class="eyebrow">服务项目</p>',
  'Everything between here and there.': '从这里到那里，一切都为您安排。',
  'Nine services under one roof, so one team can look after your whole trip, or your whole company’s.': '九项服务一站齐全，由同一个团队照顾您的整趟旅程，或整个公司的出行。',
  'aria-label="Services"': 'aria-label="服务项目"',
  '>Ask about ': '>咨询',

  # tours
  'Where will you go next?': '<span class="nw">下一站，</span><span class="nw">去哪里？</span>',
  'Our own group tours, and signature group tours from Malaysia’s leading tour brands, all booked and looked after by YSL.': 'YSL 自营团体游，以及马来西亚知名旅游品牌的招牌团体游，全部由 YSL 为您预订和照顾。',
  '<b>Looking for something else?</b> We also book packages from Apple Vacations, Lovely Vacation, UbinGO Vacations, FS Holidays, Parlo Tours and Golden Destinations. Tell us where you want to go and we’ll compare options for you.': '<b>想找其他行程？</b>我们也代订 Apple Vacations、Lovely Vacation、UbinGO Vacations、FS Holidays、Parlo Tours 及 Golden Destinations 的配套。告诉我们您想去哪里，我们为您比较各种选择。',

  # tour pages
  '<p class="eyebrow">China &nbsp; Group tour &nbsp;': '<p class="eyebrow">中国 &nbsp; 团体游 &nbsp;',
  '&nbsp; Group tour &nbsp;': '&nbsp; 团体游 &nbsp;',
  '<p class="eyebrow">Overview</p>': '<p class="eyebrow">行程概览</p>',
  '>Highlights</h3>': '>行程亮点</h3>',
  '>Day by day</h3>': '>每日行程</h3>',
  '<h3>Included</h3>': '<h3>费用包括</h3>',
  '<h3>Not included</h3>': '<h3>费用不包括</h3>',
  'aria-label="Tour details"': 'aria-label="行程资料"',
  '<dt>Duration</dt>': '<dt>天数</dt>',
  '<dt>Tour type</dt>': '<dt>类型</dt>',
  '<dd>Group tour</dd>': '<dd>团体游</dd>',
  '<dt>Departures</dt>': '<dt>出发日期</dt>',
  '<dt>Fares</dt>': '<dt>团费</dt>',
  '<dd>Latest fares on request</dd>': '<dd>最新团费，欢迎询问</dd>',
  '<dt>Route</dt>': '<dt>路线</dt>',
  '<dd>Lanzhou to Lanzhou</dd>': '<dd>兰州进出</dd>',
  '<dt>Airline</dt>': '<dt>航空公司</dt>',
  '<dt>Hotels</dt>': '<dt>酒店</dt>',
  '<dd>4-Diamond</dd>': '<dd>Ctrip 四钻</dd>',
  '>Departure dates</h3>': '>出发日期</h3>',
  'Group departures from Kuala Lumpur. Ask us which dates still have seats.': '吉隆坡出发。欢迎询问哪些日期仍有空位。',
  '<dt>Tour by</dt>': '<dt>承办</dt>',
  '>Enquire on WhatsApp</a>': '>WhatsApp 咨询</a>',
  '>Ask for fares and dates</a>': '>询问团费与日期</a>',
  'Need a visa or travel insurance for this trip? <a href="services.html#visa">We arrange both.</a>': '这趟旅程需要签证或旅游保险吗？<a href="services.html#visa">我们都能代办。</a>',
  '<p class="eyebrow">You might also like</p>': '<p class="eyebrow">您可能也喜欢</p>',
  'id="more-h">More journeys</h2>': 'id="more-h">更多旅程</h2>',
  'alt="The banded ridges of the Zhangye Rainbow Mountains"': 'alt="张掖七彩丹霞层层叠叠的山脊"',
  '<li aria-current="page">Qinghai &amp; Gansu</li>': '<li aria-current="page">青海与甘肃</li>',
  'Along the Silk Road to the roof of the plateau.': '沿着丝绸之路，直上高原之巅。',
  'Ten days from Lanzhou through the Hexi Corridor to Dunhuang, across the Qaidam Basin to the salt lakes, and on to Qinghai Lake and Xining. Painted mountains, desert caves of Buddhist art, a lake that mirrors the sky, and the food of the Northwest along the way.': '十天行程，从兰州穿越河西走廊到敦煌，横越柴达木盆地抵达盐湖，再前往青海湖与西宁。一路有七彩山峦、大漠中的佛教石窟艺术、倒映天空的湖面，还有大西北的风味美食。',
  '>Flights</h3>': '>航班</h3>',
  'China Eastern, tentative and subject to airline confirmation. One checked bag up to 23kg, through-checked to Lanzhou.': 'China Eastern 航班暂定，以航空公司确认为准。托运行李一件，限重23公斤，直挂兰州。',
  '<p class="eyebrow">The package</p>': '<p class="eyebrow">配套内容</p>',
  'Comfort for the long roads of the Northwest.': '大西北的漫漫长路，一路舒适。',
  'title="Meals included"': 'title="含餐"',
  '<span>Featured meal</span>': '<span>特色餐</span>',
  '<span>Stay</span>': '<span>住宿</span>',
  'What’s included.': '费用包括哪些。',
  'Operated by Golden Destinations. ': '由 Golden Destinations 承办。',
  'Operated by Apple Vacations. ': '由 Apple Vacations 承办。',
  'Images are for illustration purposes only. ': '图片仅供参考。',
  'Booked through YSL. We handle your booking, documents and questions from start to finish.': '通过 YSL 预订。从预订、证件到各种疑问，我们全程为您处理。',
  'Itinerary order and hotels may change with local events, weather or availability. Fares, dates and the full itinerary are confirmed when you book.': '行程顺序和酒店可能因当地活动、天气或供应情况而调整。团费、日期及完整行程以预订时确认为准。',

  # journal
  '<li aria-current="page">Journal</li>': '<li aria-current="page">旅游札记</li>',
  '<p class="eyebrow">Journal</p>': '<p class="eyebrow">旅游札记</p>',
  'Stories from <span class="nw"><em>the road.</em></span>': '来自<span class="nw"><em>旅途</em></span>的故事。',
  'Destination guides, travel tips and corporate travel advice from the YSL Travel &amp; Tours team.': 'YSL Travel &amp; Tours 团队分享的目的地指南、旅行贴士与商务旅游建议。',
  'aria-label="Filter stories"': 'aria-label="筛选文章"',
  '>All stories</button>': '>全部文章</button>',
  '>Destinations</button>': '>目的地</button>',
  '>Travel tips</button>': '>旅行贴士</button>',
  '>Corporate travel</button>': '>商务旅游</button>',
  'Read the story <svg': '阅读全文 <svg',
  'No stories in this topic yet.': '此类别暂时没有文章。',
  '<li><a href="journal.html">Journal</a></li>': '<li><a href="journal.html">旅游札记</a></li>',
  '<span>By the YSL team</span>': '<span>YSL 团队</span>',
  '<span>Share this story</span>': '<span>分享本文</span>',
  'data-copied="Copied">Copy link</button>': 'data-copied="已复制">复制链接</button>',
  'id="rel-h">More from the journal</h2>': 'id="rel-h">更多札记</h2>',
  'All stories <svg': '全部文章 <svg',

  # contact
  '<li aria-current="page">Contact</li>': '<li aria-current="page">联络我们</li>',
  '<p class="eyebrow">Contact us</p>': '<p class="eyebrow">联络我们</p>',
  'Let’s plan <em>your next trip.</em>': '一起规划<em>您的下一段旅程。</em>',
  'Message us on WhatsApp, call, or visit our office in Klang. We’d be glad to look after your travel, for business or for pleasure.': '通过 WhatsApp 留言、致电，或到访我们位于巴生的办公室。无论商务还是休闲出行，我们都乐意为您安排。',
  '<dt>Office</dt>': '<dt>办公室</dt>',
  '<dt>Phone</dt>': '<dt>电话</dt>',
  '<dt>Opening hours</dt>': '<dt>营业时间</dt>',
  '<dt>Payment</dt>': '<dt>付款方式</dt>',
  'We reply during office hours.': '我们在办公时间内回复。',
  '<span class="lbl">Proud member of</span>': '<span class="lbl">会员资格</span>',
  'aria-label="Memberships"': 'aria-label="会员资格"',
  'MATTA, Malaysian Association of Tour and Travel Agents': 'MATTA 马来西亚旅游代理商协会',
  'MITA, Malaysian Inbound Tourism Association': 'MITA 马来西亚入境旅游协会',
  'MICA, Malaysia Inbound Chinese Association': 'MICA 马来西亚中国入境旅游协会',
  'MCTA, Malaysian Chinese Tourism Association': 'MCTA 马来西亚华人旅游协会',
  'Touch ’n Go eWallet accepted at our office': '本公司接受 Touch ’n Go eWallet 付款',
  'aria-label="Filter tours by region"': 'aria-label="按地区筛选旅游团"',
  'aria-label="Tours"': 'aria-label="旅游团"',
  'class="t-stub"><span>Partner tour</span>': 'class="t-stub"><span>合作伙伴团</span>',
  '>Open in Google Maps</a>': '>在谷歌地图中打开</a>',
  'Send us a trip enquiry': '发送行程咨询',
  'Fill in what you know. We’ll turn it into a WhatsApp message so you can send it in one tap.': '填写您已知道的资料，我们会把它整理成一条 WhatsApp 讯息，一键即可发送。',
  '>Your name</label>': '>您的姓名</label>',
  'placeholder="Name"': 'placeholder="姓名"',
  '>I’m interested in</label>': '>咨询项目</label>',
  '>Destination</label>': '>目的地</label>',
  'placeholder="For example, Japan"': 'placeholder="例如：日本"',
  '>When</label>': '>出行时间</label>',
  'placeholder="For example, March 2027"': 'placeholder="例如：2027年3月"',
  '>Number of travellers</label>': '>出行人数</label>',
  '>Company (optional)</label>': '>公司（可选填）</label>',
  'placeholder="For corporate trips"': 'placeholder="企业出行适用"',
  '>Anything else?</label>': '>其他需求</label>',
  'placeholder="Budget, hotel preferences, special requests"': 'placeholder="预算、酒店偏好、特别要求"',
  '<p class="preview-label">Your message</p>': '<p class="preview-label">您的讯息</p>',
  '>Send on WhatsApp</button>': '>通过 WhatsApp 发送</button>',
  'Opens WhatsApp with your message ready to send.': '将打开 WhatsApp，讯息已准备好，可直接发送。',
  ' See our <a href="privacy.html">Privacy Notice</a>.': '详见<a href="privacy.html">隐私声明</a>。',
  '<a href="privacy.html">Privacy Notice</a>': '<a href="privacy.html">隐私声明</a>',
}

# patterns that carry a number
UI_RE = [
    (r'<span class="day">Day (\d+)</span>', r'<span class="day">第\1天</span>'),
    (r'<div class="d-num"><span>Day</span>(\d+)</div>', r'<div class="d-num"><span>第</span>\1天</div>'),
    (r'<span>(\d\d:\d\d) to (\d\d:\d\d[^<]*)</span>', r'<span>\1 – \2</span>'),
]

_KEYS = re.compile('|'.join(re.escape(k) for k in sorted(UI, key=len, reverse=True)))
_USED = set()
_RE = [(re.compile(a), b) for a, b in UI_RE]


def translate(s):
    """One pass, longest key first, so a translation is never translated again."""
    def sub(m):
        _USED.add(m.group(0))
        return UI[m.group(0)]
    s = _KEYS.sub(sub, s)
    for r, b in _RE:
        s = r.sub(b, s)
    return s


def translate_html(html, fname):
    """Translate everything except the contents of <script> and <style>."""
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>)', html, flags=re.S)
    return ''.join(p if i % 2 else translate(p) for i, p in enumerate(parts))


# English that may stay on a Chinese page: names, the legal entity, the address, contact details
KEEP = ['YSL Travel & Tours Sdn Bhd', 'YSL Travel & Tours', 'Travel & Tours', 'Golden Destinations', 'Parlo Tours', 'Apple Vacations',
        'No 5, Lorong Sungai Puloh 13A', 'Taman Klang Utama', 'Klang, Selangor', 'Max Filter Industries', 'Sendok Group', 'Megastra Jaya',
        'Ctrip', 'The Boma', 'Spice Route', 'China Eastern', 'Kitaichi Glass', 'Shiroi Koibito Park', 'Shiroi Koibito', 'Mitsui Outlet Park',
        'Galeries Lafayette', 'Parndorf Designer Outlet', 'Sky Tower Orbit',
        'Europe Legend', 'Hokkaido Delight', 'The Charms of Türkiye', 'Eastern Europe Vista', 'New Zealand North & South Island', 'Essence of South Africa',
        'The Grand Egypt Tour', 'Starfield Library', 'The Painters', 'Seoul Sky', 'Fox Town', 'Serravalle Designer Outlet', 'Peak Walk by Tissot', 'Peak Walk',
        'Eiger Express', 'Golden Pass', 'Glacier 3000',
        'Lovely Vacation', 'UbinGO Vacations', 'Golden Peak, Hidden Lake', 'Subang SkyPark', 'Batik Air', 'Rick’s Café', 'FS Holidays', 'Touch ’n Go eWallet', 'Penguins Plus', 'Santa’s Hotels', 'The Edge']  # brand names stay in English


def check(zh_dir):
    unused = sorted(set(UI) - _USED)
    if unused:
        raise SystemExit('zh.py: these UI entries no longer match any page (did the English change?):\n  ' + '\n  '.join(unused))
    problems = []
    for f in sorted(os.listdir(zh_dir)):
        if not f.endswith('.html'):
            continue
        h = open(os.path.join(zh_dir, f), encoding='utf-8').read()
        h = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', h, flags=re.S)
        attrs = ' | '.join(a for a in re.findall(r'\s(?:alt|aria-label|placeholder|title|content)="([^"]*)"', h) if 'width=' not in a)
        text = re.sub(r'<[^>]+>', ' | ', h) + ' | ' + attrs
        text = _html.unescape(text)
        for k in sorted(KEEP, key=len, reverse=True):
            text = text.replace(k, ' ')
        for m in re.finditer(r"[A-Za-z][A-Za-z’'.-]*(?:[ ,]+[A-Za-z][A-Za-z’'.-]*)+", text):
            w = m.group(0)
            if re.fullmatch(r'(?:[A-Z0-9.&-]{2,}|[A-Z][a-z]+)(?:[ ,]+(?:[A-Z0-9.&-]{2,}))*', w):  # codes and acronyms (KUL, MATTA, MICE)
                continue
            if w.startswith(('width=', 'http', 'Noto')) or '/' in w:
                continue
            problems.append(f'{f}: {w}')
    if problems:
        raise SystemExit('zh.py: English left on Chinese pages:\n  ' + '\n  '.join(dict.fromkeys(problems)))
    print('zh: all pages translated')
