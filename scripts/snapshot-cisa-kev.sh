#!/usr/bin/env bash
set -euo pipefail

# Snapshot and diff the CISA Known Exploited Vulnerabilities (KEV) catalog.
# Creates timestamped JSON snapshots under sources/, and
# writes a unified diff vs the previous snapshot when changes occur.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

OUT_DIR="sources"
mkdir -p "$OUT_DIR"

URL="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
TMP_RAW="$(mktemp)"
TMP_NORM="$(mktemp)"

curl -fsSL "$URL" -o "$TMP_RAW"

# If jq is available, write a normalized, sorted JSON to keep diffs small.
if command -v jq > /dev/null 2>&1; then
  jq -S . "$TMP_RAW" > "$TMP_NORM"
  rm -f "$TMP_RAW"
  TMP_FILE="$TMP_NORM"
else
  TMP_FILE="$TMP_RAW"
  rm -f "$TMP_NORM"
fi

LATEST_SNAPSHOT=""
if ls "$OUT_DIR"/cisa-kev-20*.json > /dev/null 2>&1; then
  LATEST_SNAPSHOT="$(ls "$OUT_DIR"/cisa-kev-20*.json | sort | tail -n 1)"
fi

if [[ -n "$LATEST_SNAPSHOT" ]] && diff -q "$LATEST_SNAPSHOT" "$TMP_FILE" > /dev/null 2>&1; then
  echo "[KEV] No change in catalog (still: $(basename "$LATEST_SNAPSHOT"))" >&2
  rm -f "$TMP_FILE"
  exit 0
fi

TIMESTAMP="$(date -u +"%Y%m%dT%H%M%SZ")"
SNAPSHOT="$OUT_DIR/cisa-kev-${TIMESTAMP}.json"

mv "$TMP_FILE" "$SNAPSHOT"
cp "$SNAPSHOT" "$OUT_DIR/cisa-kev-latest.json"

if [[ -n "$LATEST_SNAPSHOT" ]]; then
  DIFF_FILE="$OUT_DIR/cisa-kev-diff-${TIMESTAMP}.txt"
  diff -u "$LATEST_SNAPSHOT" "$SNAPSHOT" > "$DIFF_FILE" || true
  echo "[KEV] Change detected. New snapshot: $(basename "$SNAPSHOT")" >&2
  echo "[KEV] Diff written to: $(basename "$DIFF_FILE")" >&2
else
  echo "[KEV] Initial snapshot created: $(basename "$SNAPSHOT")" >&2
fi
