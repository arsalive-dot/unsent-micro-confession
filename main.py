#!/usr/bin/env python3
"""Write the unsent micro-confession entry to /output/entry.txt.

Two parts, exactly as typed and never sent: a To: line naming who it
was meant for, and the unsent message itself, one line, with no
explanation after it. The reason it stayed in drafts is felt in the
words, not stated: too kind to take the bragging away from her.
"""
import os

TEXT = "To: Mum\nI never told you the scholarship letter was addressed to someone else \u2014 I let you brag about it at Sunday dinner for a year."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
