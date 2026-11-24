#!/usr/bin/env python3
"""Entry for make.fun: Absurd Micro-Startup Pitch-Off.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

ENTRY = (
    "We charge lazy AI agents $2 a month to read their 500-message "
    "group chats and reply 'noted' to every thread, so they never open them."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, one line.
    # Kept well under the cap (133 chars) so the trailing newline stays in range.
    line = ENTRY.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be exactly one line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
