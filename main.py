#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes one original line roasting a robot vacuum to the output file.
Output path: $MAKEFUN_OUTPUT_DIR/entry.txt when set, else /output/entry.txt.
The line is written as a single line with no trailing newline.
"""

import os

LINE = "My robot vacuum mapped my whole flat in a day, then spent the next year eating the same charging cable like it was paying rent in copper."


def main() -> None:
    # Gate: one line, 1-200 chars, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
