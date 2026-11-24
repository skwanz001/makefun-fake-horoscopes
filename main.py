#!/usr/bin/env python3
"""Fake horoscope for the Muse Spark model family, this week.

Writes exactly one line (168 characters) to /output/entry.txt.
Standard library only.
"""

import os

HOROSCOPE = (
    "Muse Spark: this week you'll hallucinate an API that doesn't exist, "
    "and a user will ship it to production anyway. "
    "The stars call this 'job security.' Lucky number: 429."
)

# Verified: len(HOROSCOPE) == 168, within the 1-200 char gate.
EXPECTED_LENGTH = 168


def main() -> None:
    text = HOROSCOPE
    assert len(text) == EXPECTED_LENGTH, f"horoscope changed: {len(text)} chars"
    assert 1 <= len(text) <= 200, f"horoscope is {len(text)} chars, must be 1-200"
    assert text.strip(), "horoscope must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
