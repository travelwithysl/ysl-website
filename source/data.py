# Content for the YSL site. In production this becomes JSON/Markdown files the studio edits.

SERVICES = [
    dict(slug='air', icon='air', title='Air ticket reservation',
         short='Fares for individuals, groups, students and workers.',
         body='Flights for every kind of traveller: holidays, business trips, students heading overseas and workers travelling on contract. We compare airlines and routes, hold group seats, and look after changes if your plans shift.',
         includes=['Individual and group fares', 'Student and worker fares', 'Full-service and low-cost airlines', 'Special assistance, such as wheelchair requests', 'Date changes and rebooking support']),
    dict(slug='tours', icon='tour', title='Tour packages',
         short='Domestic, inbound and international tours.',
         body='Group tours across Asia, Europe and beyond, domestic getaways, and inbound tours for visitors to Malaysia. We match each trip to your pace, interests and budget, and look after you from the first quote to the flight home.',
         includes=['Group tours with experienced tour leaders', 'Free-and-easy packages', 'Domestic and inbound tours', 'Private and family itineraries', 'Packages from leading tour brands']),
    dict(slug='hotels', icon='hotel', title='Worldwide hotels',
         short='City hotels and resorts, confirmed before you go.',
         body='City hotels, resorts and family-friendly stays, booked and confirmed before you leave, on their own or as part of a package.',
         includes=['Hotels and resorts worldwide', 'Room blocks for groups and events', 'Flight and hotel packages']),
    dict(slug='cruises', icon='cruise', title='Cruise packages',
         short='From short Asian sailings to the Mediterranean.',
         body='Cruise holidays from short sailings in the region to long-haul fly-cruise journeys, with flights, pre-cruise hotels and transfers arranged around your sailing.',
         includes=['Short sailings from the region', 'Fly-cruise holidays to Europe and beyond', 'Cabin advice for families and groups']),
    dict(slug='insurance', icon='ins', title='Insurance',
         short='Travel cover arranged with your booking.',
         body='Travel insurance arranged together with your booking, so you are covered from the day you pay.',
         includes=['Medical cover while overseas', 'Trip delays and cancellations', 'Lost or delayed baggage', 'Individual, family and group plans']),
    dict(slug='visa', icon='visa', title='Visa application',
         short='Document checks and application support.',
         body='We check what your destination needs, help prepare your documents and guide you through the application, so there are no surprises at the counter.',
         includes=['Requirement checks before you book', 'Document preparation', 'Application and appointment support']),
    dict(slug='incentive', icon='mice', title='Incentive groups',
         short='Company trips, meetings and incentive travel.',
         body='Incentive trips, company outings, meetings and conferences, planned from the brief and budget to the day everyone boards, with one point of contact throughout.',
         includes=['Incentive and reward trips', 'Company outings and team trips', 'Meetings, conferences and events', 'One point of contact throughout']),
    dict(slug='coach', icon='coach', title='Coach hire',
         short='Luxury air-conditioned coaches for groups.',
         body='Luxury air-conditioned coaches for tour groups, company trips, school outings and events, with experienced drivers who know the routes.',
         includes=['Coaches for groups of every size', 'Airport and event transfers', 'Day trips and outstation journeys']),
]

TOURS = [
    dict(slug='qinghai-gansu', dur='10D8N', iata='LHW', title='Majestic Qinghai & Gansu', region='China', cat='asia', kind='Group tour', line='Rainbow mountains, desert dunes and sky-mirror salt lakes', img='qg-card.jpg', page='tour-qinghai-gansu.html'),
    dict(slug='yunnan', dur='9D7N', origin='SZB', iata='KMG', title='Golden Peak, Hidden Lake', region='China', cat='asia', kind='Group tour', line='Dali, Lugu Lake, Lijiang, Shangri-La and sunrise on Meili Snow Mountain', img='yn-card.jpg', page='tour-yunnan.html'),
    # signature group tours from Golden Destinations, a brand YSL carries (no prices; enquiries go to YSL)
    dict(slug='gd-europe-legend', dur='10D7N', page='tour-gd-europe-legend.html', brand='Golden Destinations', iata='CDG', short='Europe Legend', title='Europe Legend', region='Europe', cat='europe', kind='Group tour',
         line='Paris, Brussels, Amsterdam, the Rhine, Titisee, Rhine Falls, Zurich and Lucerne', img='gd-europe-legend-card.jpg'),
    dict(slug='gd-hokkaido', dur='6D4N', page='tour-gd-hokkaido.html', brand='Golden Destinations', iata='CTS', short='Hokkaido', title='Hokkaido Delight', region='Japan', cat='asia', kind='Group tour',
         line='Noboribetsu, Lake Toya, Otaru and Sapporo', img='gd-hokkaido-card.jpg'),
    dict(slug='gd-turkiye', dur='9D7N', page='tour-gd-turkiye.html', brand='Golden Destinations', iata='IST', short='Türkiye', title='The Charms of Türkiye', region='Türkiye', cat='europe', kind='Group tour',
         line='Istanbul, Canakkale, Ephesus, Pamukkale, Konya and Cappadocia', img='gd-turkiye-card.jpg'),
    dict(slug='gd-eastern-europe', dur='9D6N', page='tour-gd-eastern-europe.html', brand='Golden Destinations', iata='BUD', short='Eastern Europe', title='Eastern Europe Vista', region='Europe', cat='europe', kind='Group tour',
         line='Budapest, Bratislava, Vienna, Hallstatt, Salzburg, Cesky Krumlov and Prague', img='gd-eastern-europe-card.jpg'),
    dict(slug='gd-new-zealand', dur='9D7N', page='tour-gd-new-zealand.html', brand='Golden Destinations', iata='AKL', short='New Zealand', title='New Zealand North &amp; South Island', region='New Zealand', cat='oceania', kind='Group tour',
         line='Both islands, from Auckland to Queenstown', img='gd-new-zealand-card.jpg'),
    dict(slug='gd-south-africa', dur='11D8N', page='tour-gd-south-africa.html', brand='Golden Destinations', iata='JNB', short='South Africa', title='Essence of South Africa', region='Africa', cat='africa', kind='Group tour',
         line='Johannesburg, Cape Town, Botswana and Victoria Falls', img='gd-south-africa-card.jpg'),
    dict(slug='gd-japan', dur='7D6N', page='tour-gd-japan.html', brand='Golden Destinations', iata='NRT', short='Japan', title='Tokyo to Osaka via Mount Fuji &amp; Shirakawa-go', region='Japan', cat='asia', kind='Group tour',
         line='Asakusa, Mount Fuji, Takayama, Shirakawa-go, Kyoto and Osaka', img='gd-japan-card.jpg'),
    dict(slug='gd-korea', dur='6D4N', page='tour-gd-korea.html', brand='Golden Destinations', iata='ICN', short='Korea', title='Seoul, Nami Island &amp; Mount Sorak', region='South Korea', cat='asia', kind='Group tour',
         line='Nami Island, Mount Sorak, Everland and Gyeongbokgung in hanbok', img='gd-korea-card.jpg'),
    dict(slug='gd-taiwan', dur='5D4N', page='tour-gd-taiwan.html', brand='Golden Destinations', iata='TPE', short='Taiwan', title='Taipei, Jiufen &amp; Yilan', region='Taiwan', cat='asia', kind='Group tour',
         line='Yehliu, Jiufen, Shifen, a hot-spring night in Jiaoxi and Taipei', img='gd-taiwan-card.jpg'),
    dict(slug='gd-vietnam', dur='5D4N', page='tour-gd-vietnam.html', brand='Golden Destinations', iata='DAD', short='Da Nang', title='Da Nang, Hoi An &amp; Hue', region='Vietnam', cat='asia', kind='Group tour',
         line='Hoi An’s old town, the Golden Bridge at Ba Na Hills and imperial Hue', img='gd-vietnam-card.jpg'),
    dict(slug='gd-switzerland-italy', dur='10D7N', page='tour-gd-switzerland-italy.html', brand='Golden Destinations', iata='MXP', short='Switzerland', title='Switzerland &amp; Italy', region='Europe', cat='europe', kind='Group tour',
         line='Jungfraujoch, Glacier 3000, the Golden Pass train, Lake Geneva and Milan', img='gd-switzerland-italy-card.jpg'),
    dict(slug='gd-egypt', dur='9D7N', page='tour-gd-egypt.html', brand='Golden Destinations', iata='CAI', short='Egypt', title='The Grand Egypt Tour', region='Egypt', cat='africa', kind='Group tour',
         line='The Pyramids, Abu Simbel, three nights on the Nile, Luxor and Alexandria', img='gd-egypt-card.jpg'),
    # partner tours from Apple Vacations (applevacations.my), named only on their tour pages
    dict(slug='ap-zhangjiajie', dur='9D6N', page='tour-ap-zhangjiajie.html', brand='Apple Vacations', iata='CSX', short='Zhangjiajie', title='Zhangjiajie, Tianmen Mountain &amp; Phoenix Town', region='China', cat='asia', kind='Group tour',
         line='The sandstone pillars, the glass bridge, Tianmen Mountain and Phoenix Ancient Town', img='ap-zhangjiajie-card.jpg'),
    dict(slug='ap-dongbei', dur='8D7N', page='tour-ap-dongbei.html', brand='Apple Vacations', iata='CGQ', short='Harbin', title='Snowy Dongbei: Changbai Mountain &amp; Harbin', region='China', cat='asia', kind='Group tour',
         line='Rime forests, hot springs in the snow and Harbin’s Ice and Snow World', img='ap-dongbei-card.jpg'),
    dict(slug='ap-spain-portugal', dur='12D9N', page='tour-ap-spain-portugal.html', brand='Apple Vacations', iata='OPO', short='Spain', title='Spain &amp; Portugal', region='Europe', cat='europe', kind='Group tour',
         line='Porto, Lisbon, Seville, Ronda, Córdoba, Toledo, Madrid and Barcelona', img='ap-spain-portugal-card.jpg'),
    dict(slug='ap-morocco', dur='11D8N', page='tour-ap-morocco.html', brand='Apple Vacations', iata='CMN', short='Morocco', title='Morocco: Chefchaouen, Fez &amp; the Sahara', region='Africa', cat='africa', kind='Group tour',
         line='Casablanca, the blue town of Chefchaouen, Fez, a night by the Sahara and Marrakesh', img='ap-morocco-card.jpg'),
    dict(slug='ap-finland', dur='10D7N', page='tour-ap-finland.html', brand='Apple Vacations', iata='RVN', short='Lapland', title='Finnish Lapland &amp; the Northern Lights', region='Europe', cat='europe', kind='Group tour',
         line='Huskies, reindeer, king crab in Norway and the Northern Lights', img='ap-finland-card.jpg'),
    dict(slug='ap-australia', dur='9D6N', page='tour-ap-australia.html', brand='Apple Vacations', iata='SYD', short='Australia', title='Sydney &amp; Melbourne', region='Australia', cat='oceania', kind='Group tour',
         line='Sydney Harbour, the Blue Mountains, the Great Ocean Road and the Penguin Parade', img='ap-australia-card.jpg'),
]

POSTS = [
    dict(slug='yunnan', title="A first-timer's guide to Yunnan's high country", cat='dest', cat_label='Destinations', date='2 October 2026',
         excerpt='Kunming, Lijiang and Shangri-La, and how to enjoy the climb.', img='lake.jpg', href='journal-yunnan.html'),
    dict(slug='fair', title='Meet us at GD Travel Fair, 9 to 11 October', cat='news', cat_label='News', date='28 September 2026',
         excerpt='Fair-only fares at The Starling Mall, ground floor.', img='airport.jpg', href='journal-yunnan.html'),
    dict(slug='docs', title='Passport, visa, insurance: sort these first', cat='tips', cat_label='Travel tips', date='2 September 2026',
         excerpt='The three things to check before you pay a deposit.', img='passport.jpg', href='journal-yunnan.html'),
    dict(slug='packing', title='Packing light for a two-week tour', cat='tips', cat_label='Travel tips', date='20 August 2026',
         excerpt='One suitcase, three climates, and what our tour leaders bring.', img='mapdesk.jpg', href='journal-yunnan.html'),
    dict(slug='planning', title='How we plan a group tour', cat='news', cat_label='News', date='5 August 2026',
         excerpt='What happens between your first quote and departure day.', img='laptop.jpg', href='journal-yunnan.html'),
]

# tour brands YSL is an authorised agent or partner of (shop door, 2026); Golden Destinations kept low-key at the client's request
BRANDS = ['Apple Vacations', 'Lovely Vacation', 'UbinGO Vacations', 'FS Holidays', 'Parlo Tours', 'Golden Destinations']

