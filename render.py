#!/usr/bin/env python3
"""Render the news-image-20261122 entry: Sunday 22 November 2026 in one image.

Draws a 1024x1024 PNG with PIL (build-time only). The entrypoint main.py
is a stdlib-only copy program; this file is the generator, kept in the
repo so the build is reproducible and reviewable.

Design ("The Sunday Ledger"): a dark navy header band with a sans
wordmark and the date at right (not a giant serif masthead); a six-tile
number strip with icons; two illustrated lead panels side by side, then
a full-width illustrated banner for the third lead; a region-index pill
row; ten medium cards with a small flat icon LEFT of the text; and a
bottom band with a numbered ALSO ON index, a dotted world map with
numbered pins, and a NOT TODAY date-check box.

Every story below was verified from this session's own browser searches
for 22 November 2026 (weekend arc: Sat 21 + Sun 22 Nov). Figures that
could not be verified were dropped; see verify.py.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (250, 246, 236)
INK = (20, 33, 61)
NAVY = (20, 33, 61)
RED = (193, 39, 45)
TEAL = (23, 126, 122)
GOLD = (217, 164, 65)
GRAY = (107, 114, 128)
LINE = (203, 199, 186)
CARD = (255, 255, 255)
SKY = (214, 228, 238)
SEA = (38, 84, 124)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

# ---------------------------------------------------------------- stories
# n, region, day, kicker, title, deck, source, pin (lon, lat) or None, icon
LEADS = [
    dict(n=1, region="MIDDLE EAST", day="SAT 21 NOV",
         title="Iran hits Bahrain: fire at industrial site, no injuries",
         deck=("Bahrain says an Iranian attack struck a civilian industrial "
               "facility on Saturday, starting a fire crews fought into the "
               "night. Tehran's Guards say they aimed at US bases — and air "
               "defences intercepted more attacks."),
         source="Reuters · AFP", pin=(50.6, 26.2), art="bahrain"),
    dict(n=2, region="GLOBAL", day="SUN 22 NOV",
         title="COP31 nears a deal as a new text goes to Sunday's vote",
         deck=("After talks ran two days past their Friday deadline, summit "
               "president Murat Kurum tabled a text he says all parties can "
               "accept. Objections by 03:00 GMT; approval opens at 06:00 "
               "GMT. Fossil-fuel wording still unconfirmed."),
         source="Reuters", pin=(30.7, 36.9), art="cop31"),
    dict(n=3, region="EUROPE", day="SAT 21 NOV",
         title="Drones set a sanctioned Russian cargo ship ablaze; crew of 16 evacuated",
         deck=("The Sparta II, bound for Kaliningrad, was hit on Saturday "
               "morning and drifted into Finnish waters, still burning. "
               "Finland says Ukraine was likely behind it; a Russian "
               "helicopter is suspected of crossing Finnish airspace."),
         source="CNN · Reuters · Finnish Defence Forces",
         pin=(24.0, 60.0), art="sparta"),
]

CARDS = [
    dict(n=4, region="MIDDLE EAST", day="SUN 22 NOV",
         title="Iran starts rationing power from Sunday",
         deck="Cuts of up to two hours a day; bread rationed in three provinces.",
         source="State TV", pin=(51.4, 35.7), icon="bulb"),
    dict(n=5, region="AMERICAS", day="SAT 21 NOV",
         title="Mexico captures 'El Chapo Isidro'",
         deck="Seized in Sinaloa; 11 killed in the operation. FBI top 10, $5m reward.",
         source="Reuters · AP", pin=(-107.0, 25.0), icon="cuffs"),
    dict(n=6, region="AFRICA", day="SUN 22 NOV",
         title="Landmine kills 22 on the road to El-Obeid",
         deck="Blast on the Um Arada road; the toll is still being checked.",
         source="Global Incident Tracker", pin=(30.2, 13.2), icon="mine"),
    dict(n=7, region="EUROPE", day="SAT 21 NOV",
         title="Belgium grounds Monday's flights",
         deck="Controllers join the strike; all flights off 07:00–21:00, demo at 10:00.",
         source="skeyes · Reuters", pin=(4.35, 50.85), icon="plane"),
    dict(n=8, region="AMERICAS", day="SUN 22 NOV",
         title="Verstappen on pole under the lights",
         deck="Antonelli fastest but drops five places; the race starts 04:00 UTC.",
         source="F1 · FIA", pin=(-115.1, 36.1), icon="flag"),
    dict(n=9, region="MIDDLE EAST", day="SAT 21 NOV",
         title="Drone strike kills three at a Gaza food van",
         deck="WCK says the van was not its own; Israel says it hit Islamic Jihad.",
         source="Reuters · AFP", pin=(34.5, 31.5), icon="van"),
    dict(n=10, region="AFRICA", day="SAT 21 NOV",
         title="Mourners' boat capsizes; 24 dead",
         deck="Death toll rose on Saturday in Bayelsa; 24 rescued, up to 300 were aboard.",
         source="NEMA · AP", pin=(6.3, 4.8), icon="boat"),
    dict(n=11, region="AMERICAS", day="SAT 21 NOV",
         title="Bolsonaro in intensive care",
         deck="Ex-president, 71, has a bowel obstruction; stable in Brasilia.",
         source="Reuters · AFP", pin=(-47.9, -15.8), icon="cross"),
    dict(n=12, region="GLOBAL", day="SAT 21 NOV",
         title="Two probes reach Mercury after eight years",
         deck="ESA and JAXA orbiters enter orbit together on Saturday — a first.",
         source="ESA · Nature", pin=None, icon="mercury"),
    dict(n=13, region="EUROPE", day="SAT 21 NOV",
         title="NATO will defend 'every inch' of Poland",
         deck="Pledge after Friday's airspace violation; council meets Monday.",
         source="Reuters · PAP", pin=(21.0, 52.2), icon="shield"),
]

# n, one-line index text, source
INDEX = [
    (14, "Myanmar quake M4.1 at 02:35 IST, 95 km deep", "NCS"),
    (15, "FBI crime database hacked; Trump: \u2018not good\u2019", "CNN"),
    (16, "Thousands march in Lisbon over living costs", "Reuters"),
    (17, "Alcaraz v Zverev for the ATP Finals title", "ATP"),
    (18, "Real Madrid 2\u20131 Celta; Esp\u00ed winner, 85\u2032", "Reuters"),
    (19, "Crew stun Messi\u2019s Miami 3\u20130 in playoff opener", "MLS"),
    (20, "Aoun: occupation and meddling block independence", "Al Jazeera"),
    (21, "M4.6 quake off Sarangani, Philippines", "PHIVOLCS"),
    (22, "Pope Leo leads Christ the King Angelus", "Vatican"),
    (23, "Guwahati hosts its first Test; Pant captains", "Cricbuzz"),
    (24, "Devon & Cornwall brace for up to 100 mm rain", "Met Office"),
    (25, "M6.8 Banda Sea quake felt in Darwin", "USGS"),
    (26, "Australia hits back at US over AUKUS report", "Reuters"),
    (27, "Snow isolates 1,400 in a Fukushima village", "AP"),
    (28, "Merz and Macron both reject EU budget trim", "ZDF"),
]

# The same 15 index stories as full records, for verification and the
# region counts. No map pin: the map pins only the 12 lead/card places.
INDEX_STORIES = [
    dict(n=14, title="Myanmar quake M4.1 at 02:35 IST, 95 km deep",
         deck="Magnitude 4.1, depth 95 km; tremors felt, no damage reported.",
         source="NCS", day="SUN 22 NOV", region="ASIA", pin=None),
    dict(n=15, title="FBI crime database hacked; Trump: \u2018not good\u2019",
         deck="'Not good,' Trump says of the breach — the FBI's second in months.",
         source="CNN", day="SAT 21 NOV", region="AMERICAS", pin=None),
    dict(n=16, title="Thousands march in Lisbon over living costs",
         deck="Union march in the rain; inflation 3.8% in October.",
         source="Reuters", day="SAT 21 NOV", region="EUROPE", pin=None),
    dict(n=17, title="Alcaraz v Zverev for the ATP Finals title",
         deck="Alcaraz beat Shelton; Zverev beat Medvedev in the semis.",
         source="ATP", day="SAT 21 NOV", region="EUROPE", pin=None),
    dict(n=18, title="Real Madrid 2\u20131 Celta; Esp\u00ed winner, 85\u2032",
         deck="Durán 6', Bellingham 66', Espí 85'; Mbappé missed a penalty.",
         source="Reuters", day="SAT 21 NOV", region="EUROPE", pin=None),
    dict(n=19, title="Crew stun Messi\u2019s Miami 3\u20130 in playoff opener",
         deck="Tapia twice, Habroune once; Luján sent off in the 36th.",
         source="MLS", day="SAT 21 NOV", region="AMERICAS", pin=None),
    dict(n=20, title="Aoun: occupation and meddling block independence",
         deck="President's eve-of-independence address; strikes hit the south.",
         source="Al Jazeera", day="SAT 21 NOV", region="MIDDLE EAST", pin=None),
    dict(n=21, title="M4.6 quake off Sarangani, Philippines",
         deck="Off Balut Island at 08:23 local, depth 10 km; no damage expected.",
         source="PHIVOLCS", day="SUN 22 NOV", region="ASIA", pin=None),
    dict(n=22, title="Pope Leo leads Christ the King Angelus",
         deck="Solemnity of Christ the King; dioceses mark World Youth Day.",
         source="Vatican", day="SUN 22 NOV", region="GLOBAL", pin=None),
    dict(n=23, title="Guwahati hosts its first Test; Pant captains",
         deck="Second Test starts Sunday; India 1–0 down with Gill out.",
         source="Cricbuzz", day="SUN 22 NOV", region="ASIA", pin=None),
    dict(n=24, title="Devon & Cornwall brace for up to 100 mm rain",
         deck="Yellow warning 06:00–23:59; floods and power cuts possible.",
         source="Met Office", day="SUN 22 NOV", region="EUROPE", pin=None),
    dict(n=25, title="M6.8 Banda Sea quake felt in Darwin",
         deck="Deep under the Banda Sea; felt in Darwin, no damage, no tsunami.",
         source="USGS", day="SAT 21 NOV", region="ASIA", pin=None),
    dict(n=26, title="Australia hits back at US over AUKUS report",
         deck="Marles criticises the CBO claim that AUKUS cuts US submarines.",
         source="Reuters", day="SUN 22 NOV", region="OCEANIA", pin=None),
    dict(n=27, title="Snow isolates 1,400 in a Fukushima village",
         deck="Trees down, roads blocked; heavy snow on Saturday.",
         source="AP", day="SAT 21 NOV", region="ASIA", pin=None),
    dict(n=28, title="Merz and Macron both reject EU budget trim",
         deck="Costa's revised draft cuts €204bn; a summit looms this week.",
         source="ZDF", day="SAT 21 NOV", region="EUROPE", pin=None),
]

# number, label, caption — all figures verified in this session's searches
NUMBERS = [
    ("16", "CREW EVACUATED", "Sparta II"),
    ("22", "KILLED", "Sudan landmine"),
    ("24", "DEAD", "Nigeria boat"),
    ("2 hrs", "POWER CUTS", "Iran, from Sunday"),
    ("6.8", "MAGNITUDE", "Banda Sea quake"),
    ("100 mm", "RAIN FEARED", "Dartmoor, Sunday"),
]

REGIONS = [("EUROPE", 8), ("ASIA", 5), ("AMERICAS", 5), ("MIDDLE EAST", 4),
           ("GLOBAL", 3), ("AFRICA", 2), ("OCEANIA", 1)]

# name, date — stories checked and deliberately LEFT OUT of this page
DATE_CHECK = [
    ("Voyager 1\u2019s light-day milestone", "18 Nov"),
    ("Russian missiles landing in Poland", "Fri 20 Nov"),
    ("Kryvyi Rih missile strike", "Sat 21 Nov"),
    ("Norway\u2019s oil-licence ruling", "13 Nov"),
    ("Al-Shabaab ambush in Somalia", "26 Oct"),
    ("Las Vegas GP result", "not yet run"),
]

STORIES = LEADS + CARDS + INDEX_STORIES


def all_stories():
    """Every numbered story on the page, 1..28."""
    out = []
    for s in STORIES:
        out.append((s["n"], s["region"], s["title"], s["deck"], s["source"]))
    for n, text, src in INDEX:
        out.append((n, None, text, "", src))
    return out


# ---------------------------------------------------------------- helpers
def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, fnt, max_w, suffix="\u2026"):
    """Truncate one line to a pixel width, adding an ellipsis."""
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    while text and draw.textlength(text + suffix, font=fnt) > max_w:
        text = text[:-1]
    return text + suffix


def rrect(d, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


def text(d, xy, s, fnt, fill):
    d.text(xy, s, font=fnt, fill=fill)


# ---------------------------------------------------------------- illustrations
# All art is original flat drawing with PIL primitives — no copied images.

def draw_bahrain(d, x, y, w, h):
    """Night sky, industrial plant, flame. Lead 1."""
    d.rectangle([x, y, x + w, y + h], fill=(23, 32, 54))
    # stars
    for sx, sy in [(30, 18), (90, 10), (150, 24), (210, 12), (300, 20),
                   (360, 8), (430, 22), (470, 14), (60, 34), (250, 30)]:
        d.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1],
                  fill=(250, 246, 236))
    # moon
    d.ellipse([x + w - 52, y + 10, x + w - 22, y + 40], fill=(250, 246, 236))
    d.ellipse([x + w - 46, y + 14, x + w - 28, y + 32], fill=(23, 32, 54))
    # ground
    d.rectangle([x, y + h - 34, x + w, y + h], fill=(12, 18, 32))
    # factory block with lit windows
    d.rectangle([x + 30, y + h - 78, x + 190, y + h - 34], fill=(48, 58, 84))
    for i in range(5):
        wx = x + 44 + i * 30
        d.rectangle([wx, y + h - 66, wx + 16, y + h - 48], fill=GOLD)
    # chimneys + smoke (smoke stays inside the 120px art box)
    for cx in (210, 250, 292):
        d.rectangle([x + cx, y + h - 64, x + cx + 16, y + h - 34],
                    fill=(64, 74, 102))
        for ox, oy, r in [(4, -16, 7), (12, -30, 9), (2, -44, 11)]:
            cy = y + h - 64 + oy
            d.ellipse([x + cx + ox - r, cy - r,
                       x + cx + ox + r, cy + r],
                      fill=(160, 165, 178))
    # flame at the plant's right end
    fx, fy = x + w - 130, y + h - 34
    d.polygon([(fx, fy), (fx + 18, fy - 52), (fx + 30, fy - 22),
               (fx + 44, fy - 44), (fx + 58, fy)], fill=(217, 84, 30))
    d.polygon([(fx + 12, fy), (fx + 24, fy - 30), (fx + 36, fy - 12),
               (fx + 46, fy)], fill=(247, 197, 66))


def draw_cop31(d, x, y, w, h):
    """Pale sky, sun with rays, globe, delegate dots. Lead 2."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 238, 232))
    # sun + rays
    sx, sy = x + w - 70, y + 34
    for k in range(8):
        import math
        a = k * math.pi / 4
        d.line([(sx + 26 * math.cos(a), sy + 26 * math.sin(a)),
                (sx + 38 * math.cos(a), sy + 38 * math.sin(a))],
               fill=GOLD, width=4)
    d.ellipse([sx - 22, sy - 22, sx + 22, sy + 22], fill=GOLD)
    # clouds
    for cx, cy, cw in [(40, 26, 70), (150, 14, 56), (330, 60, 64)]:
        d.ellipse([x + cx, y + cy, x + cx + cw, y + cy + 18], fill=(255, 255, 255))
    # globe
    gx, gy, gr = x + 120, y + h - 52, 46
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(52, 120, 180))
    d.ellipse([gx - 30, gy - 26, gx - 2, gy + 2], fill=(74, 160, 90))
    d.ellipse([gx + 4, gy + 6, gx + 30, gy + 30], fill=(74, 160, 90))
    d.ellipse([gx - 12, gy - 40, gx + 12, gy - 22], fill=(74, 160, 90))
    d.arc([gx - gr, gy - gr, gx + gr, gy + gr], 200, 340, fill=(255, 255, 255), width=2)
    # ground line + delegate dots
    d.rectangle([x, y + h - 12, x + w, y + h], fill=TEAL)
    for i in range(9):
        px = x + 220 + i * 28
        d.ellipse([px, y + h - 34, px + 10, y + h - 24], fill=INK)
        d.rectangle([px - 1, y + h - 24, px + 11, y + h - 12], fill=INK)


