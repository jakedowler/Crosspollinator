#!/usr/bin/env python3
"""Use Claude Code CLI to generate a single-file HTML web app from two random words."""

import os
import subprocess
import sys
from datetime import timezone, datetime
from pathlib import Path

from pick_topics import pick

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def _clean_env() -> dict[str, str]:
    """Return env dict without CLAUDECODE so we can spawn a child session."""
    env = os.environ.copy()
    env.pop("CLAUDECODE", None)
    return env


def generate(word_a: str, word_b: str) -> str:
    """Call Claude Code CLI to produce a self-contained HTML app."""
    prompt = f"""You are the Crosspollinator — a wildly creative app designer.

Today's two random words pulled straight from the dictionary:
  • Word 1: {word_a}
  • Word 2: {word_b}

Your job: find a creative connection between these two words and build a
single-page web application inspired by their intersection. It could be a game,
a useful tool, a business idea prototype, an art piece, something educational,
or something purely whimsical — dealer's choice, surprise me. Be inventive
about HOW the two words connect — lateral thinking is encouraged.

Requirements:
1. Output a COMPLETE, self-contained HTML file (HTML + CSS + JS, no external deps).
2. The app must be interactive and actually work when opened in a browser.
3. Use modern CSS (flexbox/grid, variables, transitions) to make it look polished.
4. Include a header that names the app and a short tagline explaining the concept.
5. The entire response must be ONLY the HTML — no markdown fences, no commentary."""

    result = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "text"],
        capture_output=True,
        text=True,
        timeout=300,
        env=_clean_env(),
    )

    if result.returncode != 0:
        print(f"Claude CLI failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)

    return result.stdout


def save(html: str, word_a: str, word_b: str) -> Path:
    """Write HTML to output/<date>/ and return the file path."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    day_dir = OUTPUT_DIR / today
    day_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{word_a.lower()}_{word_b.lower()}"
    path = day_dir / f"{slug}.html"
    path.write_text(html, encoding="utf-8")
    return path


def main() -> tuple[str, str, Path]:
    word_a, word_b = pick()
    print(f"🎲  Picked: {word_a} × {word_b}")

    html = generate(word_a, word_b)
    path = save(html, word_a, word_b)
    print(f"✅  Saved to {path}")

    return word_a, word_b, path


if __name__ == "__main__":
    main()
