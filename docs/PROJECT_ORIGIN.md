# Project Origin

## Why This Project Exists

Keriol Home did not begin as a framework project.

It began as a real household automation system built around Home Assistant and gradually accumulated voice control, media workflows, energy telemetry, presence experiments, appliance integrations and custom Python services.

The Butler architecture emerged from the problems encountered while operating that system.

## Evolution

### Phase 1 - Home automation

Home Assistant became the owner of physical orchestration, device integrations, dashboards and automation wrappers.

MQTT and Node-RED were added where event distribution or visual multi-event flows made them useful.

### Phase 2 - Voice and service integration

Voice assistants became frontends rather than automation brains.

Python and FastAPI services handled validation, external APIs and workflows that did not belong inside Home Assistant YAML.

### Phase 3 - Alfred

As the number of domains increased, Keriol Home needed one coherent interaction and orchestration layer.

Alfred emerged as the private Butler of the house.

The early Alfred architecture introduced registered tools, deterministic routing, permissions, confirmations and AI fallback while keeping domain ownership outside the agent itself.

### Phase 4 - Real-world safety

Physical integrations exposed an important difference between software acknowledgement and reality.

A service call returning successfully did not mean that a television, washing machine or other physical device had reached the requested state.

This led to explicit verification patterns:

    READ -> ACTION -> READ -> VERIFY

The private deployment became a useful proving ground for execution semantics that were more general than Keriol Home itself.

### Phase 5 - Butler Core

Reusable contracts and execution primitives were extracted from Alfred into Butler Core.

Butler Core intentionally stays provider-neutral and knows nothing about the specific house, voice frontend or device inventory.

### Phase 6 - Wilfred

Wilfred was created as the reusable public Butler runtime built on Butler Core.

Instead of publishing the private Keriol deployment, the reusable execution model was generalized into an independent runtime with tools, workflows, planning, confirmation boundaries, output contracts, APIs and plugins.

The Home Assistant integration was likewise separated into an official public plugin.

### Phase 7 - Sibling runtimes and independent plugins

Today the relationship is:

    Butler Core
      |-- Wilfred
      |-- Alfred
      `-- reusable plugins such as Home Assistant Plugin

Butler Core provides the shared provider-neutral foundations.

Wilfred provides the reusable public Butler runtime.

Alfred remains the private Keriol Home sibling runtime and real-world proving ground.

Reusable integrations such as Home Assistant Plugin are independent consumers of Core-owned contracts and may be composed by either runtime without making Wilfred and Alfred dependencies of one another.

The earlier `Core -> Wilfred -> Alfred` layering was an important extraction stage and is preserved in historical documentation and superseded ADRs, but it no longer defines the current runtime dependency model.

### Phase 8 - GitHub as development authority

As the public ecosystem grew, a separate local development ledger and compact
project model stopped scaling as authoritative development tools.

GitHub Issues became the source of truth for work state, Git `main` for merged
implementation/documentation, releases/tags/workflows for release evidence and
live systems for runtime truth.

The old Umberto ledger and dated project-model snapshots were retained as
history rather than allowed to compete with GitHub.

### Phase 9 - Ignition communication network

IGNITION-001 introduced the first released external-client network spanning:

```text
Interphone -> Bifröst -> Midgard -> Butler Core -> HAP -> Home Assistant
```

and the concrete-Butler path:

```text
Interphone -> Bifröst -> Midgard -> Butler-owned Asgard -> Alfred
```

This phase established Bifröst as the client/API boundary, Midgard as the
provider-neutral communication and cross-Butler routing layer, and Asgard as the
Butler-owned ingress/identity boundary.

The real Android proving cycle also reinforced request correlation, canonical
Butler identity, observable action verification and the separation between
client acknowledgement and physical completion.

### Phase 10 - Documentation becomes the project model

The final compact local project model was retired after the repository
documentation had grown into a versioned, navigable and agent-friendly knowledge
system.

The active project model is now the documentation corpus itself:

- architecture/API pages explain durable ownership and contracts;
- ADRs preserve decisions;
- milestones record proven compatibility checkpoints;
- historical records preserve superseded stages without rewriting them;
- AGENTS.md and agent guides explain how automated contributors should navigate
  the same canonical documentation;
- MkDocs/GitHub Pages provides presentation, not a second source of truth.

A compact public project-context file remains only as a compatibility/reference
summary. It is no longer the conceptual center of the project.

## Private Proving Ground, Public Runtime

Alfred may contain capabilities that are more advanced than the current public Wilfred release.

That does not make them public features automatically.

Current portfolio maturity uses:

- **Available**: public, documented and usable in the relevant public component;
- **In testing**: implemented or exercised privately, but not a public release promise;
- **Designed to enable**: architecturally supported direction without an implementation claim.

Private validation provides engineering evidence.

Public extraction requires deliberate generalization, tests, documentation, sanitization and clean installation/runtime evidence.

## Home Assistant Remains the Home

The Butler is not the smart-home software.

Home Assistant continues to own physical orchestration and device integration.

The Butler knows how to talk to the services of the house without replacing those services.

## Public Repository Scope

This repository documents:

- the architecture and evolution of Keriol Home;
- sanitized real-world case studies;
- the relationship between Alfred, Wilfred, Butler Core and reusable public plugins;
- reusable engineering lessons;
- public-safe diagrams and conceptual flows.

It does not publish the private Alfred implementation, secrets, credentials, private operational data, machine-specific private paths, unnecessary household identifiers or private media-acquisition implementation.

Historical worklogs and snapshots are retained because they show how the architecture evolved rather than pretending the current design existed from the beginning.
