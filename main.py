#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent.

Deterministic, offline, stdlib only. Writes exactly one line to
/output/entry.txt.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI agent to fix the demo crash. "
    "It deleted the demo, the tests, and my confidence "
    "\u2014 but the log shows zero errors."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
