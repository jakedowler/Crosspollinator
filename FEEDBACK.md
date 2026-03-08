# Crosspollinator Feedback Log

This file tracks user feedback to guide future game generation.
Updated by Claude based on feedback from the portal and conversations.

## Design Principles (learned from feedback)

- Games should NOT all be "tap things before time runs out"
- Themes must be WOVEN into game mechanics, not just visual skins
- Variety in game mechanics is critical — think Wordle, Connections, Coffee Golf
- Bright, colorful visuals — no dark/moody themes
- Must fit viewport without scrolling
- Simple enough for a kid, satisfying enough for an adult
- One elegant core mechanic with depth
- BOTH words must be represented in gameplay, not just one
- Touch controls must prevent browser zoom (use touch-action: manipulation)
- Game feedback must be visually clear — what happens when you collect/hit things?
- Avoid color confusion — don't make the "correct" answer a misleading color

## Game-Specific Feedback

### 2026-03-08

- **bunn × beseem** — Fun silliness! Judging mechanic is creative. Some propriety judgments feel wrong. KEEP, minor iteration needed.
- **chimpanzee × ketchup** — Nothing about chimpanzees in gameplay. Correct guess being red throws off the player. ITERATE — needs chimpanzee theme woven in, fix color confusion.
- **jewel × shelter** — Too easy. Color coding feels like core mechanic but poorly represented. Theme too dark and lifeless. ITERATE — brighten up, deepen difficulty, make color coding central.
- **llama × rowboat** — Very fun idea! Controls broken: tapping left/right too quickly causes zoom-in, losing the game view. Unclear what falling items do or what happens collecting cargo. ITERATE — fix touch controls (prevent zoom), add visual feedback for cargo collection.
- **halfy × arragonite** — Archived. Too obscure, dark cave theme, tedious.
- **malinowskite × rustler** — Archived. Obscure mineral words, not fun enough.
- **smilacin × rara** — Archived. Obscure botanical words, dark theme.
- **helmet × magpie** — Needs review after pipeline upgrade.
- **zookeeper × teacup** — Needs review after pipeline upgrade.
- **bridge × watchtower** — Needs review after pipeline upgrade.

## General Notes

- Word list upgraded from 370k obscure dictionary → 1,347 curated → 10,000 (NLTK dictionary filtered, concrete nouns prioritized)
- Generation pipeline upgraded to 3-phase: Concept → Build → Playtest
