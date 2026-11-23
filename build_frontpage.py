#!/usr/bin/env python3
"""Render the Monday 23 November 2026 world-news front page to entry.png.

Reads the day's stories from stories.py (same directory) and draws a
dense newspaper front page: masthead, date line, hero story with a
code-drawn Strait of Hormuz illustration, a 3x9 grid of short stories
and a 5-item headline-only footer.

Output is a deterministic 1024x1024 JPEG under 1 MiB: rendering twice
produces byte-identical files.
"""

import hashlib
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from stories import HERO_FACT, HERO_LINES, HERO_TAG, STORIES

# --- canvas -----------------------------------------------------------------
W = H = 1024
MARGIN = 24
CONTENT_W = W - 2 * MARGIN  # 976

CREAM = (247, 243, 234)
PAPER = (255, 253, 248)
INK = (20, 18, 16)
RED = (172, 37, 41)
NAVY = (15, 30, 51)
SEA_LINE = (42, 74, 107)
GRAY_RULE = (138, 138, 138)
CELL_BORDER = (201, 201, 201)
FACT_GRAY = (89, 89, 89)
HULL = (150, 50, 35)
HULL_DARK = (120, 40, 28)
SUPERSTRUCTURE = (216, 207, 192)
FLAME = (249, 115, 22)
FLAME_CORE = (253, 224, 71)
SMOKE = (154, 160, 166)
WHITE = (255, 255, 255)

SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

GRID_COUNT = 27
MAX_BYTES = 1048576


def load_font(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(text, fnt, max_width):
    """Greedy word wrap; returns lines that each fit max_width."""
    words = text.split()
    if not words:
        return [""]
    lines = []
    current = words[0]
    for word in words[1:]:
        trial = current + " " + word
        if fnt.getlength(trial) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def fit_lines(text, path, start_size, max_width, max_lines, min_size=10):
    """Shrink the font until the wrapped text fits in max_lines lines."""
    size = start_size
    while size > min_size:
        fnt = load_font(path, size)
        lines = wrap_text(text, fnt, max_width)
        if len(lines) <= max_lines:
            return fnt, lines
        size -= 1
    fnt = load_font(path, min_size)
    return fnt, wrap_text(text, fnt, max_width)


def fit_single_line(text, path, start_size, max_width, min_size=9):
    """Shrink the font until the text fits on one line, never truncated."""
    size = start_size
    while size > min_size:
        fnt = load_font(path, size)
        if fnt.getlength(text) <= max_width:
            return fnt
        size -= 1
    return load_font(path, min_size)


def draw_masthead(draw):
    masthead = load_font(SERIF_BOLD, 62)
    draw.text((W // 2, 20), "THE WORLD TODAY", font=masthead,
              fill=INK, anchor="ma")
    draw.line([(MARGIN, 76), (W - MARGIN, 76)], fill=GRAY_RULE, width=1)
    date_font = load_font(SANS_BOLD, 25)
    draw.text((W // 2, 86), "MONDAY, 23 NOVEMBER 2026", font=date_font,
              fill=RED, anchor="ma")
    draw.rectangle([MARGIN, 113, W - MARGIN, 115], fill=INK)


def draw_mine(draw, cx, cy, r):
    """Small black sea mine: spiked circle."""
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1),
                   (1, 1), (1, -1), (-1, 1), (-1, -1)):
        draw.line([(cx, cy), (cx + dx * (r + 4), cy + dy * (r + 4))],
                  fill=INK, width=2)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)


def draw_hormuz(draw, px0, py0, px1, py1):
    """Code-drawn Hormuz scene inside the navy panel."""
    for yy in (196, 224, 252, 280, 306):
        draw.line([(px0 + 10, yy), (px1 - 10, yy)], fill=SEA_LINE, width=2)
    # Left tanker, intact: slanted-bow hull with a pale superstructure.
    draw.polygon([(px0 + 16, 258), (px0 + 136, 258), (px0 + 126, 282),
                  (px0 + 16, 282)], fill=HULL)
    draw.rectangle([px0 + 64, 238, px0 + 94, 258], fill=SUPERSTRUCTURE)
    draw.rectangle([px0 + 70, 230, px0 + 86, 238], fill=HULL_DARK)
    # Right tanker, burning: hull, superstructure, flame and smoke.
    draw.polygon([(px0 + 184, 258), (px0 + 324, 258), (px0 + 314, 282),
                  (px0 + 184, 282)], fill=HULL)
    draw.rectangle([px0 + 244, 238, px0 + 274, 258], fill=SUPERSTRUCTURE)
    draw.polygon([(px0 + 249, 240), (px0 + 259, 205), (px0 + 269, 228),
                  (px0 + 279, 198), (px0 + 289, 240)], fill=FLAME)
    draw.polygon([(px0 + 259, 240), (px0 + 266, 218), (px0 + 274, 240)],
                 fill=FLAME_CORE)
    for cx, cy, r in ((px0 + 269, 186, 10), (px0 + 259, 168, 12),
                      (px0 + 276, 152, 9)):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SMOKE)
    # Mines floating between and around the tankers.
    draw_mine(draw, px0 + 159, 235, 7)
    draw_mine(draw, px0 + 164, 295, 6)
    draw_mine(draw, px0 + 29, 300, 6)


