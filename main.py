"""Write the make.fun entry text to entry.txt.

Bounty: u-ronigrv-a-day-of-one-line-pitches-12cd9bb3

Standard library only, Python 3.13, no network.
"""

import os
import sys

TEXT = "My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
