# Alexa Home Assistant Bridge

Sanitized example of a FastAPI bridge used to connect an Alexa Custom Skill to Home Assistant.

## Purpose

The bridge acts as a controlled backend layer between external voice assistants and Home Assistant.

Responsibilities:

- Request validation
- Response formatting
- Home Assistant API integration
- Future command allowlisting

## Architecture

- Alexa Custom Skill
  - HTTPS Endpoint
    - Cloudflare Tunnel
      - FastAPI Bridge
        - Home Assistant REST API

## Security

The example intentionally excludes:

- Real hostnames
- Real entity IDs
- Real tokens
- Real tunnel identifiers
- Internal network information

## Files

- `.env.example`: placeholder environment configuration.
- `app_sanitized.py`: minimal FastAPI example.
- `alexa-ha-bridge.service.example`: example systemd service.

## Environment Example

- `HA_BASE_URL=http://HOME_ASSISTANT_HOST:8123`
- `HA_TOKEN_FILE=/path/to/token.txt`

## Notes

This example is read-only by design.

Remote appliance control should require explicit command allowlists, state validation, and safety checks.
