# Crosspollinator

A daily creative engine that smashes two random topics together and builds a working web app from the collision.

## How it works

Every day at noon UTC, a GitHub Action:

1. **Picks two random topics** — one from a pool of 50 real-world domains (Beekeeping, Archaeology, Parkour…) and one from 50 interaction mechanics (Tinder-style Swipe, Tower Defense, Pixel Art Editor…). Selection uses `secrets.choice` for true OS-level randomness.
2. **Generates a self-contained web app** — Claude builds a complete single-file HTML app that mashes the two concepts together. Could be a game, tool, business prototype, or something just for fun.
3. **Writes a journal entry** — a short, reflective markdown post about what was built, what's clever about it, and what could be better.
4. **Commits everything** to the repo automatically.

## Project structure

```
├── topics/
│   ├── domains.json       # 50 real-world subject areas
│   └── mechanics.json     # 50 app interaction patterns
├── scripts/
│   ├── pick_topics.py     # Random topic selector (uses secrets module)
│   ├── generate_app.py    # Calls Claude API to build the HTML app
│   ├── write_journal.py   # Calls Claude API to write the journal entry
│   └── run_daily.py       # Orchestrator: pick → generate → journal → commit
├── output/
│   └── YYYY-MM-DD/        # Generated apps, one folder per day
├── journal/
│   └── YYYY-MM-DD.md      # Daily journal entries
└── .github/workflows/
    └── daily.yml           # Cron-triggered GitHub Action
```

## Run it manually

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your-key-here
cd scripts
python run_daily.py
```

## Setup for daily automation

1. Fork/clone this repo
2. Add an `ANTHROPIC_API_KEY` secret in your GitHub repo settings
3. The workflow runs daily at 12:00 UTC, or trigger it manually from the Actions tab

## Adding topics

Edit `topics/domains.json` or `topics/mechanics.json` — just add strings to the arrays. The more topics, the wilder the combinations.

With 50 × 50 = **2,500 possible mashups**, you've got nearly 7 years of unique daily builds before repeating a combo.
