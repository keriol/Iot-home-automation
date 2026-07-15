# Project Model

This directory contains public-safe project model snapshots.

The active private model lives in the local-only Alfred repository and is never committed here.

## Export

Run:

    ./scripts/export-project-model.sh

Optional date override:

    ./scripts/export-project-model.sh 2026-07-15

Default private source:

    $HOME/alexa-ha-bridge/docs/model/home-automation-project-model-private.md

Override:

    PRIVATE_MODEL_PATH=/custom/path/model.md \
      ./scripts/export-project-model.sh

The exporter removes private-only sections, sanitizes infrastructure identifiers and validates both models against the strict `<8K` character limit.

Every generated diff must be reviewed before commit and push.
