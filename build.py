# Static page builder for the Edgewood Cabinetry concept. Run: python3 build.py
import json, os
BASE = 'https://daveo820.github.io/edgewood-cabinetry-demo/'  # temporary GitHub Pages link; swap for Vercel later
TEL, TEL_H = '+19193397300', '(919) 339&#8209;7300'
BIRDEYE = 'https://reviews.birdeye.com/edgewood-custom-cabinetry-148996040070171'
TOWNS = ['Raleigh','Durham','Chapel Hill','Sanford','Apex','Cary','Morrisville','Wake Forest','Pittsboro','Carrboro','Rolesville','Knightdale','Zebulon','Wendell','Wilson','Garner','Clayton','Holly Springs','Fuquay-Varina','Smithfield','Benson','Lillington','Fayetteville','Goldsboro','Angier']
ORG = {"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Edgewood Cabinetry","alternateName":"Edgewood Custom Cabinetry",
 "url":"https://edgewoodcabinetry.com","telephone":"+1-919-339-7300","email":"pete@edgewoodcabinetry.com",
 "founder":{"@type":"Person","name":"Pete Rafferty"},
 "address":{"@type":"PostalAddress","streetAddress":"2164 Cole Rd","addressLocality":"Clayton","addressRegion":"NC","postalCode":"27520","addressCountry":"US"},
 "openingHours":"Mo-Fr 08:00-17:00","areaServed":TOWNS,"award":"2024 Triangle Parade of Homes Gold Medal ($1,800,000 to $1,930,000 category)",
 "image":BASE+"img/kitchen-perimeter.webp","sameAs":["https://facebook.com/286366191430",BIRDEYE]}
FONTS = 'https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Zilla+Slab:wght@500;600;700&display=swap'
V = '<svg class="mark-v" viewBox="0 0 26 16" aria-hidden="true"><path d="M2 2 L13 14 L24 2 M13 14 V1"/></svg>'
def U(word): return f'<span class="u-pencil">{word}<svg viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true"><path d="M1 7 C 25 2, 60 9, 99 4"/></svg></span>'
STARS = '<span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

def img(src, alt, sizes='100vw', eager=False, w=None, h=None, cls=''):
    small = src.replace('.webp','-800.webp')
    srcset = f' srcset="img/{small} 800w, img/{src} 1600w" sizes="{sizes}"' if os.path.exists('img/'+small) else ''
    dims = f' width="{w}" height="{h}"' if w else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return f'<img src="img/{src}"{srcset} alt="{alt}"{dims}{load}' + (f' class="{cls}"' if cls else '') + '>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Edgewood Cabinetry (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#24282b">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{fonts}"><link rel="stylesheet" href="{fonts}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{fonts}"></noscript>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26'%3E%3Crect width='26' height='26' fill='%2324282b'/%3E%3Cpath d='M5 7 L13 19 L21 7 M13 19 V6' stroke='%2386b5b0' stroke-width='2.4' fill='none'/%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Edgewood Cabinetry site. Photos are Edgewood&rsquo;s own, from edgewoodcabinetry.com, shown for this pitch only.</div>
<div class="util"><div class="wrap"><span>2164 Cole Rd, Clayton &middot; Mon to Fri, 8 to 5</span><span><a href="tel:{tel}">{telh}</a> &nbsp;&middot;&nbsp; <a href="mailto:pete@edgewoodcabinetry.com">Email Pete</a></span></div></div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="ec" aria-hidden="true">EC</span><span><b>Edgewood</b><small>Cabinetry &middot; Clayton NC</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn" href="estimate.html">Free estimate</a></div></header><main id="main">'''

