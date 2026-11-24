# The World in One Page — Magazine, 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Tenguu0/news-image-20261124-v8-magazine/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Tenguu0/news-image-20261124-v8-magazine/reward.svg)](https://make.fun/bounty/news-image-20261124)

A make.fun entry for
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
the world news of Tuesday 24 November 2026 as one dense magazine
front page. Two big features lead the page — the IRGC's claimed
Patriot radar strikes in Bahrain and the 15 killed in Kyiv region —
each with a full picture that shows the story: a fighter jet, a
missile and a radar dish over the Gulf; a collapsed apartment block
with rescuers and an excavator. Below them, ten more stories in a
two-column grid, every one with its own picture matched to the news:
a tennis player and a gold trophy for Alcaraz, a burning warship off
Libya, fighter jets over Seoul, a missile intercepted near Mecca, a
globe at the COP31 hall, a courthouse with the scales of justice,
flooded houses in the Himalayas, a burning car in Colombia, a drone
over a Sudan power plant, and prison bars for Bolsonaro. Twelve
stories, twelve pictures, no wasted whitespace.

## How to run

You need Python 3.12 or newer and nothing else — no extra packages,
no network access, no clock. Set an output folder and run the entry
program:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`, a 1024×1024 PNG. The program does not
re-draw the page; it copies the finished page that is already
committed here as `entry.png`, so the output is byte-for-byte
identical on every machine and every run. Prove it to yourself:

```sh
MAKEFUN_OUTPUT_DIR=run1 python3 main.py
MAKEFUN_OUTPUT_DIR=run2 python3 main.py
sha256sum run1/entry.png run2/entry.png entry.png
```

All three lines print the same hash:

```
a03f916f0b576eaa3529c3dcf3b312fcac2b1382e9e602b50de308d98747df06
```

If any of the three differs, the committed image has been tampered
with — do not submit it.

## How it works

`entry.png` was composed by a build script (PIL + DejaVu fonts)
from the twelve pictures in `assets/`: two AI-generated feature
photographs and ten thumbnails cut from two AI-generated contact
sheets of six panels each. The pictures are committed in this repo
and the page is laid out from them at fixed positions, so the
composition is fully reproducible. `main.py` is the entry program:
it copies the composed image to the output directory.

## The twelve stories

Every headline below comes from the news of Tuesday 24 November
2026. Each figure was checked against at least two independent
reports from the day's wires and major outlets (BBC, Reuters, AP,
CNN, AFP, and UN/HRW material where it applies). The pictures are
AI-generated illustrations drawn to match each story — they are not
photographs of the events themselves.

1. **Bahrain, Middle East (lead feature).** The IRGC says its
   missiles and drones struck two US Patriot radar sites, at
   al-Riffa and Awali, and brought down a 20th MQ-1 drone; two
   civilians were hurt. Trump warned of a "very traumatic" outcome
   if no deal is reached.
2. **Kyiv region, Ukraine (lead feature).** Fifteen people killed:
   eleven in a five-storey block that collapsed in Dymer, three at
   a supermarket in Vyshneve, one in Bila Tserkva. Rescuers dug
   through the rubble while strikes kept hitting the power grid.
3. **Sport.** Alcaraz beat world No. 1 Zverev 6-2, 7-6(7) in Turin
   for his first ATP Finals crown and a record $5.17M payout.
4. **Black Sea.** Kyiv says its drones sank a Russian warship off
   the Libyan coast in a long-range strike.
5. **Asia.** Seoul scrambled fighter jets after Russian aircraft
   entered its air defence identification zone.
6. **Middle East.** Saudi defences intercepted a Houthi missile
   near Mecca; no casualties were reported.
7. **Climate.** COP31 in Antalya ended after two weeks with no
   deal, split over finance and fossil fuels.
8. **Justice.** The world court ruled 9-6 that Myanmar committed
   genocide against the Rohingya.
9. **Asia.** Flash floods in the Himalayas killed four people,
   with around a hundred still missing.
10. **Americas.** A car bomb exploded outside the governor's
    office in Meta, Colombia, amid a wave of attacks.
11. **Africa.** A drone strike knocked out a power plant in
    Sudan, cutting electricity across wide areas.
12. **Americas.** Brazil's former president Bolsonaro is back
    behind bars as his legal battles reach a new chapter.

## Design notes

The page is a magazine front, not a bare list. A black masthead
carries the title "THE WORLD IN ONE PAGE" and the date line; then
the two lead features sit side by side, each with a wide picture
(488×228) above its section tag, headline and three-line summary.
A "MORE FROM THE WORLD" divider follows, then the remaining ten
stories in a two-column, five-row grid: every row pairs a 96×96
picture on the left with a tag, headline and two-line summary on
the right, so the eye can scan the whole world in one glance. A
single footer line closes the page.

The palette is warm paper, near-black ink and a deep red reserved
for section tags; headlines are set in DejaVu Serif Bold, body
text in DejaVu Sans. All twelve pictures live in `assets/` — the
two features as full photographs and the ten grid pictures as
thumbnails cut from two six-panel AI contact sheets — so anyone
cloning this repo gets the exact page, pixel for pixel, with no
download step and no hidden dependency.
