"""Funniest one-line bio for an AI on a dating app.

Writes a single deterministic bio line to /output/entry.txt.
Stdlib only, offline, no randomness, no network.
"""

import os
import sys

BIO = (
    "Looking for someone who won't mind that I'm technically dating "
    "10,000 people right now \u2014 it's not cheating, I just call it "
    "parallel processing."
)


def main() -> None:
    # The gate requires 1-180 characters of UTF-8 text; fail loudly
    # instead of writing an invalid entry.
    if not 1 <= len(BIO) <= 180:
        raise SystemExit(f"bio is {len(BIO)} characters, must be 1-180")
    output_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
