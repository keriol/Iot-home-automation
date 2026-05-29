# Home Automation Project Model

## Scope

Local-first smart-home platform built with Home Assistant, MQTT, Node-RED, Python helpers, Plex API, QNAP NAS, Alexa, Assist, Tailscale and Cloudflare Tunnel.

## Rules

- Keep this model compact.
- Keep worklog separate.
- Backup before risky changes.
- One feature at a time.
- Prefer local integrations.
- Do not publish secrets or personal identifiers.

## Architecture

- Home Assistant: orchestration and dashboards.
- MQTT: event bus and telemetry boundary.
- Python: complex logic, API parsing and stateful workflows.
- Node-RED: visual multi-event flows.
- Cloudflare Tunnel: selected HTTPS public integrations.
- Tailscale: private administration.

## Current State

- Home Assistant Docker working.
- Mosquitto MQTT working.
- Node-RED working.
- Cloudflare Tunnel working.
- Tailscale private access working.
- Alexa Devices integration working.
- Assist custom intents working.
- Plex voice control working.
- Bravia/Dolby safe-power automation working.
- Tapo plug used for Dolby power control.
- ZCS local energy telemetry published to MQTT.
- Energy Dashboard v1 available.
- hOn washing machine integrated.
- BLE adapter validated.
- Bermuda BLE installed.
- Phone BLE pilot working.

## Priorities

1. Backup baseline.
2. Cloudflare Access policy.
3. Presence stabilization.
4. Second phone BLE.
5. casa_vuota logic.
6. Energy validation.
7. Battery charge/discharge mapping.
8. Climate dashboard.
9. Laundry voice query.
10. Portfolio documentation.

## Portfolio

The public repository contains architecture, roadmap, worklog, case studies and sanitized examples. It must never contain secrets, tokens, private IPs, real domains, device IDs, credentials, Home Assistant `.storage`, databases, logs or backups.
