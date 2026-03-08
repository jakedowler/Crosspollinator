#!/usr/bin/env python3
"""Use the Anthropic API to generate a single-file HTML web app from two topics."""

import os
import sys
from datetime import date, timezone, datetime
from pathlib import Path

import anthropic

from pick_topics import pick

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def generate(domain: str, mechanic: str) -> str:
    """Call Claude to produce a self-contained HTML app."""
    client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

    prompt = f"""You are the Crosspollinator — a wildly creative app designer.

Today's random mashup:
  • Domain: {domain}
  • Mechanic: {mechanic}

Your job: invent a fun, surprising concept that merges these two topics into a
single-page web application. It could be a game, a useful tool, a business idea
prototype, or something purely whimsical — dealer's choice, surprise me.

Requirements:
1. Output a COMPLETE, self-contained HTML file (HTML + CSS + JS, no external deps).
2. The app must be interactive and actually work when opened in a browser.
3. Use modern CSS (flexbox/grid, variables, transitions) to make it look polished.
4. Include a header that names the app and a short tagline.
5. The entire response must be ONLY the HTML — no markdown fences, no commentary.
"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        messages=[{"role": "user", "content": prompt}],
    )

    return message.content[0].text


def save(html: str, domain: str, mechanic: str) -> Path:
    """Write HTML to output/<date>/ and return the file path."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    day_dir = OUTPUT_DIR / today
    day_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{domain.lower().replace(' ', '-')}_{mechanic.lower().replace(' ', '-')}"
    path = day_dir / f"{slug}.html"
    path.write_text(html, encoding="utf-8")
    return path


def main() -> tuple[str, str, Path]:
    domain, mechanic = pick()
    print(f"🎲  Picked: {domain} × {mechanic}")

    html = generate(domain, mechanic)
    path = save(html, domain, mechanic)
    print(f"✅  Saved to {path}")

    return domain, mechanic, path


if __name__ == "__main__":
    main()
