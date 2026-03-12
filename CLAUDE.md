# Crosspollinator

## Project Structure

- `output/YYYY-MM-DD/*.html` — Self-contained single-file HTML games
- `apps.js` — Auto-generated manifest that powers the portal (index.html)
- `scripts/build_index.py` — Rebuilds `apps.js` from the `output/` directory

## Critical Rule: Always Rebuild apps.js

**After creating, modifying, or deleting any HTML file in `output/`, you MUST run:**

```bash
python3 scripts/build_index.py
```

This regenerates `apps.js`, which is the manifest the portal reads to display games.
If you skip this step, new or updated games will NOT appear on the site.

Always commit the updated `apps.js` alongside your HTML changes.
