---
title: Butler
kind: landing
scope: public
status: current
hide:
  - toc
---

# Talk to your home through a Butler

Your home already has software for lights, media, appliances, energy, automations and devices.

You should not need to remember which system owns what.

**Tell the Butler what you want.**

The Butler knows the house, the services behind it and the boundaries between them. It finds the right capability, routes the request to the right owner, respects policy and confirmation, and verifies the outcome when the result can be observed.

You ask for the outcome. The Butler handles the plumbing.

[Meet Butler](meet-butler.md){ .md-button .md-button--primary }
[Explore the architecture](architecture/overview.md){ .md-button }

---

## What brought you here?

### I want to understand Butler

Start with the idea before the internals.

Learn why Home Assistant remains the physical orchestration platform, why Butler Core stays provider-neutral, why Wilfred and Alfred are sibling runtimes, and where Bifröst, Midgard and Asgard fit.

[Meet Butler](meet-butler.md) · [Architecture overview](architecture/overview.md) · [Communication model](architecture/communication-model.md)

### I am looking for technical documentation

Go straight to the contracts, APIs, architecture, decisions and proven compatibility baselines.

[Bifröst Client API](api/bifrost.md) · [Midgard](architecture/midgard.md) · [Asgard](architecture/asgard.md) · [IGNITION-001](milestones/ignition-001.md)

### I want to evaluate the project

Browse the project as a portfolio: real engineering problems, architectural choices, reusable components, proving work and lessons learned.

[Portfolio](portfolio/index.md) · [Project showcase](SHOWCASE.md) · [Skills matrix](SKILLS_MATRIX.md)

### I want to see how this happened

The architecture did not appear fully formed. It grew from a real smart home, experiments, wrong turns, migrations, private proving and increasingly reusable public boundaries.

[Project history](history/index.md) · [Project origin](PROJECT_ORIGIN.md) · [Engineering lessons](lessons-learned/ignition-001-engineering-lessons.md)

### I want the strange ideas

Some ideas are released. Some are in testing. Some merely fit the architecture and are waiting for their turn.

Explore the experiments, future directions and the ideas that may eventually become capabilities.

[Explore ideas](explore/index.md) · [Roadmap](../ROADMAP.md)

### I want to install a Butler

There is a dedicated first-installation path for humans and agents. It starts with a small deterministic runtime and adds integrations only after each boundary is healthy.

[First Installation Assistance](agent/first-installation.md)

---

## The Butler idea in one picture

```text
You
 |
 |  "What I want"
 v
Butler
 |
 +-> understands intent and context
 +-> finds the owning capability
 +-> applies policy / confirmation
 +-> invokes the right system
 +-> verifies observable outcomes
 |
 v
Home Assistant / media / services / devices
```

The Butler is not the software of the house.

**The Butler is the one who knows how to talk to all the software of the house.**

---

## Proven, not just imagined

The architecture has been exercised against a real home and a real Android client.

IGNITION-001 proved both:

```text
Android -> Interphone -> Bifröst -> Midgard -> Core -> HAP -> Home Assistant
Android -> Interphone -> Bifröst -> Midgard -> Asgard -> Alfred
```

including request correlation, authoritative Butler identity and observable action verification.

[See IGNITION-001](milestones/ignition-001.md){ .md-button }

---

## This is also a living engineering notebook

This site intentionally keeps several views of the same project:

- **Documentation** explains what the architecture is now.
- **Portfolio** shows what was built and why it matters.
- **History** preserves how the system evolved.
- **Explore** collects experiments and future directions with explicit maturity.
- **GitHub Issues** connect the documentation to the work that created it.
- **Agent guides** teach automated contributors how to navigate the same source of truth.

The Markdown in this repository remains canonical. MkDocs is the front door, not a second truth.

---

*Documentation site development line: **0.1.0.dev0***
