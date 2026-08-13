# Project Context

The files in this directory retain their historical `project-model` naming for compatibility, but the active document is now a **derived architectural context snapshot** rather than a development-state database.

## Sources of Truth

- **Git** owns versioned implementation and documentation.
- **Umberto** owns active development state, milestones, dependencies and evidence.
- **Live systems** own operational and physical state.
- **Project context** provides a compact derived architectural view.

See [ADR-009 - Development State Sources of Truth](../adr/ADR-009-development-state-sources-of-truth.md).

## Current Public Context

The current public-safe context is:

`docs/project-model/project-model-public.md`

It describes architectural layering, component responsibilities, maturity, public/private boundaries and durable engineering rules.

It intentionally does not duplicate the full development ledger.

## Refresh Policy

Refresh the current context after significant:

- architecture changes;
- ownership changes;
- public/private boundary changes;
- release-baseline changes.

Do not refresh it merely because a task moves, a commit lands, a test passes or runtime health changes.

## Historical Snapshots

Dated files are immutable historical snapshots.

They preserve the architecture and terminology that were current when created.

## Snapshot Tool

`scripts/export-project-model.sh` validates the curated public context and creates an immutable dated snapshot.

It does not derive public documentation mechanically from the private context.

## Public Safety

The public context must exclude readable private-derived implementation, secrets, credentials, personal data, private endpoints, unnecessary real entity IDs, sensitive operational details and private-only implementation.
