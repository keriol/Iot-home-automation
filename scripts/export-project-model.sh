#!/usr/bin/env bash
set -euo pipefail

DATE="${1:-$(date +%F)}"

REPO_ROOT="$(
  cd "$(dirname "${BASH_SOURCE[0]}")/.." &&
  pwd
)"

PUBLIC_DIR="$REPO_ROOT/docs/project-model"
PUBLIC_MODEL="$PUBLIC_DIR/project-model-public.md"
PUBLIC_SNAPSHOT="$PUBLIC_DIR/project-model-public-$DATE.md"

cd "$REPO_ROOT"

if [[ ! -f "$PUBLIC_MODEL" ]]; then
  echo "ERROR: public model not found: $PUBLIC_MODEL" >&2
  exit 1
fi

python3 scripts/check-project-models.py

if [[ -e "$PUBLIC_SNAPSHOT" ]]; then
  echo "ERROR: historical snapshot already exists: $PUBLIC_SNAPSHOT" >&2
  echo "Historical project-model snapshots are immutable." >&2
  exit 1
fi

cp "$PUBLIC_MODEL" "$PUBLIC_SNAPSHOT"

echo
echo "Public model:"
echo "$PUBLIC_MODEL"

echo
echo "Immutable snapshot:"
echo "$PUBLIC_SNAPSHOT"

echo
echo "Character counts:"
wc -m \
  "$PUBLIC_MODEL" \
  "$PUBLIC_SNAPSHOT"

echo
echo "Snapshot created successfully."
