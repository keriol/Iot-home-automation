# Alfred Proving Ground

## Purpose

Alfred the Butler is the private real-world deployment where Keriol Home exercises Butler behavior before deciding whether a capability is reusable enough to become public.

The public Butler repositories deliberately expose a smaller surface than the private proving ground.

That difference is intentional.

The portfolio documents what is being learned and validated without publishing the readable private implementation.

## Maturity Model

### Public

The capability exists in Butler Core, Wilfred or an official public plugin.

Public means that the reusable contract, implementation, tests and documentation have crossed the public boundary.

### Private validated

The capability has been implemented and exercised in Keriol Home.

It has real-world engineering evidence, but may still contain household assumptions, private integrations or deployment-specific behavior.

### Candidate

The capability contains ideas that may be generalized later.

Candidate status is evidence of direction, not a release promise.

## Current Proving-Ground Areas

| Area | Current maturity | Private validation | Possible public direction |
|---|---|---|---|
| Butler execution | Public + private validation | deterministic routing, permissions, confirmations and tool execution exercised in the real deployment | Butler Core / Wilfred |
| Voice interaction | Private validated | replaceable frontend, free-text routing, contextual confirmations and AI fallback | reusable Wilfred interaction contracts |
| AI latency handling | Private validated | immediate acknowledgement before slower provider-backed responses | reusable output / interaction behavior |
| Appliance workflows | Private validated | status reads, controlled actions and asynchronous physical-state verification | workflow or domain plugin patterns |
| Verified physical actions | Public foundation + private validation | READ -> ACTION -> READ -> VERIFY exercised against physical devices | reusable Wilfred verified workflows |
| Proactive communication | Private validated | allow, defer, aggregate, deny and quiet-hours policy | reusable policy contracts |
| Media intelligence | Private validated | discovery, playback decisions, quality policy and lifecycle concepts | reusable media-domain plugin candidates |
| Energy | Private validated / candidate | telemetry, production and consumption analysis | future domain tools or plugins |
| Climate | Private validated / candidate | environmental sensing and experimental control strategies | future climate-domain capabilities |
| Presence | Candidate | real-world presence experiments and confidence evaluation | future contextual capability |
| Service observability | Private validated | health and operational visibility across household services | reusable operational tools |
| Delivery abstraction | Private validated | frontend-independent delivery concepts exercised with the current voice environment | future reusable output integrations |

## Why Private Validation Matters

A home is a useful adversarial environment.

Networks fail.

Devices report stale state.

Cloud integrations have latency.

A successful API response may not correspond to a successful physical action.

People phrase the same request in unexpected ways.

Notifications that are technically correct can still be annoying.

Those conditions force the Butler architecture to deal with problems that are easy to hide in isolated demonstrations.

The private deployment therefore acts as an engineering filter before public extraction.

## Graduation Path

A private capability does not become public merely because it works in Alfred.

A typical graduation path is:

1. validate the behavior against a real use case;
2. identify which assumptions are specific to Keriol Home;
3. define a reusable contract;
4. decide the correct owner layer;
5. remove private operational dependencies;
6. add independent tests;
7. document permissions, confirmation and failure semantics;
8. verify clean installation and runtime behavior;
9. publish it in the appropriate public repository.

Possible destinations include Butler Core, Wilfred and official plugins.

Some capabilities will deliberately never graduate because their value is specific to the private deployment.

## What the Public Repositories Show

The public code repositories demonstrate what has already crossed the maturity boundary.

The portfolio complements them by showing:

- what problems the private deployment has encountered;
- what architectural patterns emerged from those problems;
- what has already been validated privately;
- what may be reusable in the future;
- why a candidate has not yet been made public.

This is intentionally different from publishing a redacted copy of Alfred source code.

## Engineering Principle

The private proving ground is allowed to move faster than the public runtime.

The public runtime is allowed to move more slowly because it must earn stronger guarantees around reuse, installation, contracts, tests and documentation.

That asymmetry is a feature of the development model.
