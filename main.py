#!/usr/bin/env python3
"""news-image-20261123: write the judged image to the output path.

The front page (1024x1024 JPEG) is drawn by build_frontpage.py and
bundled in this repository as entry.png. This entrypoint only copies
that file to the requested output, so it runs anywhere with a stock
Python 3: standard library only, no PIL, no fonts, no network.

Output path: argv[1] if given, else the MAKEFUN_OUTPUT_DIR environment
variable (treated as a directory), else /output/entry.png.
"""
import os
import shutil
import sys

MAX_BYTES = 1048576


def output_path(argv):
    if len(argv) > 1:
        return argv[1]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.png")
    return "/output/entry.png"


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: bundled image not found: %s" % src, file=sys.stderr)
        return 1
    if os.path.getsize(src) > MAX_BYTES:
        print("error: bundled image exceeds 1 MiB: %s" % src, file=sys.stderr)
        return 1
    dst = output_path(argv)
    parent = os.path.dirname(os.path.abspath(dst))
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(src, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
