# Butler Client API

The Butler client API is the public-safe boundary through which external
clients enter the Butler communication network.

Today that boundary is **Bifröst**.

Bifröst is intentionally documented separately from Butler runtimes and
cross-Butler routing because it is the client-facing contract surface of the
ecosystem rather than a concrete Butler.

## Canonical request path

```text
External client
      |
    Bifröst
      |
    Midgard
      |
 Butler Core
   /      \
plugin   Butler-owned Asgard
```

Bifröst owns transport and protocol concerns. It does not own domain semantics,
Butler selection policy or concrete runtime behavior.

## Current released baseline

IGNITION-001 proves Bifröst `0.1.0` with Butler Interphone `0.1.0`,
Midgard `0.1.0`, Butler Core `0.3.0`, HAP `0.3.0` and private
Alfred `0.5.0`.

See:

- [Bifröst API](bifrost.md)
- [Midgard architecture](../architecture/midgard.md)
- [Asgard architecture](../architecture/asgard.md)
- [IGNITION-001](../milestones/ignition-001.md)