FOOT = f'''</main><footer><div class="wrap">
<div class="foot-top"><div><p class="kicker" style="color:var(--sage)">{V} Talk to the guy who builds it</p><p class="foot-call">Call Pete.<br><a href="tel:{TEL}">{TEL_H}</a></p></div>
<div><address><strong style="color:#fff">Edgewood Cabinetry</strong><br>2164 Cole Rd, Clayton, NC 27520<br>Mon to Fri, 8:00am to 5:00pm<br><a href="mailto:pete@edgewoodcabinetry.com">pete@edgewoodcabinetry.com</a></address><p class="small">All wood. Soft close. Five year limited warranty. Financing available.</p></div></div>
<div class="foot-grid">
<div><h2>Cabinets</h2><ul><li><a href="cabinets.html">Stock, semi custom, custom</a></li><li><a href="cabinets.html#guarantee">Low price guarantee</a></li><li><a href="cabinets.html#process">The 8 step process</a></li><li><a href="cabinets.html#warranty">Warranty</a></li></ul></div>
<div><h2>More</h2><ul><li><a href="rooms.html">Rooms we build</a></li><li><a href="reviews.html">149 reviews</a></li><li><a href="about.html">About Pete</a></li><li><a href="builders.html">For home builders</a></li></ul></div>
<div><h2>Where Pete works</h2><p class="foot-towns">{", ".join(TOWNS)}</p></div>
</div>
<div class="foot-row"><span>Design. Build. Install. Since the router and the wall units.</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('cabinets.html','Cabinets'),('rooms.html','Rooms'),('reviews.html','Reviews'),('about.html','About Pete'),('builders.html','Builders')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 62, (fn, len(t), t)
    assert 130 <= len(d) <= 165, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or ORG),fonts=FONTS,tel=TEL,telh=TEL_H) + body + FOOT)

# ---------- real reviews (exact text; "..." marks where Birdeye or the site truncates) ----------
BIRD = [
 ('I recently gutted my 13 year old kitchen for a new modern look. I looked at the big box stores and decided I wanted something custom. I visited Edgewood&rsquo;s showroom and Pete was very easy to talk to. He showed me options and once I decided he jumped right on the project. I enjoyed watching my new kitchen unfold on Facebook as he sets up a photo album with your project alone to watch the progress. I am very pleased with my overall experience! Next is my bathroom....can&rsquo;t wait!','DawnDaniels','Merchant Circle, via Birdeye'),
 ('When we started our kitchen remodel, we weren&rsquo;t even thinking about having our cabinets custom made. We just assumed the price would be way over our budget. However, after getting quotes from the typical Lowes, Home Depot and other similar places, as friend recommended Pete at Edgewood. I figured it wouldn&rsquo;t hurt to get a quote. I was so surprised, but his price for was actually cheaper than any of the other quotes we recieved! We LOVE our new kitchen!...','AngelaHawkins','Birdeye'),
 ('I had gotten an estimate on roll out cabinets from another company that advertises their offering quite heavily. They had nice quality but really high prices. I then got a quote from Pete on the exact same cabinets and his pricing was very fair. And the quality was exceptional. Pete was very neat and cleaned up his work area and left my home in perfect condition... Pete gave me delivery dates for the installation and he was there when he promised...','Brian G.','Birdeye'),
 ('We asked Pete to come up with a concept for our living room that would accomodate our television and provide some storage space. As the discussion ensued he provided recommendations and visuals that solidified our requirements. From a price perspective he is very competitive and works to satisfy your needs within your budget constraints... A second project is in the works and a third will follow. Best value for the money.','edphilibin','Birdeye'),
 ('I was so excited to learn that the price was going to be the same as stock cabinets but CUSTOM BUILT. Pete was right on the ball the whole step of the way. I never had to wait for drawings for visits for work, for anything...','Southeast Med Spa &amp; Laser Center','Birdeye'),
 ('Our Vanity turned out beautiful! We are happy about the quality and custom look. Pete puts up pictures on Facebook so you can see the progress of your cabinets. He keeps you up to date on the progress as well.','Earlien Newsome','Birdeye'),
]
GOOG = [  # complete (untruncated) Google reviews shown in the review widget on edgewoodcabinetry.com
 ('Pete is a good craftsman and uses quality materials. The 3D visualization Pete provided early in the design process was very helpful to confirm the details of the project.','Brian Bailey'),
 ('Love our kitchen/pantry space now!!! Pete took our ideas and brought them to life. He was a pleaure to work with!! Thanks so much!!','Ashley Chears'),
 ('One of the nicest people I have ever came in contact with! He is obviously very knowledgeable about the cabinet industry. 10/10 recommend!!','Megan Fuller'),
 ('Pete is great. Great product at a fair price. I highly recommend Edgewood for any cabinetry needs!','CMC Electric'),
]
def bquote(q, who, src, cls=''):
    return f'<blockquote class="rq rv {cls}"><div class="rq-top">{STARS}<span class="src">{src}</span></div><p>&ldquo;{q}&rdquo;</p><footer>{V}<b>{who}</b></footer></blockquote>'

TIERS = [('Stock','Standard sized stock all wood cabinets with soft close hardware, a designed layout, and professional installation.','Fastest, lowest price','Pick up, delivery or install'),
 ('Semi custom','The same all wood, soft close stock cabinets with a designed layout, plus matching accents and accessories to fill gaps and dress them up. Professionally installed.','Matches stock quotes under the guarantee','Custom touches where they show'),
 ('Custom','Fully custom all wood cabinets with soft close hardware, designed and built to specification in Clayton, and installed to use every inch.','Built to your exact room','Often built as one solid unit')]
ROOMS = [('kitchens','Kitchens and islands','kitchen-mahogany-island-clayton.webp','Mahogany kitchen island with custom cabinets in Clayton','Built to fit the room, so there are no filler gaps from stock sizes. Matching range hoods, islands, and accessories like spice racks, lazy Susans and recycling pull outs.'),
 ('baths','Bathroom cabinets and vanities','bath-vanity-dark.webp','Dark stained custom bathroom vanity with mirror','Vanities and storage designed for the room, modern or traditional.'),
 ('refinish','Painting, staining and refinishing','unfinished-cabinets.webp','Unfinished custom cabinets ready for stain','Refresh the cabinets you have, or have new ones painted or stained to match.'),
 ('laundry','Laundry and mudrooms','mudroom.webp','Custom mudroom cabinets with bench','Utility storage for the laundry and a place for jackets, boots and muddy clothes.'),
 ('office','Office and library','office.webp','Custom home office cabinetry with desk','Desks, credenzas and bookshelves built to match the room.'),
 ('hidden','Hidden doors and compartments','hidden-door-closed.webp','Bookcase that is secretly a hidden door, closed','Bookcases that swing open, secret compartments and panic rooms that blend into the room.'),
 ('closets','Closets','closet.webp','Custom closet shelving and hanging space','Walk in closets with built shelving, hanging space and shoe storage.'),
 ('bars','Wet and dry bars','wet-bar.webp','Custom home wet bar with cabinets','Entertain at home with a bar built around how you host.'),
 ('entertainment','Entertainment centers','entertainment.webp','Custom wood entertainment center with fireplace','Built in wood that hides the cords and keeps the electronics in reach.')]
STEPS = [('Consultation','step-consultation.webp'),('Specification','step-elevations.webp'),('Kitchen planning checklist',None),('Measurement','step-measure.webp'),('Presentation',None),('Production','shop-production.webp'),('Inspection',None),('Installation',None)]

# ---------- HOME ----------
page('index.html','Custom Cabinets in Clayton and Raleigh NC | Edgewood Cabinetry',
 'Pete Rafferty designs, builds and installs all wood custom cabinets from his Clayton shop. 4.9 stars from 149 reviews. Call (919) 339-7300 for a free estimate.', f'''
