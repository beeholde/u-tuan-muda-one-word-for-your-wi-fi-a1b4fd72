#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes a single word describing home Wi-Fi to /output/entry.txt.
Stdlib only, no network, no randomness, fully deterministic.
"""

import os

WORD = "Wallflower"


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()


# Gate self-check: the entry must be 1-20 UTF-8 characters, not blank.
# Kept separate from main() so the write path above stays trivial.
assert 1 <= len(WORD.encode("utf-8")) <= 20 and WORD.strip() == WORD
