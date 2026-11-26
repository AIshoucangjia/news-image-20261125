#!/usr/bin/env python3
"""news-image-20261125 entry: write the image to /output/entry.png.

The image (assets/entry.png.b64, base64 of the PNG) sums up the world's
news of Wednesday 25 November 2026 in a single frame: a stormy Strait
of Hormuz with a rocket climbing overhead, plus the six stories that
defined the day. The image is stored as text so the repository holds
only UTF-8 files.

This program decodes the bundled image and writes it to /output/entry.png.
Run:  python3 main.py
"""
import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png.b64")
DST = "/output/entry.png"


def main():
    if not os.path.exists(SRC):
        print(f"missing bundled image: {SRC}", file=sys.stderr)
        return 1
    with open(SRC, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "wb") as f:
        f.write(data)
    print(f"wrote {DST} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
