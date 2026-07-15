# 2026-06-01 - Alexa HTTPS Bridge MVP

## Completed

- Created a dedicated FastAPI bridge for future Alexa Custom Skill integration.
- Integrated the bridge with Home Assistant REST API through a dedicated token file stored outside the repository.
- Implemented an Alexa-compatible laundry status response.
- Added offline-state validation for the washing machine to avoid stale or misleading voice responses.
- Published a dedicated HTTPS endpoint through Cloudflare Tunnel.
- Deployed the bridge as a persistent systemd service.
- Validated the external HTTPS path end-to-end.

## Architecture

- Alexa / HTTPS client
  - Cloudflare Tunnel
    - FastAPI Bridge
      - Home Assistant REST API
        - Laundry entities

## Decisions

- Do not expose Home Assistant directly as Alexa skill backend.
- Use a dedicated bridge layer for request validation, response formatting and future command allowlisting.
- Keep the first MVP read-only.
- Treat remote appliance start/stop as a separate safety validation task.

## Validation

- Local `/health` endpoint validated.
- Public HTTPS `/health` endpoint validated.
- Public Alexa-style laundry status endpoint validated.
- Offline washing machine response validated.

## Next

- Configure Alexa Developer Console Custom Skill.
- Implement LaundryStatusIntent.
- Add read-only laundry catalog intents.
- Reuse the HTTPS bridge pattern for Plex voice search and playback.
- Investigate safe remote appliance control with strict allowlists.
