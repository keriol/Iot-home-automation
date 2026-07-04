# Home Automation Project Model (Public)

## Overview

Local-first smart-home and IoT platform built with Home Assistant, MQTT, Python/FastAPI, Node-RED, Docker and AI-assisted engineering practices.

The project focuses on:

- Voice automation
- Smart appliance integration
- Media automation
- Secure remote access
- Energy monitoring
- Presence detection
- Camera/security roadmap
- Public-safe documentation and portfolio storytelling

## Principles

- Local-first whenever possible.
- Use VPN/Tailscale for private administration.
- Use Cloudflare Tunnel only for narrow public integration endpoints.
- Do not expose Home Assistant directly.
- One owner layer per feature.
- Avoid duplicated logic across Home Assistant, Python, Node-RED and MQTT.
- Notify first, automate later.
- Never commit secrets, tokens, debug payloads, private endpoints, real device IDs, personal data or raw logs.

## Vision

Alfred the Butler is the AI Agent layer of the home automation platform.

Alfred is not the smart-home software itself. Alfred knows how to talk to the smart-home services through tools.

User-facing entrypoints can include:

- Alexa
- Web
- Telegram or chat interfaces
- Dashboards
- Future automations

Alexa remains a frontend. Alfred owns routing, tool selection and orchestration.

## Stack

Working:

- Home Assistant Docker
- Mosquitto MQTT
- Node-RED
- HACS
- Python/FastAPI
- Plex API experiments
- QNAP/NAS integrations
- Alexa custom skill MVP
- Echo TTS/text notifications
- Home Assistant Assist
- Cloudflare Tunnel
- Tailscale
- hOn washing machine integration
- Smart plugs, lights, media and appliance integrations

Planned:

- Alfred Agent Alexa integration
- Plex tools
- Bambu Lab tools
- UPS tools
- Energy tools
- Presence tools
- Camera/security tools
- NAS tools
- Calendar/weather tools
- Tool dashboard with health, logs and AI cost overview

## Architecture

Main target architecture:

    User -> Alexa/Web/Telegram/App -> FastAPI -> Alfred Agent -> Tool Registry -> Integrations

Layer ownership:

- Home Assistant: orchestration, dashboards, simple automations and physical commands.
- Python/FastAPI: Alfred Core, APIs, Tool Registry, validation, planning and workflows.
- Node-RED: visual multi-event flows.
- MQTT: event bus for decoupled integrations.

## Alfred Agent

Implemented MVP:

- Alfred Core
- Tool Registry
- Tool metadata
- deterministic-first routing
- AI planner fallback
- compact JSONL request logging
- /alfred/ask
- /alfred/tools
- /alfred/ai/status

Tool metadata:

- name
- description
- parameters
- category
- permission level
- timeout

Permission levels:

- READ: safe read-only tools
- ACTION: changes state and requires explicit rules/allowlist
- DANGEROUS: risky actions requiring explicit confirmation

## Current Tool Examples

Initial READ tools:

- get_laundry_status
- search_laundry_programs(keyword)
- get_server_status
- get_rsvp_summary
- get_rsvp_guest_status(name)

Planned tools:

- get_plex_status
- search_plex_media
- start_plex_scan
- get_bambu_status
- get_home_overview
- presence tools
- camera/security tools
- energy tools
- NAS tools

## AI Strategy

Known requests use deterministic routing first.

AI is used only as fallback or planner when the request is ambiguous or requires broader reasoning.

Observed MVP behavior:

- deterministic server status replies are near real-time
- deterministic RSVP lookups are near real-time
- deterministic laundry status/search is near real-time
- AI fallback works but is slower, so it is not the primary path for known Alexa requests
- initial MVP testing cost was negligible

## Voice UX

Alexa remains the main voice frontend.

Current skill flows remain compatible with existing Alexa intents.

Future Alfred Agent voice flow:

    Alexa -> Cloudflare HTTPS -> FastAPI -> Alfred Agent -> Tools

For slow AI or multi-tool flows, Alexa may use a progressive response:

    Un momento, apro il cruscotto della casa.

This should not be used for fast deterministic replies.

## Laundry

Laundry is exposed through Alfred tools.

Rules:

- exact validated aliases only
- no fuzzy start/stop
- backend validation before physical commands
- Home Assistant owns physical wrappers
- dispatch is not physical success
- verify state after commands
- keep responses cautious when integration data is stale

## RSVP

RSVP is exposed through Alfred tools.

Public-safe rule:

- examples must use fake guest names
- no real guest data
- no emails
- no phone numbers
- no raw RSVP payloads
- no private paths

## Server Health

Server status is exposed as a READ-only Alfred tool.

It reports high-level health such as uptime, load, disk usage, memory usage, service status and Docker container count.

## Security

- Private access through VPN/Tailscale.
- Public integrations through narrow Cloudflare Tunnel routes.
- Home Assistant is not directly exposed.
- Tool execution is permission-based.
- READ before ACTION.
- DANGEROUS actions require explicit confirmation.
- Public docs must stay sanitized.

## Roadmap

Next steps:

1. Document Alfred Agent MVP with ADR, worklog and examples.
2. Wire generic Alexa requests to Alfred Agent safely.
3. Add Plex READ tools.
4. Add home overview/cruscotto multi-tool.
5. Add progressive Alexa response for slow AI/multi-tool requests.
6. Add dashboard for tools, logs, health and AI cost.
7. Add Bambu, UPS, energy, ESP32, NAS, calendar and weather tools.
8. Add presence and video surveillance as Alfred tools.

## Motto

Alfred is not the software of the house. Alfred is the one who knows how to talk to every software of the house.
