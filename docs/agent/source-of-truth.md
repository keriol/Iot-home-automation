---
title: Sources of Truth
kind: agent-guide
scope: public
status: current
---

# Sources of Truth

Agents must use the correct source for each kind of claim.

## Development state

GitHub Issues are authoritative for:

- active work;
- priorities;
- dependencies;
- planning;
- open/closed status.

Do not infer project status from project-model prose or recent commits.

## Implementation state

Repository `main` is authoritative for merged implementation and versioned docs.

Feature branches and pull requests are development evidence, not released
capability evidence.

## Release state

Tags, releases and workflows are authoritative for release claims.

Do not infer a release from a version string on `main`.

## Runtime state

Live systems are authoritative for deployed behavior, service health and device
state.

Documentation must not be used as runtime evidence.

## Architecture

Current architecture documentation explains ownership and boundaries. Historical
snapshots and superseded ADRs remain useful for traceability but do not override
current architecture.

## Public/private boundary

Public documentation may describe public-safe architecture, contracts, ownership,
sanitized evidence and engineering lessons.

It must not expose secrets, credentials, private endpoints, household identifiers,
sensitive runtime state, private acquisition details or readable private Alfred
implementation.


## Issue links inside documentation

Current architecture/API pages may link directly to GitHub Issues to preserve
implementation, design and release lineage.

Those links are navigation and traceability aids.

They do not replace the evidence model:

- issue state describes tracked work;
- merged code/documentation on `main` describes implemented repository state;
- tags/releases/workflows describe release state;
- live systems describe runtime state.

Do not turn an open design issue into an implemented capability claim, and do
not assume that closing an issue automatically proves a release or deployed
runtime state.
