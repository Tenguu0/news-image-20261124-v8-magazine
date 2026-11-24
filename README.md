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

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It writes `out/entry.png` (1024×1024 PNG). Python 3.12+, standard
library only — no network, no randomness, no clock, so every run
writes the same bytes.

## How it works

`entry.png` was composed by a build script (PIL + DejaVu fonts)
from the twelve pictures in `assets/`: two AI-generated feature
photographs and ten thumbnails cut from two AI-generated contact
sheets of six panels each. The pictures are committed in this repo
and the page is laid out from them at fixed positions, so the
composition is fully reproducible. `main.py` is the entry program:
it copies the composed image to the output directory.
