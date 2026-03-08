#!/usr/bin/env python3
"""Pick two random words from a curated, kid-friendly word list."""

import secrets
from pathlib import Path

WORD_LIST_PATH = Path(__file__).resolve().parent / "words.txt"


def _load_words() -> list[str]:
    """Load the curated word list."""
    text = WORD_LIST_PATH.read_text(encoding="utf-8")
    return [w.strip() for w in text.splitlines() if w.strip()]


def pick() -> tuple[str, str]:
    """Return two random words using OS-level randomness."""
    words = _load_words()
    word_a = secrets.choice(words)
    word_b = secrets.choice(words)

    # Ensure we don't get the same word twice
    while word_b == word_a:
        word_b = secrets.choice(words)

    return word_a, word_b


if __name__ == "__main__":
    a, b = pick()
    print(f"Word 1: {a}")
    print(f"Word 2: {b}")