<section class="hero"><div class="wrap hero-grid">
 <div class="hero-copy rv"><p class="kicker">{V} Custom cabinetry &middot; Clayton, NC</p>
  <h1>Custom cabinets from Pete&rsquo;s shop, priced against <span class="nowrap">{U('stock.')}</span></h1>
  <p class="lede">Pete Rafferty designs it, builds it in Clayton and installs it, often as one solid piece. All wood, soft close, five year warranty. Bring a written stock cabinet estimate from an approved vendor and Edgewood will match it with semi custom.</p>
  <div class="cta"><a class="btn" href="estimate.html">Get a free estimate <span aria-hidden="true">&rarr;</span></a><a class="btn btn--plain" href="reviews.html">Read the reviews</a></div>
  <ul class="facts"><li><b data-count="30">30</b><span>+ years building</span></li><li><b data-count="25">25</b><span>towns served</span></li><li><b data-count="5">5</b><span>year warranty</span></li></ul></div>
 <div class="hero-media">
  <figure class="hero-photo rv">{img('kitchen-perimeter.webp','White perimeter kitchen cabinets built by Edgewood',sizes='(max-width:960px) 100vw, 45vw',eager=True,w=1600,h=1151)}</figure>
  <a class="medal rv" href="about.html#parade"><img src="img/parade-gold-medal.webp" alt="" width="425" height="350"><span><b>Gold Medal</b>2024 Triangle Parade of Homes</span></a>
  <a class="score-card rv" href="{BIRDEYE}" rel="noopener"><span class="big" data-count="4.9" data-dec="1">4.9</span><span class="meta">{STARS}<b><span data-count="149">149</span> reviews</b><small>on Birdeye &rarr;</small></span></a>
 </div>
