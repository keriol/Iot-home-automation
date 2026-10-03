---
title: Fundamental Concepts
kind: concept
scope: public
status: current
---

# Fundamental Concepts

## 1. You ask for an outcome

**You ask to be understood, not to operate the implementation.**

A Butler interaction starts from intent, not infrastructure.

The user should not need to know which service, entity, protocol or provider is
responsible for satisfying the request.

```text
user outcome
  -> Butler reasoning/routing
  -> owned capability
  -> integration/provider
```

## 2. The Butler knows what belongs where

A Butler does not become a giant pile of special cases.

Ownership remains explicit:

- domains own related knowledge and behavior;
- capabilities describe what the Butler knows how to do;
- tools are typed operations;
- integrations/providers connect to external systems;
- the runtime resolves, governs and executes.

Conversation code must not become the accidental owner of domain knowledge.

## 3. Deterministic first

Known requests should take deterministic paths when a suitable resolver or
capability exists.

Open-ended goals may use planning or AI fallback, but that fallback does not
bypass policy, permissions, confirmation or validation.

## 4. The Butler does not replace the house

Home Assistant remains the physical orchestration owner in Keriol Home.

The Butler reasons, routes and invokes capabilities. Home Assistant still owns
devices, integrations, dashboards and device state.

Another automation platform could be integrated through another provider/plugin
without changing Butler Core's provider-neutral contracts.

## 5. Dispatch is not success

A software call returning successfully is not proof that the physical world
changed.

Where state is observable, Butler systems prefer:

```text
READ -> ACTION -> READ -> VERIFY
```

That rule grew out of real appliance, media and home-theater failures rather
than an abstract design exercise.

## 6. Frontends are replaceable

Voice, Android, web or another future client are presentation/interaction
surfaces.

The Butler architecture should not depend on one frontend.

Bifröst exists as the client/API boundary precisely so external clients do not
need to know private runtime internals.

## 7. One house can host more than one Butler

Midgard provides provider-neutral communication and cross-Butler routing.

Each concrete Butler owns its own identity and projects it through a
Butler-owned Asgard boundary.

This allows a client to address shared Core capabilities or a specific Butler
without turning the communication layer into the owner of Butler identity.

## 8. Private proving, public extraction

Keriol Home is a real-world proving ground.

A private capability does not automatically become a public Wilfred feature.

Reusable extraction requires stable ownership, tests, sanitization,
documentation and clean installation/runtime evidence.

## 9. The project remembers how it got here

The architecture was not designed in one sitting.

It evolved through voice experiments, appliance workflows, media automation,
safe-power problems, local telemetry, Alfred, Core/Wilfred extraction and the
Ignition Android network.

That history is preserved because the failed or intermediate ideas explain many
of today's boundaries.

Continue with:

- [Architecture Overview](../architecture/overview.md)
- [Project Showcase](../SHOWCASE.md)
- [Project History](../history/index.md)
