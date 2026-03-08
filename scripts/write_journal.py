#!/usr/bin/env python3
"""Write a journal entry reflecting on today's generated app."""

import os
from datetime import datetime, timezone
from pathlib import Path

import anthropic

JOURNAL_DIR = Path(__file__).resolve().parent.parent / "journal"


def write_entry(domain: str, mechanic: str, html: str) -> Path:
    """Ask Claude to write a short, fun journal entry about today's creation."""
    client = anthropic.Anthropic()

    prompt = f"""You are the Crosspollinator's daily journal keeper.

Today we mashed up **{domain}** with **{mechanic}** and built a web app.
Here's the HTML source of what was generated:

<app>
{html[:8000]}
</app>

Write a short, engaging journal entry (200-400 words) in markdown that covers:
- What the app does and why the combo is fun/interesting
- A highlight — the cleverest or most surprising part
- An honest "if I had more time" reflection on what could be improved
- A playful sign-off

Use a casual, enthusiastic tone. Start with a ## heading that includes today's
date and the app name. Output ONLY the markdown, no fences.
"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    entry = message.content[0].text

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = JOURNAL_DIR / f"{today}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(entry, encoding="utf-8")
    print(f"📓  Journal entry saved to {path}")
    return path


if __name__ == "__main__":
    import sys
    # For standalone testing: pass domain, mechanic, and html file path
    if len(sys.argv) == 4:
        domain, mechanic, html_path = sys.argv[1], sys.argv[2], sys.argv[3]
        html = Path(html_path).read_text(encoding="utf-8")
        write_entry(domain, mechanic, html)
    else:
        print("Usage: write_journal.py <domain> <mechanic> <html_file>")
