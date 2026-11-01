# Journal articles. Written for YSL to review before publishing; no news items, no dated promotions.
# Each article: slug, cat (dest / tips / corp), title, lead (also the card excerpt), date, read time,
# image (img) or a placeholder (slot: c1, c2, label), body (HTML), and a closing call to action.

WA = 'Chat on WhatsApp'

ARTICLES = [
  dict(slug='yunnan', cat='dest', title="A first-timer’s guide to Yunnan’s high country",
    lead='Kunming, Lijiang and Shangri-La climb from a mild spring city to the edge of the Tibetan plateau in a single trip. A little preparation makes the first days much easier.',
    excerpt='Kunming, Lijiang and Shangri-La, and how to enjoy the climb.',
    date='2 October 2026', read='5 min read', img='jr-yunnan.jpg', alt='Black Dragon Pool in Lijiang, with Jade Dragon Snow Mountain behind',
    body='''<p>Yunnan is one of the most rewarding routes we run, and one of the most surprising for first-time visitors. The province rises in steps. Most tours start in Kunming, move up to the old town of Lijiang, then climb again to Shangri-La, where the air is thinner and the views open onto snow peaks and monastery roofs.</p>
    <p>None of this is difficult for a healthy traveller, but it does change how you pace the first few days. Here is what we tell every group before they fly.</p>
    <h2>Three cities, three heights</h2>
    <p>The altitude rises gradually along the usual route, which gives your body time to adjust.</p>
    <table class="data-table"><thead><tr><th scope="col">City</th><th scope="col" class="r">Approx. altitude</th></tr></thead><tbody><tr><td>Kunming</td><td class="r">1,900 m</td></tr><tr><td>Lijiang</td><td class="r">2,400 m</td></tr><tr><td>Shangri-La</td><td class="r">3,200 m</td></tr></tbody></table>
    <h2>Take the first day slowly</h2>
    <p>At Shangri-La’s height, a mild headache or shortness of breath on the stairs is common on the first day. Walk at an easy pace, drink plenty of water, and skip alcohol on the first night. Most people feel settled by the second morning.</p>
    <p class="pull">Walk slowly, drink water, and let the first afternoon be an easy one.</p>
    <div class="callout">If you have a heart or lung condition, or any concern about altitude, speak to your doctor before you travel. On tour, tell your tour leader straight away if you feel unwell.</div>
    <h2>Dress in layers</h2>
    <p>Mornings and evenings are cold at altitude, even when the afternoon sun feels warm. The sun is also much stronger up high, so cover up and use sunscreen even on cool, bright days.</p>
    <h2>What to pack</h2>
    <ul><li>A warm jacket or down layer, plus a fleece or jumper</li><li>Comfortable walking shoes with good grip</li><li>Sunscreen, sunglasses, a hat and lip balm</li><li>A reusable water bottle</li><li>Your own medication, with enough for the whole trip</li><li>A universal plug adaptor and a power bank</li></ul>
    <h2>When to go</h2>
    <p>Spring and autumn are the favourites, with clear skies and comfortable days. Winter brings crisp, quiet days in Shangri-La but cold nights. Summer is the rainy season, when the hills turn green and the crowds thin out.</p>''',
    cta=('Travel to Yunnan with us', 'Our Yunnan and Shangri-La group tours are led by experienced tour leaders, with hotels, meals and transfers arranged before you leave.', 'tour-yunnan.html', 'See the tour')),

  dict(slug='qinghai-gansu', cat='dest', title='Qinghai and Gansu: a Silk Road in colour',
    lead='Striped mountains, desert dunes, cave murals and a salt lake that mirrors the sky. Northwest China packs more landscape into ten days than almost anywhere we go.',
    excerpt='Rainbow mountains, the Mogao Caves and the sky mirror of Chaka.',
    date='24 October 2026', read='6 min read', img='qg-chaka.jpg', alt='A traveller in a red scarf reflected in the still water of Chaka Salt Lake',
    body='''<p>Most people arrive in Lanzhou knowing one picture: the striped hills of Zhangye. They leave with ten. The route through Gansu and Qinghai follows the old Hexi Corridor, the narrow passage the Silk Road took between the mountains and the desert, then climbs onto the Qinghai plateau and its great lakes.</p>
    <h2>The highlights, in the order you meet them</h2>
    <ul><li><b>Zhangye Danxia.</b> Bands of red, orange and cream sandstone, at their richest in the late afternoon light.</li><li><b>Jiayuguan.</b> The fortress at the western end of the Great Wall, where the desert begins.</li><li><b>The Mogao Caves.</b> Hundreds of Buddhist cave temples near Dunhuang, painted over a thousand years and listed by UNESCO.</li><li><b>Mingsha Mountain and Crescent Spring.</b> Tall dunes around a small spring-fed lake that has survived the desert for centuries.</li><li><b>Chaka Salt Lake.</b> On a still day the shallow water turns into a mirror of the sky.</li><li><b>Qinghai Lake.</b> China’s largest lake, high on the plateau, ringed by grassland and, in summer, yellow rapeseed fields.</li></ul>
    <p class="pull">Ten days, five landscapes, one of the great journeys in Asia.</p>
    <h2>Altitude, briefly</h2>
    <p>The Gansu half of the trip is low and dry. The Qinghai half is high: Chaka and Qinghai Lake both sit at around 3,000 metres or more. Most healthy travellers manage well if they walk slowly, drink plenty of water and keep the first evening on the plateau quiet.</p>
    <div class="callout">If you have a heart or lung condition, speak to your doctor before booking. Your tour leader will check in with the group as the route climbs.</div>
    <h2>A few things worth knowing</h2>
    <ul><li>Entry to the Mogao Caves is limited and booked ahead, and photography is not allowed inside the caves.</li><li>Distances are long. Expect several half-days on the coach, broken up by stops along the way.</li><li>The desert is hot by day and cool at night, even in summer. Pack a light jacket.</li><li>Sun protection matters on the dunes and on the salt lake, where the light reflects back up.</li></ul>
    <h2>When to go</h2>
    <p>The season runs from late spring to early autumn. July and August bring the rapeseed flowers at Qinghai Lake; September brings clear skies and fewer crowds. Winter is very cold on the plateau, and some sights close or shorten their hours.</p>''',
    cta=('Travel to Qinghai and Gansu with us', 'Our ten-day group tour covers the full route, from Lanzhou through Dunhuang to Qinghai Lake, with flights, hotels and meals arranged.', 'tour-qinghai-gansu.html', 'See the tour')),

  dict(slug='retreat', cat='corp', title='A company retreat close to home',
    lead='Not every team trip needs a passport. Malaysia has islands, highlands and heritage towns within an easy flight or drive, and a well-planned local retreat can feel every bit as special.',
    excerpt='Eight Malaysian destinations for team building and company trips.',
    date='5 October 2026', read='5 min read', slot=('#1f6a5a', '#082520', 'Langkawi'), alt='',
    body='''<p>Local retreats are quicker to organise, easier on the budget and simpler for travellers: no visas, no long flights, and familiar food. The trick is choosing the right place for what you want the team to do.</p>
    <h2>Islands and coast</h2>
    <ul><li><b>Langkawi.</b> Resorts with conference space, the SkyCab cable car, island-hopping and duty-free shopping. A short flight from Kuala Lumpur.</li><li><b>Port Dickson.</b> Beach hotels within about ninety minutes of the Klang Valley, ideal for a two-day programme.</li><li><b>Desaru.</b> A newer resort coast in Johor, with large resorts and space for outdoor team activities.</li><li><b>Sabah.</b> Island trips off Kota Kinabalu, river and rainforest excursions, and Mount Kinabalu for the adventurous.</li></ul>
    <h2>Highlands</h2>
    <ul><li><b>Genting Highlands.</b> Cool air, large hotels and entertainment, about an hour from Kuala Lumpur.</li><li><b>Cameron Highlands.</b> Tea plantations, gardens and a slower pace; good for a reflective leadership retreat.</li></ul>
    <h2>Heritage and food</h2>
    <ul><li><b>Penang.</b> George Town’s UNESCO-listed streets, street-art walks and some of the best food in the country.</li><li><b>Melaka.</b> A heritage city that works well for themed dinners, river cruises and walking trails.</li></ul>
    <p class="pull">No visas, no long flights, and everyone already likes the food.</p>
    <h2>What to plan for</h2>
    <ul><li>Transport for the whole group, timed so everyone arrives together</li><li>A venue for the working sessions, with the right AV and breakout rooms</li><li>One shared activity that gets people talking, from a cooking class to a beach challenge</li><li>A dinner that feels like an occasion, with halal and vegetarian options confirmed</li><li>A simple programme with free time built in</li></ul>
    <h2>When to go</h2>
    <p>Weekdays outside the school holidays give the best rates and the quietest venues. On the east coast, the monsoon from roughly November to March affects some islands, so check the season before you choose a beach destination.</p>''',
    cta=('Plan a retreat in Malaysia', 'Team building, company trips, annual dinners and family days, with transport for everyone arranged.', 'corporate.html', 'Local MICE')),

  dict(slug='hokkaido', cat='dest', title='Hokkaido through the seasons',
    lead='Japan’s northern island changes completely from one season to the next. Here is how to choose the Hokkaido that suits you.',
    excerpt='Snow festivals, lavender fields and early autumn colour.',
    date='18 October 2026', read='5 min read', img='jr-hokkaido.jpg', alt='Lavender and flower fields in Furano in summer',
    body='''<p>Hokkaido is the Japan many travellers fall for on a second trip: wide skies, lakes and volcanoes, hot springs, and seafood that is hard to match anywhere. It is also strongly seasonal, so the first question is not where to go but when.</p>
    <h2>Winter: December to February</h2>
    <p>Deep, dry snow, ski resorts and hot-spring towns. The Sapporo Snow Festival, held in early February, fills the city with giant snow and ice sculptures. Further northeast, drift ice reaches the coast in late winter. Days are short and very cold, so dress for it and the season is magical.</p>
    <h2>Spring: April to May</h2>
    <p>Cherry blossom arrives later than in the rest of Japan, usually from late April into early May. The snow melts from the lower hills, and the crowds are lighter than in Tokyo or Kyoto during blossom season.</p>
    <h2>Summer: June to August</h2>
    <p>Mild and comfortable, a welcome change from Malaysian heat. Furano’s lavender fields are at their best from early to late July, with flower farms in bloom across the hills of Biei. This is a good season for families and for anyone who likes to walk.</p>
    <p class="pull">Choose the season first. The rest of the trip follows.</p>
    <h2>Autumn: September to October</h2>
    <p>Autumn colour starts earlier here than anywhere else in Japan, beginning in the mountains in late September and moving down to the cities through October. Clear days, crisp mornings and the start of the seafood season make it a quiet favourite.</p>
    <h2>Good to know</h2>
    <ul><li>Distances are larger than they look on the map; a tour with coach transfers saves a lot of effort.</li><li>Many hot-spring baths have house rules, including tattoo policies. Your tour leader will brief you.</li><li>Pack for the season: proper winter boots in the snow months, light layers in summer.</li></ul>''',
    cta=('Travel to Hokkaido with us', 'Our Hokkaido Delight tour covers Noboribetsu, Lake Toya, Otaru and Sapporo, with flights, hotels and meals arranged.', 'tour-gd-hokkaido.html', 'See the tour')),

  dict(slug='documents', cat='tips', title='Passport, visa, insurance: sort these first',
    lead='Three things decide whether a trip starts smoothly. Check them before you pay a deposit, not the week before you fly.',
    excerpt='The three things to check before you pay a deposit.',
    date='2 September 2026', read='4 min read', img='airport.jpg', alt='Two travellers with a suitcase in an airport terminal',
    body='''<p>Most travel problems we help clients solve could have been avoided with ten minutes of checking at the start. Before you commit to a trip, look at these three things.</p>
    <h2>1. Your passport</h2>
    <ul><li><b>Validity.</b> Many countries require your passport to be valid for at least six months after the date you arrive. Check the expiry date now, not at the airport.</li><li><b>Blank pages.</b> Some countries need one or two clean pages for stamps or visa stickers.</li><li><b>Condition.</b> A damaged passport, with water marks or a loose page, can be refused. If in doubt, renew it.</li><li><b>Names.</b> The name on your flight booking must match your passport exactly.</li></ul>
    <h2>2. Your visa and entry rules</h2>
    <p>Entry rules change, sometimes with little notice, and they depend on your nationality and the purpose of your trip. Even where no visa is needed, some countries now ask travellers to register online before they fly. Check the official requirements for every country on your route, including any you only transit through.</p>
    <p class="pull">Check the passport, the entry rules and the insurance, in that order.</p>
    <div class="callout">When you book a tour with us, we confirm the visa and entry requirements for your passport, and we can handle the application where a visa is needed.</div>
    <h2>3. Your travel insurance</h2>
    <ul><li><b>Buy it when you pay the deposit.</b> That way cancellation cover protects you from the start, not just once you travel.</li><li><b>Declare medical conditions.</b> An undeclared pre-existing condition can void a claim.</li><li><b>Check the activities.</b> Skiing, hot-air balloons and trekking at altitude are not always covered as standard.</li><li><b>Keep the policy handy.</b> Save the emergency number and policy number on your phone and on paper.</li></ul>
    <h2>A simple checklist</h2>
    <ul><li>Passport valid for six months or more after arrival</li><li>Entry requirements checked for every country, including transits</li><li>Visa or online registration done, where needed</li><li>Insurance bought, with medical conditions declared</li><li>Copies of all documents saved on your phone and with family at home</li></ul>''',
    cta=('Let us handle the paperwork', 'Visa applications, travel insurance and document checks, arranged together with your booking.', 'services.html#visa', 'Travel services')),

  dict(slug='packing', cat='tips', title='Packing light for a two-week tour',
    lead='One suitcase, three climates and a lot of hotel changes. How to pack for a long group tour without dragging half your wardrobe around.',
    excerpt='One suitcase, three climates, and what our tour leaders bring.',
    date='20 August 2026', read='4 min read', img='mapdesk.jpg', alt='A map, camera, notebook and sunglasses laid out on a desk',
    body='''<p>On a long tour you check in and out of hotels every couple of days, and the coach is usually waiting. A lighter bag makes every one of those mornings easier. Our tour leaders pack the same way every time, and it works.</p>
    <h2>Start with the rules</h2>
    <p>Check your airline’s allowance before you pack: the weight limit for checked bags, the size and weight of cabin bags, and any limits on domestic flights within the tour, which can be stricter than on the international legs.</p>
    <h2>Pack in layers, not outfits</h2>
    <p>Choose a small set of pieces that work together in one or two colours. Layers handle changing weather better than heavy single items: a T-shirt, a long-sleeved top, a fleece or knit, and a light waterproof jacket cover most of what a tour can throw at you.</p>
    <p class="pull">If you are not sure you will wear it, leave it at home.</p>
    <h2>What our tour leaders bring</h2>
    <ul><li>Two pairs of comfortable shoes, one already worn in</li><li>Clothes for about a week, and a small bag of travel detergent</li><li>A light down jacket that packs into its own pocket</li><li>A small day bag for the coach and walking days</li><li>A universal adaptor and a power bank</li><li>Medication in its original packaging, with enough for the whole trip</li><li>A reusable water bottle and a small first-aid pouch</li></ul>
    <h2>Keep these in your hand luggage</h2>
    <ul><li>Passport, tickets and insurance details</li><li>Medication and a change of clothes</li><li>Valuables, chargers and anything fragile</li></ul>
    <h2>Leave room to come home</h2>
    <p>Pack your suitcase about three-quarters full. You will buy something along the way, and a little space saves an anxious repack on the last night.</p>''',
    cta=('Ready for the trip itself?', 'See our current group tours, or tell us where you would like to go and we’ll plan it with you.', 'tours.html', 'Browse tours')),
]

CAT_LABEL = {'dest': 'Destinations', 'tips': 'Travel tips', 'corp': 'Corporate travel'}
for _a in ARTICLES:
    _a['cat_label'] = CAT_LABEL[_a['cat']]
    _a['href'] = f"journal-{_a['slug']}.html"
