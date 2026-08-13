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

### Phase 7 - Current architecture

Today the relationship is:

    Butler Core
        |
        v
      Wilfred
        |
        v
      Alfred

Butler Core provides the shared foundations.

Wilfred provides the reusable public runtime.

Alfred is the private real-world deployment that uses and extends that runtime for Keriol Home.

Some older Alfred paths predate Wilfred and are still being converged onto this model.

## Private Proving Ground, Public Runtime

Alfred may contain capabilities that are more advanced than the current public Wilfred release.

That does not make them public features automatically.

The portfolio therefore distinguishes:

- **Public**
- **Private validated**
- **Candidate**

Private validation provides engineering evidence.

Public extraction requires deliberate generalization, tests, documentation and a clean public boundary.

## Home Assistant Remains the Home

The Butler is not the smart-home software.

Home Assistant continues to own physical orchestration and device integration.

The Butler knows how to talk to the services of the house without replacing those services.

## Public Repository Scope

This repository documents:

- the architecture and evolution of Keriol Home;
- sanitized real-world case studies;
- the relationship between Alfred, Wilfred and Butler Core;
- reusable engineering lessons;
- public-safe diagrams and conceptual flows.

It does not publish the private Alfred implementation, secrets, credentials, private operational data or unnecessary household identifiers.

Historical worklogs and snapshots are retained because they show how the architecture evolved rather than pretending the current design existed from the beginning.
