# Architecture Overview

Keriol Home separates the reusable Butler runtime from the private household deployment.

## Layers

### Butler Core

Butler Core is the lowest reusable layer.

It owns provider-neutral contracts and execution primitives shared by Butler runtimes and consumers.

It does not own smart-home orchestration, frontend behavior or Keriol-specific integrations.

### Wilfred

Wilfred is the public reusable Butler runtime built on Butler Core.

Its responsibilities include:

- registered capability discovery
- deterministic execution
- planning interfaces
- confirmation boundaries
- workflows
- verified execution
- output contracts
- standalone APIs
- plugin loading

Wilfred can run independently of Alfred.

### Alfred

Alfred is the private Keriol Home deployment.

Wilfred provides its reusable Butler runtime base. Alfred adds household-specific policy, integrations, domains and experimental capabilities.

Some legacy Alfred implementation paths predate Wilfred and are progressively converging onto the shared runtime.

### Home Assistant

Home Assistant owns physical orchestration, dashboards, integrations, device wrappers and device state.

The Butler runtime asks Home Assistant to perform explicit operations. It does not replace Home Assistant.

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
      -> Home Assistant REST API
      -> Home Assistant
      -> Device / Integration

## Keriol Home Flow

The private deployment adds Alfred above the reusable runtime:

    Voice / Web / App / other frontend
      -> Alfred
      -> Wilfred runtime
      -> Registered capability
      -> Domain / Integration

The response returns through the active frontend.

Frontend-specific speech and presentation formatting remain frontend concerns.

## Verified Physical Actions

Physical actions should not treat successful dispatch as successful execution.

Where state can be observed, the preferred lifecycle is:

    READ
      -> ACTION
      -> READ
      -> VERIFY

A workflow may therefore finish as verified, failed or indeterminate depending on observed state.

## Capability Maturity

Capabilities documented from Alfred should be labelled:

- **Public**
- **Private validated**
- **Candidate**

Private validated functionality may be ahead of the public Wilfred distribution.

Candidate functionality may later be generalized, but documentation must not present that as a guaranteed release.

## Private Domain Components

Inside the private Keriol deployment:

- Alfred owns Keriol-specific interaction and orchestration.
- Osvaldo owns proactive communication policy.
- Charon owns media-domain intelligence.
- Umberto owns development ledger and checkout coordination.

These private components do not redefine Butler Core or Wilfred responsibilities.

## Design Rules

- One owner layer per feature.
- Home Assistant owns physical orchestration.
- Butler Core stays provider-neutral.
- Wilfred stays reusable and service-agnostic.
- Alfred may contain Keriol-specific capabilities.
- Frontends stay replaceable.
- READ before ACTION when useful state is available.
- Physical ACTION requires verification when practical.
- Confirmation boundaries survive plugin and frontend changes.
- Private experiments are not automatically public roadmap commitments.

## Related Documentation

- [Alfred Ecosystem](alfred-ecosystem.md)
- [Architecture Diagram](../diagrams/architecture.md)
- [Alfred Ecosystem Flow](../diagrams/alfred-ecosystem-flow.md)
- [ADR-008 - Butler Core, Wilfred and Alfred Layering](../adr/ADR-008-butler-core-wilfred-alfred-layering.md)
