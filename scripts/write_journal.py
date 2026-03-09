#!/usr/bin/env python3
"""Write a journal entry reflecting on today's generated app.

Uses the Anthropic Python SDK when ANTHROPIC_API_KEY is set (CI),
otherwise falls back to the Claude Code CLI (local development).
"""

import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

JOURNAL_DIR = Path(__file__).resolve().parent.parent / "journal"

MODEL = "claude-sonnet-4-20250514"
_USE_SDK = bool(os.environ.get("ANTHROPIC_API_KEY"))


def _clean_env() -> dict[str, str]:
    """Return env dict without CLAUDECODE session vars for CLI fallback."""
    env = os.environ.copy()
    for key in [
        "CLAUDECODE", "CLAUDE_CODE_SESSION_ID",
        "CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR",
        "CLAUDE_CODE_CONTAINER_ID", "CLAUDE_CODE_EMIT_TOOL_USE_SUMMARIES",
        "CLAUDE_CODE_DEBUG", "CLAUDE_AUTO_BACKGROUND_TASKS",
        "CLAUDE_AFTER_LAST_COMPACT", "CLAUDE_CODE_BASE_REF",
        "CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE",
    ]:
        env.pop(key, None)
    return env


def write_entry(word_a: str, word_b: str, html: str) -> Path:
    """Ask Claude to write a short, fun journal entry about today's creation."""
    prompt = f"""You are the Crosspollinator's daily journal keeper.

Today's two random dictionary words were **{word_a}** and **{word_b}**.
Here's the HTML source of the web app that was generated from them:

<app>
{html[:8000]}
</app>

Write a short, engaging journal entry (200-400 words) in markdown that covers:
- The creative leap: how two random words became an app concept
- What the app actually does
- A highlight — the cleverest or most surprising part
- An honest "if I had more time" reflection on what could be improved
- A playful sign-off

Use a casual, enthusiastic tone. Start with a ## heading that includes today's
date, the two words, and the app name. Output ONLY the markdown, no fences."""

    if _USE_SDK:
        import anthropic
        client = anthropic.Anthropic()
        message = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        entry = message.content[0].text
    else:
        result = subprocess.run(
            ["claude", "-p", prompt, "--output-format", "text"],
            capture_output=True, text=True, timeout=120, env=_clean_env(),
        )
        if result.returncode != 0:
            print(f"Claude CLI failed:\n{result.stderr}", file=sys.stderr)
            sys.exit(1)
        entry = result.stdout

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = JOURNAL_DIR / f"{today}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(entry, encoding="utf-8")
    print(f"📓  Journal entry saved to {path}")
    return path


if __name__ == "__main__":
    if len(sys.argv) == 4:
        word_a, word_b, html_path = sys.argv[1], sys.argv[2], sys.argv[3]
        html = Path(html_path).read_text(encoding="utf-8")
        write_entry(word_a, word_b, html)
    else:
        print("Usage: write_journal.py <word_a> <word_b> <html_file>")