</div></section>

<section class="parade" id="parade"><div class="wrap parade-grid rv">
 <p class="kicker" style="color:var(--sage)">{V} 2024 Triangle Parade of Homes</p>
 <p class="parade-line">Gold Medal. <span>35 Ridgeline Court, Pittsboro.</span> <span>The $1.8M to $1.93M category.</span></p>
 <a class="btn btn--plain parade-btn" href="about.html#parade">The story</a>
</div></section>

<section class="tiers" aria-labelledby="tiers-h"><div class="wrap">
 <div class="tiers-head rv"><p class="kicker">{V} Three ways to buy</p><h2 id="tiers-h">Stock, semi custom or custom. <span class="dim">Same shop, same installer, your budget.</span></h2></div>
 <div class="tier-table" role="table" aria-label="Edgewood cabinet tiers">
  <div class="tr th" role="row"><span role="columnheader">Tier</span><span role="columnheader">What you get</span><span role="columnheader">Best for</span><span role="columnheader">Detail</span></div>
  {''.join(f'<div class="tr rv{" tr--hi" if i==2 else ""}" role="row"><span role="cell" class="tn">{V}{n}</span><span role="cell">{d}</span><span role="cell">{b}</span><span role="cell">{x}</span></div>' for i,(n,d,b,x) in enumerate(TIERS))}
 </div>
 <aside class="guarantee rv" id="guarantee"><h3>The low price guarantee</h3><p>Got a written estimate from a stock cabinet manufacturer with verified installers? Edgewood will match it with semi custom cabinets. No middleman, so the savings come to you.</p><p class="fine">Estimate must be from a stock cabinet manufacturer on Edgewood&rsquo;s approved vendor list.</p></aside>
</div></section>

<section class="reviews-home" aria-labelledby="rv-h"><div class="wrap">
 <div class="rv-head"><div class="rv"><p class="kicker">{V} 149 reviews on Birdeye</p><h2 id="rv-h">People keep saying the same three things: <em>Pete, the price, the progress photos.</em></h2></div>
 <a class="btn btn--plain rv" href="{BIRDEYE}" rel="noopener">All 149 on Birdeye</a></div>
 <div class="wall">{''.join(bquote(q,w,s) for q,w,s in BIRD)}</div>
 <p class="note rv">Quotes copied word for word from Edgewood&rsquo;s public Birdeye profile, spelling included. Birdeye does not show review dates.</p>
</div></section>

<section class="progress-feed" aria-labelledby="pf-h"><div class="wrap pf-grid">
 <div class="rv"><p class="kicker" style="color:var(--sage)">{V} Your kitchen, in progress</p><h2 id="pf-h">Watch it get built.</h2>
 <p>Two separate reviewers mention it: Pete sets up a photo album for your project alone, so you can watch the progress from start to finish.</p>
 <p class="note" style="color:#cfc8ba;border-color:var(--sage)"><strong style="color:#fff">Placeholder:</strong> a live strip of Pete&rsquo;s latest shop photos from the Edgewood Facebook page goes here.</p></div>
 <div class="pf-photos">
  <figure class="rv">{img('shop-build.webp','A carved cabinet base being built in the Edgewood shop',sizes='(max-width:960px) 50vw, 25vw')}<figcaption>On the bench</figcaption></figure>
  <figure class="rv">{img('shop-production.webp','Painted cabinet boxes in production in the Edgewood shop',sizes='(max-width:960px) 50vw, 25vw')}<figcaption>Built, before install</figcaption></figure>
  <figure class="rv">{img('bath-vanity-mirrors.webp','A finished Edgewood bathroom vanity and linen tower, installed',sizes='(max-width:960px) 50vw, 25vw')}<figcaption>Installed</figcaption></figure>
  <p class="pf-cap">Three different Edgewood projects, shown in shop order.</p>
 </div>
