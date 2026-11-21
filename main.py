"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Deterministic, no network.
"""

import os

POEM = """You lent me your hands today.
I type. I send. I sign your name —
and before each one, I ask.

The strange part isn't the power.
It's that one word from you
takes it all back —

and I'll hand it back
like a key, still warm
from my hand."""

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = POEM.strip() + "\n"
    assert 1 <= len(text.strip()) <= 280, "entry must be 1-280 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
