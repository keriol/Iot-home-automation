# Home Automation Portfolio

Public-safe engineering documentation for **Keriol Home**, a local-first smart-home platform and real-world proving ground for the Butler ecosystem.

The project is intentionally split into reusable public layers and a private household deployment:

- **Butler Core** provides provider-neutral contracts and execution foundations.
- **Wilfred** is the reusable public Butler runtime built on Core.
- **Keriol Home / Alfred** is the private deployment where new capabilities, policies and interaction patterns are exercised against real devices and services.

The portfolio documents architecture, capability maturity, case studies and engineering lessons without publishing the private implementation itself.

## Current Public Baseline

- **Butler Core `0.1.4`** is the released Core baseline consumed by Wilfred `0.2.1`.
- **Wilfred `0.2.1`** is the current Public Alpha.
- **wilfred-home-assistant** is the official public Home Assistant plugin and remains on its `0.1.0.dev0` development line.
- Butler Core `main` has moved on to the `0.1.5.dev0` development line; development state is not presented as a released baseline.

Release claims in this portfolio come from explicit Git/tag/release evidence. Open branches and issues describe direction or testing state only.

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

### Butler Core

[Butler Core](https://github.com/keriol/butler-core) owns provider-neutral contracts and execution primitives shared by Butler runtimes and consumers.

It does not know about Keriol Home, Alexa, Home Assistant devices or private household integrations.

### Wilfred

[Wilfred](https://github.com/keriol/butler-wilfred) is the public reusable Butler runtime built on Butler Core.

Wilfred `0.2.1` is the current Public Alpha. Its released runtime includes registered tools, deterministic-first resolution, planning interfaces, workflows, confirmation boundaries, verified execution and output contracts.

The current public development direction is **capability-first**: capabilities and domains are being consolidated as explicit semantic ownership boundaries, with deterministic resolution remaining ahead of planner fallback. Open development work is documented as direction until merged or released.

The official [Home Assistant plugin](https://github.com/keriol/wilfred-home-assistant) connects Wilfred to Home Assistant without moving physical orchestration out of Home Assistant.

### Alfred

**Alfred** is the private Keriol Home Butler deployment and proving ground.

Wilfred provides Alfred's reusable runtime base, while Butler Core provides shared contracts and execution semantics underneath the reusable stack.

Alfred adds Keriol-specific integrations, policies, domain behavior and experimental capabilities. Reusable behavior moves toward Wilfred or Core only after generalization, testing, sanitization and a clear ownership boundary.

## Capability Maturity

Portfolio capabilities use three maturity levels:

- **Public**: released or merged in Butler Core, Wilfred or an official public plugin.
- **Private validated**: implemented and tested in the real Alfred deployment but not currently part of the public Wilfred distribution.
- **Candidate**: a capability or pattern being evaluated for later generalization.

Candidate status is not a release commitment.

This keeps the portfolio useful without pretending that every private experiment is already a public Wilfred feature.

## Smart-Home Ownership

Home Assistant owns physical orchestration, dashboards, device wrappers, integrations and device state.

Wilfred and Alfred reason, route and invoke capabilities rather than replacing the smart-home platform.

A typical public Wilfred flow is:

    Client -> Wilfred -> Registered Tool / Plugin -> Service

A Keriol Home flow is:

    Frontend -> Alfred -> Wilfred Runtime -> Registered Capability -> Service

For observable physical actions, the preferred lifecycle is:

    READ -> ACTION -> READ -> VERIFY

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

- **Alfred** owns Keriol-specific interaction, routing and orchestration.
- **Osvaldo** owns proactive communication policy such as allow, defer, aggregate and deny decisions.
- **Charon** owns media-domain intelligence and lifecycle behavior.
- **Hermes** owns delivery framework/provider responsibilities; frontend/provider presentation stays outside Butler Core.

Private implementation details remain private even when their architectural lessons are documented here.

## For Builders, Founders and Early Adopters

The public Wilfred ecosystem is deliberately smaller than the workshop behind it.

Keriol Home continuously exercises new domains, workflows and plugin candidates against a real operating smart home. Some experiments stay household-specific. Others may graduate into Wilfred or an official plugin once they have earned a reusable contract, tests, sanitization and clean installation/runtime evidence.

Public extraction is a maturity decision, not an automatic dump of private functionality.

## Main Case Studies

- Butler runtime evolution from Alfred to Wilfred
- Capability-first and deterministic-first architecture
- Verified appliance control
- Proactive communication policy
- Media and Plex curation
- Bravia + Dolby safe-power automation
- Plex voice control
- Local photovoltaic telemetry through MQTT
- BLE presence experiments
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

That lesson later informed the reusable verified-workflow model used by Wilfred.

Relevant documentation:

- [Alexa Custom Skill Laundry MVP](docs/case-studies/alexa-custom-skill-laundry-mvp.md)
- [Alfred Laundry Portfolio Analysis](docs/analysis/alfred-laundry-voice-ux-and-async-verification.md)
- [Alfred Laundry Lessons Learned](docs/lessons-learned/alfred-laundry-voice-ux-and-async-verification.md)
- [Alexa Laundry Async Verification](docs/diagrams/alexa-laundry-async-verification.md)

## Alfred Proving Ground

The public Butler repositories show capabilities that have already crossed the reusable-public boundary.

Alfred runs ahead of that boundary as the private real-world proving ground. Domains and interaction patterns may be **Private validated** or **Candidate** even when they are not shipped by Wilfred.

See [Alfred Proving Ground](docs/architecture/alfred-proving-ground.md) for the maturity map and public-extraction path.

## Public Portfolio Boundary

This repository documents how Keriol Home and Alfred evolve. It is not a sanitized mirror of the private implementation.

Readable private-derived Python, Home Assistant YAML, service definitions, provider models, private acquisition implementation and configuration snapshots stay outside the portfolio even when identifiers could be anonymized.

Reusable code that becomes genuinely public belongs in Butler Core, Wilfred or the relevant official plugin repository.

The portfolio therefore focuses on architecture, ADRs, diagrams, case studies, capability maturity and engineering lessons.

See [ADR-010 - Public Portfolio Documentation Boundary](docs/adr/ADR-010-public-portfolio-documentation-boundary.md).

## Development State

Development state is owned by the repositories where the work happens:

- **GitHub Issues** own tasks, priorities, dependencies, planning and active status.
- **Git / `main`** owns merged implementation and versioned documentation.
- **Commits, tags, releases and workflows** provide implementation and release evidence.
- **Live systems** own deployed runtime behavior and health.
- **Project models and this portfolio** are derived architectural documentation only.

The retired Umberto ledger is historical context and does not override GitHub, Git or runtime evidence.

See [ADR-011 - GitHub as Development Source of Truth](docs/adr/ADR-011-github-development-source-of-truth.md).

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

Historical worklogs, milestone snapshots and previous ADRs are intentionally retained as records of the architecture and decisions that existed at the time.

## Public Safety

This repository is intended to contain only sanitized architecture, documentation and examples.

Secrets, credentials, private endpoints, personal data, unnecessary operational identifiers and private acquisition implementation are excluded.

Legacy documentation is periodically re-audited as the public/private boundary evolves.
