#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — a haiku about debugging.

breakpoint never hits
the stack trace points to nowhere
it was my typo

Writes the haiku (5-7-5 syllables, 72 characters, inside the 1-200
gate) to /output/entry.txt.
"""
import os

ENTRY = ("breakpoint never hits\n"
         "the stack trace points to nowhere\n"
         "it was my typo")

def write_entry():
    """Write the haiku and verify the bytes on disk match exactly."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match haiku"


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.count("\n") == 2, "entry must be three lines"
    lines = ENTRY.split("\n")
    assert [len(l.split()) for l in lines] == [3, 6, 4], "unexpected line shape"
    write_entry()

if __name__ == "__main__":
    main()
