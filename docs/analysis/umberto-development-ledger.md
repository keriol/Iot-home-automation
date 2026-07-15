# Umberto Development Ledger

## Purpose

Umberto is the development ledger and checkout coordinator for Keriol Home.

It keeps engineering planning separate from the smart-home runtime. Alfred operates the house; Umberto records what work exists, what is active and which evidence supports completion.

## Current Foundation

The current implementation provides:

- SQLite-backed milestones and tasks
- explicit status and priority values
- owner, branch and acceptance criteria
- task-to-commit evidence
- deterministic task ordering
- session-start summaries
- Markdown ledger export
- automated unit tests

The runtime SQLite database remains local and is not published.

## Structural Model

| Entity | Purpose |
|---|---|
| Milestone | Groups work into an ordered delivery horizon |
| Task | Stores scope, status, priority, owner and acceptance criteria |
| Dependency | Describes prerequisites between tasks |
| Commit evidence | Links implementation history to planning records |
| Markdown export | Produces a reviewable development snapshot |

## Deterministic Selection

Task recommendation does not require an AI model.

Current ordering prefers work already in progress, followed by review, ready and backlog work. Within the same status, higher priority wins. Blocked, completed and cancelled work is excluded.

This makes recommendations repeatable and explainable.

## Checkout Direction

The planned checkout engine will:

1. read task requirements
2. verify service health
3. compile and run declared tests
4. collect closure evidence
5. generate reviewable documentation
6. validate the private-to-public boundary
7. show repository diffs
8. prepare task-aware commit messages
9. require human approval before commit, merge or push

## Public Example

- [Sanitized SQLite Development Ledger](../../examples/umberto/development_ledger_sanitized.py)
- [Checkout Flow Diagram](../diagrams/umberto-checkout-flow.md)

## Design Principles

- planning state has one source of truth
- task closure requires real evidence
- generated documentation remains reviewable
- checkout automation never bypasses human Git approval
- private operational details never enter the public portfolio
