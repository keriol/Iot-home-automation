# Home Automation Portfolio

Public-safe engineering documentation for **Keriol Home**, a local-first smart-home platform and real-world proving ground for the Butler ecosystem.

The project is intentionally split into reusable public layers and a private household deployment:

- **Butler Core** provides provider-neutral contracts and execution foundations.
- **Wilfred** is the reusable public Butler runtime built on Core.
- **Home Assistant Plugin (HAP)** is the public reusable Home Assistant integration, evolving toward a consumer-neutral Butler plugin built on Core contracts.
- **Keriol Home / Alfred** is the private sibling Butler runtime/deployment where new capabilities, policies and interaction patterns are exercised against real devices and services.

The portfolio documents architecture, capability maturity, case studies and engineering lessons without publishing the private implementation itself.

## Current Public Baseline

- **Butler Core `0.2.0`** is the current released Core baseline. It establishes the shared provider-neutral execution, asynchronous-job, tracing and domain-contribution contract layer.
- **Wilfred `0.2.2`** is the current Public Alpha and independently consumes Butler Core `0.2.0`.
- **Home Assistant Plugin** lives at [keriol/home-assistant-plugin](https://github.com/keriol/home-assistant-plugin) and remains on its `0.1.0.dev0` development line while its consumer-neutral Core boundary is being consolidated.
- **HAP** is the canonical task namespace for Home Assistant Plugin work. Historical WHA/WILF identifiers remain useful only as historical aliases.
- Core `0.2.0` being available does not imply that every future Core contract is already adopted by Wilfred, Alfred or HAP. Adoption is tracked and evidenced independently in the owning repository.

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
- Replaceable smart-home platform integrations through Butler plugins

## Butler Architecture

### Butler Core

[Butler Core](https://github.com/keriol/butler-core) owns provider-neutral contracts and small execution primitives shared by Butler runtimes and consumers.

The `0.2.0` baseline includes tool/registry contracts, planning boundaries, deterministic resolution, policy-governed execution, asynchronous job contracts, structured tracing, domain/capability contribution declarations and provider-neutral output contracts.

Core deliberately does not own application routing, plugin discovery/loading/lifecycle, concrete domains, AI-provider configuration, frontend rendering, delivery providers, trace storage or Keriol-specific integrations.

### Wilfred

[Wilfred](https://github.com/keriol/butler-wilfred) is the public reusable Butler runtime built on Butler Core.

Wilfred `0.2.2` is the current Public Alpha. Its released runtime includes registered tools, deterministic-first capability resolution, planning interfaces, workflows, confirmation boundaries, verified execution and public capability/domain contracts adopted from Core.

Wilfred is one consumer of the Butler plugin model, not the owner of every reusable integration.

### Home Assistant Plugin

[Home Assistant Plugin](https://github.com/keriol/home-assistant-plugin) is the public Home Assistant integration for the Butler ecosystem.

It was originally created as a concrete proving example around Wilfred so the plugin/capability model would be exercised against a real smart-home platform rather than only a toy integration.

The project is now evolving into a **consumer-neutral Butler plugin**. The target boundary is:

```text
                Butler Core
                    |
          Home Assistant Plugin
             /              \
         Wilfred            Alfred
```

Home Assistant remains responsible for devices, integrations, dashboards and physical orchestration. HAP owns reusable Home Assistant transport/configuration/state/action behavior. Wilfred and Alfred independently own their runtime composition, policy and semantic routing.

This also makes the ecosystem extensible beyond Home Assistant. Another home-automation manager can in future be integrated through another dedicated Butler plugin following the same provider-neutral contracts rather than by adding that platform directly to Core or hard-coding it into Wilfred/Alfred.

The consumer-neutral HAP migration is active development and is not retroactively claimed as part of released Wilfred or Alfred versions.

### Alfred

**Alfred** is the private Keriol Home Butler runtime/deployment and proving ground.

Alfred and Wilfred are **sibling consumers of Butler Core**. Alfred does not use Wilfred as its runtime base and must not import/install Wilfred as an architectural dependency.

Alfred adds Keriol-specific integrations, policies, domain behavior and experimental capabilities. Reusable behavior moves toward Butler Core, Wilfred or an independent public plugin only after generalization, testing, sanitization and a clear ownership boundary.

The planned HAP adoption follows exactly this model: Alfred may consume the same public Home Assistant Plugin as Wilfred without depending on Wilfred itself.

## Capability Maturity

Portfolio capabilities use three maturity levels:

- **Public**: released or merged in Butler Core, Wilfred or an official public plugin.
- **Private validated**: implemented and tested in the real Alfred deployment but not currently part of the public Wilfred/plugin distribution.
- **Candidate**: a capability or pattern being evaluated for later generalization.

Candidate status is not a release commitment.

This keeps the portfolio useful without pretending that every private experiment is already a public Wilfred feature.

## Smart-Home Ownership

Home Assistant owns physical orchestration, dashboards, device wrappers, integrations and device state.

Wilfred and Alfred reason, route and invoke capabilities rather than replacing the smart-home platform.

The reusable integration direction is:

    Butler Runtime -> Home Assistant Plugin -> Home Assistant

A current public Wilfred flow can be represented as:

    Client -> Wilfred -> Registered Capability / Plugin -> Service

A Keriol Home flow is:

    Frontend -> Alfred -> Registered Capability / Plugin -> Service

As HAP adoption matures, generic mapped Home Assistant access inside Alfred is intended to converge on:

    Semantic Owner -> Alfred Composition -> HAP -> Home Assistant

For observable physical actions, the preferred lifecycle is:

    READ -> ACTION -> READ -> VERIFY

Dispatch alone is not considered physical success.

## Core Stack

- Home Assistant
- Butler Core
- Wilfred
- Home Assistant Plugin (HAP)
- Alfred (private Keriol runtime)
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

- **Alfred** owns Keriol-specific composition, interaction, routing and orchestration.
- **Rosie** owns household appliance semantics, with Laundry as the first proving domain.
- **Osvaldo** owns proactive communication policy such as allow, defer, aggregate and deny decisions.
- **Charon** owns media-domain intelligence and lifecycle behavior.
- **Hermes** owns delivery framework/provider responsibilities; frontend/provider presentation stays outside Butler Core.

Private implementation details remain private even when their architectural lessons are documented here.

## For Builders, Founders and Early Adopters

The public Wilfred ecosystem is deliberately smaller than the workshop behind it.

Keriol Home continuously exercises new domains, workflows and plugin candidates against a real operating smart home. Some experiments stay household-specific. Others may graduate into Wilfred, Butler Core or an independent official plugin once they have earned a reusable contract, tests, sanitization and clean installation/runtime evidence.

Home Assistant Plugin is an important example of that maturation path: it began as a concrete integration created to prove the model, then earned a separate repository and is now being pushed toward a consumer-neutral boundary so it can become infrastructure used by the project's own runtimes.

The same path can support future plugins for other home-automation managers without changing the Butler architecture itself.

Public extraction is a maturity decision, not an automatic dump of private functionality.

## Main Case Studies

- Butler runtime evolution across Alfred, Core and Wilfred
- Capability-first and deterministic-first architecture
- Reusable Home Assistant plugin boundary
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

That lesson later informed the reusable verified-workflow model used by Butler Core/Wilfred and now guides HAP integration work as well.

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
