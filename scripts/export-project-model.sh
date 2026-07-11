#!/usr/bin/env bash
set -euo pipefail

DATE="${1:-$(date +%F)}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PRIVATE_MODEL="${PRIVATE_MODEL_PATH:-$HOME/alexa-ha-bridge/docs/model/home-automation-project-model-private.md}"

PUBLIC_DIR="$REPO_ROOT/docs/project-model"
PUBLIC_MODEL="$PUBLIC_DIR/project-model-public.md"
PUBLIC_SNAPSHOT="$PUBLIC_DIR/project-model-public-$DATE.md"

cd "$REPO_ROOT"

if [[ ! -f "$PRIVATE_MODEL" ]]; then
  echo "ERROR: private model not found: $PRIVATE_MODEL" >&2
  exit 1
fi

mkdir -p "$PUBLIC_DIR"

python3 - "$PRIVATE_MODEL" "$PUBLIC_MODEL" <<'PY'
from __future__ import annotations

import re
import sys
from pathlib import Path


MAX_CHARS = 8000

source = Path(sys.argv[1]).expanduser().resolve()
target = Path(sys.argv[2]).expanduser().resolve()

text = source.read_text(encoding="utf-8")

private_title = (
    "HOME AUTOMATION PROJECT MODEL - PRIVATE ACTIVE (<8K)"
)
public_title = (
    "HOME AUTOMATION PROJECT MODEL - PUBLIC (<8K)"
)

if private_title not in text:
    raise SystemExit(
        f"ERROR: expected private title not found in {source}"
    )

text = text.replace(
    private_title,
    public_title,
    1,
)

wording_replacements = {
    (
        "One feature per commit. PRIVATE first, "
        "PUBLIC sanitized snapshot second."
    ): (
        "One feature per commit. Private source first, "
        "public sanitized snapshot second."
    ),
    (
        "Release target is salotto, debug target bagno."
    ): (
        "Production and debug notification targets are separated."
    ),
    (
        "Update worklog, ADR/docs and PRIVATE model; "
        "validate below 8K."
    ): (
        "Update worklog, ADR/docs and the private source model; "
        "validate below 8K."
    ),
    (
        "Run sanitizing shell script and review PUBLIC diff."
    ): (
        "Run the sanitizing export and review the public diff."
    ),
    (
        "Commit/push private repo and portfolio."
    ): (
        "Commit the private source and publish the reviewed portfolio."
    ),
}

for old, new in wording_replacements.items():
    text = text.replace(old, new)

sanitize_rules = [
    (
        r"(?i)\bkeriolhome\.online\b",
        "<private-domain>",
    ),
    (
        r"/home/server(?:/[^\s`)]*)?",
        "<private-path>",
    ),
    (
        r"\bserver-keriol-home\b",
        "<private-host>",
    ),
    (
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "<private-ip>",
    ),
    (
        r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "<private-email>",
    ),
    (
        r"\b(?:notify|media_player|switch|input_boolean|"
        r"sensor|binary_sensor|button|rsvp|alexa)"
        r"\.[A-Za-z0-9_]+\b",
        "<private-entity>",
    ),
]

for pattern, replacement in sanitize_rules:
    text = re.sub(pattern, replacement, text)

text = text.rstrip() + "\n"

required_markers = [
    "HOME AUTOMATION PROJECT MODEL - PUBLIC",
    "Alfred the Butler",
    "Tool Registry",
    "Osvaldo",
    "Charon",
    "Presence:",
    "Security/cameras:",
    "Energy/UPS:",
    "Climate:",
    "ROADMAP",
]

for marker in required_markers:
    if marker not in text:
        raise SystemExit(
            f"ERROR: public model missing marker: {marker}"
        )

forbidden_patterns = [
    r"PRIVATE ACTIVE",
    r"(?i)keriolhome\.online",
    r"/home/server",
    r"\bserver-keriol-home\b",
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    r"\bnotify\.",
    r"\bmedia_player\.",
    r"\bswitch\.",
    r"\binput_boolean\.",
    r"\bsensor\.",
    r"\bbinary_sensor\.",
    r"\bbutton\.",
    r"\brsvp\.",
    r"\balexa\.",
]

for pattern in forbidden_patterns:
    if re.search(pattern, text):
        raise SystemExit(
            "ERROR: private pattern remains after sanitization: "
            f"{pattern}"
        )

character_count = len(text)

if character_count >= MAX_CHARS:
    raise SystemExit(
        f"ERROR: public model has {character_count} characters; "
        f"the requirement is fewer than {MAX_CHARS}."
    )

target.write_text(text, encoding="utf-8")

print(f"Private source: {source}")
print(f"Public model: {target}")
print(f"Characters: {character_count}")
print(f"Remaining margin: {MAX_CHARS - character_count}")
PY

cp "$PUBLIC_MODEL" "$PUBLIC_SNAPSHOT"

PRIVATE_MODEL_PATH="$PRIVATE_MODEL" \
  python3 scripts/check-project-models.py

echo
echo "Private source:"
echo "$PRIVATE_MODEL"

echo
echo "Public model:"
echo "$PUBLIC_MODEL"

echo
echo "Public snapshot:"
echo "$PUBLIC_SNAPSHOT"

echo
echo "Character counts:"
wc -m \
  "$PRIVATE_MODEL" \
  "$PUBLIC_MODEL" \
  "$PUBLIC_SNAPSHOT"

echo
echo "Export completed successfully."
