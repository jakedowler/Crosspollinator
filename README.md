# Crosspollinator

A daily creative engine that picks two random words from the dictionary and builds a working web app from their collision.

## How it works

Every day at noon UTC, a GitHub Action:

1. **Picks two random words** — pulled from a ~370k English dictionary ([dwyl/english-words](https://github.com/dwyl/english-words)) using `secrets.choice` for true OS-level randomness. No curated lists, no bias — just two raw words from the dictionary.
2. **Generates a self-contained web app** — Claude finds a creative connection between the words and builds a complete single-file HTML app. Could be a game, tool, business prototype, art piece, or something just for fun.
3. **Writes a journal entry** — a short, reflective markdown post about the creative leap from random words to working app.
4. **Commits everything** to the repo automatically.

## Project structure

```
├── scripts/
│   ├── pick_topics.py     # Downloads dictionary, picks 2 random words
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

Or just pick two random words to see what you'd get:

```bash
python scripts/pick_topics.py
```

## Setup for daily automation

1. Fork/clone this repo
2. Add an `ANTHROPIC_API_KEY` secret in your GitHub repo settings
3. The workflow runs daily at 12:00 UTC, or trigger it manually from the Actions tab

## The math

With ~80k qualifying words (4-12 letters), there are over **6 billion** possible word pairs. You will never run out of fresh combinations.
