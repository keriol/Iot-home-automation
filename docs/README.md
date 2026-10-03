# Documentation Index

## Start Here

- [Agent Guide](agent/index.md)
- [Portfolio README](../README.md)
- [Project Showcase](SHOWCASE.md)
- [Project Status](PROJECT_STATUS.md)
- [Project Model](PROJECT_MODEL.md)
- [Compact Public Context](project-model/project-model-public.md)
- [Roadmap](../ROADMAP.md)
- [Project History](history/index.md)
- [Historical Records](HISTORICAL_RECORDS.md)

## Butler Ecosystem

- [Architecture Overview](architecture/overview.md)
- [Butler Communication Model](architecture/communication-model.md)
- [Butler Client API](api/index.md)
  - [Bifröst API](api/bifrost.md)
- [Midgard](architecture/midgard.md)
- [Asgard](architecture/asgard.md)
- [Node Manifest and Self-Description](architecture/node-manifest.md)
- [Routing Failures and Observability](architecture/routing-failures-and-observability.md)
- [IGNITION-001 - Butler-to-Android Network Baseline](milestones/ignition-001.md)
- [IGNITION-001 Engineering Lessons](lessons-learned/ignition-001-engineering-lessons.md)
- [Alfred Ecosystem](architecture/alfred-ecosystem.md)
- [Alfred Proving Ground](architecture/alfred-proving-ground.md)
- [Architecture Diagram](diagrams/architecture.md)
- [Alfred Ecosystem Flow](diagrams/alfred-ecosystem-flow.md)
- [Docker Stack](architecture/docker-stack.md)

## Architecture Decision Records

Current governance and architecture:

- [ADR-012 - Sibling Butler Runtimes and Independent Platform Plugins](adr/ADR-012-sibling-runtimes-and-independent-platform-plugins.md)
- [ADR-011 - GitHub as Development Source of Truth](adr/ADR-011-github-development-source-of-truth.md)
- [ADR-010 - Public Portfolio Documentation Boundary](adr/ADR-010-public-portfolio-documentation-boundary.md)

Foundational ADRs:

- [ADR-001 - Home Assistant as Orchestrator](adr/ADR-001-home-assistant-as-orchestrator.md)
- [ADR-002 - MQTT as Event Bus](adr/ADR-002-mqtt-as-event-bus.md)
- [ADR-003 - Tailscale for Private Access](adr/ADR-003-tailscale-for-private-access.md)
- [ADR-004 - Cloudflare Tunnel for Public Integrations](adr/ADR-004-cloudflare-tunnel-for-public-integrations.md)
- [ADR-005 - AI-Assisted Development Workflow](adr/ADR-005-ai-assisted-development.md)
- [ADR-006 - Proactive Notification Policy](adr/ADR-006-proactive-notification-policy.md)
- [ADR-007 - Alfred Agent and Tool Registry](adr/ADR-007-alfred-agent-tool-registry.md)

Historical / superseded ADRs:

- [ADR-008 - Butler Core, Wilfred and Alfred Layering](adr/ADR-008-butler-core-wilfred-alfred-layering.md), retained as the historical extraction-stage model and superseded by ADR-012 for the current runtime relationship.
- [ADR-009 - Development State Sources of Truth](adr/ADR-009-development-state-sources-of-truth.md), retained as the historical record of the former ledger-based model and superseded by ADR-011 for current development-state ownership.

See [Historical Records](HISTORICAL_RECORDS.md) for the ADR lifecycle in the wider project chronology.

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

The current web-safe historical entrypoint is:

- **[Project History](history/index.md)**

The repository also retains the broader repo-centric historical index:

- **[Historical Records](HISTORICAL_RECORDS.md)**

It maps:

- the pre-Alfred model under `history/`;
- monthly worklogs from April through July 2026;
- focused worklog reports and milestone snapshots;
- dated public project-model snapshots;
- ADR history and supersession;
- retired development-process records;
- historical/intermediate case studies;
- the DOC-003 analysis trail itself;
- IGNITION-001 and the Bifröst/Midgard/Asgard communication era;
- the 2026-10-03 retirement of the local compact project model.

Historical records are intentionally preserved rather than rewritten to match current architecture. They are project memory, not current development-state authority.

## Public Boundary

This documentation repository contains public-safe architecture, ADRs, diagrams, analyses, case studies and engineering lessons.

It is not a readable mirror of the private Alfred implementation. Private source, private endpoints, sensitive operational identifiers, credentials, private acquisition implementation and other non-public deployment details remain excluded.


## Documentation Site

The public documentation site is generated from this repository with MkDocs
Material and GitHub Pages.

Canonical source remains the Markdown under `docs/`.

Local validation:

```bash
python -m pip install -r requirements-docs.txt
python scripts/check_docs_source.py
mkdocs build --strict
python scripts/check_docs_build.py
```

The GitHub Actions documentation workflow runs the same source/build checks on
documentation pull requests and publishes the built `site/` artifact from
`main`.

Unlinked easter-egg pages may exist in the generated site, but they must remain
public-safe and must not become a second documentation source of truth.
