# 05 — Delivery, Frontend and Voice Boundary

## Question

Where should proactive communication, delivery providers, Alexa-specific rendering and configured voice selection live in the architecture?

## Problem

Earlier documentation sometimes compressed proactive communication into a generic path such as:

`Domain Event -> Osvaldo -> Shared Delivery -> Notification Frontend`

That hid an important ownership boundary.

Policy and delivery are separate concerns.

## Ownership established

### Osvaldo

Osvaldo decides communication policy:

- allow;
- defer;
- aggregate;
- deny;
- quiet-hours behavior;
- communication mode where policy affects presentation, such as normal vs whispered speech.

Osvaldo should not know Alexa-specific SSML, provider credentials, physical frontend targets or named voices.

### Hermes

Hermes owns delivery framework and provider routing.

Conceptually:

`Domain Event -> Osvaldo Policy -> Hermes -> Provider -> Frontend`

Hermes core remains provider-neutral. Provider-specific behavior stays in plugins/providers.

### Frontend/provider

The provider/frontend owns presentation details such as speech rendering and SSML.

Alexa is the current private voice frontend and first Hermes target exercised in Keriol Home. That fact demonstrates a private integration path; it does not mean Wilfred currently ships an official Alexa integration.

## Configured voice analysis

During the DOC-003 review, the configured Alexa voice required clarification.

The important distinction is:

- it is **not** an architectural component;
- it is **not** a domain owner;
- it is **not** communication policy;
- it is a provider/frontend speech-rendering parameter.

The current Alfred Alexa speech path uses a configured voice for speech notifications. The architecture must preserve that configuration through delivery composition without leaking it into provider-neutral Core contracts or Osvaldo policy.

## Runtime discrepancy discovered during review

A real speech notification was observed using a different/default voice instead of the configured one.

A rapid private-source triage checked the obvious architecture path and found that:

- the configured voice was still present in the voice catalog;
- the normal Alexa renderer still applied a named voice to speech;
- Hermes still registered the Alexa speech provider;
- immediate notification speech used the speech output kind;
- deferred/snoozed notification speech also reconstructed the speech output kind before delivery.

Therefore the discrepancy was **not** treated as evidence that the architecture model had changed.

The likely next step is runtime tracing of the concrete notification class/target or a fallback provider path. A speculative public-source patch would have been the wrong response.

## Why the fix was deferred

The user-facing documentation task was already in progress, and the quick triage showed that the bug was not a safe one-line correction.

The decision was therefore:

- record the private regression in the owning private repository;
- preserve the existing architectural model;
- defer implementation until the exact runtime path can be observed;
- continue the public documentation refresh.

## Public extraction direction

The private Alexa/Hermes work is valuable architectural evidence, but the portfolio should describe a future reusable Alexa path only as **Designed to enable** until reusable contracts, tests, sanitization and public implementation exist.

## Outcome

The refreshed diagrams and architecture docs make the boundary explicit:

`event -> policy -> delivery framework -> provider/frontend rendering`

This keeps policy, transport and presentation independently replaceable and prevents frontend details from contaminating Butler Core.
