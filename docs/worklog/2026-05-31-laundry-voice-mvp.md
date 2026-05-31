# 2026-05-31 - Laundry voice query MVP

## Goal

Build a reliable local-first voice flow for washing machine status and program catalog queries.

## Completed

- Validated Home Assistant Assist intent for washing machine runtime status.
- Created Python helpers for washing machine runtime status and program catalog queries.
- Extracted hOn washing machine program catalog from generated program detail notifications.
- Added Italian program names using local hOn translation files.
- Added Echo Pop TTS announcements through Home Assistant notify service.
- Moved AdGuard Home UI from host port 80 to host port 3000.
- Enabled Emulated Hue on host port 80 for local Alexa-to-Home-Assistant triggers.
- Created virtual Alexa triggers:
  - Washing machine status
  - White laundry programs
- Validated Alexa routine flow:
  - Alexa voice command
  - Emulated Hue virtual input
  - Home Assistant automation
  - Python helper/catalog
  - Echo spoken response
- Avoided native hOn Alexa catalog responses because they returned unreliable/wrong program mappings.

## Key lesson

Vendor voice integrations can expose ambiguous or incorrect program mappings.  
A local Home Assistant orchestration layer gives better control, safer mappings, and predictable voice responses.

## Public-safety notes

- No tokens committed.
- No real device IDs committed.
- No personal entity names committed.
- No public endpoints committed.
- Examples use placeholders.
