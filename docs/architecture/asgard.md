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
