# Project Showcase

## Overview

This document highlights representative engineering work across the public Butler stack and the private Keriol Home proving ground.

The goal is not to present every experiment as shipped functionality. Each example is labelled according to current evidence:

- **Available**: public, documented and usable in the relevant public repository or plugin.
- **In testing**: exercised privately or under active validation, but not a public release promise.
- **Designed to enable**: architecturally supported direction that must not be read as implemented functionality.

---

# 1. Butler Runtime Evolution

## Status

**Available + In testing**

## Objective

Separate reusable Butler execution foundations from Keriol-specific household behavior.

## Architecture

`Butler Core -> Wilfred -> Alfred`

## Current result

- Butler Core `0.1.4` is the released provider-neutral foundation consumed by Wilfred `0.2.1`.
- Wilfred `0.2.1` is the current Public Alpha.
- Alfred remains the private real-world proving ground.
- Home Assistant remains the physical orchestration owner.

## Engineering themes

- provider-neutral contracts;
- deterministic-first resolution;
- capability/domain ownership;
- confirmation boundaries;
- verified execution;
- public/private extraction discipline.

---

# 2. Alfred Laundry Voice Workflow

## Status

**In testing / privately validated**

## Objective

Expose washing-machine state, catalog queries and controlled actions through a voice workflow while avoiding false success claims.

## Validated capabilities

- appliance status and remaining-time queries;
- validated local program catalog;
- translated display names and controlled aliases;
- keyword search and pagination;
- allowlisted start/stop actions;
- cautious command feedback;
- asynchronous physical-state verification;
- follow-up communication only after observable state changes when possible.

## Key engineering lesson

**Dispatch is not physical success.**

The workflow separates command acceptance from observable confirmation and uses the broader pattern:

`READ -> ACTION -> READ -> VERIFY`

This case study is one of the main real-world inputs into the reusable verified-execution model.

---

# 3. Proactive Communication Policy

## Status

**In testing**

## Objective

Prevent every domain from inventing its own notification timing, quiet-hours logic and delivery behavior.

## Ownership

- Domains describe what happened.
- Osvaldo decides whether and when unsolicited communication may occur.
- Hermes owns provider/delivery routing.
- Frontends/providers own presentation-specific rendering.

## Supported policy concepts

- allow;
- defer;
- aggregate;
- deny;
- quiet-hours handling;
- communication-mode selection.

User-requested asynchronous replies are treated separately from generic unsolicited notifications because they continue an explicit interaction.

---

# 4. Media Intelligence and Plex Workflows

## Status

**In testing**

## Objective

Treat media handling as a domain with explicit ownership rather than scattering Plex and playback behavior through conversation code.

## Public-safe capabilities demonstrated

- media identity and discovery;
- Plex integration;
- playback-related reasoning;
- quality and availability policy;
- lifecycle concepts;
- observed-state verification;
- domain-event handoff to communication policy.

## Ownership lesson

Charon owns media-domain intelligence and lifecycle behavior. It does not own generic conversation routing, proactive policy or provider delivery.

Private acquisition implementation is intentionally outside this repository.

---

# 5. Home Theater Safe-Power Workflow

## Status

**In testing / privately validated**

## Objective

Prevent audio initialization failures caused by startup timing between the TV and home-theater equipment.

## Technologies

- Home Assistant;
- smart-plug control;
- state-based automations;
- guarded sequencing.

## Outcome

The workflow demonstrates why physical orchestration belongs in Home Assistant: startup ordering, race-condition mitigation and recovery remain local, observable and easy to debug.

---

# 6. Local Energy Telemetry

## Status

**In testing**

## Objective

Collect and validate local photovoltaic, grid and battery telemetry without depending exclusively on vendor cloud services.

## Demonstrated work

- local polling and normalization;
- MQTT publication;
- Home Assistant sensors and dashboards;
- directional grid and battery flows;
- energy-balance comparison against independent observations.

## Current result

The pipeline is stable and usable, but full long-duration validation is not yet complete. It is therefore not presented as production-ready or generally available.

---

# 7. Privacy-Preserving Presence

## Status

**Designed to enable**

## Objective

Answer the operational question “is the home occupied?” without turning presence into continuous room-level tracking.

## Private experiments

BLE and presence tooling were evaluated, but the available signals were not reliable enough to become an authoritative automation dependency.

## Current direction

The preferred future model is deliberately small:

`occupied / empty / uncertain`

with no requirement for room-level localization or continuous movement profiling.

The work is currently parked pending better evidence and hardware choices.

---

# 8. Alexa / Hermes Delivery Path

## Status

**In testing**

## Objective

Keep voice frontends replaceable while allowing the private deployment to exercise provider-specific speech delivery.

## Current ownership

- Alexa is the current voice frontend and first Hermes target in Keriol Home.
- Hermes owns the private provider/delivery boundary.
- Speech and SSML remain frontend details.
- Provider-specific voice selection remains a rendering parameter, not an architectural component.

## Public direction

The architecture is designed to enable later reusable frontend/provider integrations if private validation, contracts, tests and sanitization justify extraction.

A working private Alexa path is not evidence that Wilfred currently ships an official Alexa integration.

---

# Key Engineering Themes

Across the portfolio, the recurring lessons are:

- local-first architecture where practical;
- Home Assistant as physical orchestration owner;
- deterministic behavior before AI fallback for known requests;
- explicit capability/domain ownership;
- dispatch and observed success kept separate;
- communication policy separated from delivery;
- replaceable frontends;
- public/private boundaries treated as architecture, not redaction afterthought;
- GitHub/Git/release/runtime evidence used according to responsibility.