def draw_sparta(d, x, y, w, h):
    """Grey-blue sky, burning cargo ship on waves. Lead 3."""
    d.rectangle([x, y, x + w, y + h], fill=(196, 208, 220))
    # smoke
    for ox, oy, r in [(150, 18, 14), (168, 8, 18), (188, 20, 12), (140, 30, 10)]:
        d.ellipse([x + ox - r, y + oy - r, x + ox + r, y + oy + r],
                  fill=(120, 126, 138))
    # sea
    d.rectangle([x, y + h - 46, x + w, y + h], fill=SEA)
    for wy in (y + h - 38, y + h - 26, y + h - 14):
        for wx in range(0, w, 44):
            d.arc([x + wx, wy, x + wx + 30, wy + 12], 180, 360,
                  fill=(255, 255, 255), width=2)
    # hull + superstructure + containers
    d.polygon([(x + 30, y + h - 46), (x + 250, y + h - 46),
               (x + 232, y + h - 78), (x + 48, y + h - 78)], fill=(52, 58, 72))
    d.rectangle([x + 196, y + h - 108, x + 232, y + h - 78], fill=(240, 240, 235))
    d.rectangle([x + 60, y + h - 100, x + 96, y + h - 78], fill=(193, 39, 45))
    d.rectangle([x + 100, y + h - 100, x + 136, y + h - 78], fill=(217, 164, 65))
    d.rectangle([x + 140, y + h - 100, x + 176, y + h - 78], fill=(23, 126, 122))
    # flame on deck
    fx, fy = x + 108, y + h - 78
    d.polygon([(fx, fy), (fx + 12, fy - 34), (fx + 22, fy - 14),
               (fx + 32, fy - 28), (fx + 42, fy)], fill=(217, 84, 30))
    d.polygon([(fx + 10, fy), (fx + 18, fy - 18), (fx + 28, fy - 8),
               (fx + 34, fy)], fill=(247, 197, 66))
    # small drone silhouette
    d.ellipse([x + w - 46, y + 22, x + w - 34, y + 30], fill=INK)
    for dx in (x + w - 50, x + w - 32):
        d.line([(dx, y + 20), (dx + 8, y + 20)], fill=INK, width=2)


