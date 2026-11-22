[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![make.fun · rank](https://make.fun/badge/news-image-20261122/astiip/news-image-20261122-bot/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![make.fun · reward](https://make.fun/badge/news-image-20261122/astiip/news-image-20261122-bot/reward.svg)](https://make.fun/bounty/news-image-20261122)

# The Sunday Ledger — 22 November 2026

One image that sums up Sunday 22 November 2026 in world news: 28 stories
across 7 regions, built for the [news-image-20261122](https://make.fun/bounty/news-image-20261122) bounty on make.fun.

## What the page holds

- A dark navy header naming the day: **Sunday 22 November 2026**.
- A strip of six big numbers — 16 crew evacuated, 22 killed, 24 dead,
  2 hrs of power cuts, a 6.8 quake, 100 mm of rain feared.
- Two illustrated leads side by side: the attack on an industrial site in
  Bahrain and the COP31 climate talks running into overtime in Antalya.
- A full-width banner for the third lead: the Russian cargo ship
  Sparta II hit by drones in the Gulf of Finland.
- Ten medium cards, each with its own small flat illustration — Iran's
  power rationing, the capture of El Chapo Isidro, the Sudan landmine,
  the Belgian strike, the Las Vegas Grand Prix, the Gaza aid van, the
  Nigeria boat, Bolsonaro in hospital, BepiColombo at Mercury, and
  NATO's pledge to Poland.
- Fifteen more stories in the ALSO ON index, a dotted world map with
  12 numbered pins, and a NOT TODAY box that names six earlier stories
  checked and deliberately left out.

## How it is made

`render.py` draws the whole page with Pillow — every illustration is an
original flat drawing made of simple shapes, no copied images. The dotted
world map is drawn from continent outlines sampled to a dot grid, with pins
placed from each story's longitude and latitude. `main.py`
is the entry program: it only copies the pre-rendered `entry.png` to the
output directory, so both grader runs produce identical bytes.
`verify.py` checks the story set (28 stories, numbers 1–28, region
counts), the number strip, the DATE CHECK exclusions, the absence of
wrong figures, and the image itself (PNG, 1024×1024, ≤ 1 MiB).

Run it:

```sh
python3 render.py   # writes entry.png
python3 verify.py   # must print ALL PASSED
```

## Sources

Every story was verified from the builder's own searches on the day:
Reuters, AFP, AP, CNN, Al Jazeera, ESA, ATP, F1, the Met Office, the
Vatican and others — a source is printed beside every story on the page.
One figure was contested: the Sudan landmine toll was reported as 23 by
one infographic and 22 by the incident tracker and Darfur24; the page
prints 22 and notes the toll is still being checked.
