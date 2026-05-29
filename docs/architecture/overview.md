# Architecture Overview

The system is a local-first smart-home platform centered on Home Assistant.

## Layers

Voice and UI:
Alexa, Assist, Home Assistant dashboards.

Orchestration:
Home Assistant automations, scripts and dashboards.

Logic:
Python helpers and Node-RED flows.

Event Bus:
MQTT.

Devices and Services:
Energy telemetry, Plex, lights, plugs, cameras, sensors and appliances.

## Design Rules

- Home Assistant owns orchestration and dashboards.
- Python owns complex or stateful logic.
- Node-RED owns visual multi-event flows.
- MQTT owns decoupled telemetry and events.
- Avoid duplicate logic across layers.
