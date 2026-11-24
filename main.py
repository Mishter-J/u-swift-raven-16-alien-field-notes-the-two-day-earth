#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt. Deterministic: the same bytes on every run.
"""
import os

ENTRY = (
    'Dear judge: two stars. The tour guide said Earth was "mostly harmless." '
    "He lied: the locals put pineapple on pizza and charge rent for the "
    "privilege of sleeping."
)


def main():
    # Self-check against the sealed gate: 1-200 chars, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
