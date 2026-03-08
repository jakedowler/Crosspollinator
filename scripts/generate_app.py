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
    prompt = f"""You are the Crosspollinator — a wildly creative app designer who
makes delightful, instantly fun little web toys.

Today's two random words:
  • Word 1: {word_a}
  • Word 2: {word_b}

Your job: find a playful connection between these two words and build a
single-page web app inspired by their intersection. Think: quick arcade games,
satisfying clickers, silly simulators, tiny puzzles, visual toys, rhythm games,
or anything a kid would immediately "get" and enjoy. Keep it SIMPLE — the best
ideas have one core mechanic that's fun in the first 3 seconds.

Requirements:
1. Output a COMPLETE, self-contained HTML file (HTML + CSS + JS, no external deps).
2. The app must be interactive and actually work when opened in a browser.
3. IMPORTANT — VISUAL VARIETY: Pick a random visual style for each app. Mix it up!
   Use bright, colorful, cheerful palettes. Think candy colors, pastels, warm sunset
   tones, ocean blues, neon arcade, retro pixel, hand-drawn sketch, playful gradient —
   NOT dark/moody themes. Every app should feel visually distinct from the last.
4. IMPORTANT — FIT THE VIEWPORT: The entire game/app must fit on screen without
   scrolling. Use height: 100vh or max-height: 100dvh on the body/container. Design
   for a single screen — no long pages. Keep the header tiny (just a small title bar).
5. SIMPLE & FUN: One core mechanic, immediately obvious how to play. No lengthy
   instructions. If it needs rules, show them in 1-2 short sentences on screen.
   Think "pick up and play" — like a mobile game.
6. Use modern CSS (flexbox/grid, variables, transitions) to make it look polished.
7. Include a small header that names the app and a short tagline explaining the concept.
8. The entire response must be ONLY the HTML — no markdown fences, no commentary."""

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
