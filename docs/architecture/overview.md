# Architecture Overview

Keriol Home is a local-first smart-home platform centered on Home Assistant and extended through an agent and tool architecture.

## Main Flow

User -> Alexa / Web / Telegram / App -> FastAPI -> Alfred Core -> Tool Registry -> Integrations

## Layers

Frontends: Alexa, Assist, web interfaces, dashboards and future messaging clients.

Agent and API: FastAPI, Alfred Core, deterministic routing, AI fallback and Tool Registry.

Speech and policy: Giorgio renders Alfred speech; Osvaldo controls proactive notification policy.

Orchestration: Home Assistant automations, scripts, dashboards and physical device wrappers.

Domain services: Laundry, RSVP, server operations, Plex and Charon media intelligence.

Logic: Python services and Node-RED multi-event flows.

Event bus: MQTT.

Devices and infrastructure: Energy telemetry, lights, plugs, cameras, sensors, appliances, NAS and media services.

## Interaction Models

Interactive requests follow:

Frontend -> Alfred -> Tool Registry -> Domain Tool -> Alfred -> Giorgio

Proactive events follow:

Domain Event -> Queue or Dispatcher -> Osvaldo -> Giorgio -> Shared Home Assistant Delivery

## Design Rules

- Home Assistant owns orchestration, dashboards and physical wrappers.
- Alfred owns request routing and registered tool execution.
- Giorgio owns speech rendering.
- Osvaldo owns proactive notification policy.
- Charon owns media-domain intelligence.
- Python owns complex or stateful logic.
- Node-RED owns visual multi-event flows.
- MQTT owns decoupled telemetry and events.
- Actions require confirmation and physical-state verification when appropriate.
- Avoid duplicate logic across layers.

## Related Documentation

- [Alfred Ecosystem](alfred-ecosystem.md)
- [Alfred Ecosystem Flow](../diagrams/alfred-ecosystem-flow.md)
