---
title: Alfred Proving Ground
kind: development
scope: public-safe
status: current
---

# Alfred Proving Ground

Alfred is the private real-world environment used to test Butler ideas before
deciding whether they deserve a reusable public form.

This page documents the **development model**, not the private implementation.

## Why a proving ground exists

A real home is useful precisely because it is inconvenient.

Devices report stale state. Networks fail. Cloud services pause. People phrase
requests unpredictably. A successful API call may not correspond to a successful
physical action.

Private proving exposes those failures before reusable contracts are promoted
into public components.

## What may be tested privately

Examples include:

- domain ownership patterns;
- verified actions;
- proactive communication policy;
- frontend/delivery behavior;
- appliance semantics;
- media-domain reasoning;
- local telemetry and context;
- interaction patterns;
- future capability/plugin candidates.

These examples should be read as **In testing** unless public release evidence
exists in an owning repository.

## What this page does not claim

It does not claim that Wilfred already ships Alfred behavior.

It does not document:

- private source code;
- private service topology;
- household identifiers;
- credentials or endpoints;
- private configuration;
- provider-specific operational settings;
- sensitive runtime state.

## Maturity model

### Available

Public, documented and usable in the relevant public repository.

### In testing

Implemented/exercised privately or under validation, but not a public release
promise.

### Designed to enable

Architecturally supported direction without an implementation claim.

## Graduation path

A private capability does not become public merely because it works.

A reusable candidate should pass through:

1. real-world validation;
2. ownership clarification;
3. removal of household assumptions;
4. reusable contract design;
5. independent tests;
6. privacy/sanitization review;
7. clean install/runtime proving;
8. public documentation;
9. explicit release in the correct repository.

Potential destinations include Butler Core, Wilfred or an independent public
plugin.

## The important asymmetry

The proving ground is allowed to move faster.

The public ecosystem moves more slowly because reuse, contracts, installation,
documentation and release guarantees have a higher bar.

That asymmetry is intentional.

## Asgard exception

Asgard is documented outside this development section because IGNITION-001
proved the Butler-owned boundary as part of the released communication model.

The Ignition implementation is still Alfred-owned and not a standalone public
package.

See [Asgard](asgard.md).

## Related pages

- [Development & Proving Ground](../ecosystem/development.md)
- [Released Public Ecosystem](../ecosystem/released.md)
- [Alfred Development Architecture](alfred-ecosystem.md)
