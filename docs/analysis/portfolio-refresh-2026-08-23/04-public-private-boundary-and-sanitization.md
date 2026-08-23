# 04 — Public/Private Boundary and Sanitization

## Question

How can the portfolio show credible real-world engineering without leaking private Alfred implementation or sensitive household details?

## Core boundary

The public portfolio is not a redacted mirror of the private deployment.

It publishes **derived engineering knowledge**, not private source with names removed.

That distinction matters because implementation can remain identifiable even after obvious identifiers are changed.

## Material appropriate for the public portfolio

Public documentation may include:

- architecture and ownership boundaries;
- public ADRs;
- reusable engineering lessons;
- sanitized case studies;
- capability maturity;
- public-safe diagrams;
- conceptual request and delivery flows;
- public repository/release evidence;
- high-level descriptions of private validation.

## Material excluded from the public portfolio

The refresh treats the following as outside the public boundary:

- private Alfred source code;
- private endpoints;
- credentials, tokens or account identifiers;
- machine-specific private paths;
- unnecessary Home Assistant entity/device identifiers;
- personal data;
- sensitive household state;
- implementation details of private media-acquisition mechanisms;
- provider bindings or operational mappings that would unnecessarily expose the private deployment.

## Sanitization is not simple renaming

A source excerpt does not become public-safe merely because private identifiers are replaced with generic names.

The correct public form is usually a higher-level statement such as:

- a media workflow may continue through a private acquisition path;
- a delivery framework routes approved speech to a configured frontend provider;
- a private mapping resolves an interaction endpoint to an appropriate delivery target.

The portfolio should explain the architectural lesson without publishing enough implementation detail to recreate the private system.

## Private proving-ground evidence

Private Alfred behavior may justify statements such as:

- `In testing`;
- validated against a real household workflow;
- exercised with physical devices;
- designed to enable later public extraction.

It does not justify exposing how the private implementation works internally.

## Public links

The portfolio reference map should point only to intentionally public repositories and public documentation.

The private Alfred repository may be named conceptually when necessary to explain the ecosystem, but public documentation must not rely on readers having access to its source.

## Case-study rule

A public case study should be built around:

1. the engineering problem;
2. the ownership decision;
3. the reusable pattern;
4. observable validation;
5. failure semantics;
6. what remains private;
7. what, if anything, may later become reusable.

It should not become an operational deployment recipe for Keriol Home.

## Runtime bugs discovered during documentation work

A documentation audit can reveal a private runtime discrepancy. Such a discrepancy may be recorded publicly only when doing so teaches an architectural lesson without disclosing private internals.

If the discrepancy is purely operational, the public portfolio should retain only the architectural conclusion, while detailed debugging remains in the owning private repository.

## Outcome

The portfolio boundary is intentionally asymmetric:

- private systems may provide evidence for public engineering conclusions;
- public documentation must not provide enough detail to reconstruct those private systems.

This allows Keriol Home to remain a real proving ground without turning the portfolio into an accidental source release.
