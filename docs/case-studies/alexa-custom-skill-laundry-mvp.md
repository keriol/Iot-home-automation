# Case Study - Alexa Custom Skill Laundry MVP

## Goal

Build a public HTTPS voice bridge that lets an Alexa Custom Skill interact with Home Assistant laundry workflows without exposing Home Assistant directly.

The first milestone was read-only washing machine status. The second extended it to catalog queries and controlled laundry start/stop operations.

## Architecture

Flow:

Alexa Custom Skill
-> Cloudflare Tunnel HTTPS endpoint
-> FastAPI bridge
-> Home Assistant REST API
-> hOn washing machine integration

For controlled start commands, the bridge also uses:

FastAPI bridge
-> validated laundry program catalog
-> Home Assistant script wrapper
-> hOn washing machine integration

## Components

- Alexa Developer Console custom skill
- Cloudflare Tunnel HTTPS hostname
- FastAPI bridge running through Uvicorn
- systemd service for persistent bridge execution
- Home Assistant REST API
- Home Assistant script wrapper for physical hOn start command
- hOn washing machine entities
- local validated laundry program catalog

## Implemented Routes

- GET /
- GET /health
- GET /laundry/status
- POST /alexa
- POST /alexa/laundry

## Validated Voice Flow

Alexa
-> Custom Skill
-> HTTPS endpoint
-> Cloudflare Tunnel
-> FastAPI bridge
-> Home Assistant
-> hOn integration
-> Alexa voice response

## MVP Outcome

The custom Alexa skill was validated end-to-end.

Validated read-only flows:

- Ask Alfred The Butler how much time is left on the washing machine.
- Ask Alfred The Butler what programs are available.
- Ask Alfred The Butler which programs are available for whites.

Validated controlled appliance flows:

- Ask Alfred The Butler to start a validated laundry program.
- Ask Alfred The Butler to stop the washing machine.

## Supported Laundry Intents

Canonical backend intent names use the `Laundry` prefix to keep related features grouped and recognizable.

- LaundryStatusIntent
- LaundryLastIntent
- LaundryStartIntent
- LaundryStopIntent
- LaundryAvailableProgramsIntent
- LaundryProgramsByCategoryIntent
- LaundrySearchProgramsIntent
- AlfredExitIntent

Temporary backend aliases are supported for older test names.

- LastLaundryIntent
- StartLaundryIntent
- StopLaundryIntent

## Laundry Catalog

The real washing machine catalog is owned locally and used as the source of truth for voice UX.

The catalog contains:

- internal hOn program code
- English/raw program name
- Italian display name
- categories
- program parameters
- default parameter values

The bridge uses the catalog to map an Italian voice name to a validated internal hOn program code.

Sanitized catalog shape:

- code: iot_wash_example_program
- name: Example Program
- name_it: Programma esempio
- categories: example
- parameters:
  - temp default: 40
  - spinSpeed default: 1200

## Start Program Safety Model

Laundry start is not based on free text.

The bridge only starts a program when all of these conditions are true:

- the washing machine is connected
- remote control is enabled
- no cycle appears to be running
- the requested program exists in the validated local catalog
- the internal hOn program code is known
- default parameters are available or safely derived
- the command is sent through the Home Assistant wrapper script

Unknown program names are rejected.

No fuzzy matching is used for appliance control.

Deterministic normalization is allowed for controlled voice variants, for example:

- Bianco perfetto + Vapore
- bianco perfetto con vapore
- programma bianco perfetto più vapore

These can map to the same validated catalog entry only when the normalized alias is derived from the catalog.

## Home Assistant Script Wrapper

The FastAPI bridge does not directly own the physical device action.

The split is intentional:

- Python/FastAPI owns validation, catalog lookup and voice request handling.
- Home Assistant owns the physical hOn command wrapper and device targeting.

This keeps device targeting visible in Home Assistant and avoids duplicated control logic.

Sanitized wrapper shape:

- script: Laundry - Start program
- input: program_code
- input: program_parameters
- action: hOn start program
- target: washing machine entity
- data:
  - device: sanitized hOn internal device identifier
  - program: selected validated program code
  - parameters: selected validated default parameters

## Start/Stop UX Decision

Initial testing used long polling after start and stop commands.

