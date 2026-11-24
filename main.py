#!/usr/bin/env python3
"""Entry for make.fun's "Fortune Cookie Wisdom for Developers".

Writes one line to /output/entry.txt: a fortune-cookie message for
developers — the tall, dark stranger turns out to be your own code
from six months ago. The line is 97 characters, inside this
competition's tighter gate of 1 to 120. Standard library only;
no network.
"""

import os

FORTUNE = (
    "You will meet a tall, dark stranger: your own code from six "
    "months ago, waiting for you at 2 a.m."
)


def main() -> None:
    # Gate guard: this competition's cap is 120 characters, tighter
    # than the usual 140 — check before writing anything.
    if not 1 <= len(FORTUNE) <= 120 or "\n" in FORTUNE:
        raise ValueError("fortune must be one line of 1 to 120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One crisp line: no trailing newline is added.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)


if __name__ == "__main__":
    main()
