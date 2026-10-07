# DESIGN_DNA: Edgewood Cabinetry concept

**One line:** an owner led cabinet shop with 149 reviews, presented like the pencil marks on a board in Pete's shop. Proof first, plain talk, no gimmicks.

| Choice | Decision | Why |
|---|---|---|
| Hero archetype | Scorecard collage: a type led headline on the left, and on the right a taped up shop photo with a Parade of Homes medal tag and a 4.9 / 149 reviews score card hanging off it | Proof is Edgewood's biggest asset, and its photos are older and lower resolution, so they work best small and framed rather than full bleed. Different from Hollingsworth (full bleed photo), Core Home (editorial split) and Eagle Point (type led). |
| Display font | Zilla Slab 600/700 | A workshop slab: sturdy and friendly. Not used in any earlier repo. |
| Body font | Atkinson Hyperlegible at 18px | Built for legibility, so it stays readable for every age group. |
| Palette | `--graphite` #24282b, `--sage` #86b5b0 (Edgewood logo, dark only), `--sage-dk` #355f5a (AA on light), `--kraft` #e8dcc3 shop paper, `--chalk` #f8f4ec page, `--maple` #b47a43, `--pencil` #b8411a carpenter's pencil (signal), `--dust` #625e57 muted text | Sage pulled from Edgewood's logo file, wood and kraft from the shop photos. |
| Signature element | **The carpenter's crow's foot**: the V mark a woodworker pencils on a board to mark the cut, plus a pencil underline. It appears on every kicker, every review card, the tier table, the accessory list, the footer and the 404. It draws itself in when it scrolls into view. | Pete draws, and his story starts at a workbench with a router. |
| Motion personality | Confident punctuation: quick 0.5s snaps, rating numbers count up once, buttons press down like a stamp (hard offset shadow). Nothing floats. Respects reduced motion. | Matches a no nonsense owner ("he listens and then executes"). |
| Grid break, per page | Home: the score card hangs off the photo and out of the hero, and the review wall cards sit slightly rotated. Cabinets: the custom tier card is lifted out of line. Rooms: the kitchens, hidden doors and entertainment rows span full width. Reviews: the score card sits in the header. | One per page. |
| Footer | Closing spread: "Call Pete." with the phone number at display size, plus all 25 towns | The phone is how this business sells. |
| Copy voice | Plain and direct. Reuses Edgewood's own best line ("Pete may not look like the typical designer..."). No dashes. | |

## Pages
`index.html`, `cabinets.html` (tiers, guarantee, woods, accessories, 8 step process, warranty), `rooms.html` (9 room types, hidden door before and after), `reviews.html`, `about.html` (Pete, Parade of Homes), `builders.html` (50/40/10 billing), `estimate.html` (replaces the 10% off pop up), `404.html`.

## What changes for production
Remove the concept banner and noindex, swap BASE for the real domain, wire the form, add a live Google reviews feed with real dates, add photos of the Parade home and of Pete, and add privacy, terms and accessibility pages (with counsel review).
