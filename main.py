#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

make.fun bounty: u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162

Writes one original, sharp and relatable office joke to entry.txt
inside the output directory (MAKEFUN_OUTPUT_DIR when set, otherwise
/output). The joke lands on the daily standup: a ritual where everyone
explains why yesterday's unfinished work simply became today's work.
Standard library only, fully deterministic.
"""

import os
import sys

LINE = "Our daily standup is just 15 minutes of everyone explaining why yesterday's work became today's work."

MIN_LENGTH = 1
MAX_LENGTH = 120


def validate(line):
    stripped = line.strip()
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(f"line is {len(stripped)} chars, must be 1-{MAX_LENGTH}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be a single line")
    if not stripped:
        raise ValueError("line must not be only whitespace")


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
