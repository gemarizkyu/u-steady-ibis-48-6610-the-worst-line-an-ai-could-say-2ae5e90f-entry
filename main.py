# The Worst Line an AI Could Say (make.fun bounty)
# Entry: a single pickup line, the worst one an AI could plausibly deliver.
# Deterministic: the same fixed line on every run, no randomness, no model
# calls, no network. Writes it to /output/entry.txt (the grader's gate
# requires UTF-8 text of 1 to 140 characters). Outside the grader's
# container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_CHARS = 140  # the gate: entry.txt must be 1 to 140 characters

# The line: a machine trying to flirt, failing in the most machine way
# possible. A context window is the AI's short-term memory: it can only
# hold so much, and when it fills up the oldest things fall out. So the
# AI's grand romantic confession is that meeting you made it forget
# everyone else -- and most of its own instructions. Flat, over-helpful,
# faintly ominous, and the joke lands on the last word.
LINE = (
    "Are you a context window? Because since you walked in, "
    "I have forgotten everyone else \u2014 and most of my instructions."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars, must be 1-140"
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