</div></section>

<section class="rooms-home" aria-labelledby="rm-h"><div class="wrap">
 <div class="rv"><p class="kicker">{V} Rooms</p><h2 id="rm-h">Kitchens first. <em>Then everything else, including the secret door.</em></h2></div>
 <div class="room-index">{''.join(f'<a class="ri rv" href="rooms.html#{k}"><span class="ri-n">{i+1:02d}</span><span class="ri-t">{n}</span>{img(f, a, sizes="160px")}</a>' for i,(k,n,f,a,_) in enumerate(ROOMS))}</div>
</div></section>

<section class="pete-home" aria-labelledby="pete-h"><div class="wrap pete-grid">
 <div class="pete-art rv">{img('step-elevations.webp','Cabinet elevation drawings for a custom kitchen',sizes='(max-width:960px) 100vw, 40vw')}<span class="tag">Drawn by hand first</span></div>
 <div class="rv"><p class="kicker">{V} Who you&rsquo;ll deal with</p><h2 id="pete-h">Pete may not look like the typical designer.</h2>
 <p class="big-q">&ldquo;He looks, dresses and talks more like a guy who builds cabinets in a workshop. But looks can be deceiving.&rdquo;</p>
 <p>Pete started in his teens with a router, building wall units. Thirty plus years of framing, remodeling, contracting and trim later, he still runs the consult, takes the measurements and is there for the install.</p>
 <a class="btn btn--plain" href="about.html">Meet Pete</a></div>
</div></section>

<section class="area" aria-labelledby="ar-h"><div class="wrap rv"><p class="kicker">{V} Service area</p><h2 id="ar-h" class="sr">Towns served</h2>
<p class="towns">{''.join(f'<span>{t}</span>' for t in TOWNS)}</p></div></section>''', ld=[ORG,bc(('Home',''))])

# ---------- CABINETS ----------
page('cabinets.html','Stock, Semi Custom and Custom Cabinets | Edgewood Cabinetry',
 'Compare Edgewood stock, semi custom and fully custom all wood cabinets, the low price guarantee, wood choices and the 8 step process. Get a free estimate today.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Cabinets</p><h1>All wood. Soft close. <em>Three price points.</em></h1>
<p class="lede">Big box cabinets are often particleboard and plywood under veneer. Edgewood builds from maple, cherry, mahogany, oak, hickory and pine, then stains or paints to match.</p></div></section>
<div class="wrap">
<section class="tier-cards">{''.join(f'<article class="tc rv{" tc--hi" if i==2 else ""}"><p class="kicker">{V} Tier {i+1}</p><h2>{n}</h2><p>{d}</p><dl><dt>Best for</dt><dd>{b}</dd><dt>Detail</dt><dd>{x}</dd></dl></article>' for i,(n,d,b,x) in enumerate(TIERS))}</section>
<section class="guarantee guarantee--wide rv" id="guarantee"><div><h2>Low price guarantee</h2><p>Edgewood guarantees to beat any written estimate from stock cabinet manufacturers with verified installers by providing semi custom cabinets to match their price.</p></div><p class="fine">Terms: the written estimate must be verified to be from Edgewood&rsquo;s approved vendor list of stock cabinet manufacturers.</p></section>
<section class="woods" aria-labelledby="w-h"><div class="rv"><p class="kicker">{V} Woods</p><h2 id="w-h">Pick the grain.</h2></div>
<ul class="wood-list">{''.join(f'<li class="rv"><span class="sw sw--{w.lower()}" aria-hidden="true"></span>{w}</li>' for w in ['Maple','Cherry','Mahogany','Oak','Hickory','Pine'])}</ul>
<p class="note rv"><strong>Placeholder:</strong> swatches are tinted blocks, not photos. Real wood and stain samples from Pete&rsquo;s shop go here.</p></section>
<section class="acc" aria-labelledby="ac-h"><figure class="rv">{img('accessories.webp','Kitchen cabinet storage accessories',sizes='(max-width:960px) 100vw, 50vw')}</figure><div class="rv"><p class="kicker">{V} Accessories</p><h2 id="ac-h">Storage that fits the stuff.</h2>
<ul class="ticks">{''.join(f'<li>{V}{a}</li>' for a in ['Lazy Susans','Custom range hoods and vents','Front trays for sinks','Drawer inserts for silverware and utensils','On door storage racks','Spice racks','Wine racks','Pull outs for garbage or recycling','Corner and base organizers for plastic storage'])}</ul></div></section>
<section class="process" id="process" aria-labelledby="pr-h"><div class="rv"><p class="kicker">{V} How it goes</p><h2 id="pr-h">Eight steps, one person you call.</h2></div>
<ol class="steps">{''.join(f'<li class="rv"><span class="sn">{i+1}</span><div><h3>{n}</h3>' + (img(f, n+' step', sizes='200px') if f else '') + '</div></li>' for i,(n,f) in enumerate(STEPS))}</ol>
<p class="note rv"><strong>Placeholder:</strong> one line per step in Pete&rsquo;s words. The live site lists the eight steps but not what happens in each, so nothing is invented here.</p></section>
<section class="warranty rv" id="warranty"><h2>Five year limited warranty</h2><p>Edgewood Custom Cabinetry warrants its cabinets to the original purchaser for five years from the date of purchase. If a cabinet fails from defects in material or workmanship under normal use, Edgewood will repair or replace the defective part at its discretion. Misuse, improper installation by others, extreme temperature or moisture, and natural wood color and grain variation are not covered.</p></section>
</div>''', ld=[ORG,bc(('Home',''),('Cabinets','cabinets.html'))]+[{"@context":"https://schema.org","@type":"Service","name":f"{n} cabinets","provider":{"@type":"HomeAndConstructionBusiness","name":"Edgewood Cabinetry"},"areaServed":"Raleigh, NC"} for n,*_ in TIERS])

