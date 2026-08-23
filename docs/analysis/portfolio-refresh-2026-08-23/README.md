# Portfolio Refresh Analysis Trail — 2026-08-23

This directory preserves the intermediate analysis behind the DOC-003 portfolio refresh.

It is intentionally different from the final architecture documentation:

- final documentation states the current public-safe model;
- these notes preserve the evidence checks, drift findings, trade-offs and rejected interpretations that led to that model;
- historical documents are not rewritten to make old decisions look current;
- private implementation is never copied into this public repository.

## Analysis sequence

1. [Baseline and documentation drift audit](01-baseline-and-drift-audit.md)
2. [Governance and evidence model](02-governance-and-evidence-model.md)
3. [Architecture ownership and maturity analysis](03-architecture-ownership-and-maturity.md)
4. [Public/private boundary and sanitization](04-public-private-boundary-and-sanitization.md)
5. [Delivery, frontend and voice boundary](05-delivery-frontend-and-voice-boundary.md)
6. [Decisions and rejected alternatives](06-decisions-and-rejected-alternatives.md)
7. [Case-study and narrative audit](07-case-study-and-narrative-audit.md)
8. [Final safety, navigation and stale-reference audit](08-final-safety-link-and-stale-reference-audit.md)
9. [Historical records coverage](09-historical-records-coverage.md)

## Evidence rule

The analysis follows the same source hierarchy as the current portfolio:

- GitHub Issues for development planning and status;
- Git `main` for merged implementation and documentation;
- commits, tags, workflows and releases for implementation/release evidence;
- live systems for deployed and physical behavior;
- portfolio documents as derived public-safe material only.

A branch, issue or design note is evidence of activity or direction, not proof that a public capability is available.

## Public-safety rule

This analysis records conclusions, not readable private implementation.

Private household code, private endpoints, secrets, operational identifiers, unnecessary entity IDs and private media-acquisition implementation are excluded. Where a private mechanism matters to the reasoning, it is described only at the architectural boundary necessary to explain the decision.