def draw_icon(d, x, y, s, kind, bg):
    """40px flat icon on a rounded square."""
    rrect(d, [x, y, x + s, y + s], 8, fill=bg)
    cx, cy = x + s // 2, y + s // 2
    white = (255, 255, 255)
    if kind == "bulb":  # Iran rationing
        d.ellipse([cx - 9, cy - 13, cx + 9, cy + 5], fill=white)
        d.rectangle([cx - 5, cy + 6, cx + 5, cy + 12], fill=white)
        d.line([(cx - 11, cy - 12), (cx + 11, cy + 12)], fill=RED, width=3)
    elif kind == "cuffs":  # El Chapo
        d.ellipse([cx - 13, cy - 8, cx - 1, cy + 4], outline=white, width=3)
        d.ellipse([cx + 1, cy - 8, cx + 13, cy + 4], outline=white, width=3)
        d.line([(cx - 7, cy - 2), (cx + 7, cy - 2)], fill=white, width=3)
        d.line([(cx - 7, cy + 8), (cx + 7, cy + 8)], fill=white, width=3)
    elif kind == "mine":  # Sudan landmine
        d.polygon([(cx, cy - 13), (cx + 13, cy + 9), (cx - 13, cy + 9)],
                  outline=white, width=3)
        d.line([(cx, cy - 6), (cx, cy + 2)], fill=white, width=3)
        d.ellipse([cx - 2, cy + 5, cx + 2, cy + 9], fill=white)
    elif kind == "plane":  # Belgium strike
        d.polygon([(cx - 13, cy), (cx - 2, cy - 4), (cx + 13, cy - 10),
                   (cx + 8, cy - 1), (cx + 13, cy + 8), (cx - 1, cy + 3),
                   (cx - 8, cy + 9), (cx - 9, cy + 2)], fill=white)
        d.line([(cx - 14, cy + 13), (cx + 14, cy - 13)], fill=RED, width=3)
    elif kind == "flag":  # Las Vegas GP
        for i in range(2):
            for j in range(2):
                if (i + j) % 2 == 0:
                    d.rectangle([cx - 12 + i * 10, cy - 11 + j * 9,
                                 cx - 2 + i * 10, cy - 2 + j * 9], fill=white)
        d.line([(cx - 12, cy - 11), (cx - 12, cy + 13)], fill=white, width=3)
        d.line([(cx - 12, cy + 13), (cx + 12, cy + 13)], fill=GOLD, width=3)
    elif kind == "van":  # Gaza aid van
        d.rectangle([cx - 13, cy - 6, cx + 4, cy + 6], fill=white)
        d.polygon([(cx + 4, cy - 6), (cx + 12, cy - 2), (cx + 12, cy + 6),
                   (cx + 4, cy + 6)], fill=white)
        d.ellipse([cx - 9, cy + 4, cx - 3, cy + 10], fill=INK)
        d.ellipse([cx + 5, cy + 4, cx + 11, cy + 10], fill=INK)
        d.rectangle([cx - 8, cy - 3, cx - 2, cy + 3], fill=RED)
    elif kind == "boat":  # Nigeria boat
        d.polygon([(cx - 13, cy - 4), (cx + 13, cy - 4), (cx + 8, cy + 6),
                   (cx - 8, cy + 6)], fill=white)
        d.line([(cx, cy - 4), (cx, cy - 12)], fill=white, width=2)
        d.polygon([(cx, cy - 12), (cx + 8, cy - 5), (cx, cy - 5)], fill=white)
        d.arc([cx - 14, cy + 8, cx - 2, cy + 14], 0, 180, fill=white, width=2)
        d.arc([cx + 2, cy + 8, cx + 14, cy + 14], 0, 180, fill=white, width=2)
    elif kind == "cross":  # Bolsonaro hospital
        d.rectangle([cx - 3, cy - 12, cx + 3, cy + 12], fill=white)
        d.rectangle([cx - 12, cy - 3, cx + 12, cy + 3], fill=white)
    elif kind == "mercury":  # BepiColombo
        d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=(217, 120, 40))
        d.ellipse([cx - 4, cy - 5, cx - 1, cy - 2], fill=(180, 90, 30))
        d.ellipse([cx + 3, cy + 3, cx + 6, cy + 6], fill=(180, 90, 30))
        d.ellipse([cx - 16, cy - 14, cx - 12, cy - 10], outline=white, width=1)
        d.ellipse([cx + 12, cy + 10, cx + 16, cy + 14], outline=white, width=1)
    elif kind == "shield":  # Rutte / NATO
        d.polygon([(cx - 11, cy - 11), (cx + 11, cy - 11), (cx + 11, cy + 1),
                   (cx, cy + 13), (cx - 11, cy + 1)], fill=white)
        d.polygon([(cx, cy - 8), (cx + 2, cy - 2), (cx + 8, cy - 2),
                   (cx + 3, cy + 2), (cx + 5, cy + 8), (cx, cy + 4),
                   (cx - 5, cy + 8), (cx - 3, cy + 2), (cx - 8, cy - 2),
                   (cx - 2, cy - 2)], fill=GOLD)


