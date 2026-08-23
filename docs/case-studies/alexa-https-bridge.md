# Alexa HTTPS Bridge MVP

> **Historical engineering milestone.** This case study documents an earlier standalone Alexa-to-Home-Assistant bridge used before the current Alfred / Wilfred / Hermes ownership model matured. The implementation remains useful as evidence of the integration path and security decisions, but it should not be read as the complete current Butler architecture. See the current architecture documentation for present ownership boundaries.

## Problem

Voice assistants are excellent at triggering predefined actions, but become limiting when dynamic queries, parameterized requests, or custom integrations are required.

The goal was to create a secure and extensible path between Alexa and Home Assistant without exposing Home Assistant directly to the Internet.

## Solution

A dedicated FastAPI bridge was introduced between Alexa and Home Assistant.

The bridge acts as a controlled backend layer responsible for:

- Request validation
- Alexa response formatting
- Home Assistant API integration
- Future command allowlisting
- Future business logic expansion

## Architecture

- Alexa Custom Skill
  - HTTPS Endpoint
    - Cloudflare Tunnel
      - FastAPI Bridge
        - Home Assistant REST API
          - Smart Home Entities

## Current MVP

Implemented:

- FastAPI service
- Health endpoint
- Alexa-compatible laundry status endpoint
- Home Assistant REST integration
- Dedicated token-based authentication
- Offline appliance detection
- Cloudflare Tunnel publication
- Persistent systemd deployment

## Validation

The following path was successfully validated:

- Internet
  - Cloudflare HTTPS Endpoint
    - FastAPI Bridge
      - Home Assistant
        - Washing Machine Entities

Health endpoint validation:

`{"status":"ok"}`

Laundry status endpoint validation:

- Response version: 1.0
- Output type: PlainText
- Example response:
  - "The washing machine is currently not connected."

## Security Considerations

The MVP is intentionally read-only.

Home Assistant is not exposed directly as the Alexa backend.

Future appliance control capabilities will require:

- Command allowlists
- Appliance state validation
- Explicit safety checks
- No fuzzy matching for critical commands

## Future Evolution at the Time

The original milestone anticipated richer Alexa intents, laundry catalog queries, media search/playback and controlled appliance workflows.

Those directions later evolved under the broader Butler architecture. Current ownership and maturity should therefore be read from the current architecture, project status and roadmap rather than inferred from this historical future-work section.

## Lessons Learned

Cloudflare Tunnel provides a lightweight method to publish secure HTTPS endpoints without exposing ports or deploying a traditional reverse proxy.

A dedicated bridge layer significantly simplified early integrations while keeping Home Assistant isolated from external consumers.

The later architecture preserved the important boundary lesson while moving interaction, capability and delivery ownership into clearer layers.

## Outcome

A complete HTTPS path was validated from an external client to Home Assistant through Cloudflare Tunnel and a dedicated FastAPI backend.

The enduring portfolio value of this milestone is the security boundary and iterative architecture lesson, not the claim that this bridge remains the complete current Alfred design.
