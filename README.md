# Home Automation Portfolio

Public-safe documentation repository for a local-first smart-home platform built around Home Assistant, MQTT, Node-RED, Python/FastAPI services and the Alfred agent and tool architecture.

## Goals

- Local-first smart home orchestration
- Agent-based access through Alfred and registered tools
- Policy-driven proactive notifications
- Secure private access through VPN
- Public HTTPS integration layer for selected services
- Voice-controlled media and home automations
- MQTT-based telemetry and event bus
- Energy monitoring and automation-ready data
- Portfolio-ready IoT documentation

## Core Stack

- Home Assistant Docker
- Python / FastAPI
- Alfred Core and Tool Registry
- Mosquitto MQTT Docker
- Node-RED
- Python helper scripts
- HACS integrations
- Plex API
- QNAP NAS
- Tailscale
- Cloudflare Tunnel

## Main Case Studies

- Alfred Agent and Tool Registry architecture
- Osvaldo proactive notification policy
- Charon media and Plex curation
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

## Current Architecture - Alfred Ecosystem

Keriol Home separates orchestration, speech, proactive policy and domain expertise into explicit components:

- **Alfred** is the user-facing agent and registered-tool orchestrator.
- **Giorgio** renders Alfred speech and SSML.
- **Osvaldo** decides whether proactive notifications are allowed, deferred, aggregated or denied.
- **Charon** provides Plex and media-domain intelligence.
- **Umberto** tracks milestones, tasks, commit evidence and checkout work.

Interactive requests follow:

    Frontend -> Alfred -> Tool Registry -> Domain Tool -> Alfred -> Giorgio

Proactive events follow:

    Domain Event -> Queue or Dispatcher -> Osvaldo -> Giorgio -> Shared Home Assistant Delivery

Home Assistant remains responsible for physical orchestration and device wrappers. Alfred coordinates capabilities but does not replace the smart-home core.

Relevant documentation:

- [Architecture Overview](docs/architecture/overview.md)
- [Alfred Ecosystem](docs/architecture/alfred-ecosystem.md)
- [Architecture Diagram](docs/diagrams/architecture.md)
- [Alfred Ecosystem Flow](docs/diagrams/alfred-ecosystem-flow.md)
- [ADR-007 - Alfred Agent and Tool Registry](docs/adr/ADR-007-alfred-agent-tool-registry.md)
- [ADR-006 - Proactive Notification Policy](docs/adr/ADR-006-proactive-notification-policy.md)
- [Current Public Project Model](docs/project-model/project-model-public.md)
- [Umberto Development Ledger](docs/analysis/umberto-development-ledger.md)
- [Umberto Checkout Flow](docs/diagrams/umberto-checkout-flow.md)

## Featured Case Study - Alfred Laundry Workflow

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