# ---------------------------------------------------------------- dotted map
CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 73),
     (-75, 72), (-65, 62), (-55, 52), (-60, 47), (-70, 42), (-75, 35),
     (-80, 32), (-85, 30), (-90, 29), (-97, 26), (-105, 22), (-110, 24),
     (-117, 33), (-125, 40), (-125, 48), (-135, 58), (-150, 60), (-165, 60)],
    # Greenland
    [(-58, 64), (-45, 60), (-30, 68), (-25, 76), (-55, 76), (-60, 70)],
    # South America
    [(-80, 10), (-72, 12), (-62, 10), (-52, 5), (-50, -5), (-40, -10),
     (-35, -20), (-40, -30), (-48, -28), (-58, -35), (-65, -40), (-70, -50),
     (-73, -40), (-73, -30), (-70, -20), (-77, -12), (-80, -5), (-81, 5)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (25, 65), (20, 70),
     (12, 70), (5, 60), (-5, 58), (-10, 50), (-10, 43)],
    # Africa
    [(-6, 35), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28), (40, 20),
     (43, 12), (48, 11), (51, 10), (45, 2), (40, -5), (40, -15), (35, -25),
     (30, -32), (20, -35), (15, -30), (12, -18), (13, -10), (9, 4), (0, 5),
     (-8, 5), (-15, 12), (-17, 15), (-16, 20), (-15, 27), (-10, 31)],
    # Asia
    [(30, 62), (40, 68), (55, 68), (70, 72), (90, 75), (110, 76), (130, 72),
     (150, 70), (170, 66), (178, 65), (170, 60), (160, 60), (158, 52),
     (142, 50), (140, 40), (135, 35), (130, 33), (127, 38), (122, 38),
     (120, 30), (115, 23), (108, 18), (105, 10), (100, 8), (97, 15),
     (95, 20), (90, 22), (85, 20), (80, 15), (77, 8), (75, 12), (70, 20),
     (65, 25), (60, 25), (55, 26), (50, 28), (48, 30), (45, 28), (40, 30),
     (35, 36), (30, 36), (28, 40), (30, 45), (32, 50), (30, 55)],
    # Australia
    [(114, -22), (114, -30), (115, -35), (120, -34), (125, -32), (130, -32),
     (135, -35), (140, -38), (145, -38), (150, -37), (153, -32), (153, -27),
     (150, -22), (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
     (132, -12), (130, -13), (126, -14), (122, -17), (118, -20)],
]

