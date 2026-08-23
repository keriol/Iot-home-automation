# Documentation Index

## Start Here

- [Portfolio README](../README.md)
- [Project Showcase](SHOWCASE.md)
- [Project Status](PROJECT_STATUS.md)
- [Current Public Project Model](project-model/project-model-public.md)
- [Roadmap](../ROADMAP.md)

## Architecture

- [Architecture Overview](architecture/overview.md)
- [Alfred Ecosystem](architecture/alfred-ecosystem.md)
- [Alfred Proving Ground](architecture/alfred-proving-ground.md)
- [Architecture Diagram](diagrams/architecture.md)
- [Alfred Ecosystem Flow](diagrams/alfred-ecosystem-flow.md)
- [Docker Stack](architecture/docker-stack.md)

## Architecture Decision Records

Current governance:

- [ADR-011 - GitHub as Development Source of Truth](adr/ADR-011-github-development-source-of-truth.md)
- [ADR-010 - Public Portfolio Documentation Boundary](adr/ADR-010-public-portfolio-documentation-boundary.md)
- [ADR-008 - Butler Core, Wilfred and Alfred Layering](adr/ADR-008-butler-core-wilfred-alfred-layering.md)

Foundational ADRs:

- [ADR-001 - Home Assistant as Orchestrator](adr/ADR-001-home-assistant-as-orchestrator.md)
- [ADR-002 - MQTT as Event Bus](adr/ADR-002-mqtt-as-event-bus.md)
- [ADR-003 - Tailscale for Private Access](adr/ADR-003-tailscale-for-private-access.md)
- [ADR-004 - Cloudflare Tunnel for Public Integrations](adr/ADR-004-cloudflare-tunnel-for-public-integrations.md)
- [ADR-005 - AI-Assisted Development Workflow](adr/ADR-005-ai-assisted-development.md)
- [ADR-006 - Proactive Notification Policy](adr/ADR-006-proactive-notification-policy.md)
- [ADR-007 - Alfred Agent and Tool Registry](adr/ADR-007-alfred-agent-tool-registry.md)

Historical governance:

- [ADR-009 - Development State Sources of Truth](adr/ADR-009-development-state-sources-of-truth.md), retained as the historical record of the former ledger-based model and superseded by ADR-011 for current development-state ownership.

## Case Studies

- [Alexa Custom Skill Laundry MVP](case-studies/alexa-custom-skill-laundry-mvp.md)
- [Local-first Laundry Voice MVP](case-studies/laundry-voice-mvp.md)
- [Alexa HTTPS Bridge MVP](case-studies/alexa-https-bridge.md)
- [Bravia and Dolby Safe Power](case-studies/bravia-dolby-safe-power.md)

The laundry and HTTPS bridge documents preserve important intermediate architecture and engineering lessons. Current ownership boundaries are described by the architecture documents above.

## Analysis

Current DOC-003 portfolio refresh:

- [Portfolio Refresh Analysis Trail](analysis/portfolio-refresh-2026-08-23/README.md)

Selected prior analyses:

- [Alfred Laundry Voice UX and Async Verification](analysis/alfred-laundry-voice-ux-and-async-verification.md)

Historical development-process analysis:

- [Former Development Ledger Analysis](analysis/umberto-development-ledger.md)

Historical analysis is retained for traceability. It does not define current project governance.

## Engineering Lessons and Reference

- [Lessons Learned](../LESSONS_LEARNED.md)
- [Skills Matrix](SKILLS_MATRIX.md)
- [Integrations](INTEGRATIONS.md)
- [Hardware](HARDWARE.md)
- [Metrics](METRICS.md)
- [AI Collaboration](AI_COLLABORATION.md)
- [Project Origin](PROJECT_ORIGIN.md)

## AI-Assisted Development

- [AI Collaboration](AI_COLLABORATION.md)
- [AI-Assisted Development Flow](diagrams/ai-assisted-development-flow.md)
- [ADR-005 - AI-Assisted Development Workflow](adr/ADR-005-ai-assisted-development.md)

AI assists research, troubleshooting, design review, documentation and structured engineering work. Repository evidence and runtime verification remain authoritative according to their responsibility.

## Historical Records

- [May 2026 Worklog](../WORKLOG/2026-05.md)
- [July 2026 Worklog](../WORKLOG/2026-07.md)
- dated project-model snapshots under `history/` and the project-model archive

Historical records are intentionally preserved rather than rewritten to match current architecture.

## Public Boundary

This documentation repository contains public-safe architecture, ADRs, diagrams, analyses, case studies and engineering lessons.

It is not a readable mirror of the private Alfred implementation. Private source, private endpoints, sensitive operational identifiers, credentials, private acquisition implementation and other non-public deployment details remain excluded.
