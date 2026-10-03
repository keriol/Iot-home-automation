---
title: Documentation
kind: documentation-index
scope: public
status: current
---

# Documentation

You already know what you are looking for. Good. The machinery is this way. 🎩

## Documentation by depth

```text
Discover
  -> Understand
    -> Install
      -> Build
        -> Deep Dive
```

- **Discover**: [Meet Butler](../meet/index.md)
- **Understand**: [Fundamental Concepts](../meet/fundamentals.md)
- **Install**: [Install a Butler in your home](../install/index.md)
- **Build**: this technical map
- **Deep Dive**: ADRs, issue lineage, history and [Explore](../explore/index.md)

You can jump directly to any level. The layers are a reading aid, not a gate.

<div class="grid cards" markdown>

-   **Architecture**

    Understand component ownership, runtime boundaries and how the Butler
    ecosystem fits together.

    [Architecture overview](../architecture/overview.md)

-   **Client API**

    External applications enter the Butler network through Bifröst.

    [Bifröst API](../api/bifrost.md)

-   **Communication**

    Midgard routes across shared Core capabilities and concrete Butler-owned
    Asgard boundaries.

    [Communication model](../architecture/communication-model.md)

-   **Proven baselines**

    See what was actually tested together rather than inferring compatibility
    from version numbers.

    [IGNITION-001](../milestones/ignition-001.md)

-   **Architecture decisions**

    Why Home Assistant owns physical orchestration, why runtimes are siblings,
    why GitHub is the development authority and other durable decisions.

    [Browse ADRs](../adr/ADR-012-sibling-runtimes-and-independent-platform-plugins.md)

-   **First installation**

    Installing a Butler for the first time? Follow the staged path rather than
    enabling every subsystem at once.

    [Install a Butler in your home](../install/index.md)

    Want guided troubleshooting instead?
    [First Installation Assistance](../agent/first-installation.md)

</div>

## Core reading path

For a technical overview:

1. [Fundamental Concepts](../meet/fundamentals.md)
2. [Architecture Overview](../architecture/overview.md)
3. [Bifröst API](../api/bifrost.md)
4. [Midgard](../architecture/midgard.md)
5. [Asgard](../architecture/asgard.md)
6. [Node Manifest and Self-Description](../architecture/node-manifest.md)
7. [IGNITION-001](../milestones/ignition-001.md)

If you are designing new work, use the [Agent Guide](../agent/index.md) or the
same ownership rules manually.
