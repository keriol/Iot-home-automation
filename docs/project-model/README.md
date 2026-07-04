# Project Model

This directory contains public-safe project model snapshots.

The private operational model is stored outside the repository and must never be committed.

## Export Procedure

Run:

./scripts/export-project-model.sh

Optional date override:

./scripts/export-project-model.sh 2026-05-30

## Private Model

Default private path:

$HOME/project-model-private/project-model-private.md

Override with:

PRIVATE_MODEL_DIR=/custom/private/path ./scripts/export-project-model.sh

## Rules

Public snapshots must not contain:

- Secrets
- Tokens
- IP addresses
- Domains
- Entity IDs
- Hostnames
- Emails
- Personal identifiers
