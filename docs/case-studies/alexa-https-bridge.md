# Alexa HTTPS Bridge MVP

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

## Future Evolution

Planned integrations:

- Alexa Custom Skill
- Laundry catalog queries
- Plex media search
- Plex playback control
- Future voice-driven appliance workflows

## Lessons Learned

Cloudflare Tunnel provides a lightweight method to publish secure HTTPS endpoints without exposing ports or deploying a traditional reverse proxy.

A dedicated bridge layer significantly simplifies future integrations while keeping Home Assistant isolated from external consumers.

## Outcome

A complete HTTPS path was validated from an external client to Home Assistant through Cloudflare Tunnel and a dedicated FastAPI backend.

This capability establishes the foundation for future voice-driven integrations including Alexa Custom Skills, Plex media search, appliance catalogs, and controlled remote appliance operations.

