---
title: Install a Butler in your home
kind: installation
scope: public
status: current
---

# Install a Butler in your home

You do not need the entire Butler ecosystem on day one.

Start with one working Butler. Prove it. Then teach it how to talk to the systems
you actually use.

## The short version

```text
1. Install Wilfred
        ↓
2. Prove the base runtime
        ↓
3. Add Home Assistant if you use it
        ↓
4. Add optional AI / HTTP
        ↓
5. Add Bifröst + Midgard if you need external clients
        ↓
6. Add Interphone or another client
```

Every layer is optional except the Butler runtime itself.

## Level 1 — Get a Butler running

For a public installation, start with **Wilfred**.

Wilfred is the reusable public Butler runtime. It is the right starting point for
a home that is not the private Keriol deployment.

Use the released installation documentation:

- [Wilfred repository](https://github.com/keriol/butler-wilfred)
- [Public onboarding](https://github.com/keriol/butler-wilfred/blob/main/docs/onboarding.md)
- [Installation and first run](https://github.com/keriol/butler-wilfred/blob/main/docs/installation.md)
- [Docker distribution](https://github.com/keriol/butler-wilfred/blob/main/docs/docker.md)

Before adding anything else, prove:

```text
Wilfred starts
    ↓
status is healthy
    ↓
tools are visible
    ↓
demo.echo works
```

If this does not work, stop here and fix this layer first.

## Level 2 — Connect the house

If your house already uses Home Assistant, add the **Home Assistant Plugin
(HAP)**.

```text
Wilfred
  ↓
HAP
  ↓
Home Assistant
  ↓
devices / integrations
```

Home Assistant remains responsible for physical orchestration.

Start with READ-only access and readiness. Only after the integration is healthy
should you test actions.

For observable actions, prefer:

```text
READ -> ACTION -> READ -> VERIFY
```

Resources:

- [Home Assistant Plugin](https://github.com/keriol/home-assistant-plugin)
- [Architecture Overview](../architecture/overview.md)

## Level 3 — Add intelligence where it helps

Butler does not require AI for known requests.

Deterministic capabilities should handle known operations when possible.

If you want open-ended goals, planning or AI-backed interpretation, add the
optional provider only after the base runtime works.

AI does not bypass permissions, confirmation or execution policy.

## Level 4 — Make the Butler reachable by other clients

If you need Android, another app or another external frontend, add the
communication stack:

```text
external client
      ↓
   Bifröst
      ↓
   Midgard
    ↙   ↘
 Core   concrete Butler
```

Read:

- [Bifröst API](../api/bifrost.md)
- [Midgard](../architecture/midgard.md)
- [Asgard](../architecture/asgard.md)
- [IGNITION-001](../milestones/ignition-001.md)

You do **not** need this network layer just to run Wilfred locally.

## Level 5 — Add a client

Butler Interphone is the released Android client proven in IGNITION-001.

- [Butler Interphone repository](https://github.com/keriol/butler-interphone-android)

A future client should talk through the same public boundary rather than learning
private Butler internals.

## Secrets stay secret

Do not commit Home Assistant tokens, API keys, Bifröst credentials or private
endpoints.

Use the secret/configuration mechanisms documented by the owning repository.

Do not paste production secrets into support chats.

## Want guided assistance?

The documentation also defines a dedicated agent-assisted installation path.

It follows the same staged model and diagnoses one boundary at a time.

[Open First Installation Assistance](../agent/first-installation.md){ .md-button .md-button--primary }

## Want to understand before installing?

Go back one level:

[Meet Butler](../meet/index.md) ·
[Fundamental Concepts](../meet/fundamentals.md)

Or go deeper:

[Technical Documentation](../documentation/index.md)
