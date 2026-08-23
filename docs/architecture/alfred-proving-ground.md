# Alfred Proving Ground

## Purpose

Alfred the Butler is the private real-world deployment where Keriol Home exercises Butler behavior before deciding whether a capability is reusable enough to become public.

The public Butler repositories deliberately expose a smaller surface than the private proving ground. That difference is intentional.

The portfolio documents what is being learned and validated without publishing the readable private implementation.

## Maturity Model

### Available

The capability is public, documented and usable in Butler Core, Wilfred or an official public plugin.

Availability requires implementation evidence in the owning public repository. Release-specific claims require release/tag evidence.

### In testing

The capability or pattern has been implemented and exercised privately, or is undergoing active validation, but is not yet a public release promise.

It may still contain household assumptions, private integrations or deployment-specific behavior.

### Designed to enable

The architecture deliberately supports a direction, but the portfolio must not present that direction as implemented functionality.

An open issue, branch or design note may support this label. It does not support an availability claim.

## Current Proving-Ground Areas

| Area | Current maturity | Private evidence | Public direction |
|---|---|---|---|
| Butler execution | Available + In testing | deterministic-first routing, permissions, confirmations and execution exercised in the real deployment | Butler Core / Wilfred |
| Capability/domain ownership | In testing | domain-owned deterministic behavior and capability-oriented routing exercised privately | first-class Wilfred capability/domain contracts |
| Voice interaction | In testing | replaceable Alexa frontend, free-text routing, contextual confirmations and AI fallback | reusable frontend/interaction contracts where appropriate |
| AI latency handling | In testing | immediate acknowledgement before slower provider-backed responses | reusable output / interaction behavior |
| Appliance workflows | In testing | status reads, controlled actions and asynchronous physical-state verification | workflow or domain plugin patterns |
| Verified physical actions | Available + In testing | READ -> ACTION -> READ -> VERIFY exercised against physical devices | reusable Wilfred/Core execution patterns |
| Proactive communication | In testing | Osvaldo allow, defer, aggregate, deny and quiet-hours policy | reusable policy contracts after generalization |
| Delivery abstraction | In testing | Hermes provider/plugin delivery boundaries exercised with current voice paths | designed to enable reusable delivery integrations without coupling Core to providers |
| Alexa delivery | In testing | provider-specific speech/SSML rendering and target routing in the private deployment | may mature toward a reusable Wilfred/Alexa integration only after private validation and sanitization |
| Media intelligence | In testing | Charon discovery, playback decisions, quality policy and lifecycle concepts | reusable media-domain plugin candidates |
| Energy | In testing | telemetry, production and consumption analysis | future domain tools or plugins |
| Climate | In testing | environmental sensing and experimental control strategies | future climate-domain capabilities |
| Presence | Designed to enable | real-world presence experiments and confidence evaluation | future contextual capability |
| Service observability | In testing | health and operational visibility across household services | reusable operational tools |

## Why Private Validation Matters

A home is a useful adversarial environment.

Networks fail. Devices report stale state. Cloud integrations have latency. A successful API response may not correspond to a successful physical action. People phrase the same request in unexpected ways. Notifications that are technically correct can still be annoying.

Those conditions force the Butler architecture to deal with problems that are easy to hide in isolated demonstrations.

The private deployment therefore acts as an engineering filter before public extraction.

## Graduation Path

A private capability does not become public merely because it works in Alfred.

A typical graduation path is:

1. validate the behavior against a real use case;
2. identify which assumptions are specific to Keriol Home;
3. define a reusable contract;
4. decide the correct owner layer or domain;
5. remove private operational dependencies;
6. add independent tests;
7. document permissions, confirmation and failure semantics;
8. sanitize public documentation and examples;
9. verify clean installation and runtime behavior;
10. publish it in the appropriate public repository.

Possible destinations include Butler Core, Wilfred and official plugins.

Some capabilities will deliberately never graduate because their value is specific to the private deployment.

## Voice and Delivery Boundary

Alexa is currently a private Keriol frontend and the first Hermes delivery target.

Provider-specific speech and SSML stay outside Butler Core. The configured Alexa voice used for Alfred speech notifications, currently Giorgio, is a frontend rendering parameter rather than an architectural component.

The existence of a working private Alexa path does not mean Wilfred currently ships an official Alexa integration. The architecture is designed to enable that direction if private validation, reusable contracts, tests and sanitization eventually justify extraction.

## What the Public Repositories Show

The public code repositories demonstrate what has already crossed the maturity boundary.

The portfolio complements them by showing:

- what problems the private deployment has encountered;
- what architectural patterns emerged from those problems;
- what has already been validated privately;
- what the architecture is designed to enable;
- why a private capability has not yet been made public.

This is intentionally different from publishing a redacted copy of Alfred source code.

## Engineering Principle

The private proving ground is allowed to move faster than the public runtime.

The public runtime is allowed to move more slowly because it must earn stronger guarantees around reuse, installation, ownership, contracts, tests and documentation.

That asymmetry is a feature of the development model.