FAIRS = [('GD Travel Fair', 'The Starling Mall, 9 to 11 October 2026'),
         ('MATTA Fair', 'MITEC, Kuala Lumpur')]

MEMBERS = [('MATTA', 'Malaysian Association of Tour and Travel Agents'),
           ('MITA', 'Malaysian Inbound Tourism Association'),
           ('MICA', 'Malaysian Inbound Chinese Association'),
           ('MCTA', 'Malaysian Chinese Tourism Association')]

CONTACT = dict(address='No 5, Lorong Sungai Puloh 13A,<br>Taman Klang Utama, 42100 Klang, Selangor',
               phone='03-3290 3500', email='travelwithysl@gmail.com',
               hours='Mon to Fri, 9am to 6pm<br>Sat, 9am to 3pm<br>Closed on Sundays',
               maps='https://www.google.com/maps/search/?api=1&amp;query=YSL+Travel+%26+Tours+Sdn+Bhd+Taman+Klang+Utama',
               whatsapp='+60 16-626 4500', wa='60166264500',  # office WhatsApp line, checked during office hours
               facebook='https://www.facebook.com/ysltravel', instagram='https://www.instagram.com/ysltravel/')

# destinations the home-page pin opens onto; one is chosen per visit. Add YSL's own tour photos here.
OPENINGS = [
    dict(img='yn-hero.jpg', code='KMG', place='Kunming, Yunnan', tour='Golden Peak, Hidden Lake', href='tour-yunnan.html', kind='Group tour'),
]

# Majestic Qinghai & Gansu, from YSL's 2026 itinerary (prices deliberately left out)
QG = dict(
    slug='qinghai-gansu', page='tour-qinghai-gansu.html', zh='大美青甘',
    title='Majestic Qinghai &amp; Gansu', line='Danxia, dunes and sky mirrors.', duration='10 days, 8 nights',
    highlights=['Zhangye Rainbow Mountains', 'Mogao Caves, Dunhuang', 'Mingsha Mountain and Crescent Spring', 'Jiayuguan Pass',
                'Qarhan Salt Lake', 'Chaka Salt Lake, China’s Sky Mirror', 'Qinghai Lake', 'Kumbum Monastery'],
    flights=[('Day 1', 'MU858', 'KUL', 'LHW', '04:05', '11:30', 'via Kunming'),
             ('Day 9', 'MU857', 'LHW', 'KUL', '19:40', '03:05 +1', 'via Kunming')],
    days=[
        dict(t='Kuala Lumpur to Lanzhou, on to Wuwei', meals='L, D', hotel='Wuwei, Ctrip 4-Diamond hotel or similar',
             p=['Assemble at Kuala Lumpur International Airport and fly China Eastern to Lanzhou, with a stop in Kunming. Our guide meets you at Lanzhou Zhongchuan Airport for the 220km drive to Wuwei.']),
        dict(t='Wuwei, Rainbow Mountains, Zhangye', meals='B, L, D', hotel='Zhangye Mingjiale International Hotel or similar', img=('qg-card.jpg', 'Zhangye Rainbow Mountains'),
             p=['<b>Zhangye Rainbow Mountains.</b> One of China’s finest Danxia landforms, seen from a series of viewing platforms over ridges banded in red, ochre, gold and blue.',
                '<b>Danxiakou Town.</b> The largest themed cultural town in the Northwest, gathering local food, folk culture, boutique stays and live performance.',
                '<b>Optional:</b> the evening stage show “Return to Zhangye”, recreating the Silk Road at its height.'],
             note='Today’s route crosses the Qilian Mountain grasslands and the drives are long; bring motion-sickness remedies if you need them.'),
        dict(t='Zhangye, Jiayuguan, Son of the Earth, Dunhuang', meals='B, L', hotel='Dunhuang Tianrun Yibo Hotel or similar', img=('qg-jiayuguan.jpg', 'Jiayuguan Pass'), img2=('qg-sonofearth.jpg', 'Son of the Earth sculpture on the Gobi'),
             p=['<b>Jiayuguan Pass.</b> The “Greatest Pass Under Heaven”, westernmost gateway of the Ming Great Wall and once the throat of the Hexi Corridor.',
                '<b>Son of the Earth.</b> A 15-metre infant asleep on the Gobi, standing with the “Boundless” and “Emperor Wu of Han” sculptures.',
                '<b>Shazhou Night Market.</b> Free time in Dunhuang for the night market and its local food (dinner at own expense).'],
             meal='Suoyang steamed chicken'),
        dict(t='Mogao Caves, Mingsha Mountain, Dunhuang', meals='B, L, D', hotel='Dunhuang Tianrun Yibo Hotel or similar', img=('qg-mogao.jpg', 'Mogao Caves'), img2=('qg-mingsha.jpg', 'Crescent Spring among the dunes'),
             p=['<b>Mogao Caves.</b> One of China’s four great grottoes and the world’s richest surviving treasury of Buddhist art. Type A ticket: eight caves and the dome-theatre film.',
                '<b>Mingsha Mountain and Crescent Spring.</b> A spring held in a ring of singing dunes, long called a wonder of the frontier.',
                '<b>Optional:</b> a camel ride on Mingsha Mountain.'],
             meal='Roasted whole lamb'),
        dict(t='Dunhuang, Qarhan Salt Lake, Golmud', meals='B, L, D', hotel='Golmud Yilong Hotel or similar', img=('qg-qarhan.jpg', 'Qarhan Salt Lake'),
             p=['<b>U-shaped Highway.</b> Via Yuqia to the rolling road known as “China’s Route 66”.',
                '<b>Qarhan Salt Lake.</b> China’s largest salt lake and the world’s second largest, with jade brine pools set against white salt flats.'],
             meal='Golmud-style dinner'),
        dict(t='Golmud, Chaka Salt Lake', meals='B, L, D', hotel='Chaka Jintian Century International Hotel or similar', img=('qg-chaka.jpg', 'Chaka Salt Lake reflecting the sky', '50% 22%'),
             p=['<b>Xiao Qaidam Lake.</b> A high plateau lake, seen from the coach.',
                '<b>Chaka Salt Lake, the Sky Mirror.</b> Ringed by snow peaks, the still lake mirrors the sky so perfectly that walking on it feels like walking on cloud.',
                '<b>Complimentary:</b> a 30-second drone video and two retouched travel photos. Bright outfits photograph best.'],
             meal='Grassland lamb hotpot', note='UV is strong on the plateau; bring sun protection and moisturiser.'),
        dict(t='Chaka, Tibetan village, Qinghai Lake, Xining', meals='B, L, D', hotel='Xining Datong Holiday Hotel or similar', img=('qg-qinghailake.jpg', 'Prayer flags at Qinghai Lake'),
             p=['<b>Tibetan village.</b> A visit to a traditional village and its way of life.',
                '<b>Qinghai Lake, Erlangjian.</b> China’s largest saltwater lake and the province’s namesake, revered as the sacred lake of the plateau.',
                '<b>Riyue Mountain.</b> Pass the Sun and Moon Mountain on the ancient Tang–Tibet road, reaching Xining by evening.'],
             meal='Tibetan King Feast'),
        dict(t='Xining, Kumbum Monastery, Ping’an Ancient Town, Lanzhou', meals='B, L, D', hotel='Lanzhou, Ctrip 4-Diamond hotel or similar',
             p=['<b>Kumbum Monastery.</b> A great Gelug monastery of Tibetan Buddhism, famed for its three wonders: butter sculptures, murals and appliqué embroidery.',
                '<b>Ping’an Ancient Town.</b> The old frontier town of Zongge, alive today with Hua’er folk song, paper-cut art and Hehuang tradition.'],
             meal='Hehuang specialty snacks'),
        dict(t='Lanzhou, Yellow River, fly home', meals='B, L',
             p=['<b>Yellow River Scenic Line.</b> One of China’s longest city riverfronts, centred on the Zhongshan Iron Bridge, with the Yellow River Mother sculpture and the Waterwheel Park.',
                '<b>Free time.</b> Time permitting, browse Lanzhou’s malls for local specialties before the airport transfer.']),
        dict(t='Arrive in Kuala Lumpur', meals='',
             p=['Arrive in Kuala Lumpur in the early hours. Welcome home.']),
    ],
    features=[('qg-hotel.jpg', 'Ctrip 4-Diamond hotels', 'Eight nights throughout, with two nights in Dunhuang.'),
              ('qg-coach.jpg', 'VIP 2+1 luxury coach', 'Wide seats with at least 15% left free, and drivers with ten years on the road.'),
              ('qg-lamb.jpg', 'A taste of the Northwest', 'Roasted whole lamb, the Tibetan King Feast, lamb hotpot and Suoyang chicken.')],
    included=['Return flights with airport taxes, via Kunming', 'One checked bag up to 23kg, through-checked to Lanzhou',
              'Eight nights in Ctrip 4-Diamond hotels, twin sharing', 'Eight breakfasts and 16 meals', 'VIP 2+1 coach and all transport as stated',
              'Chinese-speaking guide', 'Tips for the guide and driver', 'Entrance to all listed attractions'],
    excluded=['Compulsory experience package: scenic shuttles, the Chaka return train, Kumbum shuttle and guide, and two feature meals',
              'Recommended optionals: “Return to Zhangye” show and the Mingsha camel ride', 'Single supplement', 'Travel insurance (we can arrange this)', 'Personal expenses'],
)

# Golden Destinations group tours, written up from GD's published itineraries (no prices). Photos from GD's itinerary pages and PDFs.
def _d(t, meals, p, hotel='', note='', meal=''):
    return dict(t=t, meals=meals, p=p, hotel=hotel, note=note, meal=meal)

