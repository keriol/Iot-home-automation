# Portfolio Review Guide

## Purpose

This guide helps readers navigate the portfolio without confusing current architecture, private proving-ground evidence and historical records.

## If You Have 5 Minutes

Start with:

1. [Portfolio README](../README.md)
2. [Project Showcase](SHOWCASE.md)
3. [Architecture Overview](architecture/overview.md)
4. [Current Public Project Model](project-model/project-model-public.md)
5. [Skills Matrix](SKILLS_MATRIX.md)

These pages describe the current public-safe model and evidence-backed maturity.

## If You Are Interested in Architecture

Read:

- [Architecture Overview](architecture/overview.md)
- [Alfred Ecosystem](architecture/alfred-ecosystem.md)
- [Alfred Proving Ground](architecture/alfred-proving-ground.md)
- [Architecture Diagram](diagrams/architecture.md)
- [ADR-012 — Sibling Butler Runtimes and Independent Platform Plugins](adr/ADR-012-sibling-runtimes-and-independent-platform-plugins.md)
- [ADR-011 — GitHub as Development Source of Truth](adr/ADR-011-github-development-source-of-truth.md)

The current architecture uses Butler Core as the shared provider-neutral foundation. Wilfred and Alfred are sibling runtimes, while reusable platform integrations such as Home Assistant Plugin can be consumed independently by either runtime. Home Assistant remains the owner of physical orchestration and device integrations.

ADR-008 is retained as the historical record of the previous `Butler Core -> Wilfred -> Alfred` layering and is superseded by ADR-012 for current runtime dependency boundaries.

## If You Are Interested in IoT and Integrations

Read:

- [Integrations](INTEGRATIONS.md)
- [Hardware Inventory](HARDWARE.md)
- [Energy Flow](diagrams/energy-flow.md)
- [Presence Candidate Flow](diagrams/presence-flow.md)
- [Bravia and Dolby Safe Power](case-studies/bravia-dolby-safe-power.md)

Remember that integration presence is not equivalent to public Butler capability availability. Maturity labels distinguish `Available`, `In testing` and `Designed to enable`.

## If You Are Interested in Verified Automation

Start with the laundry material:

- [Alexa Custom Skill Laundry MVP](case-studies/alexa-custom-skill-laundry-mvp.md)
- [Laundry Portfolio Analysis](analysis/alfred-laundry-voice-ux-and-async-verification.md)
- [Laundry Lessons Learned](lessons-learned/alfred-laundry-voice-ux-and-async-verification.md)
- [Async Verification Diagram](diagrams/alexa-laundry-async-verification.md)

The central engineering lesson is:

`READ -> ACTION -> READ -> VERIFY`

Command dispatch alone is not accepted as proof of physical success.

## If You Are Interested in Software Engineering

Read:

- [AI Collaboration](AI_COLLABORATION.md)
- [AI-Assisted Development Flow](diagrams/ai-assisted-development-flow.md)
- [Project Status](PROJECT_STATUS.md)
- [Metrics](METRICS.md)
- [Lessons Learned](../LESSONS_LEARNED.md)
- [DOC-003 Analysis Trail](analysis/portfolio-refresh-2026-08-23/README.md)

Development-state authority lives in GitHub Issues, Git, release evidence and live systems according to responsibility. Portfolio documents are derived public-safe context.

## If You Want the Project History

Read:

- [Historical Records](HISTORICAL_RECORDS.md)
- [Project Origin](PROJECT_ORIGIN.md)
- [Worklog](../WORKLOG/README.md)

Historical records preserve previous assumptions, intermediate designs and superseded governance. They are project memory, not current-state authority.

## Main Engineering Themes

This portfolio demonstrates:

- local-first smart-home architecture;
- clear ownership between Home Assistant, integrations/providers and Butler capabilities;
- provider-neutral Core contracts shared by sibling Butler runtimes;
- reusable platform plugins that do not force runtime-to-runtime dependencies;
- deterministic-first resolution with bounded AI fallback;
- verified physical-action workflows;
- MQTT-based telemetry and event boundaries;
- private proving-ground validation before public extraction;
- provider/frontend separation, including Hermes/Alexa delivery boundaries;
- evidence-backed maturity labels;
- AI-assisted engineering under human decision and validation ownership;
- public-safe documentation that preserves both current architecture and historical reasoning.

## Public Boundary

The repository intentionally publishes architecture, decisions, analysis, diagrams, maturity and lessons rather than readable private implementation.

Private Alfred source, private endpoints, credentials, unnecessary operational identifiers, machine-specific deployment details and private media-acquisition implementation remain outside the public portfolio.
