# 02 — Governance and Evidence Model

## Question

Which source is authoritative for development state, implementation state, release state and runtime truth?

## Problem observed

The earlier portfolio model separated responsibilities between Git and a private development ledger. That model had been useful, but after the Butler ecosystem spread across multiple GitHub repositories it created duplicated development state:

- task status lived outside the repositories where implementation happened;
- public and private work needed reconciliation across two planning systems;
- branch and commit evidence could disagree with ledger state;
- portfolio maintenance risked becoming another manually synchronized state store.

This is exactly the kind of duplication that produces documentation drift.

## Current source-of-truth model

The analysis established four distinct authorities.

### GitHub Issues

Authoritative for:

- tasks;
- priorities;
- dependencies;
- planning;
- active development status;
- backlog state;
- follow-up work.

New development begins from a GitHub Issue.

### Git

Authoritative for:

- merged implementation;
- tracked configuration;
- versioned documentation;
- ADRs;
- repository history.

### Commits, tags, workflows and releases

Authoritative evidence for implementation and release state.

A branch, issue, commit message or workflow dispatch by itself does not prove that a release exists.

Release wording must be tied to explicit release/tag evidence appropriate to the repository.

### Live systems

Authoritative for:

- deployed behavior;
- service health;
- Home Assistant state;
- integrations;
- physical device state;
- observable post-action results.

Git history cannot prove that a physical action succeeded in the deployed home.

## Why the portfolio is not a fifth source of truth

The portfolio is deliberately **derived documentation**.

It summarizes architecture, evidence-backed maturity and selected engineering lessons, but it does not independently define task or release state.

That prevents the public repository from becoming another project-management database.

## Historical ADR handling

ADR-009 recorded the earlier development-governance decision and was valid for its time.

Rewriting ADR-009 to describe the new GitHub model would destroy useful history.

The correct action was therefore:

1. preserve ADR-009 unchanged as historical evidence;
2. add ADR-011 describing GitHub as the current development source of truth;
3. mark ADR-011 as superseding ADR-009 for current governance.

This preserves chronology while keeping current documentation unambiguous.

## Documentation promotion rule

The audit introduced a strict promotion rule:

- merged/released evidence may support `Available`, `Public` or implemented wording;
- open issues and branches may support only direction/testing wording;
- branch existence never proves feature availability.

This is especially important in a multi-repository project where architecture may be intentionally prepared before public extraction occurs.

## Outcome

The current documentation model is:

`GitHub Issues -> Git/main -> release evidence -> live verification -> derived portfolio`

Each layer answers a different question and no document is allowed to impersonate another source of truth.
