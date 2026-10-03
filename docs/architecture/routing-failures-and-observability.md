---
title: Routing Failures and Observability
kind: architecture
scope: public
status: current
owners:
  - midgard
  - butler-core
  - bifrost
  - interphone
---

# Routing Failures and Observability

The Butler communication network keeps routing failures, observability and
client presentation in separate ownership layers.

## Structured routing failures

Midgard owns routing decisions and therefore emits structured routing failures.

Examples include:

- requested Butler cannot be resolved;
- matching Butler boundary is unavailable;
- selected Butler fails to answer.

Midgard must not silently fall back to an unrelated Butler.

## Neutral client notification

A routing failure may carry a neutral descriptor such as:

```text
kind = butler_unavailable
presentation = system_neutral
documentation_url = optional
```

Ownership remains split:

- Midgard determines the routing failure semantics;
- Bifröst transports the neutral descriptor;
- Interphone or another client owns localized rendering/presentation.

The communication layer does not own user-facing copy or voice behavior.

## Routing observability

Midgard emits safe routing observability through Butler Core's Georges tracing
contracts.

Canonical event family:

```text
midgard.route.received
midgard.route.selected
midgard.route.completed
midgard.route.failed
```

The tracer contract is Core-owned. A concrete Butler/runtime may provide the
storage or operational sink.

Only safe routing metadata should be traced.

Do not record:

- message bodies;
- credentials;
- reusable tokens;
- private endpoints;
- provider payloads containing private data.

## Fail-safe tracing

Observability must not become a new failure mode.

A tracer/sink failure must not alter the routing result.

This preserves the distinction:

```text
routing correctness != observability availability
```

## Correlation

The request correlation identifier should remain available to safe routing
events so one request can be followed across Bifröst, Midgard and a concrete
Butler boundary without logging private payload content.


## GitHub lineage

- [MID-002 — discover Asgard identities and route by Butler name](https://github.com/keriol/butler-core-midgard-plugin/issues/3)
- [MID-003 — emit routing observability through Butler Core Georges tracing](https://github.com/keriol/butler-core-midgard-plugin/issues/5)
- [Midgard issue tracker](https://github.com/keriol/butler-core-midgard-plugin/issues)
- [Butler Core issue tracker](https://github.com/keriol/butler-core/issues)
