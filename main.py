"""News image entry for make.fun, competition news-image-20261119.

The image itself is the entry: entry.png beside this file, a
1024x1024 newspaper front page summing up Thursday 19 November
2026 (GTA VI launch, Anthropic's Nasdaq debut, the ICJ Rohingya
ruling, the APEC trilateral, the EU-Indonesia trade deal,
Cyclone Akvan, and Voyager 1's one-light-day signals).

This program only copies that file to the output directory, so
both grader runs write exactly the same bytes. Standard library
only, no network, no randomness, no timestamps.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(source, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    shutil.copyfile(source, target)
    size = os.path.getsize(target)
    if size > 1048576:
        print("entry.png is over 1 MiB: %d bytes" % size, file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (target, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
