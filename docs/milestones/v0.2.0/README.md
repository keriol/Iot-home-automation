# Milestone v0.2.0 - Alfred Agent MVP Documentation Baseline

Date: 2026-07-04  
Status: documented milestone  
Scope: private/public model update, Alfred Agent baseline, diagrams, validation tooling

## Summary

This milestone marks the point where the project stops being only a set of Home Assistant automations and becomes an assistant-oriented platform.

Alfred the Butler is now documented as the AI Agent layer of the smart home.

Core idea:

> Alfred is not the smart-home software. Alfred is the one who knows how to talk to every smart-home service.

## What changed

Before this milestone, the project model mainly described:

- Home Assistant automations.
- Assist voice commands.
- Alexa integrations.
- Media voice control.
- Laundry voice workflows.
- Home theater safe-power logic.
- Early public portfolio structure.

After this milestone, the project model is centered around:

- FastAPI as Alfred API layer.
- Alfred Core.
- Tool Registry.
- Deterministic-first routing.
- AI planner fallback.
- Registered tools only.
- READ/ACTION/DANGEROUS permissions.
- Private/public model split.
- Sanitized public snapshot export.
- Historical archive for superseded model details.

## Implemented Alfred Agent MVP

Implemented:

- Alfred Core.
- Tool Registry.
- Deterministic-first routing.
- AI planner fallback through OpenAI Responses API.
- Domain mismatch guard.
- JSONL request logging.
- FastAPI endpoints:
  - POST /alfred/ask
  - GET /alfred/tools
  - GET /alfred/ai/status

Registered READ tool domains:

- Laundry status.
- Laundry catalog search.
- Server status.
- Internal reporting summaries.

Private implementation note:

- Some internal reporting tools read private generated state and private source files.
- Public documentation must not describe their real data model, real validation rules, private file paths, real names or payload structure.

## Current voice state

Current path:

    Alexa -> Cloudflare -> FastAPI /alexa -> legacy Alexa intent logic

Target path:

    Alexa -> Cloudflare -> FastAPI -> AlfredCore.ask -> Tool Registry -> Tools

The old Alexa flow remains alive. The new Alfred Agent path exists through HTTP endpoints and still needs the generic free-text Alexa bridge.

## Safety principles

- Alfred uses registered tools only.
- Deterministic logic before AI.
- If no suitable tool exists, Alfred must say so.
- READ before ACTION.
- ACTION/DANGEROUS tools require confirmation where appropriate.
- Physical actions require state verification.
- Public documentation must not expose secrets, real endpoints, private paths, raw logs or personal data.
- Public documentation must not expose private event/reporting validation logic.

## Golden rule

Before debugging a tool, plugin or integration that does not answer, first verify that it is actually enabled, loaded and available.

Checklist:

- Is the plugin/integration installed?
- Is it enabled?
- Is it loaded after restart?
- Is it visible in the runtime/tool registry?
- Is the expected endpoint/service reachable?
- Are permissions and credentials configured?
- Are logs showing no call, failed call or rejected call?

Do not complain that a plugin is not answering before checking that the plugin is awake.

## Documentation artifacts

This milestone adds:

- Private project model snapshot.
- Public sanitized project model snapshot.
- Historical pre-Alfred model archive.
- Versioned milestone documentation.
- Mermaid diagrams.
- Python model validator.
- Python model stats generator.
- Milestone checkout script.

## Expected files

- external private source model (validated locally, not published)
- docs/project-model/public-template.md
- docs/project-model/project-model-public.md
- docs/project-model/project-model-public-2026-07-04.md
- docs/project-model/VERSION
- docs/project-model/CHANGELOG.md
- history/home-automation-model-2026-04-pre-alfred-agent.md
- docs/milestones/v0.2.0/README.md
- docs/milestones/v0.2.0/model-stats.md
- docs/milestones/v0.2.0/diagrams/alfred-agent-architecture.mmd
- docs/milestones/v0.2.0/diagrams/tool-permission-flow.mmd
- docs/milestones/v0.2.0/diagrams/checkout-flow.mmd
- scripts/check-project-models.py
- scripts/generate-model-stats.py
- scripts/milestone-checkout.sh

## Credits and folklore

Project catalyst:

- Lorenzo Zini, officially credited as the person who helped trigger this rabbit hole.
- Marco remains merely the executor, operator and occasional cable goblin.

<!-- easter egg: osvaldo_was_here -->

## Next milestones

Likely next versions:

- v0.2.1: Media/Plex READ tool.
- v0.2.2: Alexa free-text bridge to AlfredCore.ask.
- v0.3.0: First safe ACTION tools with confirmation and verification.