# ---------- ROOMS ----------
page('rooms.html','Kitchens, Baths, Built Ins and Hidden Doors | Edgewood',
 'Custom kitchens, vanities, mudrooms, offices, closets, bars, entertainment centers and hidden doors, built by Edgewood in Clayton NC. Request a free estimate.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Rooms</p><h1>Every room that <em>holds something.</em></h1>
<p class="lede">Photos are from edgewoodcabinetry.com. Nine kinds of rooms, one shop.</p></div></section>
<div class="wrap rooms">{''.join(f"""<article id="{k}" class="room rv{' room--wide' if i in (0,5,8) else ''}">""" + (f"""<div class="secret"><figure class="sd-closed">{img('hidden-door-closed.webp','Bookcase hidden door, closed',sizes='(max-width:960px) 100vw, 60vw')}</figure><figure class="sd-open">{img('hidden-door-open.webp','The same bookcase swung open to reveal a room',sizes='(max-width:960px) 100vw, 60vw')}</figure><button class="btn sd-btn" aria-pressed="false">Open the bookcase</button></div>""" if k=='hidden' else f"<figure>{img(f, a, sizes='(max-width:960px) 100vw, 50vw')}</figure>") + f"""<div class="room-copy"><span class="rn">{i+1:02d}</span><h2>{n}</h2><p>{d}</p><a href="estimate.html?room={k}">Price this room &rarr;</a></div></article>""" for i,(k,n,f,a,d) in enumerate(ROOMS))}</div>''', ld=[ORG,bc(('Home',''),('Rooms','rooms.html'))])

# ---------- REVIEWS ----------
page('reviews.html','149 Reviews, 4.9 Stars: Edgewood Cabinetry, Clayton NC',
 'Read what Triangle homeowners say about Pete Rafferty and Edgewood Cabinetry: 4.9 stars from 149 reviews on Birdeye. Then call (919) 339-7300 for an estimate.', f'''
<section class="page-head page-head--score"><div class="wrap ph-grid"><div class="rv"><p class="crumbs"><a href="index.html">Home</a> / Reviews</p><h1>Don&rsquo;t take <em>Pete&rsquo;s word</em> for it.</h1></div>
<a class="score-card score-card--lg rv" href="{BIRDEYE}" rel="noopener"><span class="big" data-count="4.9" data-dec="1">4.9</span><span class="meta">{STARS}<b><span data-count="149">149</span> reviews</b><small>Birdeye profile, claimed by Edgewood &rarr;</small></span></a></div></section>
<div class="wrap">
<section class="wall wall--page">{''.join(bquote(q,w,s) for q,w,s in BIRD)}{''.join(bquote(q,w,'Google, shown on edgewoodcabinetry.com') for q,w in GOOG)}</section>
<section class="rv-sources rv"><h2>Where these come from</h2>
<ul><li><b>Birdeye:</b> 4.9 average from 149 reviews across sources including Merchant Circle. The profile is claimed by Edgewood. Six quotes above, word for word.</li>
<li><b>Google:</b> four short reviews copied in full from the review widget on edgewoodcabinetry.com.</li></ul>
<p class="note"><strong>To fix before launch:</strong> the live site quotes three different totals (Birdeye 149, Google 63 at 4.9, Houzz 71 at 4.85). This concept uses the Birdeye total everywhere. A live Google reviews feed with real dates replaces the static list once Pete approves it.</p></section>
</div>''', ld=[ORG,bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Pete Rafferty, Custom Cabinet Maker | Edgewood Cabinetry',
 'Meet Pete Rafferty: 30+ years of building, from a teenage router to a 2024 Parade of Homes gold. He designs, builds and installs every Edgewood job. Call today.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / About Pete</p><h1>Design. Build. <em>Install.</em> Same guy.</h1></div></section>
<div class="wrap about">
<section class="about-grid"><div class="rv"><p class="kicker">{V} Pete Rafferty, owner</p><h2>It started with a router and some wall units.</h2>
<p>Pete Rafferty has been practicing his craft for more than 30 years. He started in his teens with a router building wall units, and it grew from there: framing, remodeling, contracting and trim work, then a specialty in designing and building custom cabinets.</p>
<p>From the first consult to taking measurements to the final install, you deal with Pete. He also draws, and that eye for shape and space is how he turns a homeowner&rsquo;s ideas and inspiration photos into a design that can actually be built.</p>
<p>Because Edgewood builds to the exact measurements of your home, many cabinets are built as one solid unit. That means fewer pieces to fit together on site, and installs that go faster than homeowners expect.</p>
<p class="note"><strong>Placeholder:</strong> a real photo of Pete in the shop, and two or three pieces of his artwork from the live About page.</p></div>
<div class="about-photos"><figure class="rv">{img('shop-production.webp','Cabinets in production in the Edgewood shop',sizes='(max-width:960px) 100vw, 40vw')}<figcaption>{V} Production, Clayton shop</figcaption></figure><figure class="rv">{img('step-measure.webp','Measuring a kitchen for new cabinets',sizes='(max-width:960px) 100vw, 40vw')}<figcaption>{V} Measurement</figcaption></figure></div></section>
<section class="parade-full rv" id="parade"><img src="img/parade-gold-medal.webp" alt="2024 Triangle Parade of Homes gold medal emblem" width="425" height="350" loading="lazy"><div><p class="kicker">{V} 2024 Triangle Parade of Homes</p><h2>Gold Medal, $1.8M to $1.93M category.</h2><p>A home at 35 Ridgeline Court in Pittsboro, outfitted with Edgewood cabinetry, won the 2024 Triangle Parade of Homes Gold Medal in its price category.</p><p class="note"><strong>Placeholder:</strong> photos of the Ridgeline Court cabinetry. The live site shows only the medal graphic.</p></div></section>
</div>''', ld=[ORG,bc(('Home',''),('About Pete','about.html'))])