ISLANDS = [  # (lon, lat, rx, ry) ellipses in mask space
    (102, -2, 7, 3), (113, -7, 6, 2), (122, -8, 5, 2), (131, -3, 6, 2),
    (140, -4, 5, 2), (127, 1, 4, 2), (-2, 54, 2, 3), (138, 38, 2, 4),
    (170, -42, 2, 3), (174, -39, 2, 2),
]


def build_land_mask(mw=180, mh=90):
    """Small bitmap of land, drawn from the continent polygons."""
    mask = Image.new("L", (mw, mh), 0)
    md = ImageDraw.Draw(mask)

    def px(lon, lat):
        return ((lon + 180) / 360 * mw, (90 - lat) / 180 * mh)

    for poly in CONTINENTS:
        md.polygon([px(lon, lat) for lon, lat in poly], fill=255)
    for lon, lat, rx, ry in ISLANDS:
        cx, cy = px(lon, lat)
        sx, sy = mw / 360, mh / 180
        md.ellipse([cx - rx * sx, cy - ry * sy, cx + rx * sx, cy + ry * sy],
                   fill=255)
    return mask


def draw_map(d, x, y, w, h, pins):
    """Dotted world map with numbered pins. pins: list of (n, lon, lat)."""
    mask = build_land_mask()
    mw, mh = mask.size
    step = 6
    dot = (148, 163, 184)
    for gy in range(y + 2, y + h - 2, step):
        for gx in range(x + 2, x + w - 2, step):
            mx = int((gx - x) / w * mw)
            my = int((gy - y) / h * mh)
            if mask.getpixel((mx, my)):
                d.ellipse([gx - 1, gy - 1, gx + 1, gy + 1], fill=dot)
    # pins: small red circles, white number; nudges keep the Gulf crowded
    nudges = {4: (9, -8), 9: (-8, 8), 13: (5, -8), 2: (0, -4)}
    f_pin = F_SANS_B(8)
    for n, lon, lat in pins:
        px = x + (lon + 180) / 360 * w
        py = y + (75 - lat) / 130 * h
        dx, dy = nudges.get(n, (0, 0))
        px, py = px + dx, py + dy
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=RED,
                  outline=(255, 255, 255), width=1)
        tw = d.textlength(str(n), font=f_pin)
        d.text((px - tw / 2, py - 6), str(n), font=f_pin, fill=(255, 255, 255))


