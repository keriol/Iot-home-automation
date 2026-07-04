# Alfred Agent examples

Sanitized examples for the Alfred Agent MVP.

## Goal

Alfred the Butler acts as the AI Agent layer of the home automation system.

Main flow:

    User -> Alexa/Web/Telegram/App -> FastAPI -> Alfred Agent -> Tool Registry -> Integrations

Alexa remains a frontend. Alfred owns routing and tool selection.

## Rules

- Known requests use deterministic routing first.
- AI is fallback only.
- Alfred can use registered tools only.
- Tools declare permission levels: READ, ACTION, DANGEROUS.
- ACTION and DANGEROUS tools require explicit confirmation rules.
- Public examples must never contain private domains, credentials, emails, phone numbers, raw logs or real guest data.

## Example requests

- How is the home server doing?
- Has Guest Example confirmed?
- How is Plex doing?

## Current public example tools

- get_laundry_status
- search_laundry_programs
- get_server_status
- get_rsvp_summary
- get_rsvp_guest_status

Plex, Bambu Lab, energy, presence and camera/security tools are planned future extensions.
