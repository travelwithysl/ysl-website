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
    dict(slug='yunnan', dur='8D7N', iata='KMG', title='Yunnan & Shangri-La', region='China', cat='asia', kind='Group tour', line='Old towns, snow peaks and Tibetan monasteries', img='lake.jpg', page='tour-yunnan.html'),
    # signature group tours from Golden Destinations, a brand YSL carries (no prices; enquiries go to YSL)
    dict(slug='gd-europe-legend', dur='10D7N', page='tour-gd-europe-legend.html', brand='Golden Destinations', iata='CDG', short='Europe Legend', title='Europe Legend', region='Europe', cat='europe', kind='Group tour',
         line='Paris, Brussels, Amsterdam, the Rhine, Titisee, Rhine Falls, Zurich and Lucerne', img='gd-europe-legend-card.jpg'),
    dict(slug='gd-hokkaido', dur='6D4N', page='tour-gd-hokkaido.html', brand='Golden Destinations', iata='CTS', short='Hokkaido', title='Hokkaido Delight', region='Japan', cat='asia', kind='Group tour',
         line='Noboribetsu, Lake Toya, Otaru and Sapporo', img='gd-hokkaido-card.jpg'),
    dict(slug='gd-turkiye', dur='9D7N', page='tour-gd-turkiye.html', brand='Golden Destinations', iata='IST', short='Türkiye', title='The Charms of Türkiye', region='Türkiye', cat='europe', kind='Group tour',
         line='Istanbul, Canakkale, Ephesus, Pamukkale, Konya and Cappadocia', img='gd-turkiye-card.jpg'),
    dict(slug='gd-eastern-europe', dur='9D6N', page='tour-gd-eastern-europe.html', brand='Golden Destinations', iata='BUD', short='Eastern Europe', title='Eastern Europe Vista', region='Europe', cat='europe', kind='Group tour',
         line='Budapest, Bratislava, Vienna, Hallstatt, Salzburg, Cesky Krumlov and Prague', img='gd-eastern-europe-card.jpg'),
    dict(slug='gd-new-zealand', dur='9D7N', page='tour-gd-new-zealand.html', brand='Golden Destinations', iata='AKL', short='New Zealand', title='New Zealand North &amp; South Island', region='New Zealand', cat='longhaul', kind='Group tour',
         line='Both islands, from Auckland to Queenstown', img='gd-new-zealand-card.jpg'),
    dict(slug='gd-south-africa', dur='11D8N', page='tour-gd-south-africa.html', brand='Golden Destinations', iata='JNB', short='South Africa', title='Essence of South Africa', region='Africa', cat='longhaul', kind='Group tour',
         line='Johannesburg, Cape Town, Botswana and Victoria Falls', img='gd-south-africa-card.jpg'),
]

POSTS = [
    dict(slug='yunnan', title="A first-timer's guide to Yunnan's high country", cat='dest', cat_label='Destinations', date='2 October 2026',
         excerpt='Kunming, Lijiang and Shangri-La, and how to enjoy the climb.', img='lake.jpg', href='journal-yunnan.html'),
    dict(slug='fair', title='Meet us at GD Travel Fair, 9 to 11 October', cat='news', cat_label='News', date='28 September 2026',
         excerpt='Fair-only fares at The Starling Mall, ground floor.', img='airport.jpg', href='journal-yunnan.html'),
    dict(slug='incentive', title='Planning a company incentive trip', cat='corp', cat_label='Corporate travel', date='15 September 2026',
         excerpt='A checklist for HR teams, from budget to boarding.', img='business.jpg', href='journal-yunnan.html'),
    dict(slug='docs', title='Passport, visa, insurance: sort these first', cat='tips', cat_label='Travel tips', date='2 September 2026',
         excerpt='The three things to check before you pay a deposit.', img='passport.jpg', href='journal-yunnan.html'),
    dict(slug='packing', title='Packing light for a two-week tour', cat='tips', cat_label='Travel tips', date='20 August 2026',
         excerpt='One suitcase, three climates, and what our tour leaders bring.', img='mapdesk.jpg', href='journal-yunnan.html'),
    dict(slug='planning', title='How we plan a group tour', cat='news', cat_label='News', date='5 August 2026',
         excerpt='What happens between your first quote and departure day.', img='laptop.jpg', href='journal-yunnan.html'),
]

BRANDS = ['Golden Destinations', 'Parlo Tours', 'Apple Vacations']

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
               facebook='https://www.facebook.com/ysltravel')

# destinations the home-page pin opens onto; one is chosen per visit. Add YSL's own tour photos here.
OPENINGS = [
    dict(img='lake.jpg', code='KMG', place='Kunming, Yunnan', tour='Yunnan &amp; Shangri-La', href='tour-yunnan.html', kind='Group tour'),
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
]

# Golden Destinations departure dates, matched from gd.my on 1 November 2026 (prices deliberately left out).
# slug: (GD tour code, dates). New Zealand: NZW (Dec 2026) and NZW(R) (2027) run the same itinerary.
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

for _t in TOURS + GD_TOURS:
    if _t['slug'] in GD_DATES:
        _t['gd_code'], _t['dates'] = GD_DATES[_t['slug']]
        _t['departs'] = departs_en(_t['dates'])
