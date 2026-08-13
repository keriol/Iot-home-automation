# Project Model Changelog

## 2026-08-13 - Public portfolio documentation boundary

### Changed

- Stop publishing readable private-derived implementation examples.
- Keep the portfolio focused on architecture, evolution, decisions and capability maturity.
- Route genuinely reusable public code to Butler Core, Wilfred or official plugin repositories.
- Retire the old public-model template and milestone checkout pipeline.

## 2026-08-13 - Project model becomes derived context

### Changed

- Retire the project model as a development-state authority.
- Treat the current public file as a derived architectural context snapshot.
- Keep Git, Umberto and live runtime as separate sources of truth.
- Add public repository reference map and technology-stack context.
- Make the private proving ground and plugin graduation path explicit.
- Preserve the historical `project-model` filenames for compatibility.

## 2026-08-13 - Butler runtime layering refresh

### Changed

- Document Butler Core as the provider-neutral shared foundation.
- Document Wilfred as the reusable public Butler runtime.
- Document Alfred as the private Keriol deployment built on the reusable runtime.
- Add Public / Private validated / Candidate maturity labels.
- Clarify Home Assistant ownership and READ -> ACTION -> READ -> VERIFY.
- Remove the obsolete local-only Alfred repository assumption from current documentation.
- Keep historical snapshots unchanged.

## v0.2.0 - Alfred Agent MVP documentation baseline

This milestone marks the transition from a collection of smart-home automations and voice workflows to an agent-oriented architecture.

### Added

- Alfred Agent MVP documented as current project baseline.
- Tool Registry architecture documented.
- Deterministic-first routing documented.
- AI planner fallback documented.
- READ/ACTION/DANGEROUS permission model documented.
- Private/public model split documented.
- Historical pre-Alfred model archived.
- Public model export workflow preserved.
- Milestone-specific documentation added.
- Model validation tooling added.
- Architecture diagrams added.

### Current registered Alfred READ tool domains

- Laundry status.
- Laundry catalog search.
- Server status.
- Internal reporting summaries.

### Still pending

- Plex READ tool.
- Alexa free-text bridge to AlfredCore.ask.
- Laundry ACTION tools with confirmation and verification.
- Home Assistant notification tool.
- Dashboard for tools, logs, AI usage and health.
- Memory JSON -> SQLite.
