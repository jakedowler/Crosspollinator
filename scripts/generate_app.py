#!/usr/bin/env python3
"""Multi-phase game generation pipeline using Claude Code CLI.

Phase 1 — CONCEPT: Topic experts + game designer brainstorm a concept
Phase 2 — BUILD: Expert developer builds the game from the concept
Phase 3 — PLAYTEST: Playtester reviews and the developer fixes issues
"""

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


def _call_claude(prompt: str, timeout: int = 300) -> str:
    """Call Claude Code CLI and return the text output."""
    result = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "text"],
        capture_output=True,
        text=True,
        timeout=timeout,
        env=_clean_env(),
    )
    if result.returncode != 0:
        print(f"Claude CLI failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result.stdout


def phase_concept(word_a: str, word_b: str) -> str:
    """Phase 1: Expert brainstorm to design the game concept."""
    prompt = f"""You are a panel of experts designing a brilliant once-a-day web game.

Today's two random seed words: "{word_a}" and "{word_b}"

Work through these roles IN ORDER, writing out each expert's contribution:

── TOPIC EXPERT A ──
You are a world expert on "{word_a}". Share 3-4 fascinating, surprising, or
delightful facts about {word_a} that most people wouldn't know. What makes
{word_a} interesting, weird, beautiful, or fun? Think about its properties,
behaviors, cultural significance, or how it connects to everyday life.

── TOPIC EXPERT B ──
You are a world expert on "{word_b}". Same thing — 3-4 surprising facts about
{word_b}. What's genuinely interesting about it?

── CONNECTION WEAVER ──
Now find 2-3 creative connections between {word_a} and {word_b}. Don't just
mash the words together — find a GENUINE thematic link. Maybe they share an
underlying principle, an unexpected parallel, a visual similarity, or an
emotional resonance. The best connections feel like "aha!" moments.

── GAME DESIGNER (daily game specialist) ──
You design games like Wordle, Connections, Mini Crossword, Coffee Golf, Spelling
Bee, and other beloved daily web games. Your games have these qualities:
• ONE elegant core mechanic (not multiple mini-games)
• Depth from simplicity — easy to learn, satisfying to master
• The theme is WOVEN INTO the mechanic, not just a skin
• A sense of discovery or "aha!" moments during play
• Replayable or has a clear satisfying arc (30 sec to 3 min)
• NO "tap things before time runs out" — that's lazy design

Using the connections above, design ONE game concept. Describe:
1. The core mechanic (what does the player DO?)
2. How the theme of {word_a} × {word_b} is woven into gameplay (not just visual)
3. The win/lose condition or satisfying endpoint
4. Why it's immediately fun (the "hook")

── VISUAL DIRECTOR ──
Choose a specific, distinctive visual style for this game. NOT dark/moody.
Pick from styles like: watercolor wash, retro pixel art, paper cutout,
chalkboard sketch, candy-coated 3D, sunset gradient, ocean palette, neon
arcade, botanical illustration, comic book pop art, construction paper collage,
stained glass, crayon drawing, or invent your own. Describe the exact color
palette (3-5 specific hex colors) and visual mood.

Output ONLY the expert discussion above. No code."""

    return _call_claude(prompt, timeout=120)


def phase_build(word_a: str, word_b: str, concept: str) -> str:
    """Phase 2: Build the game from the concept document."""
    prompt = f"""You are an expert web game developer. A design team has created
this game concept for the words "{word_a}" × "{word_b}":

--- CONCEPT DOCUMENT ---
{concept}
--- END CONCEPT ---

Now BUILD this game as a single, self-contained HTML file.

CRITICAL REQUIREMENTS:
1. Output ONLY the complete HTML file — no markdown fences, no commentary.
2. Self-contained: HTML + CSS + JS in one file, no external dependencies.
3. The game must WORK — all mechanics described in the concept must function.
4. FIT THE VIEWPORT: Use height: 100vh / max-height: 100dvh. No scrolling.
   Keep the header tiny (one line: game name + short tagline).
5. Use the EXACT visual style and color palette from the Visual Director.
6. The theme must be WOVEN into gameplay, not just decorative.
7. Modern CSS (flexbox/grid, variables, transitions, animations).
8. Clean, readable code — this will be reviewed by a playtester.
9. Touch-friendly — must work on mobile (use click/touch events, big tap targets).
10. Include a brief "how to play" hint on screen (1 sentence max)."""

    return _call_claude(prompt, timeout=300)


def phase_playtest(word_a: str, word_b: str, concept: str, html: str) -> str:
    """Phase 3: Playtest the game and fix issues."""
    prompt = f"""You are a panel of playtesters reviewing a web game for
"{word_a}" × "{word_b}".

--- ORIGINAL CONCEPT ---
{concept}
--- END CONCEPT ---

--- CURRENT HTML ---
{html}
--- END HTML ---

Review this game from THREE perspectives:

🧒 CHILD (age 8): "Is this fun? Do I understand what to do immediately?
Can I play it without reading instructions? Is anything confusing or broken?"

🎮 DAILY GAMER (plays Wordle/NYT Games daily): "Is the core mechanic
satisfying? Does it have depth? Is the theme genuinely woven in or just
a paint job? Would I share this with friends?"

🔧 QA TESTER: Read the JavaScript carefully. Are there bugs? Does the game
loop work? Can the player get stuck? Does it handle edge cases? Is anything
broken — missing event listeners, wrong selectors, logic errors, NaN scores?

After all three reviews, output the FIXED AND IMPROVED complete HTML file.
Apply all fixes and improvements. If the game is fundamentally flawed
(e.g., the mechanic doesn't match the concept), redesign it.

Output ONLY the final HTML — no markdown fences, no commentary."""

    return _call_claude(prompt, timeout=300)


def generate(word_a: str, word_b: str) -> str:
    """Run the full 3-phase generation pipeline."""
    print(f"  📋 Phase 1: Concept design...")
    concept = phase_concept(word_a, word_b)
    print(f"  🔨 Phase 2: Building game...")
    html = phase_build(word_a, word_b, concept)
    print(f"  🎮 Phase 3: Playtesting & fixing...")
    html = phase_playtest(word_a, word_b, concept, html)
    return html


def save(html: str, word_a: str, word_b: str, date: str | None = None) -> Path:
    """Write HTML to output/<date>/ and return the file path.

    If a file for this word pair already exists on the given date,
    auto-increment the version (word_a_word_b_v2.html, _v3.html, etc.).
    """
    import re as _re

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
    word_a, word_b = pick()
    print(f"🎲  Picked: {word_a} × {word_b}")

    html = generate(word_a, word_b)
    path = save(html, word_a, word_b)
    print(f"✅  Saved to {path}")

    return word_a, word_b, path


if __name__ == "__main__":
    main()
