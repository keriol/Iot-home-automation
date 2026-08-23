# 03 — Architecture Ownership and Maturity Analysis

## Question

How should the portfolio describe the Butler ecosystem after the recent architecture work without turning development direction into release claims?

## Ownership model confirmed

The current durable layering remains:

`Butler Core -> Wilfred -> Alfred`

with Home Assistant retaining ownership of physical smart-home orchestration.

### Butler Core

Owns provider-neutral contracts and execution foundations.

It must remain independent from:

- Home Assistant-specific device behavior;
- Alexa-specific rendering;
- Keriol-specific policy;
- private delivery providers;
- household domain assumptions.

### Wilfred

Owns the reusable public Butler runtime.

The current design direction is capability-first and deterministic-first:

- integrations/providers connect to external services;
- tools are typed executable operations;
- capabilities describe what the Butler knows how to do;
- domains own related knowledge and behavior;
- goals describe requested outcomes.

Known requests should resolve deterministically before open-goal planning or AI fallback.

This direction is actively being consolidated, but open capability/domain work is not described as already shipped merely because issues exist.

### Alfred

Owns private Keriol composition, orchestration context, routing and AI fallback.

It is the proving ground where reusable behavior can be exercised against real services and devices before public extraction.

Alfred does not replace Home Assistant and should not become the long-term owner of behavior that is clearly reusable and provider-neutral.

### Home Assistant

Owns:

- devices;
- integrations;
- dashboards;
- physical orchestration;
- observable smart-home state.

Butler layers reason, route and invoke explicit capabilities rather than becoming a second home-automation platform.

### Osvaldo

Owns proactive communication policy such as allow, defer, aggregate, deny and quiet-hours behavior.

It does not own provider-specific rendering or transport.

### Charon

Owns media intelligence and lifecycle behavior.

It does not own generic conversation routing, communication policy or delivery transport.

### Hermes

Owns the private delivery framework/provider boundary.

It allows approved or requested output to reach provider-specific delivery paths without coupling Butler Core to those providers.

Frontend-specific rendering belongs at the provider/frontend boundary.

## Maturity vocabulary analysis

The older portfolio vocabulary was:

- Public;
- Private validated;
- Candidate.

That wording mixed two different concepts:

1. where a capability lives;
2. how strongly its availability is supported by evidence.

The refresh therefore moved current-state documentation toward:

### Available

Public, documented and usable in the relevant public component.

### In testing

Implemented or exercised privately, or undergoing active validation, without constituting a public release promise.

### Designed to enable

Architecture intentionally supports the direction, but implementation availability is not claimed.

## Why this matters

A working private behavior can provide strong engineering evidence while still being unsuitable for public release because it may contain:

- household assumptions;
- private provider bindings;
- incomplete contracts;
- insufficient independent tests;
- sensitive operational context;
- unstable ownership boundaries.

Likewise, a public architecture can deliberately enable a future frontend or capability without that feature existing today.

## Graduation rule

Private proving-ground functionality should cross the public boundary only after:

1. real-world validation;
2. reusable ownership is identified;
3. private assumptions are removed;
4. provider-neutral contracts are defined where appropriate;
5. independent tests exist;
6. permissions, confirmation and failure semantics are explicit;
7. documentation is sanitized;
8. clean installation/runtime evidence exists.

## Outcome

The portfolio now describes **ownership separately from maturity**.

That makes it possible to say that an architecture is designed to enable a future capability without accidentally claiming that the capability is already available.
