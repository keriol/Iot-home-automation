# Home Automation Project Status

Last Updated: 2026-08-13

## Overview

Keriol Home is an operational local-first smart-home platform and the private proving ground behind the public Wilfred Butler runtime.

The current architecture separates reusable public runtime components from Keriol-specific deployment behavior.

## Platform Status

| Area | Status | Notes |
|---|---|---|
| Home Assistant | Operational | Owns physical orchestration, dashboards and device wrappers |
| MQTT | Operational | Event and telemetry bus |
| Node-RED | Operational | Visual multi-event workflows |
| Cloudflare Tunnel | Operational | Narrow public integration transport |
| Tailscale | Operational | Private administration |
| Alfred | Operational | Private Keriol Butler deployment |
| Butler Core | Public stable | Provider-neutral contracts and execution primitives |
| Wilfred | Active development | `0.2.0.dev0`, preparing Public Alpha |
| wilfred-home-assistant | Active development | Official public Home Assistant plugin |

## Butler Runtime

### Public

Butler Core provides shared contracts and execution primitives.

Wilfred builds the reusable Butler runtime on those foundations and provides:

- registered tools and capabilities
- execution and planning interfaces
- confirmation boundaries
- verified workflows
- output contracts
- standalone HTTP APIs
- configured plugin loading
- Docker distribution

The official Home Assistant plugin provides explicit state reads and service actions through the Home Assistant REST API.

### Private validated

Alfred uses the reusable Butler foundations while adding Keriol-specific integrations, interaction behavior and domain policy.

Some capabilities remain ahead of the public Wilfred distribution and are intentionally described as **Private validated** rather than public features.

## Safety Model

The active design rules include:

- one owner layer per feature;
- READ before ACTION where useful state exists;
- explicit confirmation for sensitive actions;
- dispatch is not physical success;
- READ / VERIFY after physical actions when observable;
- deterministic execution before AI fallback where appropriate;
- frontend-specific presentation must not become an orchestration component.

## Voice and Interaction

Status: **Operational / Private validated**

- Alexa is the current primary voice frontend.
- Free-text and legacy deterministic paths coexist during migration.
- Alfred owns Keriol interaction context.
- Wilfred provides the reusable runtime foundation.
- Speech and SSML rendering remain Alexa/frontend-specific.
- Slow AI-backed interactions can acknowledge the request before provider latency becomes noticeable.

## Proactive Communication

Status: **Operational / Private validated**

Osvaldo owns policy for unsolicited communication, including:

- allow;
- defer;
- aggregate;
- deny;
- quiet-hours behavior;
- communication mode selection.

Domains emit events but do not own proactive delivery policy.

## Appliances

Status: **Operational / Private validated**

The laundry workflow validates the core safety principle that successful command dispatch does not prove physical success.

Implemented behavior includes status queries, catalog handling, controlled actions and asynchronous state verification.

## Media

Status: **Operational / Private validated**

Plex and Tautulli are integrated.

Charon owns media-domain intelligence including discovery, catalog policy, playback-related workflows and lifecycle analysis.

Selected reusable concepts may become future public Wilfred capabilities.

## Energy

Status: **Operational with ongoing expansion**

Local telemetry includes photovoltaic and battery-related data exposed through Home Assistant and MQTT.

Further work includes richer consumption analysis and context-aware recommendations.

## Presence and Security

Status: **Experimental / In progress**

BLE and other presence inputs are being evaluated.

Critical automation remains conservative until presence confidence is sufficient.

## Climate

Status: **Experimental / Private validated**

Temperature and humidity sensing are available.

Climate-control strategies are being tested incrementally, with particular attention to feedback quality and post-command verification.

## Public Alpha Status

Wilfred `0.2.0` has not yet completed its final public release checkout.

Before calling the Public Alpha complete, the project still requires:

- final compatible-version coordination;
- stable public artifacts;
- stable public container publication;
- clean pull and runtime verification;
- final release checkout;
- release-adjacent public communication.

## Known Documentation Gap

The portfolio historically documented Alfred before Wilfred existed.

Current documentation is being realigned so that:

- historical files preserve the architecture of their time;
- current documents describe Butler Core -> Wilfred -> Alfred accurately;
- private validated capabilities are distinguished from public Wilfred features;
- legacy readable implementation examples are removed from the portfolio under the current public/private boundary.
