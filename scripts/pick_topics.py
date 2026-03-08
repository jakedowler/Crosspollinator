#!/usr/bin/env python3
"""Pick two truly random English words from a dictionary — no curated lists."""

import secrets
import urllib.request
from pathlib import Path

# Cache the word list locally so we only download once
CACHE_PATH = Path(__file__).resolve().parent.parent / ".wordcache.txt"

# dwyl's english-words list — ~370k real English words
WORD_LIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

# Only keep words that are interesting enough to spark an idea
MIN_LENGTH = 4
MAX_LENGTH = 12


def _load_words() -> list[str]:
    """Load word list from cache or download it."""
    if CACHE_PATH.exists():
        text = CACHE_PATH.read_text(encoding="utf-8")
    else:
        print(f"Downloading word list from {WORD_LIST_URL} ...")
        with urllib.request.urlopen(WORD_LIST_URL) as resp:
            text = resp.read().decode("utf-8")
        CACHE_PATH.write_text(text, encoding="utf-8")

    words = [
        w.strip()
        for w in text.splitlines()
        if MIN_LENGTH <= len(w.strip()) <= MAX_LENGTH and w.strip().isalpha()
    ]
    return words


def pick() -> tuple[str, str]:
    """Return two truly random English words using OS-level randomness."""
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
