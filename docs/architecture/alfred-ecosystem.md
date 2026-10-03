---
title: Alfred Development Architecture
kind: development
scope: public-safe
status: in-testing
---

# Alfred Development Architecture

Alfred is the private Keriol Home Butler runtime and proving ground.

This page explains **development concepts and ownership boundaries** that are
being exercised privately. It does not document the private implementation and
must not be read as an installation guide or as evidence that Wilfred already
ships the same behavior.

## Relationship to the public ecosystem

```text
                Butler Core
                /        \
        Wilfred            Alfred
   public runtime      private proving runtime
```

Wilfred and Alfred are sibling consumers of Core-owned contracts.

Reusable plugins may be consumed by either runtime without making one runtime a
dependency of the other.

## What Alfred is used to prove

Alfred is where Keriol-specific work can move faster than the public runtime.

Typical proving themes include:

- domain-owned behavior instead of conversation-owned special cases;
- deterministic resolution before AI fallback;
- policy and confirmation boundaries;
- verified physical actions;
- proactive communication policy;
- media-domain reasoning;
- replaceable frontend/delivery paths;
- interaction patterns that may later justify reusable contracts.

These themes are **In testing** unless a public repository release provides
separate evidence of availability.

## Public/private boundary

Public documentation may explain:

- architectural ownership;
- the problem being tested;
- maturity;
- engineering lessons;
- the route a reusable pattern could take toward public extraction.

It must not expose:

- readable Alfred source;
- private endpoints;
- household identifiers;
- configuration values;
- deployment topology;
- secrets or credentials;
- private acquisition implementation.

## Asgard exception

IGNITION-001 proved a Butler-owned Asgard boundary end to end through Alfred.

Therefore Asgard remains part of the public communication architecture even
though the Ignition implementation is Alfred-owned.

```text
Bifröst -> Midgard -> Butler-owned Asgard -> concrete Butler
```

For IGNITION-001:

- Asgard compatibility version is `0.1.0`;
- Alfred owns the concrete implementation;
- no standalone public Asgard package is claimed.

See [Asgard](asgard.md).

## Graduation path

A private Alfred capability becomes public only after:

1. reusable ownership is clear;
2. household assumptions are removed;
3. contracts are generalized;
4. tests exist independently of Keriol Home;
5. public-safe documentation exists;
6. clean installation/runtime evidence exists;
7. a public repository release explicitly ships it.

Possible destinations include Butler Core, Wilfred or an independent public
plugin.

## What to read next

- [Development & Proving Ground](../ecosystem/development.md)
- [Alfred Proving Ground](alfred-proving-ground.md)
- [Released Public Ecosystem](../ecosystem/released.md)
- [ADR-012](../adr/ADR-012-sibling-runtimes-and-independent-platform-plugins.md)
