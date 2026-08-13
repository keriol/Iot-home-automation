# Alfred Ecosystem

Alfred is the private Keriol Home Butler deployment and the real-world proving ground from which much of the reusable Wilfred architecture has been extracted.

## Runtime Relationship

The current layering is:

    Butler Core
        |
        v
      Wilfred
        |
        v
      Alfred

Butler Core provides shared provider-neutral contracts and execution semantics.

Wilfred provides the reusable public Butler runtime.

Alfred builds Keriol-specific behavior on top of that runtime.

Some older Alfred paths existed before Wilfred and are still being migrated toward this layering.

## Alfred

Alfred owns the Keriol-specific interaction layer and orchestration context.

Its responsibilities include:

- receiving requests from supported frontends
- routing Keriol-specific interactions
- using reusable Wilfred execution facilities
- exposing private domain capabilities
- coordinating private policy and domain services
- preserving confirmation and safety boundaries

Alfred is not the smart-home platform itself.

Home Assistant remains responsible for physical orchestration and device wrappers.

## Osvaldo

Osvaldo is the private proactive communication policy layer.

It evaluates unsolicited events and may:

- allow immediate delivery
- defer delivery
- aggregate compatible events
- deny delivery
- select applicable communication policy

Interactive responses to explicit requests do not require proactive-policy approval.

## Charon

Charon owns media-domain intelligence.

It may handle discovery, catalog quality, playback decisions, lifecycle analysis and other media-specific concerns while exposing useful capabilities through the Butler tool surface.

Charon does not replace Alfred or Wilfred.

## Umberto

Umberto is the development ledger and checkout coordinator.

It tracks tasks, milestones, implementation evidence and repository-level development state.

It is a development-support concern rather than a runtime orchestration layer.

## Interactive Flow

A private Keriol interaction follows the reusable runtime path:

    Frontend
      -> Alfred
      -> Wilfred runtime
      -> Registered capability
      -> Domain / Integration
      -> Alfred
      -> Frontend

Presentation and speech rendering belong to the active frontend.

## Proactive Flow

A proactive domain event follows:

    Domain Event
      -> Queue / Dispatcher
      -> Osvaldo
      -> Shared Delivery
      -> Notification Frontend

The originating domain describes the event.

Osvaldo decides whether and when it may be communicated.

The delivery implementation does not own policy.

## Capability Status

Alfred may contain functionality that is not available in public Wilfred releases.

Documentation should distinguish:

- **Public** capabilities already available from Wilfred, Butler Core or an official plugin.
- **Private validated** capabilities running in Keriol Home.
- **Candidate** capabilities that may later be generalized for public release.

A private capability is evidence of real-world validation, not a promise that an identical public feature will ship.

## Component Boundaries

- Butler Core owns provider-neutral foundations.
- Wilfred owns the reusable Butler runtime.
- Alfred owns Keriol-specific orchestration and interaction.
- Home Assistant owns physical orchestration.
- Osvaldo owns proactive communication policy.
- Charon owns media-domain intelligence.
- Frontends own presentation-specific rendering.
- Domain services should not duplicate policy or execution boundaries.
