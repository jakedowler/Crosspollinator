#!/usr/bin/env bash
# Batch-file feedback entries as GitHub issues.
# Skips entries already marked "filed": true to prevent duplicates.
# Usage: ./feedback/file-issues.sh [feedback/2026-03-08.json]

set -euo pipefail

REPO="jakedowler/Crosspollinator"
FILE="${1:-feedback/$(date +%Y-%m-%d).json}"

if [ ! -f "$FILE" ]; then
  echo "No feedback file found: $FILE"
  exit 1
fi

if ! command -v gh &>/dev/null; then
  echo "Error: gh CLI not found. Install it first: https://cli.github.com"
  exit 1
fi

COUNT=$(jq length "$FILE")
FILED=0
SKIPPED=0

for i in $(seq 0 $((COUNT - 1))); do
  entry=$(jq ".[$i]" "$FILE")
  already_filed=$(echo "$entry" | jq -r '.filed')

  if [ "$already_filed" = "true" ]; then
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  game=$(echo "$entry" | jq -r '.game')
  text=$(echo "$entry" | jq -r '.text')
  path=$(echo "$entry" | jq -r '.path')
  type=$(echo "$entry" | jq -r '.type')
  timestamp=$(echo "$entry" | jq -r '.time')

  title="[feedback] ${game}"
  body="**Game:** ${game}
**Path:** ${path}
**Type:** ${type}
**Submitted:** ${timestamp}

${text}"

  echo "Filing: ${title}"
  if gh issue create --repo "$REPO" --title "$title" --body "$body" --label feedback; then
    # Mark as filed in the JSON
    jq ".[$i].filed = true" "$FILE" > "${FILE}.tmp" && mv "${FILE}.tmp" "$FILE"
    FILED=$((FILED + 1))
    sleep 1  # rate-limit courtesy
  else
    echo "  FAILED to file issue for entry $i — will retry next run"
  fi
done

echo ""
echo "Done. Filed: $FILED, Skipped (already filed): $SKIPPED, Total: $COUNT"
