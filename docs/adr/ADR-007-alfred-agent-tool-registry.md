# ADR-007 - Alfred Agent and Tool Registry Architecture

## Status

Accepted.

## Context

Keriol Home started as a collection of Home Assistant automations, Alexa intents, FastAPI helpers and integration-specific scripts.

This approach worked for isolated features, but adding more hardcoded intents and duplicated workflows was becoming difficult to maintain.

Laundry, RSVP, server operations, Plex, media curation, presence, energy, cameras, climate, NAS and future maker integrations require a consistent access model.

Alexa remains a frontend. It must not become the reasoning or orchestration layer of the system.

## Decision

Alfred the Butler is the user-facing agent and tool orchestrator of Keriol Home.

Architecture:

    User -> Alexa/Web/Telegram/App -> FastAPI -> Alfred Core -> Tool Registry -> Integrations

Alfred accesses services through registered tools rather than integration-specific conversation logic.

Each tool declares:

- name;
- description;
- parameters;
- category;
- permission level;
- timeout.

Permission levels:

- READ: safe read-only operations;
- ACTION: operations that change state and require validation;
- DANGEROUS: destructive or risky operations requiring explicit confirmation.

Known requests use deterministic routing first.

AI planning is a fallback for ambiguous language and future multi-tool workflows. It is not the default route for known commands.

## Supporting Components

The Alfred ecosystem separates responsibilities:

- Alfred owns request routing and tool execution.
- Giorgio owns speech and SSML rendering.
- Osvaldo owns proactive notification policy.
- Charon owns media-domain and catalog intelligence.

Interactive requests follow:

    Frontend -> Alfred -> Tool Registry -> Domain Tool -> Alfred -> Giorgio

Proactive events follow:

    Domain Event -> Queue or Dispatcher -> Osvaldo -> Giorgio -> Shared Home Assistant Delivery

Direct responses to explicit user requests do not require Osvaldo's permission.

Unsolicited notifications must pass through Osvaldo so they may be allowed, deferred, aggregated or denied.

## Implemented Architecture

Routes:

- POST /alfred/ask
- GET /alfred/tools
- GET /alfred/ai/status
- Alexa free-text backend bridge through Alfred Core

Core capabilities:

- Alfred Core
- Tool Registry
- deterministic-first routing
- OpenAI planner fallback
- domain mismatch guard
- tool permissions and timeouts
- JSONL request logging
- pending-action confirmation support

Registered READ capabilities include:

- laundry status and program search;
- server status;
- RSVP summary and guest status;
- Plex status, libraries, activity and media search.

Registered ACTION capabilities include confirmed Plex library and path scans.

The Plex update workflow can evaluate recent viewing, apply cooldown rules, send proactive notifications through Osvaldo and create playback offers.

Shared Home Assistant delivery and Giorgio rendering are reusable services rather than Plex-specific helpers.

Laundry asynchronous verification, RSVP, Plex and snoozable notifications use the same proactive policy path.

## Consequences

Adding a capability should normally mean registering a new tool or emitting a domain event.

Alexa-specific intent logic remains only where needed for compatibility or deterministic device interactions.

Domain services must not duplicate:

- agent routing;
- proactive notification policy;
- speech rendering;
- physical notification delivery.

This architecture allows Alfred to grow without turning the agent core into a monolith.

Future domains include:

- presence and house modes;
- camera and security tools;
- energy and UPS tools;
- climate intelligence;
- NAS and backup health;
- calendar and weather;
- Bambu and maker workflows;
- Charon catalog analysis and recommendations.

## Safety Consequences

READ operations may execute directly.

ACTION and DANGEROUS operations require validation and confirmation according to their risk.

Dispatching a physical command is not considered success. State must be verified whenever the integration supports it.

Live information must come from tools. Alfred must not invent unavailable state.

## UX Decision

Fast deterministic requests should receive immediate responses.

Slow AI or multi-tool workflows may use a progressive response such as:

    Un momento, apro il cruscotto della casa.

Progressive responses must not be added to fast deterministic paths.
