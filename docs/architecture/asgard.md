---
title: Asgard
kind: architecture
owner: concrete-butler
scope: public-safe
status: released-boundary
baseline: 0.1.0
related:
  - ../api/bifrost.md
  - midgard.md
  - ../milestones/ignition-001.md
---

# Asgard

Asgard is the Butler-owned ingress and identity boundary used when Midgard must
enter a concrete Butler runtime.

Asgard is **not** a Butler Core plugin and is **not** owned by Midgard.

## Ownership

Each concrete Butler owns its own Asgard.

The Butler owns:

- canonical Butler identity;
- aliases/nicknames where supported;
- runtime-specific ingress composition;
- policy and lifecycle around the active Butler instance.

Asgard projects that Butler-owned identity to Midgard and exposes the governed
entry boundary for Butler-owned behavior.

## Canonical topology

```text
Interphone
   |
Bifröst
   |
Midgard
   |
Asgard ("Alfred")
   |
Alfred
```

Another compatible Butler can own another Asgard without changing Bifröst,
Midgard or Butler Core.

## IGNITION-001 implementation

In IGNITION-001, Asgard `0.1.0` is an Alfred-owned internal compatibility
component shipped inside Alfred `0.5.0`.

It does not have an independent package, repository, tag or artifact lifecycle
in that release.

## Identity authority

On the concrete-Butler path, Asgard is authoritative for the responding
Butler's identity.

IGNITION-001 proved this contract by returning canonical:

```text
Source Butler: Alfred
```

to the real Android client while preserving the originating request
correlation identifier.

## Scope boundary

Asgard does not own:

- Bifröst transport;
- Midgard cross-Butler routing;
- Butler Core;
- provider plugins such as HAP;
- global client UX;
- domain behavior outside the concrete Butler that hosts it.

## Future direction

A reusable standalone Asgard package is a post-Ignition direction. The released
Ignition baseline proves the boundary through Alfred-owned Asgard without
claiming that standalone extraction is already complete.


## GitHub lineage

Asgard is Butler-owned, so its implementation lineage spans the concrete Butler
and the communication-layer extraction work.

Selected issues:

- [ALF-202 — move Alfred Butler identity ownership into the runtime](https://github.com/keriol/alfred/issues/333)
- [ALF-218 — version Alfred-owned Asgard 0.1.0 for Ignition](https://github.com/keriol/alfred/issues/359)
- [ALF-207 — complete Alfred/Asgard self-description](https://github.com/keriol/alfred/issues/342)
- [MID-005 — extract a standalone Asgard package](https://github.com/keriol/butler-core-midgard-plugin/issues/8)

The standalone extraction issue represents post-Ignition direction and must not
be read as evidence that Asgard already has an independent released package.
