#!/usr/bin/env python3
"""Daily orchestrator: pick words → generate app → write journal → commit."""

import subprocess
import sys
from pathlib import Path

from generate_app import main as generate_main
from write_journal import write_entry


def git(*args: str) -> None:
    """Run a git command from the repo root."""
    repo_root = Path(__file__).resolve().parent.parent
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"git {' '.join(args)} failed:\n{result.stderr}", file=sys.stderr)
    else:
        print(result.stdout.strip())


def run() -> None:
    # Step 1 — generate the app
    word_a, word_b, html_path = generate_main()

    # Step 2 — write the journal entry
    html = html_path.read_text(encoding="utf-8")
    journal_path = write_entry(word_a, word_b, html)

    # Step 3 — commit both files to the repo
    git("add", str(html_path), str(journal_path))
    git(
        "commit",
        "-m",
        f"daily: {word_a} × {word_b}",
    )
    print("\n🎉  Daily run complete!")


if __name__ == "__main__":
    run()
