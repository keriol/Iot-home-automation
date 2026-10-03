---
title: Project History
kind: history-index
scope: public
status: current
---

# Project History

Keriol Home and the Butler ecosystem did not appear fully formed.

This section preserves the important transitions that explain why the current
architecture looks the way it does. Historical material is evidence of its time,
not current task, release or runtime authority.

## Timeline

### April 2026 — pre-Alfred smart home

The project was still primarily a Home Assistant-centered automation system.
Voice integration, Plex control, appliance integration, home-theater sequencing,
remote access and local-first engineering were already emerging themes.

The original private/local project model belongs to this era.

### May–June 2026 — portfolio, voice and appliance workflows

The system gained public-safe portfolio documentation, energy/presence
experiments, laundry workflows and Alexa/HTTPS integration work.

Important engineering lessons started to emerge around ownership boundaries and
the difference between command dispatch and physical success.

### July 2026 — Alfred Agent MVP

Alfred evolved into an agent-oriented Butler with registered tools,
deterministic-first routing, permissions, confirmation and AI fallback.

The historical v0.2.0 milestone captures this transition.

### August 2026 — reusable Butler architecture

Butler Core, Wilfred and reusable plugins became explicit independent ownership
boundaries. Alfred and Wilfred became sibling runtimes rather than a
Core -> Wilfred -> Alfred runtime chain.

GitHub replaced the former development ledger as the development source of
truth. Historical Umberto material remains archival.

### September–October 2026 — Ignition network

Bifröst, Midgard, Butler-owned Asgard and Butler Interphone turned the Butler
architecture into a real external-client communication network.

IGNITION-001 proved:

```text
Interphone -> Bifröst -> Midgard -> Butler Core -> HAP -> Home Assistant
Interphone -> Bifröst -> Midgard -> Asgard -> Alfred
```

The release/proving cycle established request correlation, authoritative Butler
identity, client-safe self-description, routing observability and
READ -> ACTION -> READ -> VERIFY as documented network behavior.

See [IGNITION-001](../milestones/ignition-001.md) and
[Ignition Engineering Lessons](../lessons-learned/ignition-001-engineering-lessons.md).

### October 2026 — documentation becomes the project model

The final compact local project model was retired as an active authority.

The versioned documentation corpus now carries the durable project model:

- architecture and API ownership;
- current release baselines;
- ADRs and engineering decisions;
- compatibility milestones and lessons;
- agent-friendly navigation;
- historical evolution.

See [Retirement of the Local Project Model](local-project-model-retirement-2026-10-03.md).

## Preserved repository records

The repository also retains older records that are intentionally not rewritten:

- `WORKLOG/` monthly engineering records;
- `WORKLOG/details/` focused historical reports;
- `WORKLOG/milestones/` historical milestone evidence;
- dated `docs/project-model/project-model-public-YYYY-MM-DD.md` snapshots;
- superseded ADRs and analysis trails;
- the pre-Alfred material under `history/`.

These files may use obsolete terminology, ownership models or versions. That is
part of their historical value.

## Reading rule

Use current architecture/API/project-status documentation for current claims.

Use historical records to understand evolution.

Use GitHub Issues for active work, releases/tags/workflows for release evidence,
and live systems for runtime truth.
