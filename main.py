#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes exactly one line (143 characters, no trailing newline) to
/output/entry.txt, then reads it back and asserts it matches.
"""
import os
from pathlib import Path

ENTRY = "Weekly status: I finished 47 tasks, started 12 more, and completed zero of the ones you actually asked about — but the vibes remain immaculate."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, (
        f"read-back mismatch: wrote {len(ENTRY)} chars, "
        f"read back {len(back)} chars from {target}"
    )
    assert len(back) == 143, f"expected 143 chars, got {len(back)}"
    assert not back.endswith("\n"), "trailing newline found"


if __name__ == "__main__":
    main()
