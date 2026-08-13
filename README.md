# Home Automation Portfolio

Public-safe documentation for a local-first smart-home and IoT platform built around Home Assistant, MQTT, Node-RED, Python services and a Butler architecture developed through real household use.

The project has two complementary faces:

- **Keriol Home / Alfred** is the private real-world deployment and proving ground.
- **Wilfred** is the reusable public Butler runtime extracted from that experience.
- **Butler Core** provides the shared provider-neutral contracts and execution foundations underneath them.

## Goals

- Local-first smart-home orchestration
- Safe tool-based automation
- Explicit READ, ACTION and verification boundaries
- Replaceable voice, web and application frontends
- Policy-driven proactive communication
- Secure private administration and narrow public integrations
- MQTT-based telemetry and event distribution
- Energy, media, appliance and presence automation
- Public-safe engineering documentation
- Reusable open-source Butler components

## Butler Architecture

The current architecture separates reusable runtime concerns from the private Keriol Home deployment.

### Butler Core

[Butler Core](https://github.com/keriol/butler-core) contains provider-neutral contracts and execution primitives.

It does not know about Keriol Home, Alexa, Home Assistant devices or private household integrations.

### Wilfred

[Wilfred](https://github.com/keriol/butler-wilfred) is the public reusable Butler runtime built on Butler Core.

It provides general runtime facilities for registered tools, deterministic execution, planning, workflows, confirmation boundaries, verified execution and output contracts.

Wilfred is being developed toward the `0.2.0` Public Alpha.

The official [Home Assistant plugin](https://github.com/keriol/wilfred-home-assistant) connects Wilfred to Home Assistant through explicit READ and ACTION capabilities without moving physical orchestration out of Home Assistant.

### Alfred

**Alfred** is the private Keriol Home Butler deployment.

Wilfred provides Alfred's reusable runtime base, while Butler Core provides the shared contracts and execution semantics underneath them both.

Alfred adds Keriol-specific integrations, policies, domain behavior and experimental capabilities on top of the reusable public layers.

Some older Alfred paths predate Wilfred and are progressively converging onto the public runtime architecture.

## Capability Maturity

Portfolio capabilities use three maturity levels:

- **Public**: implemented in Butler Core, Wilfred or an official public plugin.
- **Private validated**: implemented and tested in the real Alfred deployment but not currently part of the public Wilfred distribution.
- **Candidate**: a private capability that may later be generalized and extracted into Wilfred or an official plugin.

Candidate status is not a release commitment.

This lets the portfolio document real engineering work without pretending that every private experiment is already a public Wilfred feature.

## Smart-Home Ownership

Home Assistant remains responsible for physical orchestration, dashboards, device wrappers and integration state.

Wilfred and Alfred coordinate capabilities through explicit tools and workflows rather than replacing the smart-home platform.

A typical public Wilfred flow is:

    Client -> Wilfred -> Registered Tool / Plugin -> Service

A Keriol Home flow is:

    Frontend -> Alfred -> Wilfred Runtime -> Registered Capability -> Service

For observable Home Assistant actions, verified workflows follow:

    READ -> ACTION -> READ / VERIFY

Dispatch alone is not considered physical success.

## Core Stack

- Home Assistant
- Butler Core
- Wilfred
- wilfred-home-assistant
- Python / FastAPI
- Mosquitto MQTT
- Node-RED
- Docker
- HACS integrations
- Plex
- NAS storage
- Tailscale
- Cloudflare Tunnel

## Private Keriol Components

Selected sanitized architecture from the private deployment can be documented publicly.

- **Alfred** owns Keriol-specific interaction and orchestration.
- **Osvaldo** owns proactive communication policy such as allow, defer, aggregate and deny decisions.
- **Charon** owns media-domain intelligence and curation.
- **Umberto** tracks development tasks, evidence and checkout work.

Frontend-specific presentation remains a frontend concern rather than an independent architectural component.


## For Builders, Founders and Early Adopters

The public Wilfred ecosystem is deliberately smaller than the workshop behind it.

Keriol Home and Alfred the Butler continuously exercise new domains, workflows and plugin candidates against a real operating smart home.

Some experiments are intentionally household-specific. Others may graduate into Wilfred or an official plugin once they have been generalized, tested, sanitized and documented.

That means the public repositories show the reusable capabilities that have already earned their way out of the private proving ground, while this portfolio also shows where new ideas are being tested.

Public extraction is a maturity decision, not an automatic dump of private functionality.

## Main Case Studies

- Butler runtime evolution from Alfred to Wilfred
- Alfred registered-capability architecture
- Verified appliance control
- Proactive notification policy
- Media and Plex curation
- Bravia + Dolby safe-power automation
- Plex voice control
- Local photovoltaic telemetry through MQTT
- BLE presence detection
- Cloudflare Tunnel and Tailscale access strategy

## Featured Case Study - Alfred Laundry Workflow

The laundry workflow is one of the project's strongest examples of designing around real device behavior rather than optimistic command dispatch.

The private Alfred deployment can interact with the washing machine through voice, Python services, Home Assistant and the appliance integration.

Validated capabilities include:

- washing-machine status queries
- remaining-time queries
- validated program catalog
- translated program names and aliases
- keyword search and pagination
- allowlisted remote start
- remote stop
- cautious command language
- asynchronous state verification
- integration refresh before verification
- proactive follow-up after verified state changes

The important design rule is simple:

**sending a command is not proof that the physical device changed state.**

That lesson later became part of the reusable verified-workflow model used by Wilfred.

Relevant documentation:

- [Alexa Custom Skill Laundry MVP](docs/case-studies/alexa-custom-skill-laundry-mvp.md)
- [Alfred Laundry Portfolio Analysis](docs/analysis/alfred-laundry-voice-ux-and-async-verification.md)
- [Alfred Laundry Lessons Learned](docs/lessons-learned/alfred-laundry-voice-ux-and-async-verification.md)
- [Alexa Laundry Async Verification](docs/diagrams/alexa-laundry-async-verification.md)

## Alfred Proving Ground

The public Butler repositories show capabilities that have already crossed the reusable-public boundary.

Alfred runs ahead of that boundary as the private real-world proving ground. Several domains and interaction patterns are already **Private validated** or **Candidate** even when they are not yet shipped by Wilfred.

See [Alfred Proving Ground](docs/architecture/alfred-proving-ground.md) for the current maturity map and public-extraction path.

## Public Portfolio Boundary

This repository documents how Keriol Home and Alfred evolve. It is not a sanitized mirror of the private implementation.

Readable private-derived Python, Home Assistant YAML, service definitions, interaction models and configuration snapshots are intentionally outside the portfolio boundary even when identifiers could be anonymized.

Reusable code that becomes genuinely public belongs in Butler Core, Wilfred or the relevant official plugin repository.

The portfolio therefore focuses on architecture, ADRs, diagrams, case studies, capability maturity and engineering lessons.

See [ADR-010 - Public Portfolio Documentation Boundary](docs/adr/ADR-010-public-portfolio-documentation-boundary.md).

## Development State

The project no longer uses a manually synchronized project model as the single source of development truth.

- **Git** owns versioned implementation and documentation.
- **Umberto** owns active tasks, milestones, priorities and development evidence.
- **Live systems** own operational truth.
- **Project models** are compact derived architectural snapshots.

This separation prevents the documentation layer from becoming a second task database.

See [ADR-009 - Development State Sources of Truth](docs/adr/ADR-009-development-state-sources-of-truth.md).

## Development Approach

The project uses an AI-assisted engineering workflow.

Architecture decisions, implementation, testing and production ownership remain human-driven. AI is used for research, troubleshooting, design review, documentation, task planning and long-term knowledge preservation.

- [AI Collaboration](docs/AI_COLLABORATION.md)
- [AI-Assisted Development Flow](docs/diagrams/ai-assisted-development-flow.md)
- [ADR-005 - AI-Assisted Development Workflow](docs/adr/ADR-005-ai-assisted-development.md)

## Architecture Documentation

- [Architecture Overview](docs/architecture/overview.md)
- [Alfred Ecosystem](docs/architecture/alfred-ecosystem.md)
- [Current Architecture Diagram](docs/diagrams/architecture.md)
- [Alfred Ecosystem Flow](docs/diagrams/alfred-ecosystem-flow.md)
- [ADR-008 - Butler Core, Wilfred and Alfred Layering](docs/adr/ADR-008-butler-core-wilfred-alfred-layering.md)
- [Current Public Project Model](docs/project-model/project-model-public.md)

Historical worklogs, milestone snapshots and previous ADRs are intentionally retained as records of the architecture that existed at the time.

## Public Safety

This repository is intended to contain only sanitized architecture, documentation and examples.

Secrets, credentials, private endpoints, personal data and unnecessary operational details are excluded.

Legacy examples are periodically re-audited as the public/private boundary evolves.