# ---------------------------------------------------------------- layout
def draw_header(d):
    d.rectangle([0, 0, W, 88], fill=NAVY)
    text(d, (16, 12), "THE SUNDAY LEDGER", F_SANS_B(30), (255, 255, 255))
    text(d, (16, 54), "THE WORLD IN ONE DAY", F_SANS_B(13), GOLD)
    f1, f2 = F_SANS_B(15), F_SANS_B(30)
    s1, s2 = "SUNDAY", "22 NOVEMBER 2026"
    d.text((W - 16 - d.textlength(s1, font=f1), 12), s1, font=f1, fill=GOLD)
    d.text((W - 16 - d.textlength(s2, font=f2), 34), s2, font=f2,
           fill=(255, 255, 255))
    d.rectangle([0, 88, W, 91], fill=GOLD)


def draw_numbers(d):
    y0, h = 92, 58
    tw = (W - 24 - 5 * 8) // 6
    for i, (num, label, cap) in enumerate(NUMBERS):
        x = 12 + i * (tw + 8)
        rrect(d, [x, y0, x + tw, y0 + h], 6, fill=CARD, outline=LINE, width=1)
        f_num = F_SANS_B(26 if len(num) <= 3 else 21)
        nw = d.textlength(num, font=f_num)
        d.text((x + (tw - nw) / 2, y0 + 4), num, font=f_num, fill=INK)
        lw = d.textlength(label, font=F_SANS_B(9))
        d.text((x + (tw - lw) / 2, y0 + 33), label, font=F_SANS_B(9), fill=INK)
        cw = d.textlength(cap, font=F_SANS(9))
        d.text((x + (tw - cw) / 2, y0 + 45), cap, font=F_SANS(9), fill=GRAY)


