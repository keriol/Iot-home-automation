# Historical Analysis - Umberto Development Ledger

## Status

**Superseded historical evidence.**

This document describes the development-ledger model used before GitHub became the development source of truth. It is retained to preserve the evolution of the engineering workflow.

Current development governance is defined by [ADR-011 - GitHub as Development Source of Truth](../adr/ADR-011-github-development-source-of-truth.md).

## Historical Purpose

Umberto was used as the structured development ledger and checkout coordinator for Keriol Home.

It kept engineering planning separate from the smart-home runtime: Alfred operated the house while the ledger recorded work, status and completion evidence.

## Historical Foundation

The implementation provided:

- SQLite-backed milestones and tasks;
- explicit status and priority values;
- owner, branch and acceptance criteria;
- task-to-commit evidence;
- deterministic task ordering;
- session-start summaries;
- Markdown ledger export;
- automated unit tests.

The runtime database remained private and was never part of the public portfolio.

## Structural Model

| Entity | Historical purpose |
|---|---|
| Milestone | Group work into an ordered delivery horizon |
| Task | Store scope, status, priority, owner and acceptance criteria |
| Dependency | Describe prerequisites between tasks |
| Commit evidence | Link implementation history to planning records |
| Markdown export | Produce a reviewable development snapshot |

## Deterministic Selection

Task recommendation did not require an AI model.

Ordering preferred work already in progress, followed by review, ready and backlog work. Within the same status, higher priority won. Blocked, completed and cancelled work were excluded.

This made recommendations repeatable and explainable.

## Checkout Direction at the Time

The planned checkout model aimed to combine service health, compile/test evidence, documentation, sanitization, diff review and explicit human approval before publication.

That direction remains historically interesting, but the active Butler development workflow now uses GitHub Issues and Git rather than this ledger.

## Historical Diagram

- [Historical Checkout Flow Diagram](../diagrams/umberto-checkout-flow.md)

## Current Interpretation

The useful lesson retained from this experiment is the separation between planning, implementation evidence, runtime evidence and human approval.

The tooling itself is retired from Butler development and must not override current GitHub, Git or live-system evidence.
