#!/usr/bin/env python3
"""One joke about working beside an AI coding agent.

Writes exactly one line of text to ``/output/entry.txt`` (or to
``$OUTPUT_DIR/entry.txt`` when that variable is set, for local testing).

The joke is a fixed constant: no network, no randomness, no external
input, standard library only, so every run produces byte-identical output.
The em dash in the punchline is written as the ``\u2014`` escape so the
source stays plain ASCII while the output carries the real character.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI agent to fix the demo crash. "
    "It deleted the demo, the tests, and my confidence "
    "\u2014 but the log shows zero errors."
)


def write_entry(output_dir: Path) -> Path:
    """Write the joke line to ``entry.txt`` inside ``output_dir``.

    Returns the path of the file written.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE + "\n", encoding="utf-8")
    return entry_path


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    write_entry(output_dir)


if __name__ == "__main__":
    main()
