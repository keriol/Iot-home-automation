---
title: Development & Proving Ground
kind: ecosystem
scope: public-safe
status: current
---

# Development & Proving Ground

Not every useful idea is already a public Butler feature.

Keriol Home and Alfred are the private proving ground where new interaction
patterns, domains and policies are exercised against a real operating home
before reusable pieces are considered for public extraction.

## Alfred's role

Alfred is **not** a public Butler distribution.

It is the private Keriol sibling runtime built on Butler Core contracts and used
to prove ideas in a real household.

Public documentation may describe:

- the kind of problem being explored;
- the architectural owner of the behavior;
- lessons learned;
- maturity;
- reusable patterns that may later move outward.

Public documentation must not expose:

- readable private implementation;
- credentials or private endpoints;
- household-specific identifiers;
- private configuration/topology;
- sensitive runtime state;
- private acquisition implementation.

## Typical proving areas

Examples of work that may exist in Alfred before public extraction include:

- appliance semantics and verified actions;
- proactive communication policy;
- media-domain intelligence;
- frontend/delivery experiments;
- environmental and energy-aware behavior;
- new interaction patterns.

These should be read as **In testing** or **Designed to enable** unless a public
repository release explicitly says otherwise.

## Graduation rule

A private behavior does not become a Wilfred/Core/plugin feature automatically.

Reusable extraction requires:

1. clear ownership;
2. generalized contracts;
3. tests;
4. sanitization;
5. public-safe documentation;
6. clean installation/runtime evidence;
7. explicit release evidence.

## Asgard remains the exception

Asgard is Alfred-owned in the Ignition implementation, but the boundary itself
is part of the released communication architecture and therefore remains in the
public technical documentation.

See:

- [Asgard](../architecture/asgard.md)
- [Released Public Ecosystem](released.md)
- [Alfred Proving Ground](../architecture/alfred-proving-ground.md)
