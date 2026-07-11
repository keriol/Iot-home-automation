# Alfred Ecosystem

Keriol Home separates user interaction, orchestration, notification policy and domain expertise into components with explicit responsibilities.

The platform grows through registered tools and domain services rather than by increasing the complexity of the central agent.

## Alfred the Butler

Alfred is the user-facing agent and tool orchestrator.

Alfred receives requests from supported frontends, selects registered tools, validates parameters and presents the result.

Known requests follow deterministic routes. AI planning is used only when language, ambiguity or multi-tool workflows require it.

Alfred does not directly implement every smart-home feature. New capabilities are exposed through tools owned by their respective domains.

Purpose:

- provide one coherent interface to Keriol Home;
- route requests to the correct capability;
- enforce tool permissions and confirmation rules;
- keep domain logic outside the agent core.

## Giorgio

Giorgio is Alfred's speech renderer.

It converts Alfred responses and proactive messages into SSML for supported voice frontends. It can render normal or whispered speech according to the applicable policy.

Giorgio is not an independent agent. It does not select tools, make automation decisions or decide whether a notification should be delivered.

Purpose:

- give Alfred a consistent voice;
- keep speech formatting separate from reasoning;
- apply the selected speech mode without owning notification policy.

## Osvaldo

Osvaldo is the policy layer for proactive communication.

It evaluates whether an unsolicited notification should be delivered immediately, deferred, aggregated or denied.

Its decisions may consider:

- quiet hours;
- notification importance;
- aggregation rules;
- speech mode;
- future presence and house-mode context.

Direct responses to explicit user requests do not require Osvaldo's permission. Proactive events do.

Purpose:

- prevent automations from becoming noisy or intrusive;
- centralize proactive communication rules;
- keep delivery decisions consistent across domains;
- make proactive behavior explainable.

## Charon

Charon is the media curator for Plex and related services.

It provides media-domain knowledge such as library status, search, recent activity, catalog quality, missing-title analysis and future recommendations.

Charon exposes its capabilities to Alfred through registered tools.

Charon does not replace Alfred. Alfred owns the conversation and orchestration; Charon owns media intelligence.

Purpose:

- isolate media-specific logic from Alfred Core;
- support catalog curation and recommendation workflows;
- evolve Plex intelligence without increasing agent complexity.

## Interaction Models

### Interactive request

A user explicitly asks Alfred for information or an action.

Flow:

Frontend -> Alfred -> Tool Registry -> Domain Tool -> Alfred -> Giorgio

Interactive replies are not blocked by proactive notification policy.

### Proactive notification

A domain event may require unsolicited communication.

Flow:

Domain Event -> Queue or Dispatcher -> Osvaldo

Osvaldo may then:

- allow delivery through Giorgio and shared Home Assistant delivery;
- defer the event to the snoozable queue;
- deny delivery.

The originating domain describes the event. Osvaldo decides whether and when it may be communicated.

## Component Boundaries

- Home Assistant owns physical orchestration and device wrappers.
- Alfred owns request routing and tool execution.
- Giorgio owns speech rendering.
- Osvaldo owns proactive notification policy.
- Charon owns media-domain intelligence.
- Shared delivery owns the physical Home Assistant notification call.
- Domain services must not duplicate policy or delivery logic.

## Extension Rule

New capabilities should be added as registered tools or domain events.

Examples include presence, cameras, energy, climate, NAS health, calendar, weather and maker workflows.

The central rule remains:

> Alfred is not the software of the house. Alfred is the component that knows how to talk to every software service of the house.
