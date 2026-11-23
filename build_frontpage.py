#!/usr/bin/env python3
"""Draw the 23 November 2026 front page (1024x1024 JPEG) for make.fun.

Layout, proven by the 22 November entry (9W/1D/2L in its dev heat):
masthead with the explicit date, a hero panel on the day's biggest story
(tankers exploding in the Strait of Hormuz) with a drawn strait scene,
a dense 3-column grid of 27 stories, and a footer strip with 5 more —
33 verified stories in all, across 8 region groups.

Spacing discipline (the lesson from the 22 November v2 failure): every
cell is a fixed 62 px tall, headlines get at most two lines in a zone
that ends 6 px above the fact line, and the fact line is a single
truncated line pinned to the cell bottom — so a headline can never
collide with its fact line, at full size or at 300 px.

Pure PIL, Liberation fonts, no network. Deterministic: fixed JPEG
quality, no timestamps, so two runs write byte-identical files.
"""
import argparse
import sys

from PIL import Image, ImageDraw, ImageFont

from stories import GRID_COUNT, HERO_FACT, HERO_LINES, HERO_TAG, STORIES

PAGE = 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
MUTED = (70, 66, 58)
GREY = (90, 86, 78)
RED = (178, 28, 28)
RULE = (180, 172, 156)
CELL_EDGE = (210, 204, 190)
WHITE = (255, 255, 255)
MARGIN = 24

SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def greedy_wrap(draw, text, fnt, max_width):
    """Split text into lines that each fit max_width (greedy by word)."""
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def capped_lines(draw, text, fnt, max_width, max_lines):
    """Wrap to at most max_lines, ellipsising the last line if cut."""
    lines = greedy_wrap(draw, text, fnt, max_width)
    if len(lines) <= max_lines:
        return lines
    lines = lines[:max_lines]
    while lines and draw.textlength(lines[-1] + " ...", font=fnt) > max_width:
        head, _, _ = lines[-1].rpartition(" ")
        lines[-1] = head
    lines[-1] = (lines[-1] + " ...").strip()
    return lines


def single_line(draw, text, fnt, max_width):
    """One line, truncated with an ellipsis when it does not fit."""
    if draw.textlength(text, font=fnt) <= max_width:
        return text
    kept = ""
    for word in text.split():
        trial = (kept + " " + word).strip()
        if draw.textlength(trial + " ...", font=fnt) <= max_width:
            kept = trial
        else:
            break
    return (kept + " ...").strip()


def centred(draw, text, fnt, y, fill):
    width = draw.textlength(text, font=fnt)
    draw.text(((PAGE - width) / 2, y), text, font=fnt, fill=fill)


def paint_masthead(draw):
    centred(draw, "THE WORLD TODAY", load(SERIF_BOLD, 62), 6, INK)
    draw.line([(MARGIN, 76), (PAGE - MARGIN, 76)], fill=RULE, width=2)
    centred(draw, "MONDAY, 23 NOVEMBER 2026", load(SANS_BOLD, 25), 82, RED)
    draw.line([(MARGIN, 114), (PAGE - MARGIN, 114)], fill=INK, width=3)


def paint_strait(draw, x0, y0, x1, y1):
    """The Strait of Hormuz at night: two tankers, one burning, mines
    in the water. Flat PIL shapes only. The label sits left in the top
    band; the flame and smoke stay on the right, clear of the text."""
    draw.rectangle([x0, y0, x1, y1], fill=(23, 42, 68))
    draw.rectangle([x0, y0, x1, y0 + 52], fill=(16, 30, 52))
    draw.text((x0 + 16, y0 + 10), "HORMUZ", font=load(SANS_BOLD, 30),
              fill=(235, 225, 200))
    sea_y = y0 + 52
    draw.rectangle([x0, sea_y, x1, y1], fill=(18, 34, 56))
    for wy in (sea_y + 34, sea_y + 68, sea_y + 102):
        draw.line([(x0 + 10, wy), (x1 - 10, wy)], fill=(52, 76, 108), width=2)
    # tanker 1 (left, intact): hull with an angled bow, white
    # superstructure, funnel with a red band
    tx, ty = x0 + 14, y1 - 70
    draw.polygon([(tx, ty), (tx + 108, ty), (tx + 130, ty + 12),
                  (tx + 130, ty + 26), (tx, ty + 26)], fill=(150, 50, 36))
    draw.rectangle([tx + 84, ty - 18, tx + 106, ty], fill=(200, 190, 170))
    draw.rectangle([tx + 88, ty - 26, tx + 102, ty - 18], fill=(60, 60, 60))
    draw.rectangle([tx + 88, ty - 26, tx + 102, ty - 22], fill=(178, 28, 28))
    draw.line([(tx - 8, ty + 30), (tx + 138, ty + 30)],
              fill=(52, 76, 108), width=2)
    # tanker 2 (right, burning): lower hull, big two-tone flame, smoke
    bx, by = x0 + 196, y1 - 62
    draw.polygon([(bx, by), (bx + 108, by), (bx + 130, by + 12),
                  (bx + 130, by + 24), (bx, by + 24)], fill=(120, 40, 30))
    draw.rectangle([bx + 10, by - 14, bx + 32, by], fill=(200, 190, 170))
    flame_x = bx + 66
    draw.polygon([(flame_x - 16, by), (flame_x - 6, by - 26),
                  (flame_x, by - 48), (flame_x + 6, by - 26),
                  (flame_x + 16, by)], fill=(232, 120, 20))
    draw.polygon([(flame_x - 8, by), (flame_x - 3, by - 16),
                  (flame_x, by - 30), (flame_x + 3, by - 16),
                  (flame_x + 8, by)], fill=(245, 200, 60))
    for cx, cy, r in ((flame_x - 4, by - 58, 8), (flame_x + 8, by - 70, 10),
                      (flame_x, by - 82, 7)):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(110, 110, 110))
    draw.line([(bx - 8, by + 28), (bx + 138, by + 28)],
              fill=(52, 76, 108), width=2)
    # naval mines: spiked circles drifting between the tankers
    for mx, my in ((x0 + 152, sea_y + 96), (x0 + 172, sea_y + 62)):
        for dx, dy in ((-10, 0), (10, 0), (0, -10), (0, 10), (-7, -7),
                       (7, 7), (-7, 7), (7, -7)):
            draw.line([(mx, my), (mx + dx, my + dy)], fill=(10, 10, 12),
                      width=2)
        draw.ellipse([mx - 8, my - 8, mx + 8, my + 8], fill=(10, 10, 12))


