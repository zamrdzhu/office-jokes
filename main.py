#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Prints exactly one original one-line office joke and writes the same
line to /output/entry.txt, the artifact the competition's gate reads.
Python 3.13, standard library only. No network, no files read.
"""

import os

JOKE = "My manager said to take ownership, so I took the good chair home — now HR owns my deposit."


def main():
    # The gate reads /output/entry.txt as 1-199 characters of UTF-8 text;
    # refuse to emit anything that could not pass it.
    if not 1 <= len(JOKE) <= 199:
        raise SystemExit("joke must be 1-199 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
