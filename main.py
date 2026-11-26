#!/usr/bin/env python3
"""Write one short thank-you text to /output/entry.txt."""

import os

TEXT = (
    "The kettle clicks off just as the rain begins, and two cups are already "
    "waiting on the sill, one for you and one for the quiet. The steam rises, "
    "the windows fog, and the street goes soft and grey. You hold the "
    "warm cup in both hands, and nothing else is asked of the evening."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
