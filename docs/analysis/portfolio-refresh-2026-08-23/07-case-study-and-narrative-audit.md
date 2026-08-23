# 07 — Case-study and Narrative Audit

## Purpose

Review the portfolio-facing examples after the architecture/governance refresh and decide which documents are current-state narrative, which remain useful historical case studies, and which maturity labels need correction.

## Inventory reviewed

Primary case studies:

- `alexa-custom-skill-laundry-mvp.md`
- `laundry-voice-mvp.md`
- `alexa-https-bridge.md`
- `bravia-dolby-safe-power.md`

Portfolio narrative:

- `SHOWCASE.md`
- `PROJECT_STATUS.md`
- `INTEGRATIONS.md`
- `SKILLS_MATRIX.md`
- `PORTFOLIO_REVIEW.md`
- `docs/README.md`

## Laundry case-study finding

The laundry material remains one of the strongest portfolio examples because it captures a real engineering lesson: command dispatch and confirmed physical state are different events.

The newer Custom Skill case study contains the useful progression from simple command handling to asynchronous verification.

However, parts of the older laundry/HTTPS material describe intermediate architecture and future work that later evolved into the private Alfred/Hermes/frontend model.

Decision:

- preserve those documents as historical engineering steps;
- add clear context when they describe an earlier architecture;
- do not silently rewrite the historical sequence as though it had always used the current architecture.

## Alexa HTTPS bridge finding

The dedicated FastAPI/Cloudflare bridge was a meaningful intermediate architecture and remains useful as a case study in secure public integration design.

It must not be read as the complete current Alfred architecture.

Decision: retain it as an earlier integration milestone and point readers toward the current architecture docs for present ownership boundaries.

## Home-theater finding

The Bravia/Dolby safe-power workflow remains a valid current case study because the core lesson is Home Assistant-owned physical orchestration, state-based sequencing and race-condition mitigation.

Its current text is small but architecturally clean.

## Energy maturity finding

Authoritative development evidence describes the local energy pipeline as stable and usable but not yet definitively validated over all required operating conditions.

Portfolio maturity should therefore be **In testing**, not production-ready or generally available.

Useful public lessons include:

- local telemetry pipeline design;
- MQTT separation of directional power flows;
- state/sign validation;
- comparing reconstructed energy balance with independent measurements.

Private operational details remain excluded.

## Presence maturity finding

Presence work is intentionally parked after private experiments showed that the available BLE signals were not reliable enough to become an authoritative occupancy source.

The design goal has also narrowed toward minimal, privacy-preserving `occupied / empty / uncertain` semantics rather than room-level tracking.

Portfolio maturity should therefore be **Designed to enable**.

## Media / Charon finding

The public portfolio should describe Charon through safe concepts:

- media identity and discovery;
- Plex integration;
- playback/lifecycle reasoning;
- quality and availability policy;
- observed-state verification;
- domain events and communication handoff.

Private acquisition implementation and identifying details remain outside the public portfolio.

The public narrative should focus on domain ownership and reusable engineering lessons rather than private provider mechanics.

## Proactive communication finding

Osvaldo is mature enough to be a useful portfolio concept, but the public value is the policy model rather than household implementation details.

The safe narrative is:

`domain event -> communication policy -> delivery framework -> provider/frontend`

with explicit distinction between unsolicited proactive communication and user-requested asynchronous replies.

## Documentation-index finding

`docs/README.md` still treated the retired private ledger as an active “Planning and Checkout” destination and mentioned “Sanitized Python examples”. Both are inconsistent with the current public boundary.

Decision:

- move the retired-ledger documents into historical/archival framing;
- add ADR-011 and the DOC-003 analysis trail to the index;
- remove wording that suggests private-derived readable code is part of the intended portfolio surface.

## Current-state status document finding

`PROJECT_STATUS.md` is stale and still reports Wilfred `0.2.0.dev0` preparing Public Alpha.

It must be refreshed before DOC-003 can close.

## Showcase finding

`SHOWCASE.md` mixes validated work, work-in-progress tracks and future concepts using older maturity terms.

It should be rewritten around the current evidence vocabulary:

- **Available** for public reusable components;
- **In testing** for private validated work not yet public;
- **Designed to enable** for architectural directions or parked experiments.

## Result

The remaining DOC-003 work is now concrete:

1. refresh `PROJECT_STATUS.md`;
2. refresh `SHOWCASE.md`;
3. refresh `docs/README.md` and portfolio navigation;
4. add historical/current context to the older Alexa/laundry bridge case studies where needed;
5. run repository-wide public-safety, stale-reference and link audits;
6. integrate only after the final diff is clean.
