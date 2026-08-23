# Project Context

The files in this directory retain their historical `project-model` naming for compatibility, but the active document is a **derived architectural context snapshot**, not a development-state database.

## Sources of Truth

- **GitHub Issues** own tasks, priorities, dependencies, planning and active development status.
- **Git `main`** owns merged implementation and versioned documentation.
- **Commits, tags, workflows and releases** provide implementation and release evidence.
- **Live systems** own deployed operational and physical truth.
- **Project context** provides a compact derived architectural view.

See [ADR-011 - GitHub as Development Source of Truth](../adr/ADR-011-github-development-source-of-truth.md).

ADR-009 remains a historical record of the former Umberto-based development model and is not the current authority.

## Current Public Context

The current public-safe context is:

`docs/project-model/project-model-public.md`

It describes architectural layering, component responsibilities, maturity, public/private boundaries and durable engineering rules.

It intentionally does not duplicate task state or release evidence.

## Refresh Policy

Refresh the current context after significant:

- architecture changes;
- ownership changes;
- public/private boundary changes;
- release-baseline changes;
- capability-maturity changes that affect public wording.

Do not refresh it merely because a task moves, a routine commit lands, a test passes or runtime health changes.

## Historical Snapshots

Dated files are immutable historical snapshots.

They preserve the architecture and terminology that were current when created and may therefore contain superseded governance or maturity language.

## Snapshot Tool

`scripts/export-project-model.sh` validates the curated public context and creates an immutable dated snapshot.

It does not derive public documentation mechanically from the private context.

## Public Safety

The public context must exclude readable private-derived implementation, secrets, credentials, personal data, private endpoints, unnecessary real entity IDs, sensitive operational details, machine-specific private paths and private media-acquisition implementation.
