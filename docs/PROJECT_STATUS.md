# Home Automation Project Status

Last Updated: 2026-08-31

## Overview

Keriol Home is an operational local-first smart-home platform and the private proving ground behind the public Butler ecosystem.

The current architecture separates reusable public runtime components from Keriol-specific deployment behavior:

`Butler Core -> Wilfred -> Alfred`

Home Assistant remains the owner of physical orchestration, integrations, dashboards and device state.

## Current Baselines

| Component | Current status | Notes |
|---|---|---|
| Butler Core | Available | `0.2.0` released baseline with provider-neutral execution, async-job, tracing and domain-contribution contracts |
| Wilfred | Available / Public Alpha | `0.2.1` current Public Alpha; Core 0.2 contract adoption remains a separate Wilfred development task |
| wilfred-home-assistant | In development | public plugin on `0.1.0.dev0` development line |
| Alfred | Private operational | `0.4.0` current private released baseline; post-0.4.0 development continues privately |
| Home Assistant | Operational | physical orchestration owner |
| MQTT | Operational | event and telemetry transport |
| Node-RED | Operational | selected visual workflows |
| Cloudflare Tunnel | Operational | narrow public integration transport |
| Tailscale | Operational | private administration |

Release claims use explicit Git/tag/release evidence. Development branches and open issues are not treated as released capability evidence.

## Butler Runtime

### Public

Butler Core `0.2.0` provides the current provider-neutral foundation for tools/registry, planning, deterministic resolution, policy-governed execution, asynchronous jobs, structured tracing, domain/capability contribution declarations and output contracts.

Core remains deliberately smaller than a runtime: plugin discovery/loading/lifecycle, concrete domain behavior, frontend rendering, AI-provider configuration and deployment-specific integrations remain outside Core.

Wilfred builds the reusable runtime on those foundations and currently provides registered tool execution, deterministic-first resolution, planning interfaces, confirmation boundaries, workflows, verified execution, output contracts, standalone interfaces and plugin loading.

The current public consolidation direction is capability-first: capabilities describe what the Butler knows how to do, while domains own related knowledge and behavior. Core 0.2.0 now supplies reusable declarations for that model, while Wilfred adoption is tracked independently and must not be inferred from the Core release alone.

### Private proving ground

Alfred composes Keriol-specific context, routing, domains, integrations and AI fallback around the reusable stack.

Private behavior may run ahead of the public distribution. That does not make it a Wilfred feature automatically.

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

DOC-005 refreshes the current-state portfolio after the Butler Core 0.2.0 release while preserving the distinction between Core availability and downstream Wilfred adoption.

Historical ADRs, worklogs and dated snapshots remain historical and are not rewritten retroactively.

The portfolio intentionally documents architecture, case studies and reusable lessons rather than mirroring private implementation.
