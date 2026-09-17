# Architecture Overview

Keriol Home separates provider-neutral Butler contracts, reusable runtimes/plugins and the private household deployment.

## Butler Core

Butler Core is the lowest reusable layer.

The current released `0.2.0` baseline owns provider-neutral contracts and small execution primitives shared by Butler runtimes and reusable plugins, including:

- tool definitions, permissions and registration;
- planner interfaces;
- deterministic request-resolution contracts;
- policy-governed execution;
- asynchronous job request/result boundaries;
- structured trace context and events;
- domain, capability and contribution declarations;
- provider-neutral output contracts.

Core deliberately does not own plugin discovery/loading/lifecycle, application routing, concrete domain behavior, Home Assistant or Alexa integrations, AI-provider configuration, frontend rendering, trace storage/viewers, delivery providers or Keriol-specific deployment behavior.

## Butler Runtimes

### Wilfred

Wilfred is the public reusable Butler runtime built on Butler Core.

Wilfred `0.2.2` is the current released Public Alpha. Its responsibilities include registered tool execution, deterministic-first resolution, planning interfaces and fallback, confirmation boundaries, workflows, verified execution, output contracts, standalone APIs and plugin loading.

Wilfred `main` is on the `0.2.3.dev0` development line.

### Alfred

Alfred is the private Keriol Home Butler runtime and proving ground built on Core-owned contracts.

Alfred owns household-specific composition, context, routing, policy, domains, integrations and AI fallback.

Alfred and Wilfred are sibling runtimes. Alfred does not depend on or execute through the Wilfred runtime.

Reusable behavior is promoted toward Butler Core, Wilfred or an independent public plugin only after ownership is stable, private assumptions have been removed, tests exist and public-safe extraction is justified.

## Independent Platform Plugins

Reusable platform integrations may depend directly on the lowest appropriate Core contracts instead of a concrete Butler runtime.

Home Assistant Plugin (HAP) is the first explicit example. It lives at `keriol/home-assistant-plugin`, is currently on the `0.2.0.dev0` development line and is intended to be consumable independently by Butler runtimes.

The reusable boundary is:

    Butler Runtime
      -> HAP
      -> Home Assistant API
      -> Home Assistant
      -> Device / Integration

Wilfred and Alfred may therefore consume HAP without becoming runtime dependencies of one another.

## Home Assistant

Home Assistant owns physical orchestration, dashboards, integrations, device wrappers and device state.

The Butler runtimes reason, route and invoke explicit operations. They do not replace Home Assistant as the smart-home platform.

## Runtime Flows

A standalone Wilfred request follows:

    Client
      -> Wilfred
      -> Registered Capability / Plugin
      -> External Service

A private Keriol request follows:

    Voice / Web / App / other frontend
      -> Alfred
      -> Registered Capability / Plugin
      -> Domain / Integration

When the target is Home Assistant, either runtime may use:

    Butler Runtime
      -> HAP
      -> Home Assistant

The response returns through the active runtime's frontend or delivery provider. Frontend-specific speech, SSML and presentation remain frontend concerns.

## Core Composition Boundary

Core makes reusable structure explicit without becoming an application framework.

A host runtime may compose Core contracts in roughly this order:

1. domain packages declare domains, capabilities, deterministic resolvers and tools;
2. the runtime discovers or loads those contributions;
3. deterministic resolvers attempt the request first;
4. a runtime-owned fallback may handle unresolved goals;
5. execution validates arguments and applies permission/confirmation policy;
6. asynchronous continuation may be represented through job contracts;
7. output is handed to a concrete provider outside Core;
8. trace context may correlate those boundaries without requiring a Core-owned logger or viewer.

Discovery, loading, lifecycle and runtime verification remain runtime responsibilities.

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

## Development Sources of Truth

Development state is intentionally kept outside the portfolio documentation layer:

- GitHub Issues own tasks, planning, priorities, dependencies and active status;
- Git `main` owns merged implementation and versioned documentation;
- commits, tags, releases and workflows provide implementation/release evidence;
- live systems own deployed runtime truth;
- project models and this portfolio are derived architectural summaries.

The retired Umberto ledger is archival only and cannot override GitHub, Git or runtime evidence.

## Design Rules

- One owner layer/domain per feature.
- Home Assistant owns physical orchestration.
- Butler Core stays provider-neutral and service-agnostic.
- Core contribution contracts do not make Core the plugin runtime.
- Wilfred and Alfred are sibling runtimes; neither is the architectural runtime base of the other.
- Reusable platform integrations should depend on Core-owned contracts when they can be consumer-neutral.
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
- [ADR-012 - Sibling Butler Runtimes and Independent Platform Plugins](../adr/ADR-012-sibling-runtimes-and-independent-platform-plugins.md)
- [ADR-011 - GitHub as Development Source of Truth](../adr/ADR-011-github-development-source-of-truth.md)
