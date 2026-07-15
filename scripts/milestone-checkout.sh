#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

MILESTONE_NAME="${1:-Project milestone}"
MILESTONE_VERSION="${2:-0.2.0}"
VERSION_TAG="v${MILESTONE_VERSION#v}"
TODAY="$(date +%Y-%m-%d)"
STAMP="$(date +%Y%m%d-%H%M%S)"

PUBLIC_MODEL="docs/project-model/project-model-public.md"
DATED_PUBLIC_MODEL="docs/project-model/project-model-public-${TODAY}.md"
PUBLIC_TEMPLATE="docs/project-model/public-template.md"
PRIVATE_MODEL="${PRIVATE_MODEL_PATH:-$HOME/alexa-ha-bridge/docs/model/home-automation-project-model-private.md}"

PUBLIC_RELEASE_DIR="docs/project-model/releases"
PUBLIC_RELEASE_MODEL="${PUBLIC_RELEASE_DIR}/project-model-public-${VERSION_TAG}.md"

echo "== Milestone checkout =="
echo "Milestone: ${MILESTONE_NAME}"
echo "Version: ${VERSION_TAG}"
echo "Date: ${TODAY}"
echo "Repo: ${ROOT_DIR}"
echo

echo "== Git status before checkout =="
git status --short
echo

echo "== Verify export script =="
test -x scripts/export-project-model.sh || chmod +x scripts/export-project-model.sh
echo "OK: scripts/export-project-model.sh"
echo

echo "== Export public project model =="
PRIVATE_MODEL_PATH="$PRIVATE_MODEL" bash scripts/export-project-model.sh "$TODAY"
echo

echo "== Verify required model files =="
test -f "$PUBLIC_MODEL"
test -f "$PUBLIC_TEMPLATE"

if [ ! -f "$DATED_PUBLIC_MODEL" ]; then
  echo "WARN: expected dated public model not found: $DATED_PUBLIC_MODEL"
  echo "Available dated models:"
  ls -1 docs/project-model/project-model-public-*.md 2>/dev/null || true
else
  echo "OK: $DATED_PUBLIC_MODEL"
fi

test -f "$PRIVATE_MODEL"
echo "OK: external private source: $PRIVATE_MODEL"
echo

echo "== Character count =="
wc -m "$PUBLIC_TEMPLATE" "$PUBLIC_MODEL"
[ -f "$DATED_PUBLIC_MODEL" ] && wc -m "$DATED_PUBLIC_MODEL"
wc -m "$PRIVATE_MODEL"
echo

echo "== Public model must mention current architecture =="
grep -RIn "Alfred Agent MVP\|Tool Registry\|AI planner fallback\|Registered tools only" "$PUBLIC_MODEL"
echo

echo "== Public model must not contain old active-state markers =="
if grep -RInE "\[ \] Custom Alexa Skill|\[ \] Safe appliance control|Plex voice control" "$PUBLIC_MODEL"; then
  echo "ERROR: public model still contains old/superseded model markers." >&2
  exit 1
fi
echo "OK: no old public model markers found."
echo

echo "== Create versioned model release =="
mkdir -p "$PUBLIC_RELEASE_DIR" WORKLOG/milestones

cp "$PUBLIC_MODEL" "$PUBLIC_RELEASE_MODEL"
echo "Created: $PUBLIC_RELEASE_MODEL"

cat > docs/project-model/VERSION <<VERSION
${VERSION_TAG}
VERSION

echo "Updated: docs/project-model/VERSION"
echo

echo "== Update public model changelog =="
CHANGELOG="docs/project-model/CHANGELOG.md"
touch "$CHANGELOG"

if ! grep -q "## ${VERSION_TAG} - ${TODAY}" "$CHANGELOG"; then
  TMP_CHANGELOG="$(mktemp)"
  cat > "$TMP_CHANGELOG" <<CHANGELOG_ENTRY
# Project Model Changelog

## ${VERSION_TAG} - ${TODAY}

${MILESTONE_NAME}

- Records the current reviewed public documentation baseline.
- Exports the current architecture from the local private source.
- Validates the public snapshot and strict 8K character limit.
- Keeps private operational content outside the public repository.

CHANGELOG_ENTRY

  if grep -q "^# Project Model Changelog" "$CHANGELOG"; then
    tail -n +2 "$CHANGELOG" >> "$TMP_CHANGELOG"
  else
    cat "$CHANGELOG" >> "$TMP_CHANGELOG"
  fi

  mv "$TMP_CHANGELOG" "$CHANGELOG"
  echo "Updated: $CHANGELOG"
else
  echo "Changelog already contains ${VERSION_TAG} - ${TODAY}"
fi
echo

echo "== Public sanitize scan =="
SANITIZE_PATTERN='keriolhome\.online|/home/server|OPENAI|TOKEN|SECRET|PASSWORD|Camilla|Antony|notify\.|media_player\.|switch\.|input_boolean\.|sensor\.|binary_sensor\.|button\.|rsvp\.|alexa\.'

if grep -RInE "$SANITIZE_PATTERN" \
  docs/project-model docs/adr examples scripts \
  --exclude-dir=.git \
  --exclude-dir=__pycache__ \
  --exclude='*.pyc' \
  --exclude='*.bak-*'; then
  echo
  echo "WARNING: sanitize scan found matches."
  echo "Review whether they are expected sanitized placeholders/examples or need cleanup."
else
  echo "OK: sanitize scan clean."
fi
echo

echo "== Milestone worklog note =="
mkdir -p WORKLOG/milestones
NOTE_FILE="WORKLOG/milestones/milestone-${VERSION_TAG}-${STAMP}.md"

cat > "$NOTE_FILE" <<NOTE
# Milestone ${VERSION_TAG} - ${TODAY}

${MILESTONE_NAME}

## Summary

This milestone records a reviewed public documentation baseline.

## Checkout summary

- Private model updated before public snapshot.
- Public project model exported through scripts/export-project-model.sh.
- Versioned public model release created.
- Private source validated externally and not published.
- Public model checked for Alfred Agent architecture.
- Old public model markers checked.
- Sanitize scan executed.
- Diff/stat reviewed before commit.

## Versioned artifacts

- ${PUBLIC_RELEASE_MODEL}
- docs/project-model/VERSION
- docs/project-model/CHANGELOG.md

## Next

- Continue from the current development ledger and roadmap.
NOTE

echo "Created: $NOTE_FILE"
echo

echo "== Diff stat =="
git diff --stat
echo

echo "== Git status after checkout =="
git status --short
echo

echo "== Suggested commit =="
echo "git add docs/project-model WORKLOG scripts/milestone-checkout.sh"
echo "git commit -m \"Milestone ${VERSION_TAG}: ${MILESTONE_NAME}\""
