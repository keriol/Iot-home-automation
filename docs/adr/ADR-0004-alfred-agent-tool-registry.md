# ADR-0004 - Alfred Agent and Tool Registry Architecture

## Status

Accepted.

## Context

The smart-home project started as a set of Home Assistant automations, Alexa intents, FastAPI helpers and integration-specific scripts.

This worked for individual features, but scaling by adding more Alexa intents and hardcoded flows was becoming hard to maintain. Laundry, RSVP, server health, Plex, QNAP, Bambu Lab, energy, presence and future camera/security capabilities all need a consistent access model.

Alexa should remain the voice frontend, not the brain of the system.

## Decision

Alfred the Butler becomes the AI Agent layer of Keriol Home.

Architecture:

    User -> Alexa/Web/Telegram/App -> FastAPI -> Alfred Agent -> Tool Registry -> Integrations

Alfred does not talk directly to services. It uses registered tools only.

Each tool declares:

- name
- description
- parameters
- category
- permission level
- timeout

Permission levels:

- READ: safe read-only tools
- ACTION: changes state and requires rules/allowlist
- DANGEROUS: destructive/risky actions requiring explicit confirmation

Known requests use deterministic routing first. The AI planner is a fallback only for ambiguous requests or future multi-tool planning.

## Implemented MVP

Routes:

- /alfred/ask
- /alfred/tools
- /alfred/ai/status

Core modules:

- AlfredCore
- ToolRegistry
- AI client
- AI planner fallback
- JSONL request logging

Initial tools:

- get_laundry_status
- search_laundry_programs(keyword)
- get_server_status
- get_rsvp_summary
- get_rsvp_guest_status(name)

## Results

Deterministic responses are fast and free:

- server status: around 25-30 ms
- RSVP guest lookup: around 50-75 ms
- RSVP summary: near instant
- laundry status/search: near instant

AI fallback works, but latency is around 3-7 seconds, so it must not be the primary path for known Alexa requests.

Initial MVP testing cost was negligible, around one cent.

## Consequences

Adding a feature should mean adding a tool, not expanding Alexa intent chaos.

Alfred can grow by adding capabilities:

- Plex tools
- Bambu Lab tools
- UPS tools
- energy tools
- presence tools
- camera/security tools
- NAS/QNAP tools
- calendar/weather tools

The system becomes more modular, safer to extend and easier to document.

## UX Decision

For slow AI or multi-tool flows, Alexa may use a progressive response:

    Un momento, apro il cruscotto della casa.

This must not be used for fast deterministic replies.
