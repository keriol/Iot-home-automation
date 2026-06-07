# Home Automation Portfolio

Public-safe documentation repository for a personal smart-home platform built around Home Assistant, MQTT, Node-RED, Python helpers, voice assistants, secure remote access and energy monitoring.

## Goals

- Local-first smart home orchestration
- Secure private access through VPN
- Public HTTPS integration layer for selected services
- Voice-controlled media and home automations
- MQTT-based telemetry and event bus
- Energy monitoring and automation-ready data
- Portfolio-ready IoT documentation

## Core Stack

- Home Assistant Docker
- Mosquitto MQTT Docker
- Node-RED
- Python helper scripts
- HACS integrations
- Plex API
- QNAP NAS
- Tailscale
- Cloudflare Tunnel

## Main Case Studies

- Bravia + Dolby safe-power automation
- Plex voice control through Assist and helper scripts
- ZCS photovoltaic local telemetry through MQTT
- BLE presence detection with Bermuda
- Cloudflare Tunnel and Tailscale access strategy

## Public Safety

This repository contains only sanitized documentation and examples. Real secrets, tokens, entity IDs, IPs, domains, device identifiers and private paths are excluded.

## Development Approach

This project follows an AI-assisted engineering workflow.

Architecture decisions, implementation and validation remain human-driven, while AI is used as a technical copilot for research, troubleshooting, documentation, roadmap management and knowledge preservation.

The project maintains a continuously updated project model, architecture documentation, roadmap, worklogs and case studies to support long-term development.

## AI-Assisted Development

This project is developed using a Human + AI engineering workflow.

ChatGPT is used as a technical copilot for research, troubleshooting, documentation, architecture review and project knowledge management.

Final architecture decisions, implementation, validation and production ownership remain human-driven.

- [AI Collaboration](docs/AI_COLLABORATION.md)
- [AI-Assisted Development Flow](docs/diagrams/ai-assisted-development-flow.md)
- [ADR-005 - AI-Assisted Development Workflow](docs/adr/ADR-005-ai-assisted-development.md)

## Current Highlight - Alfred the Butler Laundry Workflow

The laundry workflow is now one of the most complete portfolio-grade features in this project.

Alfred the Butler can interact with the washing machine through an Alexa Custom Skill, a FastAPI bridge, Home Assistant and the hOn integration without exposing Home Assistant directly.

Implemented capabilities:

- washing-machine status query
- remaining-time query
- validated program catalog
- Italian program names and aliases
- true keyword search across the laundry catalog
- paginated voice results for long program lists
- validated remote start for allowlisted programs
- remote stop command
- cautious command language
- program-name fallback when hOn reports generic values
- asynchronous start/stop verification
- hOn state refresh before each verification attempt
- Echo notification after verified start/stop state
- proactive washer-connected prompt with cooldown and guardrails

Key design decision:

The system does not treat command dispatch as physical success. Alfred sends the command, then verifies the real washer state asynchronously before announcing the final result.

Remaining work:

- validate active-cycle menu during more real washing cycles
- refine Alexa Developer Console model for help, yes/no and exit routing
- connect proactive prompts to stronger presence/home-context logic
- monitor upstream hOn behavior for remote-start program naming
- add future PV-aware laundry suggestions

Relevant documentation:

- [Alexa Custom Skill Laundry MVP](docs/case-studies/alexa-custom-skill-laundry-mvp.md)
- [Alfred Laundry Portfolio Analysis](docs/analysis/alfred-laundry-voice-ux-and-async-verification.md)
- [Alfred Laundry Lessons Learned](docs/lessons-learned/alfred-laundry-voice-ux-and-async-verification.md)
- [Alexa Laundry Async Verification Diagrams](docs/diagrams/alexa-laundry-async-verification.md)
