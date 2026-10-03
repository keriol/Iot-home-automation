---
title: Midgard
kind: architecture
owner: midgard
scope: public
status: released
baseline: 0.1.0
depends_on:
  - butler-core
related:
  - ../api/bifrost.md
  - asgard.md
  - ../milestones/ignition-001.md
---

# Midgard

Midgard is the provider-neutral communication and cross-Butler routing layer of
the Butler ecosystem.

It sits behind Bifröst and decides whether a request remains in the shared Core
world or must be routed to a concrete Butler through that Butler's Asgard.

## Canonical position

```text
External client
      |
    Bifröst
      |
    Midgard
   /       \
Core      Butler-owned Asgard
 |               |
plugin       concrete Butler
```

## Ownership

Midgard owns:

- provider-neutral request/response channel contracts;
- request correlation preservation;
- visibility of Butler-owned Asgard targets through neutral ports;
- deterministic cross-Butler selection;
- structured routing failures;
- safe routing/session metadata transport;
- routing observability through Core-owned tracing contracts.

Midgard does not own:

- the client's transport protocol;
- a Butler's canonical identity;
- a Butler's Asgard implementation;
- concrete domain behavior;
- Home Assistant semantics;
- user preference;
- authentication/permission/confirmation policy.

## Butler identity

Each concrete Butler owns its own identity through Asgard.

Midgard routes using identity projected by visible Asgard targets. It does not
maintain a second authoritative identity registry.

Request-side metadata may carry `target_butler_name`. A Butler-facing response
returns `source_butler_name` from the selected Asgard.

## Core-facing requests

A request without a concrete Butler target can remain in the shared Core world:

```text
Bifröst -> Midgard -> Butler Core -> Core plugin
```

This is how IGNITION-001 reaches HAP and Home Assistant without requiring
Alfred.

## Butler-facing requests

A request that targets runtime-owned behavior crosses a Butler-owned Asgard:

```text
Bifröst -> Midgard -> Asgard -> concrete Butler
```

IGNITION-001 proves this path with Alfred.

## Failure behavior

If a requested Butler cannot be resolved, Midgard returns a structured routing
failure. It does not silently select a different Butler.

If a matching target is unavailable or fails to answer, that failure is
reported explicitly.

## IGNITION-001 evidence

Midgard `0.1.0` was proven end-to-end from Android in both the Core/HAP and
Alfred paths, with request correlation preserved and canonical source-Butler
identity visible at the client.

See [IGNITION-001](../milestones/ignition-001.md).
