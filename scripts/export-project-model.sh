#!/usr/bin/env bash
set -euo pipefail

DATE="${1:-$(date +%F)}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PRIVATE_DIR="${PRIVATE_MODEL_DIR:-/home/server/project-model-private}"
PUBLIC_DIR="$REPO_ROOT/docs/project-model"

PRIVATE_MODEL="$PRIVATE_DIR/project-model-private.md"
PRIVATE_SNAPSHOT="$PRIVATE_DIR/project-model-private-$DATE.md"

PUBLIC_MODEL="$PUBLIC_DIR/project-model-public.md"
PUBLIC_SNAPSHOT="$PUBLIC_DIR/project-model-public-$DATE.md"

mkdir -p "$PRIVATE_DIR"
chmod 700 "$PRIVATE_DIR"

mkdir -p "$PUBLIC_DIR"

if [[ ! -f "$PRIVATE_MODEL" ]]; then
  cat > "$PRIVATE_MODEL" <<'MODEL'
# Private Project Model

Paste the current internal GPT project model here.

This file must stay outside the public repository.

Do not commit:
- domains
- IP addresses
- tokens
- secrets
- entity IDs
- emails
- hostnames
- personal identifiers
MODEL

  echo "Created private model template:"
  echo "$PRIVATE_MODEL"
  echo "Edit it, then run this script again."
  exit 0
fi

cp "$PRIVATE_MODEL" "$PRIVATE_SNAPSHOT"

PUBLIC_TEMPLATE="$PUBLIC_DIR/public-template.md"

if [[ -f "$PUBLIC_TEMPLATE" ]]; then
  cp "$PUBLIC_TEMPLATE" "$PUBLIC_MODEL"
else
  cat > "$PUBLIC_MODEL" <<'MODEL'
# Home Automation Project Model (Public)

## Overview

Local-first smart-home and IoT platform built using Home Assistant, MQTT, Python, Node-RED and AI-assisted engineering practices.

## Core Stack

- Home Assistant
- MQTT
- Node-RED
- Python
- Docker

## Architecture Principles

- Local-first
- Event-driven
- Public-safe
- One owner per feature
- Avoid duplicated logic

## Next Steps

- Voice-controlled appliance workflows
- Presence stabilization
- Energy validation
- Additional case studies
- Portfolio expansion
MODEL
fi

cp "$PUBLIC_MODEL" "$PUBLIC_SNAPSHOT"

echo "Private snapshot:"
echo "$PRIVATE_SNAPSHOT"
echo
echo "Public model:"
echo "$PUBLIC_MODEL"
echo
echo "Public snapshot:"
echo "$PUBLIC_SNAPSHOT"
echo
echo "Next:"
echo "git add docs/project-model scripts/export-project-model.sh"
echo "git commit -m \"Add project model export script\""
echo "git push"
