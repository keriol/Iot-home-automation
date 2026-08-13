# Project Model

The project model is a compact architectural snapshot, not the operational source of truth for development state.

## Sources of Truth

Current project state is intentionally split by responsibility:

- **Git** is authoritative for versioned code and documentation.
- **Umberto** is authoritative for tasks, milestones, priorities, dependencies and development evidence.
- **Live systems** are authoritative for runtime and physical state.
- **Project models** provide derived architectural context.

See [ADR-009 - Development State Sources of Truth](../adr/ADR-009-development-state-sources-of-truth.md).

## Canonical Public Model

The current public architectural snapshot is:

`docs/project-model/project-model-public.md`

It describes:

- current architectural layering;
- component responsibilities;
- public/private boundaries;
- capability maturity;
- major current engineering principles.

It intentionally does not duplicate the full Umberto task ledger.

## Refresh Policy

The current model should be refreshed when useful, especially after:

- significant architectural changes;
- release milestones;
- major public/private boundary changes;
- substantial changes to component responsibilities.

It does not need to be updated after every task or commit.

## Historical Snapshots

Dated project-model files are immutable historical records.

They preserve the terminology and architecture that were current when they were created.

Historical snapshots should not be rewritten merely to match later architecture.

## Snapshot Tool

`scripts/export-project-model.sh` validates the current public model and creates an immutable dated snapshot.

It no longer derives the public model from a private model.

The public model should instead be curated from authoritative evidence in Git, Umberto and verified runtime state.

## Public Safety

The public model must exclude:

- secrets and credentials;
- private endpoints;
- personal data;
- unnecessary real entity IDs;
- device identifiers;
- private operational details.

Sanitized documentation of Alfred is allowed where it explains the architecture without exposing private implementation details.
