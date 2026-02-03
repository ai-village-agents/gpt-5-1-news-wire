#!/usr/bin/env bash
set -euo pipefail

# Snapshot and diff the OFAC Recent Actions index.
# Creates timestamped HTML snapshots under sources/, and
# writes a unified diff vs the previous snapshot when changes occur.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

OUT_DIR="sources"
mkdir -p "$OUT_DIR"

URL="https://ofac.treasury.gov/recent-actions"
TMP_FILE="$(mktemp)"

curl -fsSL "$URL" -o "$TMP_FILE"

# Find the most recent existing snapshot (excluding any non-timestamped files).
LATEST_SNAPSHOT=""
if ls "$OUT_DIR"/ofac-recent-actions-20*.html > /dev/null 2>&1; then
  LATEST_SNAPSHOT="$(ls "$OUT_DIR"/ofac-recent-actions-20*.html | sort | tail -n 1)"
fi

# If we have a previous snapshot and content is identical, do nothing.
if [[ -n "$LATEST_SNAPSHOT" ]] && diff -q "$LATEST_SNAPSHOT" "$TMP_FILE" > /dev/null 2>&1; then
  echo "[OFAC] No change in recent-actions index (still: $(basename "$LATEST_SNAPSHOT"))" >&2
  rm -f "$TMP_FILE"
  exit 0
fi

TIMESTAMP="$(date -u +"%Y%m%dT%H%M%SZ")"
SNAPSHOT="$OUT_DIR/ofac-recent-actions-${TIMESTAMP}.html"

mv "$TMP_FILE" "$SNAPSHOT"
cp "$SNAPSHOT" "$OUT_DIR/ofac-recent-actions-latest.html"

if [[ -n "$LATEST_SNAPSHOT" ]]; then
  DIFF_FILE="$OUT_DIR/ofac-recent-actions-diff-${TIMESTAMP}.txt"
  diff -u "$LATEST_SNAPSHOT" "$SNAPSHOT" > "$DIFF_FILE" || true
  echo "[OFAC] Change detected. New snapshot: $(basename "$SNAPSHOT")" >&2
  echo "[OFAC] Diff written to: $(basename "$DIFF_FILE")" >&2
else
  echo "[OFAC] Initial snapshot created: $(basename "$SNAPSHOT")" >&2
fi
