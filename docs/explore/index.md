---
title: Explore
kind: discovery
scope: public
status: current
---

# Explore

Not everything interesting belongs under "API reference".

This part of the site is for the edges of the project: experiments, future
directions, unusual ideas and the engineering rabbit holes that helped shape the
current architecture.

## Ideas currently around the ecosystem

<div class="grid cards" markdown>

-   **A Butler on more frontends**

    Android is proven through Interphone. Voice already exists privately.
    Additional clients remain possible because presentation is kept outside
    Butler Core.

    **Maturity:** Designed to enable

-   **Automatic pairing and device trust**

    Bifröst already separates discovery from trust. Automatic pairing and
    device credentials remain post-Ignition work.

    **Maturity:** Designed to enable

-   **Proactive communication**

    Private work separates domain events, Osvaldo policy and Hermes delivery.
    Proactive Android delivery is not part of IGNITION-001.

    **Maturity:** In testing / Designed to enable

-   **Another home-automation platform**

    HAP proves that Home Assistant can live behind a reusable plugin boundary.
    Core is intentionally provider-neutral so another manager could implement a
    different integration.

    **Maturity:** Designed to enable

-   **Privacy-first presence**

    The preferred direction is intentionally modest:
    `occupied / empty / uncertain`, without requiring continuous room-level
    tracking.

    **Maturity:** Designed to enable

-   **Energy-aware household capabilities**

    Local photovoltaic and battery telemetry already exist in the proving
    ground. Energy-aware appliance suggestions and coordination remain future
    capability ideas.

    **Maturity:** Designed to enable

-   **Maker capabilities**

    Server/NAS observability and future 3D-printer READ / confirmed ACTION
    capabilities are natural proving-ground candidates.

    **Maturity:** Designed to enable

</div>

## Follow the rabbit holes

- [Roadmap](../../ROADMAP.md) for current public/private directions
- [Showcase](../SHOWCASE.md) for proven and in-testing work
- [Project History](../history/index.md) for how ideas evolved
- [ADRs](../adr/ADR-012-sibling-runtimes-and-independent-platform-plugins.md) for architectural decisions
- [GitHub Issues](https://github.com/keriol/Iot-home-automation/issues) for active tracked work

Open issues and interesting ideas are not automatically product commitments.
The maturity label matters.
