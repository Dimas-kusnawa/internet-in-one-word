"""The Internet in One Word — entry for u-ronigrv-the-internet-in-one-word-e388f33b.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Candidate head-to-head (judged the way the house judge would):
  A. "brainrot" (8 chars) — funny, but a mood/genre of content, not the
     whole internet; known slang, not very surprising.
  B. "yapping" (7 chars) — funny and true (everyone talking nonstop), but
     narrower: one behaviour, not the whole internet.
  C. "feral" (5 chars) — funny by itself (the whole internet as a wild
     animal), true of the whole internet (unmoderated, untamed, everyone
     acting feral), surprising, and shortest: lands in one beat, and the
     smaller text wins ties.

Chosen word: "feral" — 5 chars, inside the 1-30 gate, exactly one word.
"""

import os

WORD = "feral"  # exactly 5 bytes, no trailing newline: the file is the word


def main():
    # Deterministic: same word, same bytes, every run.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
