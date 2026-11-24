#!/usr/bin/env python3
"""Write the office one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "One-Line Office Joke: 24-Hour Sprint" bounty. The
program writes exactly one line of text and nothing else.

How the line targets the judge brief (funny, fresh, tight): every office
has the printer that has cried "low toner" for years. The joke promotes
that warning message to the company's longest-serving employee -- a deadpan
escalation everyone who has ever worked near a printer recognizes in one
breath, no setup wasted.
"""

import os
from pathlib import Path

LINE = "Our office printer has displayed 'low toner' since 2019. It is no longer a warning; it is the company's longest-serving employee."


def write_entry(out_dir: Path) -> Path:
    """Write the joke line to entry.txt inside out_dir.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one clean line.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
