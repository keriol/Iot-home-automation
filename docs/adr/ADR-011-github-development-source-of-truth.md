# ADR-011 - GitHub as Development Source of Truth

## Status

Accepted

Supersedes ADR-009 for current development-state ownership.

ADR-009 remains a historical record of the earlier Umberto-based development model.

## Context

Keriol Home, Alfred, Butler Core, Wilfred and public plugins now evolve across multiple GitHub repositories.

The previous model assigned active development-state ownership to Umberto while Git stored implementation and documentation. That separation was useful during an earlier phase of the project, but it created a second planning ledger beside GitHub and required reconciliation between task state, branch state, commits and public repositories.

As the Butler ecosystem became more public and multi-repository, development planning needed to live where implementation, review and public collaboration already happen.

The retired Umberto ledger remains useful only for historical recovery and archival context. It must not override current GitHub or Git evidence.

Runtime behavior remains a separate concern: neither GitHub Issues nor documentation can prove the current state of a deployed service or physical device.

## Decision

GitHub is the development source of truth for the Butler ecosystem and Keriol Home engineering workflow.

### GitHub Issues

GitHub Issues are authoritative for:

- tasks;
- priorities;
- dependencies;
- planning;
- active development status;
- backlog state;
- implementation follow-up.

New development work starts from a GitHub Issue.

### Git

Git is authoritative for:

- source code;
- tracked configuration;
- versioned documentation;
- ADRs;
- repository history;
- merged implementation state.

Branches and commits should reference the owning issue or stable project ID when useful.

### Commits, tags, workflows and releases

These are authoritative evidence for implementation and release state.

A task, branch or dispatch action does not by itself prove a release. Release claims require explicit Git/tag/release/workflow evidence appropriate to the repository.

### Live systems

Live systems are authoritative for deployed operational truth, including:

- service health;
- deployed behavior;
- Home Assistant state;
- integrations;
- physical device state;
- observable post-action results.

Documentation and Git history do not substitute for runtime verification.

### Portfolio and project models

The public portfolio and current project models are derived documentation.

They summarize:

- durable architecture;
- component ownership;
- capability maturity;
- public/private boundaries;
- selected verified engineering lessons.

They are not task ledgers and must not independently redefine development status.

## Documentation promotion rule

Public documentation must distinguish evidence maturity.

A capability or behavior may be described as **Public**, **Available** or implemented only when supported by merged/released evidence in its owning public repository.

Open branches and issues may support wording such as:

- planned;
- candidate;
- in testing;
- private proving ground;
- designed to enable.

The existence of a branch is not evidence that a feature is available.

## Historical records

Historical ADRs, worklogs, project-model snapshots and migrated issue metadata remain valid records of what the project believed or used at that time.

They should not be silently rewritten to match current architecture.

When a durable decision changes, a new ADR supersedes the old decision while preserving the historical record.

## Public/private boundary

GitHub centralization does not weaken the private/public split.

- Alfred implementation remains private.
- Public reusable implementation belongs in Butler Core, Wilfred or an official public plugin.
- The public portfolio contains sanitized architecture and derived documentation only.
- Secrets, private endpoints, sensitive state, private provider identifiers, unnecessary entity IDs and private acquisition implementation remain excluded.

## Consequences

### Positive

- Development state has one visible authority per repository.
- Branches, issues, commits and releases can be reconciled without a parallel ledger.
- Public development happens in the same system used for collaboration and evidence.
- Portfolio updates can reference explicit repository evidence.
- Historical planning data can remain archived without influencing current status.

### Trade-offs

- Cross-repository state requires consulting the owning repositories rather than one centralized private ledger.
- The portfolio must deliberately avoid becoming a second project tracker.
- Runtime claims still require live-system evidence separate from GitHub.

## Maintenance

The portfolio should be reviewed when a change materially affects:

- a public release baseline;
- architectural ownership;
- capability maturity;
- public extraction status;
- a documented case study;
- a durable ADR decision.

Routine internal fixes do not require portfolio churn when they do not change those public-facing facts.

## Superseded guidance

This ADR supersedes ADR-009 for current development-state ownership.

ADR-009 remains historically valid for the period when Umberto was the active development ledger.
