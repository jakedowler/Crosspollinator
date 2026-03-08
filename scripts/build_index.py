#!/usr/bin/env python3
"""Scan output/ and generate apps.js for the landing page."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
APPS_JS = ROOT / "apps.js"


def extract_title(html: str) -> str:
    """Pull the <title> text from an HTML file."""
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_tagline(html: str) -> str:
    """Try to pull a tagline from the first <p> inside <header>, or subtitle."""
    match = re.search(r"<header>.*?<p[^>]*>(.*?)</p>", html, re.IGNORECASE | re.DOTALL)
    if match:
        # Strip HTML tags from the tagline
        return re.sub(r"<[^>]+>", "", match.group(1)).strip()
    return ""


def scan() -> list[dict]:
    """Walk output/ directories and build the app manifest."""
    apps = []

    if not OUTPUT_DIR.exists():
        return apps

    for date_dir in sorted(OUTPUT_DIR.iterdir()):
        if not date_dir.is_dir():
            continue
        date_str = date_dir.name  # e.g. "2026-03-08"

        for html_file in sorted(date_dir.glob("*.html")):
            # Parse word_a, word_b, and optional version from filename
            # Format: word_a_word_b.html (v1) or word_a_word_b_v2.html (v2+)
            stem = html_file.stem
            version = 1
            version_match = re.search(r"_v(\d+)$", stem)
            if version_match:
                version = int(version_match.group(1))
                stem = stem[: version_match.start()]

            parts = stem.split("_", 1)
            word_a = parts[0] if len(parts) >= 1 else stem
            word_b = parts[1] if len(parts) >= 2 else ""

            html = html_file.read_text(encoding="utf-8")
            title = extract_title(html)
            tagline = extract_tagline(html)

            apps.append({
                "date": date_str,
                "word_a": word_a,
                "word_b": word_b,
                "name": title,
                "desc": tagline,
                "path": f"output/{date_str}/{html_file.name}",
                "version": version,
            })

    return apps


def build():
    apps = scan()
    js = f"APPS = {json.dumps(apps, indent=2)};\n"
    APPS_JS.write_text(js, encoding="utf-8")
    print(f"Built apps.js with {len(apps)} app(s)")


if __name__ == "__main__":
    build()
