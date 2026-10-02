# Butler Communication Model

The Butler communication network separates client transport, cross-Butler
routing, provider-neutral execution foundations, reusable integrations and
concrete Butler runtimes.

## Ignition Phase 1

> One small step for a man, one giant step for a Butler.

The first coordinated network baseline is **IGNITION-001**:

```text
Android
  |
Butler Interphone
  |
Bifröst
  |
Midgard
  |
Butler Core
  |
Home Assistant Plugin
  |
Home Assistant
```

This is the public Core-facing path.

The private proving environment also validates the concrete-Butler branch:

```text
Android
  |
Butler Interphone
  |
Bifröst
  |
Midgard
  |
Butler-owned Asgard 0.1.0
  |
Alfred 0.5.0
```

Ignition is also the first coordinated Butler checkpoint that crosses the
internal runtime boundary in both directions: external client input can enter
through a replaceable communication chain and the resulting Butler response can
return through that same chain without a frontend-specific shortcut.

## Ownership

### Butler Interphone

Owns Android presentation, user interaction and client-side connection state.
It does not own Butler routing, Home Assistant semantics or concrete Butler
runtime behavior.

### Bifröst

Owns the external/client transport boundary and client-safe protocol
projection. It preserves request correlation and routing metadata but does not
resolve Butler targets or own household policy.

### Midgard

Owns provider-neutral communication and cross-Butler routing semantics. It may
serve a Core-facing request or route an explicit Butler target through a
Butler-owned Asgard boundary.

Midgard does not invent Butler identity, own user preference or implement
concrete Butler behavior.

### Butler Core

Owns provider-neutral contracts and execution foundations. Core remains
frontend-agnostic, provider-neutral and runtime-agnostic even when a specific
Core version is validated inside an Android-reaching compatibility baseline.

### Home Assistant Plugin

Owns reusable Home Assistant integration behavior, including authorized state
reads/actions, provider diagnostics and readiness semantics.

Home Assistant remains the source of truth for devices, integrations,
dashboards and physical orchestration.

### Asgard

Asgard is a Butler-side ingress boundary owned by a concrete Butler runtime.
It is not a Butler Core plugin and is not owned by Midgard.

In Ignition Phase 1 the concrete implementation is **Asgard 0.1.0**, shipped
inside Alfred 0.5.0. The compatibility version is externally visible through
the runtime manifest, but Asgard does not have an independent package,
repository, tag or artifact lifecycle in this release.

### Alfred and Wilfred

Alfred and Wilfred are sibling Butler runtimes built on Core-owned contracts.

Alfred 0.5.0 is the private proving runtime for IGNITION-001.

Wilfred is not part of IGNITION-001. It joins the communication network only
after a reusable Butler-side Asgard path is available and proven.

## Request identity

A client request carries a stable correlation identity across the communication
path.

When a concrete Butler is explicitly targeted, the request also carries target
Butler identity. A concrete Butler response returns canonical source Butler
identity from that Butler's Asgard boundary.

No layer may fabricate or silently substitute Butler identity.

IGNITION-001 was proven on a real Android client with both a non-empty request
correlation identifier and canonical `Source Butler: Alfred` visible on the
returned concrete-Butler response.

## Core-facing vs Butler-facing requests

A Core-facing request does not require a concrete Butler target. It can reach
shared Core capabilities such as the Home Assistant integration.

A Butler-facing request targets runtime-owned behavior and therefore crosses the
Butler-owned Asgard boundary.

These are complementary paths, not competing architectures.

## Action verification

A successful provider dispatch is not sufficient evidence of physical success.

Where observable state exists, the preferred lifecycle is:

```text
READ -> ACTION -> READ -> VERIFY
```

IGNITION-001 was proven from the Android client with an observable Home
Assistant target transitioning from an initial state through a governed action
to the expected post-action state.

## Interactive latency and deferred work

Frontend transport budgets and physical-operation verification budgets are not
the same thing.

A Butler operation may legitimately need longer than a client HTTP round trip
to prepare a device, execute an action and verify the observable result.
Interactive frontends therefore propagate interaction origin so a capable
runtime can acknowledge bounded work promptly and continue long-running
verification asynchronously.

This preserves a critical distinction:

```text
client acknowledgement != physical completion
```

The Ignition proving cycle caught and corrected this boundary on real media
playback: the client now receives a timely response while the Butler continues
the deferred, verified operation.

## External output direction

Ignition proves request/reply external I/O. It does **not** claim that proactive
Android delivery is already implemented.

The architecture is designed to enable a later governed output path such as:

```text
Alfred/domain
  -> Georges
  -> Osvaldo
  -> Hermes
  -> Bifröst
  -> Interphone
```

That projection remains **Designed to enable** beyond IGNITION-001. Georges
originates structured operational facts, Osvaldo owns communication policy,
Hermes owns delivery projection and Bifröst remains the client transport
boundary.

## Security boundary

Discovery metadata must not contain reusable credentials.

Authentication, pairing policy, credential issuance/storage/revocation and
deployment network policy remain explicit boundaries. Automatic Bifröst
pairing/device credentials are intentionally deferred beyond IGNITION-001.

Public documentation and artifacts must not contain private endpoints,
credentials, household entity identifiers, private runtime state or
Keriol-specific implementation details.

## Compatibility

Component versions may be described as **network-capable from version X**, but
that does not imply every later version is automatically compatible with every
other later version.

Exact proven combinations are recorded as immutable compatibility BOMs such as
IGNITION-001.
