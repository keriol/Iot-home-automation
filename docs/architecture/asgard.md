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

## Standalone Asgard adoption after Ignition

The **Butler Asgard Plugin** is now an independently packaged, framework-neutral
Python boundary (`butler-asgard`, imported as `butler_asgard`). It accepts a
Butler-owned identity, an async request handler and an availability probe;
it supports exact name/alias matching and preserves request correlation while
returning the canonical Butler source name.

On 2026-10-10, Alfred adopted a privately distributed standalone
`0.1.0.dev0` development package and passed server integration checks,
a healthy runtime restart and an Android Interphone request/reply test
(including a laundry request). This proves a **private consumer integration**,
not a public Asgard release or general multi-Butler compatibility.

The historical **IGNITION-001** release remains unchanged: Alfred `0.5.0`
shipped its own internal Asgard compatibility boundary `0.1.0`.
The later standalone adoption must not be retroactively added to that release
Bill of Materials.

The standalone Asgard repository remains private pending publication audit.
Wilfred/Manfred as additional network-connected Butler consumers, profile-image
payload projection, and a public package/tag/release remain separately tracked
work. No private source or deployment configuration is published here.


## GitHub lineage

Asgard is Butler-owned. In the Ignition baseline its concrete implementation is
owned by Alfred.

Selected lineage:

- ALF-184, Alfred Ignition proving release: https://github.com/keriol/alfred/issues/300
- ALF-202, runtime identity ownership: https://github.com/keriol/alfred/issues/333
- ALF-218, Alfred-owned Asgard 0.1.0: https://github.com/keriol/alfred/issues/359
- HER-010, interactive output through Asgard/Midgard: https://github.com/keriol/alfred/issues/338
- MID-005, standalone Asgard extraction direction: https://github.com/keriol/butler-core-midgard-plugin/issues/8

HER-010 and standalone extraction remain follow-up design/development work unless
their owning issues/release evidence say otherwise.
