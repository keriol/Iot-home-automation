# Architecture Overview

Keriol Home separates reusable Butler runtime concerns from the private household deployment.

## Layers

### Butler Core

Butler Core is the lowest reusable layer.

It owns provider-neutral contracts and execution primitives shared by Butler runtimes and consumers.

It does not own smart-home orchestration, frontend behavior or Keriol-specific integrations.

### Wilfred

Wilfred is the public reusable Butler runtime built on Butler Core.

Its responsibilities include:

- registered tool execution;
- deterministic-first resolution;
- planning interfaces and fallback;
- confirmation boundaries;
- workflows;
- verified execution;
- output contracts;
- standalone APIs;
- plugin loading.

The current public consolidation direction is capability-first: capabilities represent what the Butler knows how to do, domains own related knowledge and behavior, and deterministic resolvers should move under the capability that owns them rather than remaining in global conversation logic.

This direction is tracked in GitHub and must not be described as released until the relevant implementation is merged or released.

Wilfred can run independently of Alfred.

### Alfred

Alfred is the private Keriol Home deployment and proving ground.

Wilfred provides its reusable Butler runtime base. Alfred adds household-specific policy, integrations, domains and experimental capabilities.

Reusable behavior is promoted toward Wilfred or Butler Core only after ownership is stable, private assumptions have been removed, tests exist and public-safe extraction is justified.

### Home Assistant

Home Assistant owns physical orchestration, dashboards, integrations, device wrappers and device state.

The Butler layers reason, route and invoke explicit operations. They do not replace Home Assistant as the smart-home platform.

## Public Runtime Flow

A standalone Wilfred request follows:

    Client
      -> Wilfred
      -> Registered Tool / Plugin
      -> External Service

For Home Assistant:

    Client
      -> Wilfred
      -> wilfred-home-assistant
      -> Home Assistant API
      -> Home Assistant
      -> Device / Integration

## Keriol Home Flow

The private deployment adds Alfred above the reusable runtime:

    Voice / Web / App / other frontend
      -> Alfred
      -> Wilfred runtime
      -> Registered capability / tool
      -> Domain / Integration

The response returns through the active frontend or delivery provider.

Frontend-specific speech, SSML and presentation remain frontend concerns.

## Deterministic First

Known requests should resolve deterministically before planner fallback when a suitable deterministic capability/resolver exists.

Open-ended goals may use a planner, but policy, permissions, confirmation and validation still govern execution.

Conversation code must not become the owner of domain knowledge simply because it performs request routing.

## Verified Physical Actions

Physical actions should not treat successful dispatch as successful execution.

Where state can be observed, the preferred lifecycle is:

    READ
      -> ACTION
      -> READ
      -> VERIFY

A workflow may finish as verified, failed or indeterminate depending on observed state.

## Capability Maturity

Capabilities documented from Alfred should be labelled according to evidence:

- **Public**: merged/released in a public Butler repository or official plugin;
- **Private validated**: exercised successfully in the real Alfred deployment;
- **Candidate**: being evaluated for later generalization;
- **In testing**: implementation exists but public maturity is not yet established;
- **Designed to enable**: architecture supports a future direction without claiming implementation.

Open branches and issues alone do not promote a capability to Public or Available.

## Private Domain Components

Inside the private Keriol deployment:

- Alfred owns Keriol-specific interaction, routing and orchestration;
- Osvaldo owns proactive communication policy;
- Charon owns media-domain intelligence and lifecycle behavior;
- Hermes owns delivery framework/provider responsibilities.

Alexa is a frontend/provider concern, not a Butler Core responsibility. Speech and SSML are presentation details.

These private components do not redefine Butler Core or Wilfred responsibilities.

## Development Sources of Truth

Development state is intentionally kept outside the portfolio documentation layer:

- GitHub Issues own tasks, planning, priorities, dependencies and active status;
- Git `main` owns merged implementation and versioned documentation;
- commits, tags, releases and workflows provide implementation/release evidence;
- live systems own deployed runtime truth;
- project models and this portfolio are derived architectural summaries.

The retired Umberto ledger is archival only and cannot override GitHub, Git or runtime evidence.

See [ADR-011 - GitHub as Development Source of Truth](../adr/ADR-011-github-development-source-of-truth.md).

## Design Rules

- One owner layer/domain per feature.
- Home Assistant owns physical orchestration.
- Butler Core stays provider-neutral and service-agnostic.
- Wilfred owns reusable Butler runtime behavior.
- Alfred may contain Keriol-specific capabilities and proving-ground experiments.
- Deterministic behavior precedes AI/planner fallback where practical.
- Frontends stay replaceable.
- READ before ACTION when useful state is available.
- Physical ACTION requires verification when practical.
- Confirmation and permission boundaries survive plugin and frontend changes.
- AI receives only the context necessary for the goal.
- Private experiments are not automatically public roadmap commitments.

## Related Documentation

- [Alfred Ecosystem](alfred-ecosystem.md)
- [Alfred Proving Ground](alfred-proving-ground.md)
- [Architecture Diagram](../diagrams/architecture.md)
- [Alfred Ecosystem Flow](../diagrams/alfred-ecosystem-flow.md)
- [ADR-008 - Butler Core, Wilfred and Alfred Layering](../adr/ADR-008-butler-core-wilfred-alfred-layering.md)
- [ADR-011 - GitHub as Development Source of Truth](../adr/ADR-011-github-development-source-of-truth.md)