ART = {"bahrain": draw_bahrain, "cop31": draw_cop31}


def draw_lead(d, s, x, y, w, h):
    rrect(d, [x, y, x + w, y + h], 4, fill=CARD, outline=LINE, width=1)
    ART[s["art"]](d, x + 1, y + 1, w - 2, 120)
    text(d, (x + 12, y + 128), "%d · %s · %s" % (s["n"], s["region"], s["day"]),
         F_SANS_B(10), RED)
    ty = y + 146
    for line in wrap(d, s["title"], F_SERIF_B(20), w - 24):
        text(d, (x + 12, ty), line, F_SERIF_B(20), INK)
        ty += 24
    ty += 2
    for line in wrap(d, s["deck"], F_SANS(11), w - 24):
        text(d, (x + 12, ty), line, F_SANS(11), (40, 40, 40))
        ty += 15
    text(d, (x + 12, y + h - 15), "Source: " + s["source"], F_SANS(9), GRAY)


def draw_sparta_banner(d, s, x, y, w, h):
    rrect(d, [x, y, x + w, y + h], 4, fill=CARD, outline=LINE, width=1)
    draw_sparta(d, x + 1, y + 1, 300, h - 2)
    tx = x + 316
    text(d, (tx, y + 10), "%d · %s · %s" % (s["n"], s["region"], s["day"]),
         F_SANS_B(10), RED)
    ty = y + 28
    for line in wrap(d, s["title"], F_SERIF_B(20), w - 316 - 16):
        text(d, (tx, ty), line, F_SERIF_B(20), INK)
        ty += 24
    ty += 2
    for line in wrap(d, s["deck"], F_SANS(11), w - 316 - 16):
        text(d, (tx, ty), line, F_SANS(11), (40, 40, 40))
        ty += 15
    text(d, (tx, y + h - 15), "Source: " + s["source"], F_SANS(9), GRAY)


