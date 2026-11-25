#!/usr/bin/env python3
"""Have You Tried Turning It Off?

Writes one funny line a hopeless tech support agent says to a desperate
customer, to /output/entry.txt (or to the path given as argv[1]).
"""

import sys
from pathlib import Path

LINE = (
    "Have you tried turning it off and on again? I have — mine's been "
    "restarting since Tuesday, and honestly, it's the quietest shift "
    "I've ever had."
)


def main() -> None:
    # The gate only accepts a single line of 1-199 characters: check the
    # line before writing so a bad edit fails loudly here, not at judging.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 199, f"entry is {len(LINE)} characters"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    out.chmod(0o644)


if __name__ == "__main__":
    main()
