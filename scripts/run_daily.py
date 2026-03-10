#!/usr/bin/env python3
"""Daily orchestrator: pick words → set up build → write journal → commit.

The actual 30-minute creative build happens interactively between
setup and finalization. This script handles the bookkeeping.
"""

import subprocess
import sys
from pathlib import Path

from build_index import build as build_index
from generate_app import setup_build, save
from pick_topics import pick
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


def setup() -> tuple[str, str, Path]:
    """Pick words and create the build directory. Returns (word_a, word_b, build_md)."""
    word_a, word_b = pick()
    print(f"🎲  Picked: {word_a} × {word_b}")
    build_md = setup_build(word_a, word_b)
    print(f"📝  Build log: {build_md}")
    return word_a, word_b, build_md


def finalize(word_a: str, word_b: str, html_path: Path) -> None:
    """Write journal, rebuild index, and commit."""
    # Step 1 — write the journal entry
    html = html_path.read_text(encoding="utf-8")
    journal_path = write_entry(word_a, word_b, html)

    # Step 2 — rebuild the landing page index
    build_index()

    # Step 3 — commit all new files to the repo
    build_md = html_path.parent / "BUILD.md"
    paths_to_add = [str(html_path), str(journal_path), "apps.js"]
    if build_md.exists():
        paths_to_add.append(str(build_md))
    git("add", *paths_to_add)
    git(
        "commit",
        "-m",
        f"daily: {word_a} × {word_b}",
    )
    print("\n🎉  Daily run complete!")


def run() -> None:
    """Full run: setup, generate (placeholder for interactive build), finalize."""
    word_a, word_b, build_md = setup()
    day_dir = build_md.parent

    # In the interactive workflow, the build happens here manually.
    # For automated runs, look for the HTML file that was already created.
    html_files = list(day_dir.glob("*.html"))
    if not html_files:
        print("⏳  No HTML file found yet — build interactively, then run finalize.")
        return

    html_path = html_files[0]
    finalize(word_a, word_b, html_path)


if __name__ == "__main__":
    run()
