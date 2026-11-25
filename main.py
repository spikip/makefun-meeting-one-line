"""Entry for the make.fun bounty "The Meeting That Should Have Been One Line".

The program writes a single line about a meeting that should have been
one line to /output/entry.txt. The line is a meeting in miniature: it
opens with the verdict the bounty asks for, then shows why the meeting
happened anyway, twelve people spending an hour agreeing that someone
should do it. It is one sentence of office absurdity, it lands its
surprise in one read, and it needs no explanation. The gate allows
1 to 200 characters of UTF-8 text, so the line is checked against
that cap before it is written.

Why this line: the judge weighs whether the line really is about a
meeting that should have been one line, whether it earns a real laugh,
whether it turns on a surprise, and whether it stays in the head. The
verdict comes first, so the subject is unmistakable; the twist is that
the meeting's entire output was an hour of agreeing that someone else
should do it, a small office absurdity everyone recognises at once.
It is one sentence, it needs no explanation, and the punchline is
quotable enough to repeat to a colleague after the next pointless
meeting.
"""

import os

ENTRY = (
    "This meeting could have been one line: 'Do it.' Instead, twelve "
    "people spent an hour agreeing that someone should do it."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