That was technically useful but poor for Alexa UX, because hOn sensor updates can lag and Alexa sessions become awkward when a command takes too long.

The production voice UX now uses quick command dispatch:

Alfred sends the command
-> Alfred replies quickly
-> user asks for status after a few seconds

Example response:

"I sent the start command. The washing machine may take a few seconds to update its status."

The status intent remains the source of truth for post-command verification.

## Observed hOn Behavior

Testing showed several important integration behaviors:

- hOn sensor updates can lag after start and stop operations.
- A stop command can physically stop the washing machine before Home Assistant sensors refresh.
- Repeated start/stop tests can temporarily make washing machine entities unavailable.
- The integration may expose program/status data later than the physical machine changes state.

Because of this, Alfred must not claim final start or stop success from dispatch alone.

## Session UX

Alfred sessions remain open after functional responses.

This allows follow-up commands without reopening the skill.

Example session:

- User opens Alfred.
- Alfred welcomes the user and keeps the session open.
- User asks which programs are available for whites.
- Alfred lists the matching programs and keeps the session open.
- User asks to start a validated program.
- Alfred sends the command and keeps the session open.
- User asks for washing machine status.
- Alfred reports the current status.
- User thanks Alfred.
- Alfred closes the session.

Functional intents use `shouldEndSession = false`.

Exit intents use `shouldEndSession = true`.

The explicit exit intent supports phrases such as:

- thanks Alfred
- that's enough
- close
- I don't need anything else

## Issues Found

### Wrong endpoint path

Alexa must call the Alexa-compatible route:

- https://PUBLIC-ALEXA-BRIDGE-HOST/alexa

not the human/API status route.

### Wildcard certificate setting

When the public HTTPS hostname uses a wildcard certificate, the Alexa Developer Console endpoint SSL option must be set to the wildcard certificate option.

### Template intent interception

The starter template intent intercepted laundry utterances before the intended laundry intent was fully configured.

The final model should remove or empty template intents that are no longer used.

### Wrong device target during script setup

During start command validation, a copied Home Assistant device target pointed to the wrong device.

The fix was to make the Home Assistant script target the washing machine entity/device explicitly and keep that device action visible inside Home Assistant.

### Long polling is not suitable for Alexa sessions

Long validation loops are useful for backend testing, but poor for live voice UX.

The Alexa-facing command handlers now respond quickly and ask the user to query status after a few seconds.

### Alexa routed catalog phrases to search intent

Some natural phrases such as "programs for whites" were routed to a search-style intent instead of the category intent.

The backend accepts this routing and treats category-compatible search values as category lookups.

## Security Notes

Do not commit:

- real public endpoint
- Home Assistant URL
- Home Assistant token
- Alexa debug payloads
- Alexa user IDs
- Alexa device IDs
- Alexa access tokens
- Home Assistant device IDs
- hOn internal device identifiers
- private hostnames or IP addresses

## 2026-06-07 Extension - Voice UX and Async Appliance Verification

### Goal

Improve the laundry Custom Skill from a command dispatcher into a cautious voice workflow that can handle slow and generic appliance state updates.

### What changed

- Added reprompts to keep Alfred sessions open after functional responses.
- Added launch and fallback guidance for "che cosa puoi fare".
- Implemented true keyword search across the laundry program catalog.
- Added voice pagination for long result lists.
- Added program-name fallback when hOn reports generic names.
- Added asynchronous start and stop verification.
- Refreshed hOn state before every verification attempt.
- Added manual-verification fallback if confirmation is not reached within the verification window.

### Async verification behavior

Alfred no longer claims success from dispatch alone.

The bridge now:

1. sends the command,
2. replies immediately,
3. verifies in the background,
4. refreshes hOn before each check,
5. polls every 15 seconds up to 90 seconds,
6. notifies only after the expected state is observed,
7. asks for manual verification if no confirmation arrives.

### Verified results

Start behavior:

- first check not confirmed
- later check confirmed the washer as running
- notification included requested program and estimated remaining time

Stop behavior:

- early checks still saw the washer running
- later check confirmed the washer as stopped
- notification reported the washer as stopped

### Lesson

For physical appliance control, command dispatch and confirmed state must be treated as separate events.

This makes the voice assistant more trustworthy and avoids false success messages.