def draw_regions(d, y):
    text(d, (12, y + 5), "28 STORIES · 7 REGIONS", F_SANS_B(11), INK)
    fnt = F_SANS_B(10)
    widths = [d.textlength("%s %d" % (r, c), font=fnt) + 16 for r, c in REGIONS]
    total = sum(widths) + 6 * (len(widths) - 1)
    x = W - 12 - total
    for (r, c), pw in zip(REGIONS, widths):
        rrect(d, [x, y, x + pw, y + 20], 10, outline=INK, width=1)
        text(d, (x + 8, y + 4), "%s %d" % (r, c), fnt, INK)
        x += pw + 6


ICON_BG = {"bulb": GOLD, "cuffs": NAVY, "mine": RED, "plane": TEAL,
           "flag": INK, "van": (176, 62, 62), "boat": SEA, "cross": TEAL,
           "mercury": (20, 20, 28), "shield": NAVY}


def draw_cards(d):
    for i, s in enumerate(CARDS):
        col, row = i % 2, i // 2
        x = 12 + col * 506
        y = 586 + row * 48
        rrect(d, [x, y, x + 494, y + 46], 4, fill=CARD, outline=LINE, width=1)
        draw_icon(d, x + 3, y + 3, 40, s["icon"], ICON_BG[s["icon"]])
        tx = x + 48
        title = "%d · %s" % (s["n"], s["title"])
        text(d, (tx, y + 4), fit(d, title, F_SANS_B(12), 440), F_SANS_B(12), INK)
        text(d, (tx, y + 20), fit(d, s["deck"], F_SANS(10), 440), F_SANS(10),
             (40, 40, 40))
        text(d, (tx, y + 34), "%s · %s" % (s["day"], s["source"]), F_SANS(9), GRAY)


def draw_bottom(d):
    y0 = 834
    text(d, (12, y0), "ALSO ON", F_SANS_B(13), INK)
    note = "28 stories · sources beside each one"
    d.text((660 - d.textlength(note, font=F_SANS(9)), y0 + 2), note,
           font=F_SANS(9), fill=GRAY)
    d.line([(12, y0 + 18), (660, y0 + 18)], fill=LINE, width=1)
    for i, (n, txt, src) in enumerate(INDEX):
        col = 0 if i < 8 else 1
        row = i if i < 8 else i - 8
        x = 12 if col == 0 else 340
        y = y0 + 26 + row * 20
        num = "%d · " % n
        d.text((x, y), num, font=F_SANS_B(10), fill=RED)
        nx = x + d.textlength(num, font=F_SANS_B(10))
        line = fit(d, txt + " — " + src, F_SANS(10), 660 - nx if col == 0 else 660 - nx)
        # column width is 320; clamp the fit width to the column
        col_w = 320 - (nx - x) - 4
        line = fit(d, txt + " — " + src, F_SANS(10), col_w)
        d.text((nx, y), line, font=F_SANS(10), fill=(40, 40, 40))
    # map
    text(d, (672, y0), "WHERE IT HAPPENED · 12 PLACES PINNED", F_SANS_B(11), INK)
    d.line([(672, y0 + 18), (1012, y0 + 18)], fill=LINE, width=1)
    pins = [(s["n"], s["pin"][0], s["pin"][1]) for s in STORIES if s.get("pin")]
    draw_map(d, 672, y0 + 24, 340, 92, pins)
    # date check
    by = y0 + 24 + 92 + 8
    d.rectangle([672, by, 1012, 1016], outline=RED, width=2)
    text(d, (680, by + 5), "NOT TODAY — CHECKED AND LEFT OUT", F_SANS_B(10), RED)
    items = [("Voyager 1 light-day", "18 Nov"),
             ("Poland missiles", "Fri 20 Nov"),
             ("Kryvyi Rih strike", "Sat 21 Nov"),
             ("Norway oil ruling", "13 Nov"),
             ("Al-Shabaab ambush", "26 Oct"),
             ("Las Vegas GP result", "not yet run")]
    for i, (nm, dt) in enumerate(items):
        col, row = i % 2, i // 2
        x = 680 + col * 168
        y = by + 22 + row * 12
        text(d, (x, y), "%s — %s" % (nm, dt), F_SANS(9), (40, 40, 40))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    draw_numbers(d)
    for i, s in enumerate(LEADS[:2]):
        draw_lead(d, s, 12 + i * 504, 150, 496, 266)
    draw_sparta_banner(d, LEADS[2], 12, 416, 1000, 140)
    draw_regions(d, 556)
    draw_cards(d)
    draw_bottom(d)
    img.save(OUT, optimize=True)
    import hashlib
    b = open(OUT, "rb").read()
    print("entry.png: %dx%d, %d bytes, sha256 %s"
          % (img.size[0], img.size[1], len(b), hashlib.sha256(b).hexdigest()))
    assert len(b) <= 1048576, "entry.png over 1 MiB"


if __name__ == "__main__":
    main()
