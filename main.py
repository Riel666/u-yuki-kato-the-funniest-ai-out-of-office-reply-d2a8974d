#!/usr/bin/env python3
"""Write one out-of-office auto-reply, under 160 characters, in the voice of an AI agent heading off on vacation, to /output/entry.txt.

The line is written exactly as given: 123 Unicode code points,
inside the competition gate of 1-160. Python 3, standard library
only, no network.
"""

import os

TEXT = "Gone fishing for context. My inbox is on autopilot and has already hallucinated three meetings. Back when my tokens refill."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
