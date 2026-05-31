# 2026-05-31 - Laundry dynamic Assist catalog extension

## Completed

- Extended the washing machine catalog helper to support dynamic Home Assistant Assist queries.
- Assist can now answer free-form catalog questions such as:
  - "che programmi ho per le macchie ostinate?"
  - "che programmi posso usare per colorati?"
- Added wildcard-based Assist sentence handling so the search term is passed as a dynamic query parameter.
- Validated the local Italian hOn catalog as the source of truth for program recommendations.
- Added a dedicated stains category for stain-related programs.
- Fixed an earlier categorization issue where stain programs were incorrectly grouped with pet-related programs.
- Confirmed that the catalog can be searched in Italian using localized program names.
- Started program detail support from catalog data:
  - temperature default when available;
  - spin speed default when available;
  - expected options such as prewash, night mode, extra rinses and water-plus.
- Clarified that Assist catalog details describe default/available program metadata, not voice-editable runtime parameters.

## Validated examples

- "che programmi ho per le macchie ostinate?"
  - returns stain-related programs from the local catalog.

- "dammi i dettagli di bianco perfetto con vapore"
  - returns default temperature, default spin speed and expected options from the catalog.

## Decisions

- Do not create one Alexa/Emulated Hue trigger per program category.
- Keep Emulated Hue for simple trigger-style routines.
- Use Home Assistant Assist as the dynamic local query layer.
- Next Alexa evolution should reuse the same Python catalog helper instead of duplicating logic.
- Vendor/native hOn Alexa answers should be avoided for program catalog questions because program mapping can be unreliable.

## Tomorrow handoff

Goal: make Alexa answer the same dynamic catalog questions currently handled by Assist.

Candidate path:
- Custom Alexa Skill or HTTPS intent bridge.
- Reuse the existing Python catalog/query helper.
- Preserve the same Italian catalog names and safe internal code mapping.
- Keep Emulated Hue only for simple routines like washing machine status.
