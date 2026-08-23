# Historical Records

This page is the public index for historical engineering records preserved in the Keriol Home portfolio.

Historical material is intentionally retained because the project did not arrive at its current architecture in one jump. The records show earlier assumptions, intermediate designs, experiments, migration points and superseded governance models.

They are **evidence of the project at a point in time**, not current implementation or current development-state authority.

## How to Read Historical Material

Use this rule throughout the portfolio:

- **Current documentation** describes the architecture, maturity and governance that apply now.
- **Historical records** describe what was implemented, believed, tested or planned when the record was created.
- A historical record may contain names, ownership models, versions or architecture that were later superseded.
- Historical material must not override GitHub Issues, current Git `main`, release evidence or live-system evidence.
- Historical records are preserved rather than silently rewritten to make the past resemble the present.

For current architecture start from [Documentation Index](README.md), [Architecture Overview](architecture/overview.md) and [Current Public Project Model](project-model/project-model-public.md).

---

## 1. Pre-Alfred History

The `history/` directory contains material from before the current Butler architecture existed.

- [April 2026 pre-Alfred home-automation model](../history/home-automation-model-2026-04-pre-alfred-agent.md)

This record is useful for understanding the original Home Assistant-centered system before Alfred emerged as a coherent private Butler layer.

---

## 2. Engineering Worklog

`WORKLOG/` is the chronological engineering record for the structured portfolio phase.

### Monthly records

- [April 2026](../WORKLOG/2026-04.md) — reliability, home-theater and access foundations.
- [May 2026](../WORKLOG/2026-05.md) — energy telemetry, BLE presence and creation of the public portfolio.
- [June 2026](../WORKLOG/2026-06.md) — voice, appliance and integration work during the early Alfred evolution.
- [July 2026](../WORKLOG/2026-07.md) — Alfred notification, speech and domain-architecture refactoring.

See the [Worklog index](../WORKLOG/README.md) for its canonical structure.

### Focused historical reports

- [Laundry voice MVP](../WORKLOG/details/2026-05-31-laundry-voice-mvp.md)
- [Laundry dynamic Assist extension](../WORKLOG/details/2026-05-31-laundry-dynamic-assist-extension.md)
- [Alexa HTTPS bridge MVP](../WORKLOG/details/2026-06-01-alexa-https-bridge-mvp.md)
- [Alfred agent MVP](../WORKLOG/details/2026-07-alfred-agent-mvp.md)

These reports preserve intermediate system shapes and implementation lessons. They should not be read as descriptions of the current Butler ownership model.

### Milestone records

- [v0.2.0 milestone record, first snapshot](../WORKLOG/milestones/milestone-v0.2.0-20260704-131246.md)
- [v0.2.0 milestone record, follow-up snapshot](../WORKLOG/milestones/milestone-v0.2.0-20260704-132529.md)

Milestone records preserve evidence around a historical checkpoint. Current public release state is documented separately and comes from current Git/tag/release evidence.

---

## 3. Dated Project-Model Snapshots

The `docs/project-model/` directory contains dated public-safe snapshots created while the architecture and governance model were evolving.

Browse the [project-model archive](project-model/) and its [maintenance README](project-model/README.md).

The active model is:

- [Current Public Project Model](project-model/project-model-public.md)

Dated files such as `project-model-public-YYYY-MM-DD.md` are immutable historical snapshots. They may mention versions, ownership or planning mechanisms that were correct at the time but are no longer current.

---

## 4. Architecture Decision Record History

ADRs preserve decisions and their context. A later ADR may supersede an earlier one without deleting the earlier record.

### Current or still-relevant decisions

- [ADR-001 — Home Assistant as Orchestrator](adr/ADR-001-home-assistant-as-orchestrator.md)
- [ADR-002 — MQTT as Event Bus](adr/ADR-002-mqtt-as-event-bus.md)
- [ADR-003 — Tailscale for Private Access](adr/ADR-003-tailscale-for-private-access.md)
- [ADR-004 — Cloudflare Tunnel for Public Integrations](adr/ADR-004-cloudflare-tunnel-for-public-integrations.md)
- [ADR-005 — AI-Assisted Development](adr/ADR-005-ai-assisted-development.md)
- [ADR-006 — Proactive Notification Policy](adr/ADR-006-proactive-notification-policy.md)
- [ADR-007 — Alfred Agent and Tool Registry](adr/ADR-007-alfred-agent-tool-registry.md)
- [ADR-008 — Butler Core, Wilfred and Alfred Layering](adr/ADR-008-butler-core-wilfred-alfred-layering.md)
- [ADR-010 — Public Portfolio Documentation Boundary](adr/ADR-010-public-portfolio-documentation-boundary.md)
- [ADR-011 — GitHub as Development Source of Truth](adr/ADR-011-github-development-source-of-truth.md)

### Superseded governance record

- [ADR-009 — Development State Sources of Truth](adr/ADR-009-development-state-sources-of-truth.md)

ADR-009 records the former ledger-based development-state model. ADR-011 supersedes it for current development governance.

---

## 5. Retired Development-Process Records

The former private development ledger is no longer part of the active Butler development workflow, but its public-safe analysis is retained as historical process evidence.

- [Historical ledger analysis](analysis/umberto-development-ledger.md)
- [Historical checkout flow](diagrams/umberto-checkout-flow.md)

These documents are explicitly superseded and must not be used to infer current task status, current architecture or current workflow ownership.

---

## 6. Historical and Intermediate Case Studies

Some case studies are intentionally preserved because they demonstrate how the present architecture was reached.

- [Local-first Laundry Voice MVP](case-studies/laundry-voice-mvp.md)
- [Alexa HTTPS Bridge MVP](case-studies/alexa-https-bridge.md)
- [Alexa Custom Skill Laundry MVP](case-studies/alexa-custom-skill-laundry-mvp.md)
- [Bravia and Dolby Safe Power](case-studies/bravia-dolby-safe-power.md)

Early bridge and laundry documents are intermediate architecture records. Their lessons remain relevant, but current owner boundaries are defined by the current architecture documents.

---

## 7. DOC-003 Refresh Analysis Trail

The 2026-08-23 portfolio refresh itself is part of the historical engineering record because it documents how the portfolio was reconciled with the modern Butler architecture.

- [DOC-003 analysis trail](analysis/portfolio-refresh-2026-08-23/README.md)

It includes baseline drift, governance, ownership, maturity, public/private sanitization, delivery/frontend boundaries, rejected alternatives, case-study review and final safety audit.

---

## Historical Record Policy

Historical records should be:

1. retained when they explain meaningful architectural or engineering evolution;
2. dated or clearly marked as historical/intermediate/superseded;
3. linked from this index when they are useful to understanding project evolution;
4. left unchanged when preserving their original meaning is important;
5. annotated at the index or wrapper level when current readers need supersession context;
6. kept public-safe under the same sanitization boundary as current documentation.

Historical records are not a second source of truth. They are the project memory.
