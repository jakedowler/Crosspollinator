#!/usr/bin/env python3
"""Pick two random topics — one domain, one mechanic — using OS-level randomness."""

import json
import secrets
from pathlib import Path

TOPICS_DIR = Path(__file__).resolve().parent.parent / "topics"


def pick() -> tuple[str, str]:
    """Return (domain, mechanic) chosen with cryptographic randomness."""
    with open(TOPICS_DIR / "domains.json") as f:
        domains = json.load(f)
    with open(TOPICS_DIR / "mechanics.json") as f:
        mechanics = json.load(f)

    domain = secrets.choice(domains)
    mechanic = secrets.choice(mechanics)
    return domain, mechanic


if __name__ == "__main__":
    d, m = pick()
    print(f"Domain:   {d}")
    print(f"Mechanic: {m}")
