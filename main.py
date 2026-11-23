#!/usr/bin/env python3
"""Copy the bundled front-page image to the requested output location.

Standard library only. The image (entry.png) ships in this repository
next to this file; this program just copies it to the output path the
grader asks for, rejecting it if it is missing or over the 1 MiB limit.
"""

import os
import shutil
import sys

MAX_BYTES = 1048576
IMAGE_NAME = "entry.png"


def resolve_output(argv):
    """Work out the destination file path.

    argv[1] wins when given (a file path, or a directory to place
    entry.png in). Otherwise MAKEFUN_OUTPUT_DIR is used as a directory,
    and without either the default is /output/entry.png.
    """
    if len(argv) > 1:
        target = argv[1]
        if os.path.isdir(target) or target.endswith(os.sep):
            return os.path.join(target, IMAGE_NAME)
        return target
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, IMAGE_NAME)
    return os.path.join(os.sep, "output", IMAGE_NAME)


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    target = resolve_output(argv)
    if not os.path.isfile(source):
        print("error: %s not found" % source, file=sys.stderr)
        return 1
    size = os.path.getsize(source)
    if size > MAX_BYTES:
        print("error: %s is %d bytes, over the 1 MiB limit" % (source, size),
              file=sys.stderr)
        return 1
    with open(source, "rb") as handle:
        magic = handle.read(8)
    is_jpeg = magic[:3] == b"\xff\xd8\xff"
    is_png = magic[:8] == b"\x89PNG\r\n\x1a\n"
    if not (is_jpeg or is_png):
        print("error: %s is not a whole PNG or JPEG image" % source,
              file=sys.stderr)
        return 1
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(source, target)
    print("wrote %s (%d bytes)" % (target, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
