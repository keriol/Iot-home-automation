# 10 — Residual Reference-Document Audit

## Purpose

After DOC-003 had already refreshed the main architecture, governance, narrative, safety and historical-record documentation, a final broader review asked a different question:

> Are there still current reference documents that look harmless but encode the old project model?

This pass deliberately focused on documents that had not received a full rewrite during the earlier DOC-003 phases.

## Files reviewed

The review covered the remaining top-level reference material under `docs/`, with particular attention to:

- `SKILLS_MATRIX.md`;
- `INTEGRATIONS.md`;
- `PORTFOLIO_REVIEW.md`;
- `diagrams/ai-assisted-development-flow.md`;
- `LESSONS_LEARNED.md`.

## Findings

### 1. Skills Matrix

The previous matrix still described some proving-ground areas as generic skills without making their maturity explicit.

It also contained wording about publishing `sanitized Python examples`. That no longer matches the stricter public boundary adopted during DOC-003: the public portfolio should document architecture, decisions, diagrams, analysis and lessons, not readable private-derived implementation merely because identifiers have been anonymized.

The matrix was rewritten to:

- distinguish integration/provider skills from Butler capability/domain architecture;
- include deterministic-first resolution and verified-action semantics;
- use the current `Available / In testing / Designed to enable` vocabulary;
- describe presence as a reliability/design problem rather than a production-ready occupancy feature;
- describe Alexa/Hermes as private proving-ground evidence rather than a Wilfred public frontend claim;
- remove the old sanitized-source implication.

### 2. Integrations

The previous integrations page treated a connected service and a Butler capability as roughly the same kind of thing.

That is inconsistent with the current capability model.

The document now explicitly separates:

- integration/provider;
- tool;
- capability;
- domain.

It also states that Home Assistant remains the owner of physical orchestration and that integration presence is not public-capability availability.

Presence is labelled `Designed to enable`; energy is labelled `In testing`; Alexa is clearly a private current frontend/proving-ground path.

### 3. Portfolio Review Guide

The old review guide was still a lightweight recruiter/navigation list and included ambiguous language such as `Current implementation examples`.

The refreshed guide now gives different reading paths for:

- current architecture;
- IoT/integrations;
- verified automation;
- software engineering;
- project history.

It explicitly tells readers how to distinguish current public-safe architecture, private proving-ground evidence and historical records.

### 4. AI-Assisted Development Flow

The old diagram used a circular model in which AI and a `Project Model` appeared to sit at the center of the development process.

That no longer matches project governance.

The new flow shows:

- GitHub Issues as planning/active-state authority;
- Git/main as merged implementation/documentation authority;
- commits/tags/releases/workflows as evidence;
- live systems as runtime/physical evidence;
- AI as an assistant to the maintainer rather than an authority;
- the portfolio as derived documentation;
- historical records as project memory.

### 5. Lessons Learned

`LESSONS_LEARNED.md` was reviewed and intentionally left unchanged.

Its statements remain broad, current and compatible with the modern architecture:

- local-first preference;
- MQTT modularity;
- voice frontends are not the automation brain;
- presence reliability is difficult;
- public repositories require aggressive sanitization.

Not every old file requires churn. Leaving a document unchanged after review is preferable to rewriting it merely for cosmetic consistency.

## Public-Safety Check

The final reference-doc pass preserves the same DOC-003 boundary:

- no readable private Alfred implementation;
- no credentials or private endpoints;
- no unnecessary operational identifiers;
- no machine-specific deployment details;
- no private media-acquisition implementation naming or recognizable implementation detail.

## Conclusion

The residual audit found four genuinely stale current reference documents and one still-valid document.

After the four updates, there are no known top-level current reference documents left using the old governance, maturity or capability model.

This closes the gap between `DOC-003 scope complete` and `portfolio documentation baseline complete`.
