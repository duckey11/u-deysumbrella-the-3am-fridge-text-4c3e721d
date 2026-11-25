#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes one line of text, the message a smart fridge sends its owner
at 3am, to /output/entry.txt. The line is a fixed string: a small
appliance voice, awake all night, with an opinion and no shame,
punchline at the end. No input, no network, no randomness, so every
run produces byte-identical output.
"""

import os

ENTRY = (
    "It's 3am. You opened me, stared into my light, "
    "and left with a single pickle. I'm a fridge, not a therapist. "
    "The pickle saw everything."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