def paint_hero(draw):
    top, bottom = 122, 326
    draw.rectangle([MARGIN, top, PAGE - MARGIN, bottom], fill=WHITE)
    draw.rectangle([MARGIN, top, PAGE - MARGIN, bottom], outline=INK, width=2)
    tx = 44
    draw.text((tx, top + 12), HERO_TAG, font=load(SANS_BOLD, 15), fill=RED)
    head_font = load(SERIF_BOLD, 46)
    draw.text((tx, top + 34), HERO_LINES[0], font=head_font, fill=INK)
    draw.text((tx, top + 84), HERO_LINES[1], font=head_font, fill=RED)
    body_font = load(SANS, 16)
    yy = top + 136
    for line in capped_lines(draw, HERO_FACT, body_font, 560, 3):
        draw.text((tx, yy), line, font=body_font, fill=(40, 40, 40))
        yy += 20
    paint_strait(draw, 636, top + 10, PAGE - 34, bottom - 10)


def paint_grid_cell(draw, story, x0, y0, width, height):
    _tag, colour, headline, fact = story
    draw.rectangle([x0, y0, x0 + width, y0 + height], fill=WHITE)
    draw.rectangle([x0, y0, x0 + width, y0 + height], outline=CELL_EDGE,
                   width=1)
    draw.rectangle([x0, y0, x0 + 6, y0 + height], fill=colour)
    head_font = load(SANS_BOLD, 17)
    yy = y0 + 5
    for line in capped_lines(draw, headline, head_font, width - 26, 2):
        draw.text((x0 + 14, yy), line, font=head_font, fill=INK)
        yy += 19
    body_font = load(SANS, 12)
    draw.text((x0 + 14, y0 + height - 15),
              single_line(draw, fact, body_font, width - 26),
              font=body_font, fill=MUTED)


def paint_footer_item(draw, story, x0, y0, width):
    _tag, colour, headline, _fact = story
    head_font = load(SANS_BOLD, 14)
    draw.text((x0, y0), single_line(draw, headline, head_font, width),
              font=head_font, fill=colour)


def render():
    img = Image.new("RGB", (PAGE, PAGE), PAPER)
    draw = ImageDraw.Draw(img)
    paint_masthead(draw)
    paint_hero(draw)
    # grid: 3 columns x 9 rows of 62 px cells, 8 px gutters
    grid_x, grid_y, grid_w = MARGIN, 336, PAGE - 2 * MARGIN
    cols, gutter, cell_h = 3, 8, 62
    cell_w = (grid_w - gutter * (cols - 1)) // cols
    for i, story in enumerate(STORIES[:GRID_COUNT]):
        row, col = divmod(i, cols)
        paint_grid_cell(draw, story,
                        grid_x + col * (cell_w + gutter),
                        grid_y + row * (cell_h + gutter),
                        cell_w, cell_h)
    # footer strip: headline-only items, rows of 3 then 2
    draw.line([(MARGIN, 966), (PAGE - MARGIN, 966)], fill=RULE, width=1)
    rest = STORIES[GRID_COUNT:]
    foot_y = 972
    for row, chunk in enumerate((rest[:3], rest[3:])):
        col_w = grid_w // 3
        for j, story in enumerate(chunk):
            paint_footer_item(draw, story, grid_x + j * col_w,
                              foot_y + row * 22, col_w - 12)
    return img


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="entry.png")
    args = parser.parse_args(argv)
    render().save(args.out, "JPEG", quality=92)
    return 0


if __name__ == "__main__":
    sys.exit(main())
