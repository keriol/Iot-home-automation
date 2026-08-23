# Project Metrics

## Purpose

This document tracks **public-safe engineering indicators**, not volatile runtime counts.

Live container counts, automation counts, entity counts and other operational statistics change frequently and belong to live systems rather than portfolio documentation.

## Public Butler Baseline

| Component | Evidence-backed state |
|---|---|
| Butler Core | `0.1.4` released baseline; `main` on `0.1.5.dev0` development line |
| Wilfred | `0.2.1` current Public Alpha |
| wilfred-home-assistant | `0.1.0.dev0` development line |
| Alfred | `0.4.0` private released baseline; later private development continues |

## Capability Maturity Snapshot

| Area | Portfolio maturity | Notes |
|---|---|---|
| Butler execution foundations | Available | Public Core/Wilfred foundations with private real-world validation |
| Verified physical actions | Available + In testing | READ -> ACTION -> READ -> VERIFY exercised against real devices |
| Voice interaction | In testing | Private Alexa frontend and Alfred interaction path |
| Proactive communication | In testing | Osvaldo policy exercised privately |
| Delivery abstraction | In testing | Hermes provider/plugin boundary exercised privately |
| Media intelligence | In testing | Charon domain/lifecycle concepts validated privately |
| Laundry workflow | In testing | Controlled actions, catalog handling and async verification exercised privately |
| Energy telemetry | In testing | Stable and usable private telemetry, still awaiting definitive long-window validation |
| Presence | Designed to enable | Privacy-conscious occupancy direction; current BLE path is not authoritative |
| Climate | In testing | Sensing and control strategies remain private validation work |
| Home theater safe power | In testing | Private Home Assistant workflow validated in real use |

## Engineering Evidence Indicators

The portfolio demonstrates:

- provider-neutral Butler foundations;
- deterministic-first request handling;
- capability/domain ownership boundaries;
- explicit confirmation and safety boundaries;
- physical post-action verification;
- replaceable frontends;
- policy separated from delivery;
- public/private extraction discipline;
- GitHub-based development governance;
- dated analysis trails for significant portfolio refreshes.

## Documentation Indicators

Current public documentation includes:

- architecture overview and diagrams;
- current public project model;
- ADRs, including current GitHub source-of-truth governance;
- case studies and historical evolution notes;
- public-safety and sanitization rules;
- analysis trail for the 2026-08-23 portfolio refresh;
- roadmap and current project status.

## Measurement Rule

A metric belongs here only when it remains meaningful without continuous runtime synchronization.

Operational truth such as service health, live entity counts, device availability or exact deployment inventory must be verified against the live systems when needed and is not treated as durable portfolio state.
