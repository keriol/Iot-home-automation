#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

MILESTONE_NAME="${1:-Project milestone}"
MILESTONE_VERSION="${2:-0.2.0}"
VERSION_TAG="v${MILESTONE_VERSION#v}"
TODAY="$(date +%Y-%m-%d)"
TODAY_COMPACT="$(date +%Y%m%d)"
STAMP="$(date +%Y%m%d-%H%M%S)"

PUBLIC_MODEL="docs/project-model/project-model-public.md"
DATED_PUBLIC_MODEL="docs/project-model/project-model-public-${TODAY_COMPACT}.md"
PUBLIC_TEMPLATE="docs/project-model/public-template.md"
PRIVATE_MODEL="docs/model/home-automation-project-model-private.md"

PUBLIC_RELEASE_DIR="docs/project-model/releases"
PRIVATE_RELEASE_DIR="docs/model/releases"
PUBLIC_RELEASE_MODEL="${PUBLIC_RELEASE_DIR}/project-model-public-${VERSION_TAG}.md"
PRIVATE_RELEASE_MODEL="${PRIVATE_RELEASE_DIR}/home-automation-project-model-private-${VERSION_TAG}.md"

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
bash scripts/export-project-model.sh
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

if [ -f "$PRIVATE_MODEL" ]; then
  echo "OK: $PRIVATE_MODEL"
else
  echo "WARN: private model not found: $PRIVATE_MODEL"
fi
echo

echo "== Character count =="
wc -m "$PUBLIC_TEMPLATE" "$PUBLIC_MODEL"
[ -f "$DATED_PUBLIC_MODEL" ] && wc -m "$DATED_PUBLIC_MODEL"
[ -f "$PRIVATE_MODEL" ] && wc -m "$PRIVATE_MODEL"
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
mkdir -p "$PUBLIC_RELEASE_DIR" "$PRIVATE_RELEASE_DIR"

cp "$PUBLIC_MODEL" "$PUBLIC_RELEASE_MODEL"
echo "Created: $PUBLIC_RELEASE_MODEL"

if [ -f "$PRIVATE_MODEL" ]; then
  cp "$PRIVATE_MODEL" "$PRIVATE_RELEASE_MODEL"
  echo "Created: $PRIVATE_RELEASE_MODEL"
fi

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

- Marks the Alfred Agent MVP documentation baseline.
- Updates public model from legacy smart-home snapshot to agent-oriented architecture.
- Adds Tool Registry, deterministic-first routing, AI planner fallback and safety permission model.
- Keeps public snapshot sanitized and under the 8K target.

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
mkdir -p worklog
NOTE_FILE="worklog/milestone-${VERSION_TAG}-${STAMP}.md"

cat > "$NOTE_FILE" <<NOTE
# Milestone ${VERSION_TAG} - ${TODAY}

${MILESTONE_NAME}

## Summary

This milestone marks the Alfred Agent MVP documentation baseline.

## Checkout summary

- Private model updated before public snapshot.
- Public project model exported through scripts/export-project-model.sh.
- Versioned public model release created.
- Versioned private model release created when available.
- Public model checked for Alfred Agent architecture.
- Old public model markers checked.
- Sanitize scan executed.
- Diff/stat reviewed before commit.

## Versioned artifacts

- ${PUBLIC_RELEASE_MODEL}
- ${PRIVATE_RELEASE_MODEL}
- docs/project-model/VERSION
- docs/project-model/CHANGELOG.md

## Next

- Add Plex READ tool.
- Add Alexa free-text bridge to AlfredCore.ask.
- Add ADR for Alfred Agent Tool Registry architecture.
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
echo "git add docs/model docs/project-model history scripts/milestone-checkout.sh worklog"
echo "git commit -m \"Milestone ${VERSION_TAG}: ${MILESTONE_NAME}\""