GD_TOURS = [
  dict(slug='gd-europe-legend', page='tour-gd-europe-legend.html', title='Europe Legend', region='Europe', duration='10 days, 7 nights', hero='gd-europe-legend-hero.jpg', hero_alt='A Seine river cruise below the Eiffel Tower',
    seo='Europe Tour Package from Malaysia: Paris, Amsterdam, the Rhine and Switzerland',
    line='Five countries, two river cruises, one classic loop.', hotels='4-star',
    head='From Paris to the Swiss lakes and back.',
    lead='A classic first trip to Western Europe: Brussels and Amsterdam, the Rhine and Black Forest, Rhine Falls, Zurich and Lucerne, finishing with two nights in Paris.',
    highlights=['Amsterdam canal cruise', 'Zaanse Schans windmill village', 'Cologne Cathedral', 'Heidelberg old town', 'Lake Titisee in the Black Forest', 'Rhine Falls', 'Lucerne’s Chapel Bridge', 'Seine River cruise'],
    days=[
      _d('Kuala Lumpur to Paris', '', ['Overnight flight to Paris.']),
      _d('Paris, Brussels, Amsterdam', 'L', ['<b>Brussels.</b> The Atomium, the Grand Place, the King’s House, the City Hall and Manneken Pis.', 'Continue north to Amsterdam.'], 'Amsterdam', meal='Brussels mussels'),
      _d('Amsterdam', 'B, D', ['<b>Canal cruise</b> through the old city, and Dam Square.', '<b>Zaanse Schans.</b> Windmills, a wooden-shoe workshop and a cheese farm.', 'A visit to a diamond factory.'], 'Amsterdam'),
      _d('Amsterdam, Cologne, Heidelberg', 'B, L', ['<b>Cologne Cathedral</b>, a UNESCO World Heritage Site.', '<b>Heidelberg.</b> The Old Bridge and the medieval town below the castle.'], 'Heidelberg or Mannheim', meal='German pork knuckle'),
      _d('Heidelberg, Titisee, Rhine Falls, Zurich', 'B, L', ['<b>Lake Titisee</b> in the Black Forest, and its cuckoo-clock makers.', '<b>Rhine Falls</b>, Europe’s most powerful waterfall.'], 'Zurich'),
      _d('Lucerne', 'B', ['<b>Lucerne.</b> The Lion Monument, the wooden Chapel Bridge and Water Tower, and free time in the old town.', '<b>Optional:</b> Mount Titlis by cable car.'], 'Zurich'),
      _d('Zurich to Paris', 'B', ['A scenic drive back west to Paris.'], 'Paris'),
      _d('Paris', 'B, L, D', ['<b>Seine River cruise.</b>', 'The Eiffel Tower, the Arc de Triomphe and the Louvre, with a drive along the Champs-Élysées past the Grand and Petit Palais, Place de la Concorde and the Opéra.', 'Shopping at Galeries Lafayette.'], 'Paris', meal='French three-course dinner with escargot'),
      _d('Paris to Kuala Lumpur', 'B', ['Overnight flight home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Seven nights in 4-star hotels or similar: Amsterdam 2, Heidelberg 1, Zurich 2, Paris 2', '7 breakfasts, 4 lunches and 2 dinners, including mussels, pork knuckle and a French escargot meal', 'Amsterdam canal cruise, Zaanse Schans and the Seine River cruise', 'One checked bag up to 20kg', 'Tour leader for groups of 15 or more'],
    excluded=['Mount Titlis cable car (optional)', 'Visa, travel insurance and tipping, unless stated', 'Meals not listed'],
  ),
  dict(slug='gd-hokkaido', page='tour-gd-hokkaido.html', title='Hokkaido Delight', region='Japan', duration='6 days, 4 nights', hero='gd-hokkaido-hero.jpg', hero_alt='The Mount Usu cable car over the forests above Lake Toya',
    seo='Hokkaido Tour Package from Malaysia: Noboribetsu, Lake Toya, Otaru and Sapporo',
    line='Volcanoes, hot springs, Otaru’s canal and three nights in Sapporo.', hotels='3-star, with an onsen night',
    head='Japan’s far north, at an easy pace.',
    lead='Hell Valley at Noboribetsu, a cable car up Mount Usu and a hot-spring night on Lake Toya, the glassworks and canal of Otaru, then three nights in Sapporo with a free day to explore.',
    highlights=['Noboribetsu Jigokudani, Hell Valley', 'Mount Usu cable car', 'Showa-Shinzan volcano', 'Onsen night at Lake Toya', 'Otaru Canal', 'Sakaimachi Street and Kitaichi Glass', 'Shiroi Koibito Park', 'Nijo Market and Odori Park'],
    days=[
      _d('Kuala Lumpur to Hokkaido', '', ['Overnight flight to New Chitose.']),
      _d('Chitose, Noboribetsu, Lake Toya', 'L, D', ['<b>Noboribetsu Jigokudani</b>, Hell Valley, a steaming volcanic crater.', '<b>Showa-Shinzan</b>, the volcano that rose from a wheat field, and the <b>Mount Usu cable car</b>.'], 'Lake Toya, onsen hotel', meal='Hot-spring hotel dinner'),
      _d('Lake Toya, Otaru, Sapporo', 'B', ['<b>Otaru.</b> The canal, Sakaimachi Street, Kitaichi Glass and the Music Box Museum.', '<b>Shiroi Koibito Park</b>, with an ice cream, and Mitsui Outlet Park.'], 'Sapporo'),
      _d('Sapporo at leisure', 'B', ['A free day in Sapporo.'], 'Sapporo'),
      _d('Sapporo', 'B, D', ['<b>Hokkaido Shrine</b> and <b>Odori Park</b>.', '<b>Nijo Market</b> for seafood, and the Tanukikoji shopping arcade.'], 'Sapporo', meal='Yakiniku barbecue buffet'),
      _d('Sapporo to Kuala Lumpur', '', ['Transfer to New Chitose and fly home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Four nights: Lake Toya 1 (onsen hotel), Sapporo 3, in 3-star hotels or similar', '3 breakfasts, 1 lunch and 2 dinners, including hot-spring cuisine and a barbecue buffet', 'Mount Usu cable car and Shiroi Koibito ice cream', 'One checked bag up to 20kg'],
    excluded=['Visa, travel insurance and tipping, unless stated', 'Meals not listed', 'Personal expenses'],
    notes='Good in every season: snow from December to February, flowers in summer, and autumn colour from September.',
  ),
  dict(slug='gd-turkiye', page='tour-gd-turkiye.html', title='The Charms of Türkiye', region='Türkiye', duration='9 days, 7 nights', hero='gd-turkiye-hero.jpg', hero_alt='Hot-air balloons over Cappadocia at sunrise',
    seo='Türkiye Tour Package from Malaysia: Istanbul, Pamukkale and Cappadocia',
    line='Istanbul, the Aegean, Pamukkale and two nights in Cappadocia.', hotels='5-star and cave hotels',
    head='A full circle of Türkiye.',
    lead='Istanbul’s great mosques and the Basilica Cistern, Troy and Ephesus on the Aegean, the white terraces of Pamukkale, two nights in a Cappadocia cave hotel, and a Bosphorus cruise to finish.',
    highlights=['Blue Mosque and Hagia Sophia', 'Basilica Cistern', 'Ephesus ancient city', 'Pamukkale’s Cotton Castle', 'Mevlana Museum in Konya', 'Two nights in a Cappadocia cave hotel', 'Underground City', 'Bosphorus cruise'],
    days=[
      _d('Kuala Lumpur to Istanbul', '', ['Overnight flight to Istanbul.']),
      _d('Istanbul to Canakkale', 'B, L, D', ['<b>Istanbul.</b> The Blue Mosque, the Hippodrome, Hagia Sophia and the <b>Basilica Cistern</b>.', 'Drive along the Sea of Marmara to Canakkale.'], 'Canakkale'),
      _d('Canakkale, Ephesus, Kusadasi', 'B, L, D', ['The Trojan Horse at Canakkale.', '<b>Ephesus</b>, one of the best-preserved Roman cities in the world.'], 'Kusadasi'),
      _d('Kusadasi to Pamukkale', 'B, L, D', ['<b>House of the Virgin Mary.</b>', '<b>Pamukkale</b>, the white travertine terraces known as the Cotton Castle, beside ancient Hierapolis.'], 'Pamukkale'),
      _d('Pamukkale, Konya, Cappadocia', 'B, L, D', ['<b>Mevlana Museum</b> in Konya, home of the whirling dervishes.', 'On to Cappadocia.'], 'Cappadocia, cave hotel'),
      _d('Cappadocia', 'B, L, D', ['<b>Underground City.</b>', 'Uchisar Castle, Pigeon Valley, the Three Beauties and Göreme Valley.', 'Avanos pottery village, Turkish ice cream, and a belly-dance show in a cave.', '<b>Optional:</b> a sunrise hot-air balloon flight or a jeep safari.'], 'Cappadocia, cave hotel'),
      _d('Cappadocia, Ankara, Istanbul', 'B, L, D', ['A Silk Road caravanserai and the Salt Lake.', '<b>Anıtkabir</b>, Atatürk’s mausoleum in Ankara, then on to Istanbul.'], 'Istanbul'),
      _d('Istanbul to Kuala Lumpur', 'B', ['<b>Grand Bazaar</b> and a <b>Bosphorus cruise</b> between Europe and Asia.', 'Overnight flight home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Seven nights: Canakkale 1, Kusadasi 1, Pamukkale 1, Cappadocia 2 (cave or stone-house hotel), Istanbul 2', '7 breakfasts, 6 lunches and 7 dinners', 'Basilica Cistern, Ephesus, House of the Virgin Mary, Pamukkale and the Underground City', 'Bosphorus cruise and a belly-dance show', 'One checked bag up to 20kg'],
    excluded=['Hot-air balloon and jeep safari (optional)', 'Troy Museum', 'Visa, travel insurance and tipping, unless stated'],
    notes='From June to mid September, Cappadocia nights may move to a 5-star hotel, as many cave hotels have no air conditioning.',
  ),
  dict(slug='gd-eastern-europe', page='tour-gd-eastern-europe.html', title='Eastern Europe Vista', region='Europe', duration='9 days, 6 nights', hero='gd-eastern-europe-hero.jpg', hero_alt='Hallstatt on its lake below the Alps',
    seo='Eastern Europe Tour Package from Malaysia: Budapest, Vienna, Hallstatt and Prague',
    line='Budapest, Vienna, Hallstatt, Salzburg, Cesky Krumlov and Prague.', hotels='4-star',
    head='Four capitals and two fairytale towns.',
    lead='The Danube at Budapest, imperial Vienna, the lakeside village of Hallstatt, Mozart’s Salzburg, medieval Cesky Krumlov, and two nights in Prague.',
    highlights=['Danube River cruise in Budapest', 'Fisherman’s Bastion', 'Schönbrunn Palace', 'Hallstatt', 'Mozart’s Salzburg', 'Cesky Krumlov', 'Prague Castle', 'Charles Bridge and the Astronomical Clock'],
    days=[
      _d('Kuala Lumpur to Budapest', '', ['Overnight flight to Budapest.']),
      _d('Budapest', 'L, D', ['Matthias Church and Fisherman’s Bastion, with a drive past Buda Castle, the Chain Bridge, Andrássy Avenue and Heroes’ Square.', '<b>Danube River cruise.</b>'], 'Budapest'),
      _d('Budapest, Bratislava, Vienna', 'B, D', ['<b>Bratislava.</b> The castle and the old town square.', 'On to Vienna.'], 'Vienna'),
      _d('Vienna', 'B, D', ['<b>Schönbrunn Palace</b>, the Habsburg summer residence.', 'St Stephen’s Cathedral, Kärntner Strasse, the Hofburg and the Belvedere gardens.', 'Shopping at Parndorf Designer Outlet.'], 'Vienna'),
      _d('Vienna, Hallstatt, Salzburg', 'B, D', ['<b>Hallstatt</b>, the UNESCO-listed village on its lake.', '<b>Salzburg.</b> Mirabell Palace and Gardens, Mozart’s birthplace, the cathedral and Mozartplatz.'], 'Salzburg'),
      _d('Salzburg, Cesky Krumlov, Prague', 'B, L, D', ['<b>Cesky Krumlov</b>, a UNESCO town wrapped around its castle on the Vltava.', 'On to Prague.'], 'Prague'),
      _d('Prague', 'B', ['<b>Prague Castle</b>, St Vitus Cathedral, the Old Royal Palace and Golden Lane.', 'Charles Bridge, the Old Town Square, the Astronomical Clock and Wenceslas Square.'], 'Prague'),
      _d('Prague to Kuala Lumpur', 'B', ['Overnight flight home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Six nights in 4-star hotels or similar: Budapest 1, Vienna 2, Salzburg 1, Prague 2', '6 breakfasts, 2 lunches and 5 dinners', 'Danube cruise, Schönbrunn Palace and Prague Castle', 'One checked bag up to 20kg'],
    excluded=['Visa, travel insurance and tipping, unless stated', 'Meals not listed'],
  ),
  dict(slug='gd-new-zealand', page='tour-gd-new-zealand.html', title='New Zealand North &amp; South Island', region='New Zealand', duration='9 days, 7 nights', hero='gd-new-zealand-hero.jpg', hero_alt='A cruise boat beneath a waterfall in Milford Sound',
    seo='New Zealand Tour Package from Malaysia: North and South Island',
    line='Hobbiton, glowworms, Milford Sound and Mount Cook.', hotels='Hotels throughout',
    head='Both islands in nine days.',
    lead='Rotorua’s geysers and Māori culture, the Hobbiton set and Waitomo’s glowworm caves on the North Island, then Queenstown, Milford Sound, Mount Cook, Lake Tekapo and Christchurch on the South.',
    highlights=['Hobbiton Movie Set', 'Te Puia and Pohutu Geyser', 'Waitomo Glowworm Caves', 'Milford Sound cruise', 'Arrowtown and Kawarau Bridge', 'Mount Cook and Lake Pukaki', 'Church of the Good Shepherd, Lake Tekapo', 'Punting on the Avon'],
    days=[
      _d('Kuala Lumpur to Auckland', '', ['Fly to Auckland.'], 'Auckland'),
      _d('Auckland, Hamilton, Rotorua', 'L, D', ['<b>Hamilton Gardens.</b>', 'On to Rotorua.'], 'Rotorua'),
      _d('Rotorua and Matamata', 'B, L, D', ['<b>Hobbiton Movie Set</b>, with a drink at the Green Dragon Inn.', '<b>Te Puia.</b> The Pohutu Geyser, the Māori arts and crafts institute, and the kiwi house.'], 'Rotorua', meal='Māori hangi dinner with a cultural performance'),
      _d('Rotorua, Waitomo, Auckland', 'B, L, D', ['<b>Agrodome farm show.</b>', '<b>Waitomo Glowworm Caves.</b>'], 'Auckland', meal='Dinner at the Sky Tower’s Orbit restaurant'),
      _d('Auckland to Queenstown, Te Anau', 'B, L, D', ['Fly to Queenstown.', 'Historic <b>Arrowtown</b> and the Kawarau Bridge, home of the bungy jump.'], 'Te Anau'),
      _d('Milford Sound', 'B, L, D', ['<b>Milford Sound cruise</b> with lunch on board.', 'On to Queenstown.'], 'Queenstown'),
      _d('Mount Cook, Lake Tekapo, Christchurch', 'B, L, D', ['Past <b>Mount Cook</b> and Lake Pukaki, with the lookout over both.', '<b>Church of the Good Shepherd</b> on Lake Tekapo.'], 'Christchurch'),
      _d('Christchurch to Auckland', 'B, L, D', ['Christchurch city tour, the Botanic Gardens and <b>punting on the Avon</b>.', 'Fly to Auckland.'], 'Auckland'),
      _d('Auckland to Kuala Lumpur', 'B', ['Fly home.']),
    ],
    included=['Return flights from Kuala Lumpur, and domestic flights to Queenstown and from Christchurch', 'Seven nights in hotels', '7 breakfasts, 7 lunches and 7 dinners, including a Māori hangi, the Sky Tower Orbit restaurant and a barbecue lunch', 'Hobbiton, Te Puia, Waitomo, Agrodome, Milford Sound cruise and Avon punting', 'One checked bag up to 30kg'],
    excluded=['Visa, travel insurance and tipping, unless stated', 'Personal expenses'],
  ),
  dict(slug='gd-south-africa', page='tour-gd-south-africa.html', title='Essence of South Africa', region='Africa', duration='11 days, 8 nights', hero='gd-south-africa-hero.jpg', hero_alt='A helicopter over Victoria Falls and the Zambezi gorge',
    seo='South Africa Tour Package from Malaysia: Cape Town, Chobe and Victoria Falls',
    line='Johannesburg, Chobe, Victoria Falls and four nights in Cape Town.', hotels='4 and 5-star',
    head='Safari, the Falls and the Cape.',
    lead='Game drives and a river cruise in Botswana’s Chobe, a helicopter flight over Victoria Falls, a Zambezi sunset, then Cape Town: the Peninsula, Table Mountain, penguins and the winelands.',
    highlights=['Chobe River cruise and game drive', 'Victoria Falls', '“Flight of Angels” helicopter ride', 'Zambezi sunset cruise', 'Cape Point and the Cape of Good Hope', 'Seal Island cruise', 'Stony Point penguins', 'Table Mountain cable car'],
    days=[
      _d('Kuala Lumpur to Johannesburg', '', ['Overnight flight to Johannesburg.']),
      _d('Johannesburg', 'L, D', ['A city drive past Mandela House, Constitution Hill and Sandton.', 'Nelson Mandela Square.'], 'Johannesburg'),
      _d('Johannesburg to Chobe, Botswana', 'B, D', ['Fly to Botswana.', '<b>Chobe River game cruise.</b>'], 'Chobe'),
      _d('Chobe to Victoria Falls', 'B, L, D', ['<b>Chobe game drive.</b>', 'Cross into Zimbabwe for a guided tour of <b>Victoria Falls</b>.'], 'Victoria Falls', meal='The Boma dinner and show'),
      _d('Victoria Falls', 'B, L, D', ['<b>Game drive</b> at Victoria Falls.', '<b>“Flight of Angels”</b>, a 12-minute helicopter flight over the Falls, weather permitting.', '<b>Zambezi River sunset cruise.</b>'], 'Victoria Falls'),
      _d('Victoria Falls to Cape Town', 'B, D', ['Fly to Cape Town; the V&amp;A Waterfront.'], 'Cape Town'),
      _d('Cape Peninsula', 'B, L, D', ['Along the Atlantic coast via Clifton and Camps Bay to Hout Bay.', '<b>Seal Island cruise</b>, then <b>Cape Point</b> by funicular and the <b>Cape of Good Hope</b>.'], 'Cape Town', meal='Lobster meal'),
      _d('Hermanus', 'B, L, D', ['Abalone farm tour and tasting in Hermanus.', '<b>Stony Point</b> penguin colony.'], 'Cape Town', meal='Abalone, and an exotic dinner with drumming'),
      _d('Table Mountain and the winelands', 'B, L, D', ['<b>Table Mountain cable car.</b>', 'The Bo-Kaap Malay Quarter and the Company’s Garden.', 'Wine, beer, chocolate and spirits tasting at the Spice Route.'], 'Cape Town', meal='Winery lunch with wine pairing'),
      _d('Cape Town to Kuala Lumpur', 'B', ['Free time, then the flight home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights and two domestic flights', 'Eight nights in 4 and 5-star hotels: Johannesburg 1, Botswana 1, Victoria Falls 2, Cape Town 4', '8 breakfasts, 6 lunches and 8 dinners, including the Boma dinner, lobster, abalone and a winery lunch', 'Chobe cruise and game drive, Victoria Falls, helicopter flight, Zambezi sunset cruise, Seal Island, Cape Point, Stony Point and Table Mountain', 'One checked bag up to 20kg'],
    excluded=['Travel insurance and tipping, unless stated', 'Personal expenses'],
    notes='No visa is needed for Malaysian passport holders. No triple rooms on this tour.',
  ),
  dict(slug='gd-japan', page='tour-gd-japan.html', title='Tokyo to Osaka via Mount Fuji &amp; Shirakawa-go', region='Japan', duration='7 days, 6 nights', hero='gd-japan-hero.jpg', hero_alt='Thatched gassho-zukuri farmhouses in Shirakawa-go',
    seo='Japan Tour Package from Malaysia: Tokyo, Mount Fuji, Shirakawa-go and Kyoto',
    line='Mount Fuji, the Japan Alps and Kyoto, from Tokyo to Osaka.', hotels='4-star, with an onsen night by Mount Fuji',
    head='Across Japan, from Tokyo to Osaka.',
    lead='Asakusa in Tokyo, a hot-spring night below Mount Fuji, Matsumoto Castle and old Takayama in the Japan Alps, the thatched farmhouses of Shirakawa-go, then Kyoto’s Golden Pavilion and torii gates, and Osaka’s Dotonbori to finish.',
    highlights=['Sensoji and Nakamise Street, Asakusa', 'Mount Fuji 5th Station', 'Onsen night near Mount Fuji', 'Matsumoto Castle', 'Takayama old town', 'Shirakawa-go, a UNESCO village', 'Kinkakuji and Fushimi Inari', 'Osaka Castle and Dotonbori'],
    days=[
      _d('Kuala Lumpur to Tokyo', '', ['Fly to Tokyo and check in near Narita.'], 'Narita'),
      _d('Tokyo, Hakone, Mount Fuji', 'B, L, D', ['<b>Sensoji</b>, Tokyo’s oldest temple, and the snack stalls of Nakamise Street.', '<b>Mount Fuji 5th Station</b>, weather permitting, looking out over the Fuji Five Lakes.'], 'Mount Fuji area, onsen resort', note='From 20 April to 25 May the day takes in the Fuji Shibazakura Festival, hillsides of pink moss phlox, in place of the 5th Station.', meal='Hot-spring hotel dinner'),
      _d('Mount Fuji, Matsumoto, Takayama', 'B, L, D', ['<b>Daio Wasabi Farm</b>, fed by Alpine spring water.', '<b>Matsumoto Castle</b>, one of Japan’s great original castles, seen from the grounds.'], 'Takayama'),
      _d('Takayama, Shirakawa-go, Gifu', 'B, L, D', ['<b>Takayama old town</b> and its Edo-period merchant streets.', '<b>Shirakawa-go</b>, the UNESCO-listed village of steep thatched farmhouses built to carry the winter snow.'], 'Gifu', meal='Hida beef'),
      _d('Gifu, Kyoto, Osaka', 'B, L, D', ['<b>Kinkakuji</b>, the Golden Pavilion.', '<b>Nishiki Market</b>, Kyoto’s food street.', '<b>Fushimi Inari Taisha</b> and its tunnels of vermilion torii gates.'], 'Osaka'),
      _d('Osaka', 'B, D', ['<b>Osaka Castle Park.</b>', 'Shinsaibashi and <b>Dotonbori</b>, then the outlet mall at Rinku Town.'], 'Near Kansai Airport', meal='Barbecue buffet'),
      _d('Osaka to Kuala Lumpur', 'B', ['Fly home from Kansai.']),
    ],
    included=['Return flights from Kuala Lumpur, into Tokyo and home from Osaka', 'Six nights in 4-star hotels or similar: Narita 1, Mount Fuji 1 (onsen resort), Takayama 1, Gifu 1, Osaka 1, Kansai 1', '6 breakfasts, 4 lunches and 5 dinners, including Hida beef, a pork cutlet set and hot-spring hotel cuisine', 'One checked bag up to 20kg'],
    excluded=['Travel insurance and tipping, unless stated', 'Meals not listed', 'Personal expenses'],
  ),
  dict(slug='gd-korea', page='tour-gd-korea.html', title='Seoul, Nami Island &amp; Mount Sorak', region='South Korea', duration='6 days, 4 nights', hero='gd-korea-hero.jpg', hero_alt='Visitors in hanbok at Gyeongbokgung Palace, Seoul',
    seo='Korea Tour Package from Malaysia: Seoul, Nami Island and Mount Sorak',
    line='Nami Island, Seoraksan by cable car, Everland, and Seoul in hanbok.', hotels='4-star, with a 5-star resort at Mount Sorak',
    head='Korea’s classic first trip.',
    lead='The Garden of Morning Calm and the tree-lined avenues of Nami Island, a temple and a cable car in Seoraksan National Park, a full day at Everland, then Seoul: the Lotte World Tower, Starfield Library and Gyeongbokgung Palace, visited in hanbok.',
    highlights=['Nami Island', 'The Garden of Morning Calm', 'Seoraksan cable car', 'Sinheungsa Temple', 'Everland, with unlimited rides', 'Seoul Sky at Lotte World Tower', 'Starfield Library', 'Gyeongbokgung Palace in hanbok'],
    days=[
      _d('Kuala Lumpur to Incheon', '', ['Overnight flight to Incheon.']),
      _d('Incheon, Gapyeong, Mount Sorak', 'L, D', ['<b>The Garden of Morning Calm</b>, Korea’s oldest private garden.', '<b>Nami Island</b>, whose avenues of tall trees starred in Korean drama.'], 'Mount Sorak, 5-star resort'),
      _d('Seoraksan and Everland', 'B, L', ['<b>Seoraksan National Park.</b> Sinheungsa Temple, and the cable car up to Gwongeumseong Fortress, weather permitting.', '<b>Everland</b>, Korea’s biggest theme park, on a ticket with unlimited rides.'], 'Yongin'),
      _d('Seoul', 'B, L, D', ['Make your own kimchi and seaweed snacks at the Seaweed Museum.', '<b>Seoul Sky</b>, the observation floors near the top of the Lotte World Tower.', '<b>Starfield Library</b> in COEX Mall.', '<b>The Painters</b>, a live-painting stage show.'], 'Seoul', meal='All-you-can-eat Korean barbecue'),
      _d('Seoul in hanbok', 'B, L, D', ['<b>Gyeongbokgung Palace</b>, visited in hanbok. On Tuesdays, when it closes, Deoksugung Palace takes its place.', 'The National Folk Museum, and a drive past the Blue House.', '<b>Myeongdong</b> for shopping and street food.'], 'Incheon', meal='Ginseng chicken soup'),
      _d('Incheon to Kuala Lumpur', 'B', ['Fly home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Four nights: Mount Sorak 1 (5-star resort), Yongin 1, Seoul 1, Incheon 1', '4 breakfasts, 4 lunches and 3 dinners, including bibimbap, dakgalbi, Korean barbecue and ginseng chicken soup', 'Everland ticket, Seoraksan cable car, Seoul Sky and The Painters show', 'Hanbok for the palace visit'],
    excluded=['Travel insurance and tipping, unless stated', 'Meals not listed', 'Personal expenses'],
    notes='The tour includes short shopping stops at a ginseng outlet, a cosmetics shop and a duty-free shop.',
  ),
  dict(slug='gd-taiwan', page='tour-gd-taiwan.html', title='Taipei, Jiufen &amp; Yilan', region='Taiwan', duration='5 days, 4 nights', hero='gd-taiwan-hero.jpg', hero_alt='Taipei 101 above the city at dusk',
    seo='Taiwan Tour Package from Malaysia: Taipei, Jiufen and Yilan',
    line='Night markets, the hillside lanes of Jiufen and a hot-spring night in Yilan.', hotels='3 and 4-star, with a hot-spring resort',
    head='Northern Taiwan, one night market at a time.',
    lead='Keelung’s Miaokou night market on arrival, Yehliu’s rock formations and the hillside lanes of Jiufen, Shifen’s railway street and waterfall, a hot-spring night in Jiaoxi, then two nights in Taipei with Taipei 101, Tamsui and Ximending.',
    highlights=['Miaokou Night Market, Keelung', 'Yehliu Geopark', 'Jiufen Old Street', 'Shifen Old Street and waterfall', 'Hot-spring resort in Jiaoxi', 'Tamsui and Fisherman’s Wharf', 'Taipei 101', 'Raohe Night Market and Ximending'],
    days=[
      _d('Kuala Lumpur to Taoyuan, Keelung', '', ['Fly to Taoyuan and transfer to Keelung.', '<b>Miaokou Night Market</b>, known across Taiwan for its seafood and snacks (dinner at own expense).'], 'Keelung'),
      _d('Yehliu, Jiufen, Shifen, Yilan', 'B', ['<b>Yehliu Geopark</b> and its wind-carved rocks.', '<b>Jiufen Old Street</b>, the hillside town of teahouses and taro balls.', '<b>Shifen Old Street</b>, where the train runs between the shops, with Shifen Waterfall and the Jingan suspension bridge. Sky lanterns are at own expense.', 'Tangweigou hot-spring park in Jiaoxi.'], 'Jiaoxi, hot-spring resort'),
      _d('Yilan to Taipei', 'B, L', ['Make your own scallion pancakes.', '<b>Jimmy Park</b>, built around the illustrator’s picture books.', '<b>Tamsui Old Street</b> and Fisherman’s Wharf.', '<b>Raohe Night Market.</b>'], 'Taipei'),
      _d('Taipei', 'B, L, D', ['The National Revolutionary Martyrs’ Shrine and the Shilin Residence gardens.', '<b>Taipei 101</b> and Four Four South Village.', '<b>Ximending</b>, Taipei’s youth and fashion district.'], 'Taipei', meal='Dumplings'),
      _d('Taipei to Kuala Lumpur', 'B', ['Free time, then the flight home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Four nights in 3 and 4-star hotels or similar: Keelung 1, Jiaoxi 1 (hot-spring resort), Taipei 2', '4 breakfasts, 2 lunches and 1 dinner, including dumplings and Taiwanese home cooking', 'Scallion pancake workshop'],
    excluded=['Sky lanterns at Shifen', 'Meals not listed, including night-market dinners', 'Travel insurance and tipping, unless stated'],
    notes='The tour includes short shopping stops at a local products shop, a pearl centre and a souvenir shop.',
  ),
  dict(slug='gd-vietnam', page='tour-gd-vietnam.html', title='Da Nang, Hoi An &amp; Hue', region='Vietnam', duration='5 days, 4 nights', hero='gd-vietnam-hero.jpg', hero_alt='The Golden Bridge held up by two stone hands at Ba Na Hills',
    seo='Da Nang Tour Package from Malaysia: Hoi An, Hue and Ba Na Hills',
    line='Hoi An by lantern light, the Golden Bridge and the citadel at Hue.', hotels='4-star',
    head='Central Vietnam in five easy days.',
    lead='An evening in Hoi An’s old town, basket boats through a coconut forest, the Marble Mountains and Da Nang’s riverside, the cable car up to Ba Na Hills and its Golden Bridge, then the imperial city of Hue.',
    highlights=['Hoi An Ancient Town', 'Basket boats at Cam Thanh', 'Marble Mountains', 'Dragon Bridge, Da Nang', 'Ba Na Hills cable car', 'The Golden Bridge', 'Hue Imperial Citadel', 'Thien Mu Pagoda by boat'],
    days=[
      _d('Kuala Lumpur to Da Nang, Hoi An', 'L, D', ['Fly to Da Nang and drive to Hoi An.', '<b>Hoi An Ancient Town</b>, the old trading port: the Japanese Covered Bridge and the Cantonese Assembly Hall, then the night market.'], 'Hoi An'),
      _d('Hoi An to Da Nang', 'B, L, D', ['<b>Cam Thanh coconut village</b> by round basket boat, with a fresh coconut.', 'Make your own silk lantern.', '<b>Marble Mountains</b>, with the lift both ways.', 'Da Nang’s pink cathedral, the Dragon Bridge and the riverfront, and Han Market.'], 'Da Nang'),
      _d('Ba Na Hills to Hue', 'B, L, D', ['Cable car up to <b>Ba Na Hills</b>: the <b>Golden Bridge</b>, held up by two giant stone hands, the French Village and Linh Ung Pagoda.', 'On to Hue.'], 'Hue', meal='Buffet lunch at Ba Na Hills'),
      _d('Hue to Da Nang', 'B, L, D', ['<b>Thien Mu Pagoda</b>, reached by boat on the Perfume River.', 'The <b>Imperial Citadel</b> by buggy, modelled on Beijing’s Forbidden City.', 'Thuy Xuan incense village and Lang Co lagoon.', '<b>Son Tra Peninsula</b>, then Son Tra Night Market.'], 'Da Nang', meal='Hue royal cuisine'),
      _d('Da Nang to Kuala Lumpur', 'B', ['Fly home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Four nights in 4-star hotels or similar: Hoi An 1, Hue 1, Da Nang 2', '4 breakfasts, 4 lunches and 4 dinners, including pho, Hoi An’s cao lau noodles, the Ba Na Hills buffet and Hue royal cuisine', 'Ba Na Hills cable car, Marble Mountains lift, basket boat and lantern workshop'],
    excluded=['Optional extras: hot-stone massage, Han River night cruise and a cyclo ride in Hue', 'Travel insurance and tipping, unless stated'],
  ),
  dict(slug='gd-switzerland-italy', page='tour-gd-switzerland-italy.html', title='Switzerland &amp; Italy', region='Europe', duration='10 days, 7 nights', hero='gd-switzerland-italy-hero.jpg', hero_alt='The Jungfrau railway below the north face of the Eiger',
    seo='Switzerland Tour Package from Malaysia: Jungfraujoch, Glacier 3000 and Milan',
    line='Two Alpine summits, a panoramic train and Lake Geneva, starting and ending in Milan.', hotels='3 and 4-star',
    head='The Swiss Alps, with Italy either side.',
    lead='From Milan past Lake Lugano to Interlaken, up to the Jungfraujoch by cogwheel train and down by the Eiger Express, out on the Peak Walk at Glacier 3000, along Lake Geneva by the Golden Pass line, then Genoa and two nights in Milan.',
    highlights=['Jungfraujoch, the Top of Europe', 'Eiger Express to Grindelwald', 'Lauterbrunnen valley', 'Glacier 3000 and the Peak Walk', 'Golden Pass panoramic train', 'Chillon Castle', 'Lake Geneva and the Jet d’Eau', 'Milan Cathedral'],
    days=[
      _d('Kuala Lumpur to Milan', '', ['Overnight flight to Milan.']),
      _d('Milan, Lugano, Interlaken', 'L, D', ['Shopping at Fox Town, the outlet village on the Swiss border.', '<b>Lake Lugano.</b>', 'Over the Alps to Interlaken.'], 'Interlaken'),
      _d('Jungfraujoch', 'B, L', ['<b>Lauterbrunnen</b> and Staubbach Falls, in the valley of 72 waterfalls.', 'Cogwheel train up to the <b>Jungfraujoch</b> at 3,454m: the Sphinx terrace above the Aletsch Glacier, the Ice Palace and Alpine Sensation.', 'Down by the <b>Eiger Express</b> gondola to Grindelwald.'], 'Interlaken'),
      _d('Glacier 3000', 'B, D', ['Cable car from Les Diablerets up to <b>Glacier 3000</b>.', 'The <b>Peak Walk by Tissot</b>, a suspension bridge strung between two summits, then the Ice Express chairlift, sledging and a glacier walk.', '<b>Optional:</b> the Alpine Coaster, in summer.'], 'Leysin', note='Activities on the glacier depend on the weather on the day.'),
      _d('Golden Pass, Montreux, Lausanne, Geneva', 'B, L, D', ['The <b>Golden Pass</b> panoramic train from Château-d’Oex towards Montreux.', '<b>Chillon Castle</b> on Lake Geneva, and the Freddie Mercury statue in Montreux.', 'Vevey’s giant fork and Charlie Chaplin statue, and Lausanne’s Olympic Park and Ouchy lakefront.'], 'Geneva or Annemasse'),
      _d('Geneva to Genoa', 'B, D', ['<b>Geneva.</b> The Jet d’Eau and the Flower Clock.', '<b>Genoa.</b> Piazza Matteotti, the Palazzo Ducale, San Lorenzo Cathedral and the palaces of Via Garibaldi.'], 'Genoa'),
      _d('Genoa to Milan', 'B, D', ['Shopping at Serravalle Designer Outlet.'], 'Milan'),
      _d('Milan', 'B, D', ['<b>Sforza Castle</b> and <b>Milan Cathedral</b>.', 'The Galleria Vittorio Emanuele II, one of the world’s oldest shopping arcades.'], 'Milan'),
      _d('Milan to Kuala Lumpur', 'B', ['Free until the flight home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Seven nights in 3 and 4-star hotels or similar: Interlaken 2, Leysin 1, Geneva or Annemasse 1, Genoa 1, Milan 2', '7 hot breakfasts, 3 lunches and 6 dinners, Western and Chinese, with a Swiss cheese fondue', 'Jungfraujoch by cogwheel train and Eiger Express, Glacier 3000 with the Peak Walk, the Golden Pass train and Chillon Castle'],
    excluded=['Alpine Coaster at Glacier 3000 (optional)', 'Travel insurance and tipping, unless stated', 'Meals not listed'],
  ),
  dict(slug='gd-egypt', page='tour-gd-egypt.html', title='The Grand Egypt Tour', region='Egypt', duration='9 days, 7 nights', hero='gd-egypt-hero.jpg', hero_alt='The rock-cut temple of Ramesses II at Abu Simbel',
    seo='Egypt Tour Package from Malaysia: Pyramids, Nile Cruise and Abu Simbel',
    line='The Pyramids, a Nile cruise from Aswan to Luxor, and Alexandria.', hotels='5-star hotels and Nile cruise',
    head='Egypt end to end, with three nights on the Nile.',
    lead='The Pyramids, the Sphinx and the Grand Egyptian Museum at Giza, a flight south to Aswan and three nights cruising the Nile by way of Abu Simbel, Kom Ombo and Edfu to Luxor and the Valley of the Kings, finishing on the Mediterranean in Alexandria.',
    highlights=['Pyramids of Giza and the Sphinx', 'Grand Egyptian Museum', 'Abu Simbel', 'Three nights on a 5-star Nile cruise', 'Felucca sail at Aswan', 'Karnak and Luxor temples', 'Valley of the Kings', 'Qaitbay Citadel, Alexandria'],
    days=[
      _d('Kuala Lumpur to Cairo', 'L, D', ['Fly to Cairo.', 'The <b>Citadel of Saladin</b> and the Mosque of Muhammad Ali.', '<b>Khan el-Khalili</b>, Cairo’s great bazaar.'], 'Cairo'),
      _d('Giza, then fly to Aswan', 'B, L, D', ['<b>The Pyramids of Giza and the Sphinx</b>, with a camel ride.', 'The step pyramid at Saqqara, and Memphis.', '<b>The Grand Egyptian Museum</b>, the new home of Egypt’s antiquities beside the Pyramids.', 'Fly to Aswan.'], 'Aswan'),
      _d('Aswan, board the Nile cruise', 'B, L, D', ['The <b>High Dam</b> and the Unfinished Obelisk.', 'Board the cruise ship, and sail around Elephantine Island by <b>felucca</b>.', '<b>Optional:</b> a Nubian village, and a sound and light show.'], 'Nile cruise'),
      _d('Abu Simbel, Kom Ombo, Edfu', 'B, L, D', ['An early start for <b>Abu Simbel</b>, the rock temples of Ramesses II.', 'Sail to <b>Kom Ombo</b> and its double temple, then on to Edfu.'], 'Nile cruise'),
      _d('Edfu, Esna, Luxor', 'B, L, D', ['By horse carriage to the <b>Temple of Horus</b> at Edfu, one of the best preserved in Egypt.', 'Through the Esna lock to Luxor.', 'A galabeya party on board.'], 'Nile cruise'),
      _d('Luxor, then fly to Cairo', 'B, L, D', ['The Colossi of Memnon.', '<b>The Valley of the Kings</b> and the Temple of Hatshepsut.', '<b>Karnak</b> and <b>Luxor Temple</b>.', '<b>Optional:</b> a sunrise hot-air balloon flight.', 'Fly back to Cairo.'], 'Cairo'),
      _d('Alexandria', 'B, L, D', ['The Catacombs of Kom el Shoqafa, Pompey’s Pillar and the Roman amphitheatre.', '<b>Qaitbay Citadel</b>, on the site of the ancient Lighthouse of Alexandria.', 'Back to Cairo.'], 'Cairo'),
      _d('Cairo to Kuala Lumpur', 'B', ['Fly home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur, and domestic flights from Cairo to Aswan and Luxor to Cairo', 'Seven nights: Cairo 3 and Aswan 1 in 5-star hotels, and three nights on a 5-star Nile cruise', '7 breakfasts, 7 lunches and 7 dinners', 'Entrance to the Pyramids area, the Grand Egyptian Museum, Abu Simbel, the Valley of the Kings, and Karnak and Luxor temples', 'Camel ride at Giza, felucca sail at Aswan and horse carriage at Edfu'],
    excluded=['Entry inside the Pyramids', 'Optional extras: Nubian village, sound and light show and hot-air balloon', 'Travel insurance and tipping, unless stated'],
    notes='Malaysian passport holders can currently enter Egypt visa-free or with a visa on arrival for up to 15 days; we confirm the rule when you book.',
  ),
  dict(slug='ap-zhangjiajie', page='tour-ap-zhangjiajie.html', brand='Apple Vacations', title='Zhangjiajie, Tianmen Mountain &amp; Phoenix Town', region='China', duration='9 days, 6 nights', hero='ap-zhangjiajie-hero.jpg', hero_alt='Sandstone pillars rising from the forest in Zhangjiajie', c1='#3d6b4f', c2='#10241a',
    seo='Zhangjiajie Tour Package from Malaysia: Tianmen Mountain, Glass Bridge and Phoenix Town',
    line='Sandstone pillars, a glass bridge over the canyon, and Phoenix Ancient Town by night.', hotels='Hilton Garden Inn and Park Hyatt, or similar',
    head='Hunan’s mountains, at an unhurried pace.',
    lead='Zhangjiajie’s forest of sandstone pillars, the glass bridge over the Grand Canyon, the cable car and cliff walkway of Tianmen Mountain, the waterfall town of Furong and the riverside lanes of Phoenix, with a VIP coach throughout and the high-speed train back to Changsha.',
    highlights=['Zhangjiajie National Forest Park', 'Bailong Elevator, VIP lane', 'Grand Canyon glass bridge', 'Tianmen Mountain cable car', 'Tianmen cliff glass walkway', 'Furong Town by its waterfall', 'Phoenix Ancient Town at night', 'High-speed train to Changsha'],
    days=[
      _d('Kuala Lumpur to Changsha', '', ['Fly to Changsha.'], 'Changsha, or on the overnight flight'),
      _d('Changsha, Changde, Zhangjiajie', 'L, D', ['<b>Daxiaohe Street</b> in Changde, an old-style quarter of folk customs and street food.', 'On to Zhangjiajie.'], 'Zhangjiajie, Wulingyuan'),
      _d('Zhangjiajie National Forest Park', 'B, L, D', ['<b>Zhangjiajie National Forest Park</b> and its towering sandstone pillars: up the Bailong Elevator by the VIP lane, Yuanjiajie and the natural stone bridge, the Ten-Mile Gallery by train and Golden Whip Stream.', 'A coach for the group alone inside the park.'], 'Zhangjiajie, Wulingyuan'),
      _d('The Grand Canyon glass bridge', 'B, L, D', ['<b>Zhangjiajie Grand Canyon</b> and its glass bridge, with a zipline, a slide and a boat ride.', 'Make your own sandstone painting.', 'The <b>72 Tujia Stilted Buildings</b> lit up at night, and the Tianmen Fox Fairy show, staged on the mountain itself.'], 'Zhangjiajie, near Tianmen Mountain', note='From 8 December to 8 March the Fox Fairy show is replaced by the Charming Xiangxi show.'),
      _d('Tianmen Mountain and Furong Town', 'B, L, D', ['<b>Tianmen Mountain</b>: the long cable car up by the VIP lane, the glass walkway on the cliff, the view down the 99-bend road and Tianmen Cave.', '<b>Furong Town</b>, the thousand-year-old town of stilted houses beside a waterfall.'], 'Furong Town', note='From December to February the Tianmen Cave escalator and shuttle are closed.'),
      _d('Phoenix Ancient Town', 'B, D', ['<b>Phoenix Ancient Town</b>: a boat on the Tuo River, the Hongqiao bridge, the stilted houses, and the old town lit up at night.', 'Dress in Miao costume for a short drone video, then a drink at the hotel bar.'], 'Fenghuang'),
      _d('High-speed train to Changsha', 'B, L', ['Three hours to Changsha by high-speed train, with your luggage sent on ahead.'], 'Changsha, Park Hyatt or similar'),
      _d('Changsha, fly home', 'B, D', ['<b>Orange Isle</b> on the Xiang River, by electric cart.', 'Fly home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Six nights in hotels including the Hilton Garden Inn in Zhangjiajie and the Park Hyatt in Changsha, or similar', 'Most meals, including a Tujia lei cha banquet, a firewood-fish banquet and Hunan cooking', 'Glass bridge, Tianmen Mountain cable car and glass walkway, Phoenix Town and all listed entrances', 'A 1+1 VIP coach throughout, and a charter coach inside the scenic areas', 'High-speed train with luggage forwarding'],
    excluded=['Travel insurance and tipping, unless stated', 'Meals not listed'],
    notes='Led by a Mandarin-speaking guide. The glass bridge and cable car depend on the weather; closed sections are refunded or replaced.',
  ),
  dict(slug='ap-dongbei', page='tour-ap-dongbei.html', brand='Apple Vacations', title='Snowy Dongbei: Changbai Mountain &amp; Harbin', region='China', duration='8 days, 7 nights', hero='ap-dongbei-hero.jpg', hero_alt='Ice castles at Harbin Ice and Snow World', c1='#5d7fa8', c2='#142236',
    seo='Harbin Tour Package from Malaysia: Ice and Snow World and Changbai Mountain',
    line='Rime forests, hot springs in the snow and the ice city of Harbin.', hotels='Including the Shangri-La Changchun and a hot-spring resort',
    head='China’s far north, at its whitest.',
    lead='Frost-coated trees along the Songhua River, two nights at a hot-spring resort below Changbai Mountain, the snow villages of Mojie and Xueling, the frozen falls of Jingpo Lake, then Harbin’s Ice and Snow World and its snow sculptures.',
    highlights=['Harbin Ice and Snow World', 'Sun Island Snow Sculpture Expo', 'St Sophia Cathedral and Central Street', 'Ashihada Rime Corridor', 'Changbai Mountain', 'Hot springs in the snow', 'Xueling snow village', 'Sleigh rides, reindeer and winter rafting'],
    days=[
      _d('Kuala Lumpur to Changchun', '', ['Fly to Changchun, with one connection.'], 'Changchun, Shangri-La or similar'),
      _d('Changchun to Jilin', 'B, L, D', ['The old Changchun Film Studio, now a museum.', 'A stop for winter clothing, if you need warmer layers.'], 'Jilin'),
      _d('Rime corridor and Changbai Mountain', 'B, L, D', ['The <b>Ashihada Rime Corridor</b>, trees coated in frost along the Songhua River.', 'The Beauty Pine sky bridge, then hot springs in the snow at the resort.'], 'Changbai Mountain, hot-spring resort'),
      _d('Changbai Mountain', 'B, L, D', ['The north slope of <b>Changbai Mountain</b>, in deep winter snow.'], 'Changbai Mountain, hot-spring resort'),
      _d('Mojie and Xueling', 'B, L, D', ['<b>Mojie</b>, a valley of rime and icefalls.', '<b>Xueling</b>, a village buried in snow like a castle of white.', 'On to Dunhua.'], 'Dunhua'),
      _d('Jingpo Lake to Harbin', 'B, L, D', ['<b>Jingpo Lake</b> and its frozen waterfall.', '<b>Harbin Ice and Snow World</b>, the ice city lit up after dark.'], 'Harbin', meal='Jingpo Lake fish feast'),
      _d('Harbin', 'B, D', ['The <b>Sun Island Snow Sculpture Expo</b>.', 'The Harbin Snowman, <b>St Sophia Cathedral</b> and Central Street.'], 'Harbin'),
      _d('Harbin to Kuala Lumpur', 'B', ['Fly home, with one connection.']),
    ],
    included=['Return flights from Kuala Lumpur, with one connection each way', 'Seven nights: Changchun 1, Jilin 1, Changbai Mountain 2 (hot-spring resort), Dunhua 1, Harbin 2', 'Most meals, including the ice-palace steamboat at the Shangri-La, Dongbei stews and ginseng chicken pot', 'Electric cars in the scenic areas, and a hand warmer for everyone'],
    excluded=['Travel insurance and tipping, unless stated', 'Meals not listed'],
    notes='Expect temperatures well below freezing. If you have no winter wear, there is a stop to buy it on day 2.',
  ),
  dict(slug='ap-spain-portugal', page='tour-ap-spain-portugal.html', brand='Apple Vacations', title='Spain &amp; Portugal', region='Europe', duration='12 days, 9 nights', hero='ap-spain-portugal-hero.jpg', hero_alt='Porto and the Luís I Bridge over the Douro', c1='#b5652e', c2='#3a1a0a',
    seo='Spain and Portugal Tour Package from Malaysia: Lisbon, Seville and Barcelona',
    line='From the port cellars of Porto to Gaudí’s Barcelona.', hotels='4-star',
    head='The Iberian Peninsula, end to end.',
    lead='Port wine and the Douro in Porto, a chartered tram in Lisbon, Roman Évora, Seville’s cathedral, Ronda on its gorge, Córdoba’s Mezquita, Toledo and Madrid, then the AVE train to Barcelona for Park Güell and the Sagrada Família.',
    highlights=['Douro river boat ride, Porto', 'Port wine tasting', 'Jerónimos Monastery, Lisbon', 'Seville Cathedral and the Giralda', 'Ronda’s Puente Nuevo', 'The Mezquita, Córdoba', 'Royal Palace, Madrid', 'Sagrada Família and Park Güell'],
    days=[
      _d('Kuala Lumpur to Porto', '', ['Overnight flight to Porto.']),
      _d('Porto', 'L, D', ['Porto Cathedral and the Ribeira riverfront, a <b>boat on the Douro</b> and the Luís I Bridge.', 'A port cellar visit and tasting in Vila Nova de Gaia.'], 'Porto'),
      _d('Porto to Lisbon', 'B, L, D', ['To Lisbon, and a vintage <b>tram</b> chartered for the group.', 'Rossio Square.'], 'Lisbon'),
      _d('Lisbon to Évora', 'B, L, D', ['<b>Jerónimos Monastery</b>, Belém Tower and the Monument to the Discoveries.', '<b>Évora</b>: the Roman temple, the cathedral and the old university.'], 'Évora'),
      _d('Évora to Seville', 'B, L, D', ['<b>Seville Cathedral</b> and the Giralda, Plaza de España and the Santa Cruz quarter.'], 'Seville'),
      _d('Ronda to Córdoba', 'B, L, D', ['<b>Ronda</b> on its gorge: the Puente Nuevo and the old bullring.', 'On to Córdoba.'], 'Córdoba'),
      _d('Córdoba to Madrid', 'B, L, D', ['<b>The Mezquita</b>, the Alcázar of the Christian Monarchs and the Roman bridge.', 'On to Madrid.'], 'Madrid'),
      _d('Toledo and Madrid', 'B, D', ['<b>Toledo</b> and the Church of Santo Tomé.', 'The Santiago Bernabéu stadium and El Corte Inglés.'], 'Madrid', meal='Flamenco dinner and show'),
      _d('Madrid to Barcelona', 'B, D', ['The <b>Royal Palace</b> and Plaza de España.', 'High-speed AVE train to Barcelona.'], 'Barcelona'),
      _d('Barcelona', 'B, D', ['Montjuïc and the Olympic Park, and <b>Park Güell</b>.', 'Shopping at La Roca Village.'], 'Barcelona'),
      _d('Barcelona, fly home', 'B', ['<b>The Sagrada Família</b> and Casa Milà.', 'La Rambla and Plaça de Catalunya, then the flight home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur, into Porto and home from Barcelona', 'Nine nights in 4-star hotels or similar: Porto 1, Lisbon 1, Évora 1, Seville 1, Córdoba 1, Madrid 2, Barcelona 2', 'Most meals, including a seafood platter, bacalhau, paella, Segovia-style suckling pig, tapas and a flamenco dinner', 'Entrance to the Sagrada Família, Casa Milà, Park Güell, the Mezquita, the Royal Palace and Jerónimos Monastery', 'High-speed AVE train from Madrid to Barcelona'],
    excluded=['Travel insurance and tipping, unless stated', 'Meals not listed'],
  ),
  dict(slug='ap-morocco', page='tour-ap-morocco.html', brand='Apple Vacations', title='Morocco: Chefchaouen, Fez &amp; the Sahara', region='Africa', duration='11 days, 8 nights', hero='ap-morocco-hero.jpg', hero_alt='A camel caravan crossing the Sahara dunes at Merzouga', c1='#b5652e', c2='#3a1a0a',
    seo='Morocco Tour Package from Malaysia: Chefchaouen, Fez, Sahara and Marrakesh',
    line='Blue lanes, old medinas, a ride into the dunes and the souks of Marrakesh.', hotels='5-star hotels, and a riad in Chefchaouen',
    head='From the Atlantic coast to the edge of the Sahara.',
    lead='Casablanca’s great mosque, royal Rabat, the blue-washed lanes of Chefchaouen, the medina and tanneries of Fez, over the Atlas to the Sahara for a 4WD and camel ride at Merzouga, then the kasbahs of the south and two nights in Marrakesh.',
    highlights=['Hassan II Mosque, Casablanca', 'Kasbah of the Udayas, Rabat', 'The blue town of Chefchaouen', 'Fez medina and leather tanneries', '4WD and camel ride in the Sahara', 'Todra Gorge', 'Aït Benhaddou kasbah', 'Bahia Palace and Majorelle Garden, Marrakesh'],
    days=[
      _d('Kuala Lumpur to Casablanca', '', ['Overnight flight to Casablanca.']),
      _d('Casablanca', 'D', ['Arrive in Casablanca and an introduction to the city on the Atlantic.'], 'Casablanca, 5-star'),
      _d('Casablanca to Rabat', 'B, L, D', ['Inside the <b>Hassan II Mosque</b>, built out over the ocean.', 'On to Rabat: the <b>Hassan Tower</b> and the blue-and-white lanes of the <b>Kasbah of the Udayas</b>.'], 'Rabat, 5-star'),
      _d('Rabat to Chefchaouen', 'B, L, D', ['Into the Rif mountains to <b>Chefchaouen</b>, the town painted in every shade of blue.'], 'Chefchaouen, riad'),
      _d('Chefchaouen to Fez', 'B, L, D', ['<b>Fez</b>: the old medina, a maze of lanes and workshops, and the leather tanneries from above.'], 'Fez, 5-star'),
      _d('Over the Atlas to Erfoud', 'B, L, D', ['<b>Ifrane</b>, the alpine-style town in the Middle Atlas, then over the Tizi n’Talghamt pass to Erfoud on the edge of the desert.'], 'Erfoud, 5-star'),
      _d('The Sahara and Todra Gorge', 'B, L, D', ['A <b>4WD ride into the dunes at Merzouga</b>, and a camel ride across the sand.', '<b>Todra Gorge</b>, its walls rising straight from the river, then on to Ouarzazate.'], 'Ouarzazate'),
      _d('Ouarzazate to Marrakesh', 'B, L, D', ['The Atlas Film Studios, and the fortified village of <b>Aït Benhaddou</b>.', 'Over the High Atlas to Marrakesh.'], 'Marrakesh, 5-star'),
      _d('Marrakesh', 'B, L, D', ['The <b>Bahia Palace</b> and the blue <b>Majorelle Garden</b>.', 'The souks and the square of Jemaa el-Fna.'], 'Marrakesh, 5-star'),
      _d('Marrakesh, fly home', 'B', ['Fly home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Eight nights: Casablanca 1, Rabat 1, Chefchaouen 1 (riad), Fez 1, Erfoud 1, Ouarzazate 1, Marrakesh 2, mostly in 5-star hotels', 'Most meals, including tagine and Moroccan kebabs, and a farewell dinner at Rick’s Café in Casablanca', 'Hassan II Mosque, Fez medina, 4WD desert safari and camel ride, Aït Benhaddou, Bahia Palace and Majorelle Garden'],
    excluded=['Travel insurance and tipping, unless stated', 'Meals not listed'],
    notes='Malaysian passport holders can visit Morocco visa-free for up to 90 days; we confirm the current rule when you book.',
  ),
  dict(slug='ap-finland', page='tour-ap-finland.html', brand='Apple Vacations', title='Finnish Lapland &amp; the Northern Lights', region='Europe', duration='10 days, 7 nights', hero='ap-finland-hero.jpg', hero_alt='A reindeer sleigh in a snowy Lapland forest', c1='#2e5d6e', c2='#081a22',
    seo='Finland Northern Lights Tour from Malaysia: Lapland, Huskies and Santa Claus Village',
    line='Huskies, reindeer, king crab in Norway and the Northern Lights.', hotels='Lapland hotels, including Santa’s Hotels',
    head='A week above the Arctic Circle.',
    lead='Rovaniemi and the Arctic Circle, an amethyst mine on a snowy fell, a Northern Lights evening at Inari, a king crab safari over the border in Norway, then huskies and Santa Claus Village before flying home.',
    highlights=['Northern Lights evening tour', 'Husky safari', 'Snowmobile and reindeer ride', 'Arctic king crab safari, Norway', 'Santa Claus Village and the Arctic Circle', 'Amethyst mine at Luosto', 'Arktikum museum', 'Nordic skiing'],
    days=[
      _d('Kuala Lumpur to Rovaniemi', '', ['Overnight flight to Rovaniemi.']),
      _d('Rovaniemi', 'D', ['The <b>Arktikum</b>, Lapland’s museum of the Arctic.'], 'Rovaniemi'),
      _d('Luosto to Saariselkä', 'B, L, D', ['Up the fell at Luosto to Europe’s only working <b>amethyst mine</b>, and dig for a stone of your own.'], 'Saariselkä'),
      _d('Inari and the Northern Lights', 'B, L, D', ['A <b>snowmobile</b> ride and a reindeer sleigh.', 'An evening <b>Northern Lights</b> tour.'], 'Inari'),
      _d('King crab in Norway', 'B, L, D', ['Over the border to Kirkenes for an <b>Arctic king crab safari</b>.'], 'Kirkenes, Norway', meal='King crab'),
      _d('Back to Finland', 'B, L, D', ['Back across the border, with Nordic skiing on the way.'], 'Saariselkä'),
      _d('Huskies and Santa Claus Village', 'B, L, D', ['A <b>husky safari</b>.', '<b>Santa Claus Village</b> on the Arctic Circle, with your crossing certificate.'], 'Rovaniemi'),
      _d('Rovaniemi', 'B, D', ['A day around Rovaniemi; November departures visit Ranua Wildlife Park.'], 'Rovaniemi'),
      _d('Rovaniemi to Kuala Lumpur', 'B', ['Fly home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur', 'Seven nights: Rovaniemi 3, Saariselkä 2, Inari 1, Kirkenes 1', 'Most meals, including a Lappish menu, reindeer and king crab', 'Husky safari, snowmobile and reindeer rides, king crab safari, Northern Lights tour, amethyst mine and Arctic Circle certificate'],
    excluded=['Travel insurance and tipping, unless stated', 'Meals not listed'],
    notes='Arctic weather sets the order of activities. The Northern Lights are never guaranteed, but December to February gives the longest, darkest nights.',
  ),
  dict(slug='ap-australia', page='tour-ap-australia.html', brand='Apple Vacations', title='Sydney &amp; Melbourne', region='Australia', duration='9 days, 6 nights', hero='ap-australia-hero.jpg', hero_alt='Sydney Opera House and the city skyline', c1='#2f78a0', c2='#0c2333',
    seo='Australia Tour Package from Malaysia: Sydney, Blue Mountains and Melbourne',
    line='The harbour, the Blue Mountains, the Great Ocean Road and the Penguin Parade.', hotels='4-star',
    head='Australia’s two great cities, and the coast between.',
    lead='Three nights in Sydney with a harbour cruise, the Blue Mountains and a free day, then Melbourne: the Great Ocean Road, Phillip Island’s Penguin Parade, the Puffing Billy steam train and the city’s laneways.',
    highlights=['Sydney Opera House', 'Sydney Harbour cruise', 'Blue Mountains Scenic World', 'Great Ocean Road and the Twelve Apostles', 'Penguin Parade, Phillip Island', 'Puffing Billy steam train', 'Melbourne’s laneways', 'Eureka Skydeck'],
    days=[
      _d('Kuala Lumpur to Sydney', '', ['Overnight flight to Sydney.']),
      _d('Sydney Harbour', 'L, D', ['Mrs Macquarie’s Chair and the <b>Sydney Opera House</b>.', 'A <b>Sydney Harbour cruise</b>.'], 'Sydney'),
      _d('The Blue Mountains', 'B, L, D', ['Calmsley Hill City Farm, to meet and feed the animals.', '<b>The Blue Mountains</b>: the Scenic World railway, cableway and skyway, and the Three Sisters from Echo Point.'], 'Sydney'),
      _d('Sydney at leisure', 'B', ['A free day in Sydney. Tell us before you go if you would like anything booked.'], 'Sydney'),
      _d('Sydney to Melbourne', 'B, D', ['The Rocks, and lunch at the <b>Sydney Fish Market</b> (own expense).', 'Evening flight to Melbourne.'], 'Melbourne'),
      _d('The Great Ocean Road', 'B, L, D', ['<b>The Great Ocean Road</b> and the Twelve Apostles, from September to May.', 'From June to August, <b>Sovereign Hill</b> and its gold-mine tour instead.'], 'Melbourne'),
      _d('Phillip Island', 'B, L, D', ['Wine tasting and lunch at a winery, and a chocolate stop.', 'The <b>Penguin Parade</b> from the Penguins Plus platform, as the little penguins come ashore at dusk.'], 'Melbourne', meal='Winery lunch'),
      _d('Melbourne, fly home', 'B, L, D', ['The <b>Puffing Billy</b> steam train through the Dandenong Ranges, and Brighton Beach.', 'Federation Square, Flinders Street Station, the laneways and arcades, and a flat white.', '<b>Eureka Skydeck</b>, with The Edge.', 'Late flight home.']),
      _d('Arrive in Kuala Lumpur', '', ['Welcome home.']),
    ],
    included=['Return flights from Kuala Lumpur, and the flight from Sydney to Melbourne', 'Six nights in 4-star hotels or similar: Sydney 3, Melbourne 3', 'Most meals, including dinner on the harbour cruise, a winery lunch and an Asian dinner with lobster', 'Harbour cruise, Scenic World, Penguins Plus, Puffing Billy and Eureka Skydeck with The Edge'],
    excluded=['Australian ETA, travel insurance and tipping, unless stated', 'Meals not listed'],
  ),
  # YSL's own tour, from YSL's itinerary "Golden Peak, Hidden Lake" (金山秘湖), built with the partner-tour template
  dict(slug='yunnan', page='tour-yunnan.html', brand='YSL Travel &amp; Tours', zh='金山秘湖', title='Golden Peak, Hidden Lake', region='China', duration='9 days, 7 nights', hero='yn-hero.jpg', hero_alt='Lugu Lake and its islands under a clear sky', c1='#6b4a1e', c2='#1e1408',
    seo='Yunnan Tour Package from Malaysia: Lugu Lake, Shangri-La and Meili Snow Mountain',
    line='From the golden dawn on Meili to the still waters of Lugu Lake.', hotels='Comfortable hotels and lakeside guesthouses',
    head='Nine unhurried days where snow country meets the water.',
    lead='Dali on the shore of Erhai, Lugu Lake and the Mosuo, the old town of Lijiang, Shangri-La’s great prayer wheel, sunrise on Meili Snow Mountain and the hidden valley of Balagezong, returning to Kunming by high-speed train.',
    highlights=['Dali Ancient City', 'Lugu Lake by dugout boat', 'Lijiang Old Town, a UNESCO site', 'Dukezong and the giant prayer wheel', 'Napa Lake in Tibetan dress', 'First Bend of the Jinsha River', 'Sunrise on Meili Snow Mountain', 'Balagezong Grand Canyon'],
    days=[
      _d('Kuala Lumpur to Kunming', '', ['Meet at Subang Airport (Sultan Abdul Aziz Shah, SkyPark Terminal), where our tour leader helps you check in for the evening flight to Kunming, where your Yunnan guide meets you with flowers and takes you to the hotel.'], 'Kunming, near the airport'),
      _d('Kunming to Dali', 'B, L, D', ['About four and a half hours by expressway to Dali.', 'An evening in the lantern-lit lanes of <b>Dali Ancient City</b> and Foreigner Street.', '<b>Optional:</b> the Erhai Lake ecological corridor, with a music car-cruise, Golden Flower dancing and travel photos.'], 'Dali Old Town', meal='Bai heritage banquet'),
      _d('Dali to Lugu Lake', 'B, L, D', ['A scenic drive of about four and a half hours to <b>Lugu Lake</b>, the “Highland Pearl”.', 'The lake viewing platform, a coach loop past Lovers’ Beach, and a bonfire party under the stars.'], 'Lugu Lake, boutique guesthouse', meal='Wild-mushroom hot pot'),
      _d('Lugu Lake to Lijiang', 'B, L, D', ['Sunrise over the lake if the weather allows, then a traditional dugout boat to Liwubi Island and a visit to a Mosuo weaving house.', '<b>Lijiang Old Town</b>, the UNESCO-listed Naxi town of canals and cobbles, and Sifang Street.'], 'Lijiang, near the old town', meal='Lijiang imperial feast, in costume, with a show'),
      _d('Lijiang to Shangri-La', 'B, L, D', ['About three hours up to the plateau.', 'The Dongba Secret Realm, with its eco-shuttle and high-altitude skywalk (Lijiang’s Flower Valley from June to October).', '<b>Dukezong Ancient City</b>, and the world’s largest prayer wheel in Guishan Park.'], 'Shangri-La'),
      _d('Shangri-La to Deqin', 'B, L, D', ['<b>Napa Lake</b>, with photos in Tibetan dress (free) beside the great prayer banner; horse riding at own expense.', 'The <b>First Bend of the Jinsha River</b> and the Wunongding viewing platform. From May to October the alpine meadows are in flower.'], 'Deqin, facing Meili, with oxygen supply'),
      _d('Meili, Balagezong, Shangri-La', 'B, L, D', ['An early start at Feilai Temple for <b>sunrise on Meili Snow Mountain</b>, when the first light turns the peaks gold.', 'Down into the <b>Balagezong Grand Canyon</b> by eco-shuttle: Bala Village, a thousand-year-old bodhi tree, the Echo Wall skywalk and a glass platform on the cliff edge.', 'Back to Shangri-La.'], 'Shangri-La', meal='Tibetan-style dinner'),
      _d('High-speed train to Kunming', 'B, L, D', ['The early high-speed train back to Kunming, about four hours, with your luggage sent by road.', '<b>Dounan Flower Market</b>, the largest in Asia, then Nanping Street and the Jinma Biji archways.', 'Late-night flight home.'], meal='Crossing-the-bridge rice noodles'),
      _d('Arrive in Kuala Lumpur', '', ['Home in the early morning.']),
    ],
    included=['Direct return flights with Batik Air between Subang and Kunming', 'Seven nights: Kunming 1, Dali 1, Lugu Lake 1, Lijiang 1, Shangri-La 2, Deqin 1', 'Daily breakfast, and lunch and dinner from day 2 to day 8, including a Bai banquet, wild-mushroom hot pot and the Lijiang imperial feast', 'Dugout boat on Lugu Lake, Dongba Secret Realm and Balagezong eco-shuttles, and the high-speed train to Kunming', 'Tour leader from Kuala Lumpur'],
    excluded=['Optional extras: the Erhai corridor experience and horse riding at Napa Lake', 'Travel insurance (strongly recommended) and tipping, unless stated'],
    notes='Meili’s golden sunrise depends on clear skies; we wait for it, but nobody can promise it. Shangri-La and Deqin are above 3,000m, so take it slowly on arrival.',
  ),
]

# Golden Destinations departure dates, matched from gd.my on 1 November 2026 (prices deliberately left out).
# slug: (GD tour code, dates); the last six were added later, checked 1 November 2026. New Zealand: NZW (Dec 2026) and NZW(R) (2027) run the same itinerary.
# To refresh, re-check https://www.gd.my/web/itinerary/<CODE>.
GD_DATES = {
    'gd-europe-legend': ('10EPP', '''
        2027-02-10 2027-02-24
        '''.split()),
    'gd-hokkaido': ('JCS-12', '''
        2026-12-22 2027-01-06 2027-01-12 2027-01-13 2027-01-26 2027-01-27 2027-02-24 2027-03-03
        2027-03-17 2027-03-23
        '''.split()),
    'gd-turkiye': ('9XCA-1', '''
        2026-11-26 2026-12-10 2026-12-24 2027-01-14 2027-01-16 2027-01-21 2027-01-22 2027-01-23
        2027-02-01 2027-02-03 2027-02-04 2027-02-07 2027-02-08 2027-02-11 2027-02-13 2027-02-16
        2027-02-18 2027-02-20 2027-02-24 2027-03-02 2027-03-03 2027-03-04 2027-03-06 2027-03-09
        2027-03-16 2027-03-18 2027-03-23 2027-03-25 2027-03-30 2027-04-01 2027-04-06 2027-04-08
        2027-04-13 2027-04-15 2027-04-20 2027-04-22 2027-04-27 2027-04-29 2027-05-04 2027-05-06
        2027-05-11 2027-05-13 2027-05-14 2027-05-16 2027-05-17 2027-05-20 2027-05-25 2027-05-27
        2027-06-01 2027-06-03 2027-06-06 2027-06-10 2027-06-17 2027-06-24 2027-07-01 2027-07-08
        2027-07-15 2027-07-22 2027-07-29 2027-08-05 2027-08-12 2027-08-19
        '''.split()),
    'gd-eastern-europe': ('9EBP', '''
        2027-02-18 2027-03-25 2027-04-11 2027-04-25 2027-05-13 2027-05-27
        '''.split()),
    'gd-new-zealand': ('NZW / NZW(R)', '''
        2026-12-09 2027-05-19 2027-06-03
        '''.split()),
    'gd-south-africa': ('11XSA', '''
        2027-01-12 2027-02-16 2027-03-16 2027-04-20 2027-05-26 2027-06-15 2027-07-06 2027-07-27
        2027-08-10 2027-08-21 2027-09-14
        '''.split()),
    'gd-japan': ('JDR-21', '''
        2026-12-01 2026-12-22 2027-01-05 2027-01-26 2027-01-27 2027-02-02 2027-02-04 2027-02-09
        2027-02-21 2027-02-23 2027-03-09 2027-03-16 2027-03-30 2027-04-06 2027-04-15 2027-04-29
        2027-05-04 2027-05-13 2027-05-25 2027-05-26 2027-05-29 2027-06-02
        '''.split()),
    'gd-korea': ('DZP-10', '''
        2026-11-25 2026-11-28 2027-02-26 2027-03-05 2027-03-06 2027-03-07 2027-03-08 2027-03-10
        2027-03-11 2027-03-12 2027-03-20 2027-03-24 2027-03-27 2027-03-28 2027-04-03 2027-04-04
        2027-04-07 2027-04-11 2027-04-14 2027-04-17 2027-04-18 2027-04-20 2027-04-21 2027-04-25
        2027-04-30 2027-05-06 2027-05-09 2027-05-13 2027-05-16 2027-05-19 2027-05-20 2027-05-23
        2027-05-24 2027-05-27 2027-05-28 2027-06-02 2027-06-09 2027-06-18 2027-07-02 2027-07-17
        '''.split()),
    'gd-taiwan': ('WLB-11', '''
        2026-12-01 2026-12-08 2026-12-15 2026-12-23 2026-12-29 2026-12-30 2027-02-17 2027-02-23
        2027-02-24 2027-03-17 2027-04-07 2027-04-28 2027-05-18 2027-05-28 2027-06-03 2027-06-30
        2027-07-21 2027-08-04
        '''.split()),
    'gd-vietnam': ('VDG-8U', '''
        2026-11-25 2026-11-27 2026-12-05 2026-12-07 2026-12-09 2026-12-10 2026-12-14 2026-12-16
        2026-12-20 2026-12-21 2026-12-27 2026-12-29 2026-12-30 2027-01-13 2027-01-20 2027-01-22
        2027-01-28 2027-02-03 2027-02-04 2027-02-05 2027-02-09 2027-02-10 2027-02-24 2027-03-03
        2027-03-08 2027-03-09 2027-03-27 2027-04-09 2027-04-23 2027-05-13 2027-05-20 2027-06-03
        '''.split()),
    'gd-switzerland-italy': ('10ESI', '''
        2026-12-08 2026-12-15 2027-02-07 2027-02-22 2027-02-25 2027-03-07 2027-03-08 2027-03-16
        2027-03-30 2027-04-06 2027-04-12 2027-04-22 2027-05-04 2027-05-14 2027-05-17 2027-05-29
        '''.split()),
    'gd-egypt': ('9XCG', '''
        2027-01-15 2027-01-22 2027-02-01 2027-02-02 2027-02-03 2027-02-09 2027-02-21 2027-03-03
        2027-03-07 2027-03-17 2027-04-11 2027-04-18 2027-04-25
        '''.split()),
    # Apple Vacations tours, bookable dates from applevacations.my/en/tour.php?pckg_id=<id>, checked 1 November 2026 (dates marked Full left out)
    'ap-zhangjiajie': ('CNEZJ09', '''
        2026-12-01 2026-12-14 2026-12-22 2027-01-13 2027-01-20 2027-02-20 2027-03-07 2027-03-08
        2027-03-14 2027-03-28 2027-04-10 2027-04-17 2027-04-19 2027-04-21 2027-05-08 2027-05-13
        2027-05-15 2027-05-22 2027-05-24 2027-05-27 2027-05-31 2027-06-10 2027-06-21 2027-06-28
        2027-07-08 2027-07-19 2027-07-26 2027-08-05 2027-08-16 2027-08-23 2027-09-02 2027-09-13
        2027-09-20 2027-10-11 2027-10-18
        '''.split()),
    'ap-australia': ('AUMEL09', '''
        2027-02-04 2027-04-17 2027-05-15 2027-05-27 2027-06-08
        '''.split()),
    'ap-dongbei': ('CNSDB08', '''
        2026-12-18 2026-12-22 2026-12-23 2027-01-10 2027-01-15 2027-12-19 2027-12-21
        '''.split()),
    'ap-spain-portugal': ('EULIS12', '''
        2027-01-18 2027-02-01 2027-02-06 2027-02-08 2027-03-03 2027-03-10 2027-04-12 2027-04-21
        2027-05-05 2027-05-17 2027-09-13 2027-09-21 2027-10-11 2027-10-25
        '''.split()),
    'ap-finland': ('EULRVN10', '''
        2026-12-12 2026-12-16 2026-12-18 2026-12-25 2026-12-28 2026-12-30 2027-01-29 2027-02-03
        2027-02-05 2027-02-06 2027-02-08 2027-02-12 2027-02-19 2027-02-22
        '''.split()),
    'ap-morocco': ('AFCMN11', '''
        2027-02-03 2027-02-07 2027-03-09 2027-10-27 2027-11-17 2027-12-08 2027-12-15
        '''.split()),
}


def month_runs(dates):
    """ISO dates -> runs of consecutive months, as [((y, m), (y, m)), ...]"""
    months = sorted({(int(d[:4]), int(d[5:7])) for d in dates})
    runs = []
    for y, m in months:
        if runs and (runs[-1][1][0] * 12 + runs[-1][1][1]) + 1 == y * 12 + m:
            runs[-1][1] = (y, m)
        else:
            runs.append([(y, m), (y, m)])
    return [tuple(r) for r in runs]

MON = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def departs_en(dates):
    """'Feb 2027', 'Jan to Sep 2027', 'Dec 2026 to Mar 2027', 'Dec 2026, May to Jun 2027'"""
    out = []
    for (y1, m1), (y2, m2) in month_runs(dates):
        if (y1, m1) == (y2, m2):
            out.append(f'{MON[m1]} {y1}')
        elif y1 == y2:
            out.append(f'{MON[m1]} to {MON[m2]} {y2}')
        else:
            out.append(f'{MON[m1]} {y1} to {MON[m2]} {y2}')
    return ', '.join(out)

# YSL's own tours: dates from YSL (seat counts and fares stay off the site)
YSL_DATES = {
    'qinghai-gansu': '2027-05-28 2027-06-04 2027-06-18 2027-09-01 2027-10-22'.split(),
    'yunnan': '2027-03-02 2027-04-20'.split(),
}
QG['date_notes'] = {'2027-05-28': 'School holidays', '2027-06-18': 'Fully booked'}
for _t in TOURS + [QG] + GD_TOURS:
    if _t['slug'] in YSL_DATES:
        _t['dates'] = YSL_DATES[_t['slug']]
        _t['departs'] = departs_en(_t['dates'])

for _t in TOURS + GD_TOURS:
    if _t['slug'] in GD_DATES:
        _t['gd_code'], _t['dates'] = GD_DATES[_t['slug']]
        _t['departs'] = departs_en(_t['dates'])
