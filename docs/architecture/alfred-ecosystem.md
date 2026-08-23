# Alfred Ecosystem

Alfred is the private Keriol Home Butler deployment and the real-world proving ground from which reusable Butler patterns can graduate into Wilfred, Butler Core or official public plugins.

## Runtime Relationship

The current layering is:

    Butler Core
        |
        v
      Wilfred
        |
        v
      Alfred

Butler Core provides provider-neutral contracts and execution foundations.

Wilfred provides the reusable public Butler runtime.

Alfred composes Keriol-specific context, policy, domains, integrations and experimental behavior on top of that reusable stack.

Older private paths that predate Wilfred are progressively converging onto this ownership model when doing so improves reuse and clarity.

## Capability Model

Wilfred and Alfred use a capability-first model:

- an **integration/provider** connects to an external service;
- a **tool** is a typed executable operation;
- a **capability** describes something the Butler knows how to do;
- a **domain** owns related knowledge and behavior;
- a **goal** is the outcome requested by the user.

Known requests should resolve deterministically before planner fallback. Policy, permissions, confirmation and verification still govern execution regardless of how a goal was resolved.

Conversation and frontend code should not become the owner of domain behavior.

## Alfred

Alfred owns private Keriol composition, context, routing and AI fallback.

Its responsibilities include:

- receiving normalized requests from supported frontends;
- composing the private runtime and loaded packages;
- routing Keriol-specific context and policy;
- invoking reusable Wilfred/Core execution facilities;
- exposing private domain capabilities;
- preserving permissions, confirmation and safety boundaries;
- providing AI fallback only when deterministic resolution does not already own the request.

Alfred is not the smart-home platform itself.

Home Assistant remains responsible for physical orchestration, integrations, dashboards and device state.

## Osvaldo

Osvaldo owns proactive communication policy.

It may:

- allow immediate delivery;
- defer delivery;
- aggregate compatible events;
- deny delivery;
- apply quiet-hours and related communication policy.

A requested asynchronous reply is a continuation of an explicit user interaction and should not be treated as a generic unsolicited notification merely because delivery happens later.

## Charon

Charon owns media-domain intelligence and lifecycle behavior.

It may handle discovery, identity, quality policy, playback decisions, observation and lifecycle analysis while exposing media capabilities through the Butler runtime.

Charon does not own generic conversation routing or provider delivery.

## Hermes

Hermes is the private delivery framework for provider-specific output paths.

It owns delivery providers, routing and transport-specific rendering where appropriate.

Hermes does not own domain semantics or proactive communication policy. Osvaldo decides whether communication may occur; Hermes handles how an approved or requested output reaches a provider.

Alexa is one current frontend/provider target. Speech and SSML are presentation details, not Butler architecture.

## Voice and Persona Parameters

Named voices or personas remain frontend presentation parameters rather than architectural components.

In the private deployment, **Giorgio** remains a configurable voice/persona parameter. Changing, disabling or replacing that voice does not change capability ownership, domain behavior, policy or execution semantics.

This distinction keeps presentation replaceable without pretending that a voice profile is a runtime owner.

## Interactive Flow

A private Keriol interaction follows:

    Frontend
      -> Alfred
      -> Wilfred runtime
      -> Registered capability
      -> Domain / Integration
      -> Alfred
      -> Frontend rendering / delivery

Frontend-specific speech, SSML, voice/persona selection and presentation remain frontend concerns.

## Proactive Flow

A proactive domain event follows:

    Domain Event
      -> Osvaldo policy
      -> Hermes delivery
      -> Provider / Frontend

The originating domain describes the event.

Osvaldo decides whether and when it may be communicated.

Hermes and its providers deliver the approved output without acquiring domain or policy ownership.

## Capability Status

Portfolio wording should distinguish:

- **Available**: public, documented and usable;
- **In testing**: exercised privately but not yet a public release promise;
- **Designed to enable**: architecturally supported direction without an implementation claim.

Private proving-ground evidence may justify **In testing**, but a branch or issue alone never justifies an availability claim.

## Component Boundaries

- Butler Core owns provider-neutral foundations.
- Wilfred owns the reusable Butler runtime and public semantic capability/domain contracts.
- Alfred owns private Keriol composition, context, routing and AI fallback.
- Home Assistant owns physical orchestration and device/integration state.
- Osvaldo owns proactive communication policy.
- Charon owns media-domain intelligence and lifecycle behavior.
- Hermes owns delivery framework/provider responsibilities.
- Frontends own provider-specific input and presentation.
- Voice/persona profiles such as Giorgio are presentation parameters, not owners.
- Domain services should not duplicate policy, execution or provider responsibilities.
