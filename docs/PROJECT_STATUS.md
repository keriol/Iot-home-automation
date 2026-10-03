# Home Automation Project Status

Last Updated: 2026-10-03

## Overview

Keriol Home is an operational local-first smart-home platform and the private proving ground behind the public Butler ecosystem.

The current architecture is centered on Butler Core contracts with sibling Butler runtimes and reusable plugins:

`Butler Core -> Wilfred / Alfred / reusable plugins`

Home Assistant remains the owner of physical orchestration, integrations, dashboards and device state.

## Current Baselines

| Component | Current status | Notes |
|---|---|---|
| Butler Core | Available | `0.3.0` released Ignition baseline; `main` on `0.3.1.dev0` |
| Wilfred | Available / Public Alpha | `0.2.2` current Public Alpha; not part of Ignition |
| Home Assistant Plugin (HAP) | Available | `0.3.0` released Ignition baseline; `main` on `0.3.1.dev0` |
| Bifröst | Available | `0.1.0` released Butler client/API bridge |
| Midgard | Available | `0.1.0` released communication/cross-Butler routing layer |
| Butler Interphone | Available | `0.1.0` released Android client |
| Alfred | Private operational | `0.5.0` current private released baseline; includes Asgard compatibility `0.1.0` |
| Home Assistant | Operational | physical orchestration owner |
| MQTT | Operational | event and telemetry transport |
| Node-RED | Operational | selected visual workflows |
| Cloudflare Tunnel | Operational | narrow public integration transport |
| Tailscale | Operational | private administration |

Release claims use explicit Git/tag/release evidence. Development branches and open issues are not treated as released capability evidence.

## Butler Runtime Model

### Shared Core

Butler Core `0.3.0` is the current released provider-neutral foundation for the Ignition baseline. Core `main` is on `0.3.1.dev0`. It owns provider-neutral tools/registry, planning, deterministic resolution, policy-governed execution, asynchronous jobs, tracing, domain/capability contribution declarations and output contracts.

Core remains deliberately smaller than a runtime: plugin discovery/loading/lifecycle, concrete domain behavior, frontend rendering, AI-provider configuration and deployment-specific integrations remain outside Core.

### Wilfred

Wilfred is the public reusable Butler runtime built on Core-owned contracts. Its released `0.2.2` baseline includes registered tool execution, deterministic-first resolution, planning interfaces, confirmation boundaries, workflows, verified execution, output contracts, standalone interfaces and adopted public capability/domain contribution contracts.

### Alfred

Alfred is the private Keriol Home sibling runtime and proving ground. It owns Keriol-specific context, routing, domains, integrations, policies and AI fallback.

Alfred does not use Wilfred as its architectural runtime base. Reusable behavior may graduate toward Butler Core, Wilfred or an independent public plugin after generalization, tests and sanitization.

### Home Assistant Plugin

HAP is the reusable public Home Assistant integration package built on Butler Core contracts rather than on Wilfred.

Wilfred and Alfred may consume HAP independently. HAP owns reusable Home Assistant transport/configuration/state/action behavior while Home Assistant remains the physical orchestration owner.

## Ignition communication baseline

The released Butler-to-Android path is:

```text
Interphone -> Bifröst -> Midgard -> Butler Core -> HAP -> Home Assistant
```

For concrete Butler-owned behavior:

```text
Interphone -> Bifröst -> Midgard -> Butler-owned Asgard -> Alfred
```

Bifröst is the client/API boundary. Midgard owns provider-neutral communication
and cross-Butler routing. Asgard is owned by the concrete Butler and provides
its governed ingress/identity boundary.

IGNITION-001 proved both paths from the real signed Android client, including
preserved request correlation, canonical `Source Butler: Alfred`, and
observable `READ -> ACTION -> READ -> VERIFY` for a Home Assistant action.

## Safety Model

Current design rules include:

- one owner layer or domain per feature;
- deterministic behavior before AI fallback for known requests;
- explicit confirmation for sensitive actions when appropriate;
- successful dispatch is not proof of physical success;
- observable actions use `READ -> ACTION -> READ -> VERIFY` where possible;
- frontend presentation stays outside Butler Core;
- AI receives only the context needed for the task.

## Voice and Interaction

Status: **In testing / private operational**

- Alexa is the current primary voice frontend for Alfred.
- Frontends remain replaceable.
- Speech and SSML remain frontend concerns.
- Alfred owns Keriol interaction context and routing.
- Slow AI-backed interactions can acknowledge before noticeable provider latency.
- Provider-specific voice choices remain frontend rendering parameters rather than architectural components.

The private Alexa path is evidence for future reusable patterns, not evidence that Wilfred currently ships an official Alexa integration.

## Proactive Communication

Status: **In testing**

Osvaldo owns communication policy for unsolicited output, including allow, defer, aggregate, deny and quiet-hours decisions.

Hermes owns the private delivery/provider boundary.

A requested asynchronous reply is treated as a continuation of an explicit interaction rather than generic unsolicited communication.

## Appliances

Status: **In testing**

The laundry workflow demonstrates status reads, validated catalog handling, controlled appliance actions and asynchronous physical-state verification.

Its main engineering lesson is that command dispatch and confirmed device state are separate events.

## Media

Status: **In testing**

Charon owns media-domain intelligence and lifecycle behavior.

Public-safe portfolio material may describe discovery, media identity, Plex integration, playback/lifecycle reasoning, quality policy, observed-state verification and domain-event handoff.

Private acquisition implementation is intentionally excluded from this repository.

## Energy

Status: **In testing**

The local energy pipeline has produced stable and usable telemetry for grid, photovoltaic and battery behavior, including MQTT/Home Assistant integration and energy-balance validation.

Full long-duration validation remains incomplete, so the portfolio does not describe it as production-ready or generally available.

## Presence

Status: **Designed to enable**

BLE experiments demonstrated that available signals were not reliable enough to become an authoritative occupancy source.

The preferred future direction is deliberately minimal and privacy-preserving: `occupied / empty / uncertain`, without room-level tracking or continuous movement profiling.

The work is currently parked rather than treated as an active reliable automation dependency.

## Climate

Status: **In testing**

Environmental sensing and selected control strategies are exercised privately.

Physical orchestration remains in Home Assistant and feedback quality matters before any capability is promoted as reliable.

## Home Theater

Status: **In testing / privately validated**

The Bravia and Dolby safe-power workflow remains a representative Home Assistant-owned physical orchestration case study.

State-based sequencing avoids startup race conditions and keeps recovery logic local and observable.

## Development State

Current development truth comes from:

- GitHub Issues for tasks, priorities, dependencies and active status;
- Git `main` for merged implementation and documentation;
- commits, tags, workflows and releases for implementation/release evidence;
- live systems for deployed behavior and health.

The retired private development ledger is historical only and does not override GitHub or runtime evidence.

## Documentation Status

The repository-backed documentation corpus is now the active durable project model.

- current architecture, API, ownership and maturity live in versioned Markdown;
- `AGENTS.md`, `docs/agent/` and `docs/llms.txt` provide agent-oriented entrypoints without creating a second source of truth;
- MkDocs/GitHub Pages is a presentation layer over the same Markdown;
- historical ADRs, worklogs and dated project-model snapshots remain immutable historical records.

The legacy local compact project model is retired as an active source and preserved only through sanitized historical context.

The portfolio intentionally documents architecture, case studies and reusable lessons rather than mirroring private implementation.
