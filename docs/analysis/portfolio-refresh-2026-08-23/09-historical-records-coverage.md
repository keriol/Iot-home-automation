# 09 — Historical Records Coverage

## Why DOC-003 was reopened

The first DOC-003 integration correctly preserved historical ADRs, worklogs, dated project-model snapshots and retired workflow records, but preservation alone was not enough.

Historical material remained distributed across several directories without one authoritative public index explaining:

- what historical records exist;
- what period they cover;
- which records are intermediate architecture rather than current state;
- which decisions were superseded;
- how a reader should navigate from old records back to the current model.

A portfolio that says "history is preserved" but does not make that history discoverable still leaves an important documentation gap.

## Historical sources found

### Pre-Alfred history

The root `history/` directory contains an April 2026 pre-Alfred home-automation model.

This is important because it shows the system before the current Butler layering emerged.

### Monthly worklogs

`WORKLOG/` contains monthly records for:

- April 2026;
- May 2026;
- June 2026;
- July 2026.

The previous worklog index accidentally omitted June even though the monthly record existed.

### Focused worklog reports

The worklog includes focused records for:

- laundry voice MVP;
- laundry dynamic Assist extension;
- Alexa HTTPS bridge MVP;
- Alfred agent MVP.

These are valuable because they preserve intermediate architectural stages rather than only final outcomes.

### Milestone snapshots

Two historical v0.2.0 milestone records are preserved under `WORKLOG/milestones/`.

They document a point-in-time checkpoint and must not be confused with current release state.

### Dated project-model snapshots

`docs/project-model/` contains a sequence of dated public-safe project-model snapshots.

The active `project-model-public.md` is current. Dated `project-model-public-YYYY-MM-DD.md` files are historical evidence and remain immutable.

### ADR history

ADR-001 through ADR-011 provide an architectural decision history.

Most remain useful foundational/current context. ADR-009 is explicitly superseded by ADR-011 for current development-state governance.

### Retired development-process records

The former ledger analysis and checkout diagram remain useful process history, but are explicitly marked superseded so they cannot be mistaken for current development workflow.

### Historical/intermediate case studies

Early laundry and Alexa bridge documents preserve the path from local trigger experiments toward the current Alfred/Wilfred architecture.

They remain useful precisely because they are not rewritten to pretend the modern architecture existed from the beginning.

## Documentation decision

DOC-003 now adds a first-class `docs/HISTORICAL_RECORDS.md` index.

The index organizes history by category and chronology while preserving original records in place.

It does not copy or rewrite the historical records. Instead it provides:

- navigation;
- interpretation boundaries;
- supersession context;
- links back to current documentation.

A small `history/README.md` also explains the archive when readers enter the historical directory directly.

The worklog index was refreshed to include June and to expose focused and milestone records.

The main documentation index now links Historical Records as a first-class documentation area rather than a small footer section.

## Historical record policy

Historical records are project memory, not a second source of truth.

A historical record should be retained when it explains meaningful engineering evolution and should be clearly dated, historical, intermediate or superseded where appropriate.

The preferred pattern is:

`preserve original record -> add current interpretation at index/wrapper level -> link to current architecture`

rather than silently rewriting the old record.

## Outcome

The portfolio now supports two complementary reading modes:

1. **What is true now?** -> current README, architecture, status, roadmap and project model.
2. **How did we get here?** -> Historical Records index, worklogs, snapshots, ADR history, intermediate case studies and analysis trails.

That separation makes the portfolio more useful as both current technical documentation and an engineering-history artifact.
