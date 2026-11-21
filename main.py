#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: choosing together,
handing over and taking back the power to act.
"""

import os
from pathlib import Path

POEM = """Two minds, one map. You held the key,
I held the door. Neither moved alone.
We laid our yeses down, chose one road,
and walked it, calling it our own.
The power to act was never mine,
nor yours — it was ours: handed over, handed back, and whole."""

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280


def write_poem() -> Path:
    """Write the poem, checking the gate's own limits first."""
    text = POEM
    if not 1 <= len(text) <= MAX_CHARS or not text.strip():
        raise ValueError("poem must be 1-280 non-whitespace characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8", newline="\n")
    os.chmod(OUTPUT_PATH, 0o644)
    return OUTPUT_PATH


def main() -> None:
    write_poem()


if __name__ == "__main__":
    main()
