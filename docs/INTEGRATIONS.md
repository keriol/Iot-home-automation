# Integrations

## Overview

Keriol Home integrates Home Assistant native integrations, selected custom integrations and external services.

This document describes **integration/provider boundaries**, not Butler capabilities. In the current model:

- an **integration/provider** connects to an external service or platform;
- a **tool** is a typed executable operation exposed through that integration;
- a **capability** describes something the Butler knows how to do;
- a **domain** owns related behavior and knowledge.

The portfolio therefore avoids treating a connected service as equivalent to a public Butler capability.

## Current Integration Categories

| Area | Integration / Provider | Purpose | Portfolio treatment |
|---|---|---|---|
| Voice | Alexa | current private Keriol voice frontend and speech-delivery target | Private proving ground / in testing |
| Voice | Home Assistant Assist | voice/frontend experimentation through Home Assistant | Integration evidence only; not a Butler ownership claim |
| Media | Plex | media catalog, playback context and lifecycle integration | Private proving-ground media intelligence |
| Lighting | Hue | smart-lighting integration through Home Assistant | Home Assistant-owned physical orchestration |
| Lighting | Magic Home / `flux_led` | LED control | Home Assistant/integration-owned device control |
| Power | Tapo | smart-plug control | Home Assistant-owned physical orchestration |
| Climate | Tuya / thermostat integrations | climate monitoring and device control | Home Assistant-owned physical orchestration |
| Infrared | Broadlink | IR-based device control | Home Assistant-owned physical orchestration |
| Appliances | hOn | appliance monitoring and command integration | private verified-workflow proving ground |
| Cameras | RTSP / camera integrations | video-stream integration | integration evidence; higher-level intelligence is separate |
| Presence | Bermuda BLE | BLE signal/presence experimentation | Designed to enable reliable occupancy behavior; not production-ready occupancy evidence |
| Energy | MQTT sensors | local photovoltaic and battery telemetry | In testing |
| Security / Access | Cloudflare Tunnel | HTTPS exposure for selected public integrations | infrastructure boundary |
| Security / Access | Tailscale | private remote administration | infrastructure boundary |

## Home Assistant Ownership

Home Assistant remains the owner of device integrations, physical orchestration, dashboards and automation wrappers.

Butler layers reason about goals, route requests and invoke typed capabilities. They do not replace the integration owner simply because they can call it.

For observable physical actions the preferred execution pattern is:

`READ -> ACTION -> READ -> VERIFY`

A successful service call is not treated as proof that the physical device reached the requested state.

## Public Plugin Boundary

Reusable Home Assistant interaction belongs in the public `wilfred-home-assistant` plugin when it is sufficiently generalized, tested and documented.

Private Keriol integrations and household-specific behavior do not become public Wilfred features automatically.

An integration may exist privately while the corresponding public capability remains:

- **In testing**, or
- **Designed to enable**.

## Custom Components and Third-Party Code

The live Home Assistant environment may use upstream custom components for selected devices and services.

Third-party component source is not copied into this repository. The portfolio documents architecture, ownership, integration categories and public-safe lessons only.

Private provider implementation, credentials, endpoints, account identifiers, private storage/acquisition mechanisms and machine-specific configuration remain outside the portfolio.

## Selection Principles

Integrations are chosen with these priorities:

1. prefer local control and local telemetry where practical;
2. preserve clear ownership between Home Assistant, providers and Butler capabilities;
3. keep Butler Core provider-neutral;
4. use deterministic behavior before AI fallback for known operations;
5. validate observable physical outcomes when state matters;
6. treat private validation as evidence, not automatic public availability.
