# Market research: custom cabinetry sites, for the Edgewood Cabinetry concept

## How this was done (and what I could not get)
- Researched 7 October 2026. I picked 14 cabinetry sites: national custom brands that set the visual bar, Southeast shops with strong showroom or trade pages, and the local shops that show up on searches for "custom cabinets Wilmington NC", "custom cabinets Raleigh NC" and "custom cabinets Clayton NC".
- Lighthouse 12, mobile, run from this box on each homepage. A single run is noisy, so treat the numbers as rough.
- **No traffic numbers.** Similarweb blocks automated requests and Semrush needs a login, so I did not guess. "Best performing" here means the sites that set the design bar, the sites that rank on local searches, and how fast they load.
- Screenshots of every homepage (desktop and iPhone 13) are in `research/`. Crown Point's screenshots failed, but its Lighthouse run worked.

## Lighthouse, mobile homepage
| Site | Region / role | Perf | A11y | Best pr. | SEO | LCP | Page weight |
|---|---|---|---|---|---|---|---|
| crown-point.com | National, sells custom direct | 67 | 100 | 39 | 100 | 6.4 s | 1.2 MB |
| plainfancycabinetry.com | National custom, PA | 57 | 78 | 79 | 85 | 9.4 s | 3.0 MB |
| peacockhome.com | National luxury (Christopher Peacock) | 56 | 96 | 82 | 92 | 16.8 s | 3.5 MB |
| wood-mode.com | National custom | 46 | 91 | 100 | 85 | 43.3 s | 11.1 MB |
| devolkitchens.com | Design benchmark (UK and US) | 45 | 89 | 79 | 92 | 44.5 s | 14.5 MB |
| mousercabinetry.com | Kentucky maker, sells through dealers | 47 | 58 | 57 | 100 | 35.5 s | 9.3 MB |
| charlestoncabinetsinc.com | SC showroom | 71 | 96 | 100 | 92 | 6.2 s | 1.4 MB |
| eurokbw.com | Atlanta showroom | 51 | 96 | 79 | 100 | 10.1 s | 5.1 MB |
| mycabinetfactory.com | North Georgia factory with a showroom | 32 | 94 | 96 | 100 | 19.4 s | 3.2 MB |
| precisioncustomcabinetsnc.com | Charlotte custom shop | 43 | 93 | 93 | 82 | 11.4 s | 2.1 MB |
| **hollingsworthcabinetry.com** | **Client, Wilmington** | **38** | 85 | 100 | 91 | **8.9 s** | **5.7 MB** |
| **edgewoodcabinetry.com** | **Client, Clayton** | **69** | 93 | 71 | 100 | **8.7 s** | 1.2 MB |

What this means: nobody in this category is fast. Every site here takes over 6 seconds to load its main image on mobile, and the expensive brands are the worst offenders (Wood-Mode and deVOL send 11 to 14 MB). A cabinetry site that loads in under 2.5 seconds would beat every one of them, including the national brands.

## Patterns the strongest sites share
1. **The first screen shows a real room, not a slogan.** Peacock, Plain & Fancy, Wood-Mode, Mouser, deVOL and Charleston Cabinets all open with one large photo of a finished kitchen. The weaker local sites open with a stock image or a sliding carousel (JHR, Cardinal, My Cabinet Factory).
2. **Separate doors for different buyers.** Peacock has "How to Work With Us" and "Luxury Developments". Mouser sells through dealers and built them a virtual showroom. Precision lists who it serves: homeowners, builders, designers, decorators and contractors. ATA splits residential and commercial. Builders and designers want different things than homeowners, and the good sites route them early.
3. **Galleries organized by room and by style.** Plain & Fancy splits Kitchens, Bathrooms and Other Rooms. Burlew's and MDI file every project under kitchens, vanities, built-ins, mudrooms and closets. PineWood and MDI give each project a name and a place, the way Hollingsworth's tours already do.
4. **The process gets its own section.** ATA shows "Four stages. No surprises." European Kitchen & BathWorks has a dedicated cabinet process page. PineWood describes a six phase process. Laying out the steps answers the biggest worry about custom work, which is not knowing what happens next.
5. **The showroom is a reason to visit, not just an address.** Charleston Cabinets has a showroom page ("over 15 custom cabinetry vignettes"), EKBW leads with "See, Touch, and Feel Before You Decide" and even hosts showroom lunches, and Plain & Fancy has a showroom finder. For a high priced custom job, the in person visit is where the sale gets made.
6. **Proof with a source.** Plain & Fancy puts its 2026 NKBA KBIS award on the homepage, Wood-Mode runs design awards, and JHR shows its Google review count in the header. Awards and review counts are shown with where they came from.
7. **The weak spots are the same everywhere:** carousels, cookie banners covering the first screen (deVOL, Coastal, EKBW, My Cabinet Factory), all caps headings, generic stock kitchens, and pages that are more than 3 MB.

## Local competition
- **Wilmington:** Hollingsworth shows up first for "custom cabinets Wilmington NC" in the search index I used, ahead of Coastal Cabinets (since 1983), Creative Custom Woodworks, Three Arrows Cabinetry and Infinity Custom Cabinets. Search ranking is not Hollingsworth's problem. The problem is that the site visitors land on looks unfinished. Coastal Cabinets outlasts them in years (1983 vs 1990), and Creative Custom Woodworks pitches "only six people handle your custom cabinets."
- **Triangle:** for "custom cabinets Raleigh NC", Edgewood does not make the top 5. JHR (shows 66 Google reviews in its header), Cardinal Cabinetworks, Raleigh Woodworks, Carpathian Woodworks and MeKkelek do. Edgewood does rank first for "custom cabinets Clayton NC". Cardinal is the closest match to Edgewood's pitch: an in house custom shop that also sources semi custom cabinets "at better prices than our competitors."

## What this means for Edgewood (and what I built)
| Winning pattern | What I built |
|---|---|
| Proof with a source | The 149 Birdeye reviews and the 2024 Parade of Homes Gold are on the first screen as a score card and a medal tag, both linked. The live site buries the medal below a pop up form and shows reviews with dates frozen in 2015 to 2020. |
| The process gets a section | The 8 steps from Edgewood's kitchen page, with Edgewood's own photos where they exist. |
| Separate doors for different buyers | A builders page (50/40/10 billing, the Parade medal as proof) separate from the homeowner pages. |
| Galleries by room | Nine room types with Edgewood's photos, plus a working before and after for the hidden bookcase door. |
| Price clarity (Cardinal and JHR both push "fair price") | A tier table comparing stock, semi custom and custom, with the low price guarantee and its terms spelled out. This replaces the "10% off, limited time" pop up form. |
| Owner front and center | "Pete may not look like the typical designer", quoted from Edgewood's own About page. The reviews keep naming Pete, so the site does too. |
| Speed | Static HTML, no plugins, with Edgewood's 51 script tags cut to one small file. |
