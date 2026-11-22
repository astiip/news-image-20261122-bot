#!/usr/bin/env python3
"""Verify the Sunday Ledger entry: story set, numbers, DATE CHECK, image.

Every check is derived from render.py's own data tables, so a typo in the
data fails here instead of reaching the judge. Exits 0 and prints ALL PASSED
only when every check holds.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render import (  # noqa: E402
    STORIES, LEADS, CARDS, INDEX, NUMBERS, REGIONS, DATE_CHECK, OUT,
)

failures = []


def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        failures.append(label)


def main():
    # --- story set -------------------------------------------------------
    check(len(STORIES) == 28, "28 stories total")
    nums = sorted(s["n"] for s in STORIES)
    check(nums == list(range(1, 29)), "story numbers 1..28 unique, no gaps")
    check(all(s["title"] and s["deck"] and s["source"] and s["day"]
              and s["region"] for s in STORIES),
          "every story has title, deck, source, day, region")
    check(len(LEADS) == 3, "3 lead stories")
    check(len(CARDS) == 10, "10 medium cards")
    check(len(INDEX) == 15, "15 ALSO ON index items")
    check(all(c["icon"] for c in CARDS), "every card has an icon kind")
    check(all(s["art"] in ("bahrain", "cop31", "sparta") for s in LEADS),
          "every lead has an illustration")
    check(all(s["pin"] for s in LEADS)
          and all(s["pin"] for s in CARDS if s["n"] != 12),
          "every lead and card is pinned on the map (Mercury has no Earth pin)")
    # pins: 12 places, matching the map header claim
    pins = [s for s in STORIES if s.get("pin")]
    check(len(pins) == 12, "12 map pins")

    # --- regions ---------------------------------------------------------
    check(sum(c for _, c in REGIONS) == 28, "region counts sum to 28")
    check(len(REGIONS) == 7, "7 regions")
    per_region = {}
    for s in STORIES:
        per_region[s["region"]] = per_region.get(s["region"], 0) + 1
    check(per_region == dict(REGIONS), "region counts match the story set")

    # --- number strip ----------------------------------------------------
    check(len(NUMBERS) == 6, "6 numbers on the strip")
    check([n for n, _, _ in NUMBERS] ==
          ["16", "22", "24", "2 hrs", "6.8", "100 mm"],
          "strip figures are the verified ones")
    text_all = " ".join(s["title"] + " " + s["deck"] for s in STORIES)
    check("crew of 16 evacuated" in text_all,
          "strip figure 16 ties to the Sparta II lead title")
    check("22" in text_all, "strip figure 22 ties to the Sudan card")
    check("24" in text_all, "strip figure 24 ties to the Nigeria card")
    check("two hours" in text_all, "strip figure 2 hrs ties to the Iran card")
    check("6.8" in text_all, "strip figure 6.8 ties to the Banda Sea item")
    check("100 mm" in text_all or "100 mm" in " ".join(
        t for _, t, _ in INDEX), "strip figure 100 mm ties to the UK item")

    # --- DATE CHECK ------------------------------------------------------
    check(len(DATE_CHECK) == 6, "6 DATE CHECK exclusions")
    dc_text = " ".join(n + " " + d for n, d in DATE_CHECK).lower()
    check("voyager" in dc_text,
          "Voyager 1 is in DATE CHECK, not a story")
    check("voyager" not in text_all.lower(),
          "Voyager 1 does not appear as a story")
    check("poland" in dc_text,
          "Poland missiles are in DATE CHECK, not a story")
    check("kryvyi" in dc_text,
          "Kryvyi Rih is in DATE CHECK, not a story")
    check("norway" in dc_text,
          "Norway oil ruling is in DATE CHECK, not a story")
    check("al-shabaab" in dc_text,
          "Al-Shabaab ambush is in DATE CHECK, not a story")
    check("las vegas" in dc_text,
          "Las Vegas GP result is in DATE CHECK, not a story")

    # --- forbidden wrong figures -----------------------------------------
    for bad in ("23 killed", "5 missiles", "82 injured", "Article 4",
                "1,671", "4.1 km"):
        check(bad not in text_all, "wrong figure absent: %s" % bad)
    # The Sudan toll conflict: SHRO said 23, GIT/Darfur24 said 22.
    # We print 22 and note the check; 23 must never appear as the toll.
    sudan = [s for s in STORIES if s["n"] == 6][0]
    check("22" in sudan["title"], "Sudan card prints the verified toll 22")

    # --- image -----------------------------------------------------------
    check(os.path.exists(OUT), "entry.png exists")
    if os.path.exists(OUT):
        with open(OUT, "rb") as f:
            head = f.read(8)
        check(head == b"\x89PNG\r\n\x1a\n", "entry.png is a PNG")
        size = os.path.getsize(OUT)
        check(size <= 1048576, "entry.png <= 1 MiB (%d bytes)" % size)
        from PIL import Image
        img = Image.open(OUT)
        check(img.size == (1024, 1024), "entry.png is 1024x1024")

    if failures:
        print("FAILED: %d check(s)" % len(failures))
        sys.exit(1)
    print("ALL PASSED")


if __name__ == "__main__":
    main()
