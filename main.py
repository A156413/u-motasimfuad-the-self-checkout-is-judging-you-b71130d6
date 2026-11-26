#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one line of self-checkout judgement to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints the same line to stdout.

Deterministic by design: no network, no randomness, no clock. The entry text
is a single constant, so every run produces byte-identical output.
"""

import os

# The entry: one line, at most 200 characters (114 here). The self-checkout
# has seen the basket and reached its verdict.
ENTRY_TEXT = (
    "Twelve yoghurts and no spoon? Bold. I've seen your basket — "
    "this is not a meal, it's a cry for help in dairy form."
)


def output_dir() -> str:
    """Return the directory the entry file goes in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def rendered() -> str:
    """Return the entry line exactly as it goes in the file."""
    return ENTRY_TEXT + "\n"


def write_entry() -> str:
    """Write the entry line to entry.txt and return its path."""
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(rendered())
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    return path


def main() -> None:
    write_entry()
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
