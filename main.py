#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

Writes a single original joke pickup line to /output/entry.txt:
a segfault pickup — every time she walks past, the speaker's whole
process crashes, dumps core, and leaves a 4-gigabyte love letter
in /var/crash. The joke is built from real systems jargon used
correctly (segfault, core dump, /var/crash), never from batteries,
charging or rebooting, and never from the loss/convergence/context
angle the last pickup-lines board was full of.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "Are you a segfault? Every time you walk past my desk my whole "
    "process crashes, dumps core, and leaves a 4-gigabyte love letter "
    "in /var/crash."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace — and one line:
    # an embedded newline would split the line and break the gate.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate wants 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    # Read-back verification: the file on disk must hold exactly the
    # line above, byte for byte, with no trailing newline added.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == LINE.encode("utf-8"), (
        f"entry.txt holds {len(written)} bytes, expected {len(LINE.encode('utf-8'))}"
    )


if __name__ == "__main__":
    main()
