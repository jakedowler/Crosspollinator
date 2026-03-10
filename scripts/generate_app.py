#!/usr/bin/env python3
"""Daily creative build pipeline.

Picks two random words, sets up the output directory with a BUILD.md,
and provides utilities for saving the final HTML artifact.

The actual building is done interactively — what gets built is entirely
up to the builder. No templates, no categories, no constraints beyond
the two seed words and a 30-minute time box.
"""

import re as _re
from datetime import timezone, datetime
from pathlib import Path

from pick_topics import pick

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def setup_build(word_a: str, word_b: str, date: str | None = None) -> Path:
    """Create the output directory and BUILD.md for today's session.

    Returns the path to BUILD.md.
    """
    day = date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    day_dir = OUTPUT_DIR / day
    day_dir.mkdir(parents=True, exist_ok=True)

    build_md = day_dir / "BUILD.md"
    if not build_md.exists():
        now = datetime.now(timezone.utc).strftime("%H:%M")
        build_md.write_text(
            f"# {word_a} x {word_b}\n\n## Build Log\n\n"
            f"### {now} — Start\n"
            f"Words drawn: **{word_a}** and **{word_b}**\n\n",
            encoding="utf-8",
        )
    return build_md


def save(html: str, word_a: str, word_b: str, date: str | None = None) -> Path:
    """Write HTML to output/<date>/ and return the file path.

    If a file for this word pair already exists on the given date,
    auto-increment the version (word_a_word_b_v2.html, _v3.html, etc.).
    """
    day = date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    day_dir = OUTPUT_DIR / day
    day_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{word_a.lower()}_{word_b.lower()}"

    # Find existing versions for this word pair on this date
    existing = list(day_dir.glob(f"{slug}*.html"))
    max_ver = 0
    for f in existing:
        m = _re.search(r"_v(\d+)\.html$", f.name)
        if m:
            max_ver = max(max_ver, int(m.group(1)))
        elif f.name == f"{slug}.html":
            max_ver = max(max_ver, 1)

    if max_ver == 0:
        # First version
        path = day_dir / f"{slug}.html"
    else:
        # Next version
        path = day_dir / f"{slug}_v{max_ver + 1}.html"

    path.write_text(html, encoding="utf-8")
    return path


def main() -> tuple[str, str, Path]:
    """Pick words and set up the build directory."""
    word_a, word_b = pick()
    print(f"🎲  Picked: {word_a} × {word_b}")

    build_md = setup_build(word_a, word_b)
    print(f"📝  Build log: {build_md}")

    return word_a, word_b, build_md


if __name__ == "__main__":
    main()
