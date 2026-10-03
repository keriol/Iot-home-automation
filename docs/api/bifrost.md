---
title: Bifröst API
kind: api
owner: bifrost
scope: public
status: released
baseline: 0.1.0
depends_on:
  - midgard
related:
  - ../architecture/midgard.md
  - ../architecture/asgard.md
  - ../milestones/ignition-001.md
---

# Bifröst API

Bifröst is the external/client bridge of the Butler ecosystem.

Conceptually, it is the **Butler client API boundary**: external applications
talk to Bifröst, not directly to Alfred, Wilfred, Home Assistant or a
Butler-owned Asgard.

## Role

Bifröst owns:

- client-facing protocol versioning;
- request correlation at the external boundary;
- transport/session concerns;
- authenticated ingress projection;
- optional target-Butler metadata transport;
- safe speaker/client metadata transport;
- structured transport-level errors;
- propagation of canonical source-Butler identity returned from the network;
- client-safe manifest projection.

Bifröst does not own:

- domain behavior;
- Butler identity;
- Core-vs-Butler routing policy;
- cross-Butler selection;
- Asgard;
- Home Assistant semantics;
- notification significance;
- household policy.

## Canonical topology

Core-facing request:

```text
Interphone
   |
Bifröst
   |
Midgard
   |
Butler Core
   |
provider/plugin capability
```

Concrete Butler request:

```text
Interphone
   |
Bifröst
   |
Midgard
   |
Butler-owned Asgard
   |
concrete Butler
```

## Request and response identity

A request carries a stable request/correlation identifier.

When a concrete Butler is addressed, Bifröst preserves the requested target
metadata for Midgard. The responding Butler's Asgard supplies canonical
`source_butler_name`, which returns to the client through Midgard and Bifröst.

Bifröst must not fabricate or silently replace Butler identity.

## HTTP adapter boundary

The reusable Bifröst package owns a framework-neutral HTTP payload adapter.
The concrete host owns web-framework mounting, binding and authentication
policy.

This keeps Bifröst reusable without coupling the package to a specific web
framework or private deployment.

## Manifest surface

Bifröst exposes client-safe compatibility and topology metadata assembled from
the communication stack.

The manifest can include:

- protocol compatibility;
- Bifröst version;
- Butler Core version;
- visible Core plugins;
- visible Butler descriptors;
- Butler-owned Asgard compatibility metadata where projected by the runtime.

Private endpoints, credentials, filesystem paths and household identifiers are
not part of the public contract.

## IGNITION-001 evidence

Bifröst `0.1.0` was proven from the signed Android Interphone client in both
released Ignition paths:

```text
Interphone -> Bifröst -> Midgard -> Core -> HAP -> Home Assistant
Interphone -> Bifröst -> Midgard -> Asgard -> Alfred
```

The proving confirmed:

- request/reply transport from a real Android client;
- preserved non-empty request correlation;
- canonical `Source Butler: Alfred` on the Butler-facing path;
- client-visible responses after real Home Assistant state reads/actions;
- correct handling of long-running interactive work after the
  interaction-origin/deferred-work boundary was corrected.

## Not yet claimed

The released `0.1.0` baseline does not claim:

- automatic pairing/device enrollment;
- proactive Android notification delivery;
- structured continuation/confirmation UI;
- arbitrary remote discovery through public credentials.

Those remain post-Ignition work.

## Related documentation

- [Butler Client API](index.md)
- [Midgard](../architecture/midgard.md)
- [Asgard](../architecture/asgard.md)
- [Communication Model](../architecture/communication-model.md)
- [IGNITION-001](../milestones/ignition-001.md)


## GitHub lineage

Repository: https://github.com/keriol/Butler-Core-Bifrost-Plugin  
Issue tracker: https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues

Selected lineage:

- BIF-008, Ignition release: https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues/15
- BIF-010, Butler directory transport: https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues/18
- BIF-011, composed node manifest: https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues/20

Issue links provide implementation/history traceability. Current capability claims
still follow repository main and release evidence.
