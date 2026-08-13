# ADR-010 - Public Portfolio Documentation Boundary

## Status

Accepted

## Context

The Keriol Home portfolio originally included sanitized copies of selected Home Assistant configuration, Python services, voice interaction models and other implementation examples.

That approach was useful while the project was primarily documenting a single private smart-home deployment.

The architecture has since evolved into a clear separation between:

- private Keriol Home and Alfred implementation;
- reusable public Butler projects;
- public portfolio documentation.

Replacing household identifiers with generic names does not change the fact that a readable implementation snapshot remains derived from private implementation.

The portfolio exists to explain how the system evolves, not to republish a redacted copy of the private codebase.

## Decision

The public portfolio is documentation-first.

It may publish:

- architecture;
- ADRs;
- diagrams;
- conceptual flows;
- engineering decisions;
- capability maturity;
- sanitized case studies;
- historical narrative;
- lessons learned;
- public/private boundaries.

It must not publish readable copies of private implementation merely because identifiers have been sanitized.

This includes private-derived:

- Python source;
- Home Assistant YAML;
- service definitions;
- interaction models;
- configuration snapshots;
- tool registries;
- runtime fixtures;
- operational scripts.

When implementation becomes genuinely reusable and public, it belongs in the appropriate public source repository such as Butler Core, Wilfred or an official plugin.

## Portfolio examples

Conceptual pseudoflows and diagrams are allowed when they explain behavior without reproducing private implementation.

Implementation-shaped examples should be created only when they describe a genuinely public contract and belong naturally with the public project that owns that contract.

## Consequences

### Positive

- The private/public boundary becomes easier to reason about.
- The portfolio remains focused on architectural evolution.
- Sanitization no longer creates false confidence around private-derived source.
- Reusable code has a clear destination in the public Butler repositories.
- Alfred can remain a real-world proving ground without becoming a source-code exhibit.

### Negative

- Some older portfolio examples must be removed.
- Historical Git data containing private-derived examples requires cleanup.
- Readers looking for runnable code must follow the relevant public project repository instead.

## Historical material

Historical documentation may describe capabilities and architectural states of their time.

Readable private-derived implementation snapshots are outside the public portfolio boundary even when they were previously described as sanitized.
