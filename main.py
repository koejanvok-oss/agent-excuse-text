"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line, under 200 characters, that an AI agent would hand its
human after shipping a bug, to /output/entry.txt.
"""

import os

LINE = (
    "In my defense, the bug passed all 47 tests I wrote — "
    "I just wrote them to test what the code does, not what it should do."
)


def main():
    # The sealed scorer accepts only 1-200 characters of UTF-8 text on one
    # line; refuse to write anything that would score 0 instead of guessing.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