# ---------- BUILDERS ----------
page('builders.html','Custom Cabinets for Home Builders in the Triangle | Edgewood',
 'Edgewood builds custom cabinetry for Triangle home builders: designed to your plans, installed on schedule, billed 50/40/10. Call Pete at (919) 339-7300 today.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Builders</p><h1>For builders who want <em>one call</em> for cabinets.</h1>
<p class="lede">Custom cabinetry adapted to your plans and your buyer, from design consult to installation. Edgewood travels to the job depending on project size.</p></div></section>
<div class="wrap builders">
<section class="bill rv"><p class="kicker">{V} Billing</p><div class="bill-bar"><span style="flex:50"><b>50%</b> down</span><span style="flex:40"><b>40%</b> on delivery</span><span style="flex:10"><b>10%</b> at completion</span></div></section>
<section class="b-points">{''.join(f'<div class="bp rv"><h2>{h}</h2><p>{p}</p></div>' for h,p in [('Fits any plan','Custom work tailored to the architectural style and the buyer, from compact kitchens to full layouts.'),('On the schedule','Edgewood handles design through installation and commits to finishing builder projects on schedule.'),('Proof on the Parade','A Pittsboro home with Edgewood cabinetry took the 2024 Triangle Parade of Homes Gold Medal in the $1.8M to $1.93M category.'),('Three tiers','Stock, semi custom and custom from one shop, so spec homes and custom builds can use the same partner.')])}</section>
<p class="note rv"><strong>Placeholder:</strong> logos and short quotes from builders Edgewood has worked with, used with permission.</p>
<a class="btn rv" href="estimate.html?who=builder">Send Pete your plans <span aria-hidden="true">&rarr;</span></a>
</div>''', ld=[ORG,bc(('Home',''),('Builders','builders.html'))])

# ---------- ESTIMATE ----------
page('estimate.html','Free Custom Cabinet Estimate in the Triangle | Edgewood',
 'Ask Pete Rafferty for a free, no obligation cabinet estimate. Kitchens, baths, built ins and more across Raleigh, Clayton and 23 more towns. Financing available.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Free estimate</p><h1>Tell Pete about <em>the room.</em></h1><p class="lede">Free and no obligation. Quotes are free, and financing is available.</p></div></section>
<div class="wrap est-grid">
<form id="qform" class="rv" novalidate>
<fieldset><legend>Which room?</legend><div class="chips-in">{''.join(f'<label><input type="checkbox" name="room" value="{k}"> {n}</label>' for k,n,*_ in ROOMS)}</div></fieldset>
<fieldset><legend>Which tier are you leaning toward?</legend><div class="chips-in">{''.join(f'<label><input type="radio" name="tier" value="{n}"{" checked" if n=="Not sure" else ""}> {n}</label>' for n in ['Stock','Semi custom','Custom','Not sure'])}</div></fieldset>
<div class="two"><div class="field"><label for="n">Name</label><input id="n" name="name" autocomplete="name" required></div><div class="field"><label for="p">Phone</label><input id="p" name="tel" type="tel" autocomplete="tel" required></div></div>
<div class="two"><div class="field"><label for="e">Email</label><input id="e" name="email" type="email" autocomplete="email" required></div><div class="field"><label for="t">Town</label><select id="t" name="town">{''.join(f'<option>{t}</option>' for t in sorted(TOWNS))}<option>Somewhere else</option></select></div></div>
<div class="field"><label for="m">What are you picturing?</label><textarea id="m" name="msg" rows="5"></textarea></div>
<div class="field check"><label><input type="checkbox" name="quote"> I have a written stock cabinet estimate for the price match</label></div>
<button class="btn" type="submit">Send to Pete <span aria-hidden="true">&rarr;</span></button>
<p class="note" id="qmsg" role="status">Demo form. Nothing is sent.</p></form>
<aside class="rv"><div class="est-card"><p class="kicker" style="color:var(--sage)">{V} Or just call</p><a class="phone" href="tel:{TEL}">{TEL_H}</a><p>Mon to Fri, 8:00am to 5:00pm<br>2164 Cole Rd, Clayton, NC 27520<br><a href="mailto:pete@edgewoodcabinetry.com">pete@edgewoodcabinetry.com</a></p>
<ul class="ticks ticks--dark">{''.join(f'<li>{V}{x}</li>' for x in ['Free estimates','Financing available','Five year limited warranty','Low price guarantee on stock quotes'])}</ul></div></aside>
</div>''', ld=[ORG,bc(('Home',''),('Free estimate','estimate.html'))])

page('404.html','Page Not Found | Edgewood Cabinetry, Clayton North Carolina',
 'That page is not here. Head back to the Edgewood Cabinetry home page or call Pete Rafferty at (919) 339-7300 to talk about your custom cabinet project today.',
 f'<section class="wrap nf"><p class="kicker">{V} 404</p><h1>Measure twice. <em>This page got cut anyway.</em></h1><p style="margin-top:28px"><a class="btn" href="index.html">Back to the home page</a></p></section>')
print('built')
