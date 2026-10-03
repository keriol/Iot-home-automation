---
title: Portfolio
kind: landing
scope: public
status: current
---

# Portfolio

The Butler ecosystem is the reusable result of solving real problems in a real
home.

This section is for people who want to evaluate the engineering rather than read
the entire architecture manual from page one.

## Start with the showcase

[Project Showcase](../SHOWCASE.md) collects representative work with explicit
maturity labels.

It includes:

- Butler runtime evolution;
- laundry and appliance interaction;
- proactive communication policy;
- media intelligence;
- home-theater safe-power orchestration;
- local energy telemetry;
- privacy-preserving presence experiments;
- Alexa/Hermes delivery;
- the Android-reaching Ignition network.

## Released public ecosystem

The components a reader can evaluate from public repositories today are:

- Butler Core;
- Wilfred;
- Home Assistant Plugin;
- Bifröst;
- Midgard;
- Butler Interphone.

[Released Public Ecosystem →](../ecosystem/released.md)

## Development & proving ground

Alfred and Keriol-specific behavior are documented separately as private proving
work.

That section explains concepts, maturity and reusable lessons without exposing
private implementation details or implying that Wilfred already ships them.

[Development & Proving Ground →](../ecosystem/development.md)

**Asgard is the deliberate exception:** the boundary is part of the released
Ignition architecture, while the Ignition implementation remains Alfred-owned
and is not a standalone public package.

[See current project status →](../PROJECT_STATUS.md)

## Selected engineering stories

<div class="grid cards" markdown>

-   **Physical success is not API success**

    Laundry and home-control work drove the verified-action pattern.

    [Laundry voice case study →](../case-studies/laundry-voice-mvp.md)

-   **Voice is a frontend, not the architecture**

    Alexa evolved from an automation brain into a replaceable entry point.

    [Alexa HTTPS bridge →](../case-studies/alexa-https-bridge.md)

-   **Home Assistant owns the physical world**

    Startup sequencing and recovery stay where device state can be observed.

    [Bravia & Dolby safe power →](../case-studies/bravia-dolby-safe-power.md)

-   **A Butler can become a network**

    Ignition proved Android -> Bifröst -> Midgard -> Core/Asgard end to end.

    [IGNITION-001 →](../milestones/ignition-001.md)

</div>

## How the project is engineered

- [Architecture Overview](../architecture/overview.md)
- [Architecture Diagram](../diagrams/architecture.md)
- [Engineering Lessons](../lessons-learned/ignition-001-engineering-lessons.md)
- [ADRs](../adr/ADR-012-sibling-runtimes-and-independent-platform-plugins.md)
- [AI-Assisted Development](../AI_COLLABORATION.md)
- [Skills Matrix](../SKILLS_MATRIX.md)
- [Metrics](../METRICS.md)

## Where it came from

The current architecture makes more sense when you can see the mistakes,
experiments and intermediate designs that produced it.

[Read the project origin →](../PROJECT_ORIGIN.md)  
[Browse the historical timeline →](../history/index.md)


## Support the project

If the Butler ecosystem, case studies or documentation are useful to you:

[Support on Ko-fi](https://ko-fi.com/butlerwilfred){ .md-button .md-button--primary }
[GitHub](https://github.com/keriol){ .md-button }
[LinkedIn](https://www.linkedin.com/in/marco-carolo/){ .md-button }
