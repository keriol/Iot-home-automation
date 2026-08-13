# ADR-009 - Development State Sources of Truth

## Status

Accepted

## Context

The project originally used a compact project model as the primary persistent knowledge source between development sessions.

That approach was useful while Keriol Home was smaller and most work happened inside one private repository.

The project has since evolved into several repositories and independently versioned components, including Butler Core, Wilfred, official plugins and the private Alfred deployment.

At the same time, Umberto evolved from a documentation aid into the structured development ledger and checkout coordinator.

Maintaining task status, priorities, milestones and implementation evidence both in Umberto and in a manually synchronized project model creates duplicated state and inevitable drift.

Runtime state also cannot be made authoritative through documentation because live services and physical systems remain the only reliable source for operational truth.

## Decision

The project uses separate sources of truth according to responsibility.

### Git

Git is authoritative for:

- source code;
- tracked configuration;
- versioned documentation;
- ADRs;
- repository history;
- released implementation state.

### Umberto

Umberto is authoritative for active development state:

- tasks;
- status;
- priorities;
- milestones;
- dependencies;
- repository coordination;
- implementation evidence;
- checkout evidence;
- release coordination state.

Task and milestone state should not be manually duplicated into a project model.

### Runtime

Live systems are authoritative for operational state.

Examples include:

- service health;
- container state;
- Home Assistant entities;
- physical device state;
- deployed versions;
- reachable integrations.

Documentation must not substitute for runtime verification.

### Project model

The project model is a derived architectural summary.

Its purpose is to provide compact context about:

- current architecture;
- component responsibilities;
- major design principles;
- public/private boundaries;
- high-level capability maturity.

It is not the authoritative ledger for tasks, priorities, milestones or runtime status.

The model may be refreshed after meaningful architectural changes or release milestones rather than continuously after every development action.

## Public project model

The public model is maintained as a sanitized current architectural snapshot.

Dated copies are immutable historical snapshots.

The public model may be informed by Git, Umberto and verified runtime evidence, but it does not replace any of them.

## Consequences

### Positive

- Development state has one structured authority.
- Documentation no longer requires duplicate task bookkeeping.
- Project-model drift no longer blocks unrelated development.
- Runtime claims remain grounded in live verification.
- Public documentation can stay concise and architecture-focused.
- Multi-repository development scales more naturally.

### Negative

- Recovering full project state may require consulting more than one source.
- Project-model snapshots may intentionally lag minor implementation changes.
- Tooling built around strict private/public model parity must be updated.

## Superseded guidance

This ADR supersedes the parts of ADR-005 that describe the continuously updated project model as the primary or authoritative project knowledge source.

ADR-005 remains historically valid as the description of the earlier AI-assisted development workflow.