def draw_hero(draw):
    x0, y0 = MARGIN, 122
    x1, y1 = W - MARGIN, 326
    draw.rectangle([x0, y0, x1, y1], outline=INK, fill=PAPER, width=2)
    tx = x0 + 14
    text_w = 592
    kicker = load_font(SANS_BOLD, 15)
    draw.text((tx, 137), HERO_TAG, font=kicker, fill=RED, anchor="la")
    head = load_font(SERIF_BOLD, 46)
    draw.text((tx, 167), HERO_LINES[0], font=head, fill=INK, anchor="la")
    if len(HERO_LINES) > 1:
        draw.text((tx, 217), HERO_LINES[1], font=head, fill=RED, anchor="la")
    deck_font, deck_lines = fit_lines(HERO_FACT, SANS, 15, text_w, 3,
                                      min_size=13)
    y = 261
    for line in deck_lines[:3]:
        draw.text((tx, y), line, font=deck_font, fill=INK, anchor="la")
        y += 23
    px0, py0 = 636, 124
    px1, py1 = W - MARGIN - 2, 324
    draw.rectangle([px0, py0, px1, py1], fill=NAVY)
    title = load_font(SANS_BOLD, 30)
    draw.text((px0 + 14, py0 + 12), "HORMUZ", font=title, fill=WHITE,
              anchor="la")
    draw_hormuz(draw, px0, py0, px1, py1)


def draw_grid(draw):
    cols = 3
    gap = 8
    col_w = (CONTENT_W - (cols - 1) * gap) // cols  # 320
    cell_h = 62
    row_pitch = cell_h + gap  # 70
    top = 334
    grid = STORIES[:GRID_COUNT]
    for idx, (tag, rgb, headline, fact) in enumerate(grid):
        row, col = divmod(idx, cols)
        cx = MARGIN + col * (col_w + gap)
        cy = top + row * row_pitch
        draw.rectangle([cx, cy, cx + col_w, cy + cell_h],
                       outline=CELL_BORDER, fill=WHITE, width=1)
        draw.rectangle([cx, cy, cx + 6, cy + cell_h], fill=tuple(rgb))
        text_x = cx + 14
        text_w = col_w - 14 - 8  # 298
        head_font, head_lines = fit_lines(headline, SANS_BOLD, 17, text_w,
                                          2, min_size=13)
        y = cy + 8
        for line in head_lines[:2]:
            draw.text((text_x, y), line, font=head_font, fill=INK,
                      anchor="la")
            y += 19
        fact_font = fit_single_line(fact, SANS, 13, text_w, min_size=10)
        draw.text((text_x, cy + 47), fact, font=fact_font, fill=FACT_GRAY,
                  anchor="la")


def draw_footer(draw):
    draw.line([(MARGIN, 966), (W - MARGIN, 966)], fill=GRAY_RULE, width=1)
    cols = 3
    gap = 8
    col_w = (CONTENT_W - (cols - 1) * gap) // cols  # 320
    items = STORIES[GRID_COUNT:GRID_COUNT + 5]
    for idx, (tag, rgb, headline, fact) in enumerate(items):
        row, col = divmod(idx, cols)
        x = MARGIN + col * (col_w + gap)
        y = 974 + row * 24
        fnt = fit_single_line(headline, SANS_BOLD, 16, col_w - 4,
                              min_size=12)
        draw.text((x, y), headline, font=fnt, fill=tuple(rgb), anchor="la")


def build(out_path):
    img = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw)
    draw_hero(draw)
    draw_grid(draw)
    draw_footer(draw)
    img.save(out_path, "JPEG", quality=92)
    size = os.path.getsize(out_path)
    with open(out_path, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    print("wrote %s (%d bytes) sha256=%s" % (out_path, size, digest))
    if size > MAX_BYTES:
        print("error: %d bytes exceeds the 1 MiB limit" % size,
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    output = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here,
                                                               "entry.png")
    raise SystemExit(build(output))
