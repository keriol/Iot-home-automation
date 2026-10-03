---
title: Node Manifest and Self-Description
kind: architecture
scope: public
status: mixed-maturity
owners:
  - bifrost
  - midgard
  - concrete-butler
related:
  - ../api/bifrost.md
  - midgard.md
  - asgard.md
---

# Node Manifest and Self-Description

The Butler communication stack is designed so clients can understand the node
they connected to without hard-coded knowledge of Alfred, Wilfred or another
concrete Butler.

The client-facing manifest is composed from metadata owned by the layers that
actually know it.

## Ownership model

```text
Bifröst
  -> protocol version
  -> Bifröst version
  -> client-safe wire serialization
  -> final manifest composition

Midgard
  -> Butler Core version
  -> shared Core plugin metadata
  -> visible Butler descriptors

Asgard
  -> projects the descriptor of one concrete Butler
  -> Asgard compatibility/version metadata
  -> availability projection

Concrete Butler
  -> canonical identity
  -> aliases
  -> description
  -> version
  -> entities
  -> declared capabilities/methods
  -> Butler-local components
  -> readiness/dependencies when authoritative
```

No layer should invent metadata owned by another layer.

## Shared Core stack vs Butler-local stack

A client-safe node description distinguishes shared Core-side components from
components owned by a specific Butler.

Conceptually:

```text
Butler Core
├── Midgard
├── Georges
└── Home Assistant Plugin

Concrete Butler
├── Asgard
├── entities
│   └── declared methods/capabilities
└── Butler-local plugins/components
```

Shared components such as HAP are represented once per node, not duplicated
under every visible Butler.

Bifröst is the external bridge and adds its own protocol/version metadata rather
than pretending to be a Core plugin.

## Privacy boundary

The manifest must remain client-safe.

It must not expose by default:

- credentials or reusable tokens;
- private endpoints;
- filesystem paths;
- private network topology;
- unnecessary Home Assistant entity IDs;
- Keriol-only operational state.

If an address is ever included, it must be explicitly configured as safe to
advertise by the host.

## Butler directory

A smaller read-only Butler directory can expose routable identities independently
of the richer node manifest.

Minimum conceptual entry:

```text
canonical_name
aliases
available
```

Ownership remains:

```text
Concrete Butler
  -> owns identity and aliases

Asgard
  -> projects identity and availability

Midgard
  -> derives the visible directory

Bifröst
  -> transports directory data to clients
```

Midgard must not maintain a second independent Butler identity registry.

## Availability semantics

These terms are intentionally distinct:

- **visible**: an Asgard target is known to the current Midgard composition;
- **available**: that Asgard currently declares itself addressable;
- **responsive**: explicit future health/last-seen evidence confirms response.

`available` must not silently be upgraded into a stronger health claim.

## Maturity

The ownership model and client-safe manifest architecture are established by the
post-Ignition implementation/proving work.

The exact directory/self-description surfaces may continue to evolve on
development lines. Open issues or development branches must not be interpreted
as additional released compatibility claims beyond their owning component's
published release evidence.


## GitHub lineage

The self-description model was assembled across several owners:

- [BIF-010 — transport Butler directory](https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues/18)
- [BIF-011 — compose node manifest](https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues/20)
- [MID-006 — derive Butler directory from visible Asgard identities](https://github.com/keriol/butler-core-midgard-plugin/issues/9)
- [MID-008 — expose Core stack metadata and Butler descriptors](https://github.com/keriol/butler-core-midgard-plugin/issues/12)
- [ALF-205 — mount the Bifröst node manifest on Alfred's authenticated host](https://github.com/keriol/alfred/issues/339)
- [ALF-207 — complete Alfred/Asgard self-description](https://github.com/keriol/alfred/issues/342)

Use the owning issue tracker for active follow-up rather than inferring issue
status from this page.
