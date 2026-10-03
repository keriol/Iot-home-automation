---
title: Butler
kind: landing
scope: public
status: current
---

# Talk to your home through a Butler

**Your home already has software. A Butler gives it someone you can talk to.**

Home Assistant knows the devices. Integrations know the services. Media systems
know the library. Automations know the routines.

A Butler sits above those systems, understands the capabilities available to it,
and turns a request for an **outcome** into governed actions.

You should not need to think in entity IDs, service calls or integration APIs.

> **Tell the Butler what you want. Let the Butler figure out which systems need
> to be involved.**

The goal is not to replace Home Assistant or the software already running the
house. The goal is to give the house a coherent interaction layer that knows how
to talk to them.

<div class="grid cards" markdown>

-   :material-compass-outline: **Meet Butler**

    ---

    Start with the idea, the architecture and why the project exists.

    [Meet Butler →](meet/index.md)

-   :material-book-open-page-variant-outline: **Read the documentation**

    ---

    Bifröst, Midgard, Asgard, Core, HAP, contracts, routing and proven baselines.

    [Open the technical map →](PROJECT_MODEL.md)

-   :material-rocket-launch-outline: **Install your first Butler**

    ---

    Follow the agent-friendly path from a clean runtime to optional integrations
    and client networking.

    [First installation →](agent/first-installation.md)

-   :material-briefcase-outline: **Browse the portfolio**

    ---

    Real engineering work, public components, private proving and reusable
    lessons.

    [Explore the portfolio →](portfolio/index.md)

-   :material-timeline-clock-outline: **Follow the story**

    ---

    From a Home Assistant-centered house to Alfred, Wilfred, Core and the
    Android-reaching Ignition network.

    [Walk through the history →](history/index.md)

-   :material-flask-outline: **Enter the rabbit holes**

    ---

    Experiments, future directions, parked ideas and concepts that are still
    being proved.

    [Ideas & experiments →](explore/index.md)

</div>

## The idea in one minute

Traditional smart-home interaction often exposes the implementation:

```text
find the device
-> know the integration
-> know the service
-> provide the right parameters
-> hope the command worked
```

The Butler model aims for a different conversation:

```text
"I want this outcome"
        ↓
Butler understands the relevant capability/domain
        ↓
deterministic path when the request is known
        ↓
policy / permission / confirmation
        ↓
the owning integration performs the work
        ↓
observable actions are verified when possible
```

That last part matters.

A Butler should not say *done* merely because an API accepted a request.

Where the result can be observed, the preferred pattern is:

```text
READ -> ACTION -> READ -> VERIFY
```

## A Butler is not the house

Home Assistant remains the physical orchestration owner.

Butler Core provides reusable contracts. Wilfred is the public reusable Butler
runtime. Alfred is the private Keriol proving runtime. HAP connects Butler
runtimes to Home Assistant.

For external clients, the released Ignition network adds:

```text
Client / Butler Interphone
        ↓
      Bifröst
        ↓
      Midgard
      ↙    ↘
   Core    Butler-owned Asgard
                    ↓
              concrete Butler
```

Bifröst is the client/API boundary. Midgard owns communication and cross-Butler
routing. Asgard is owned by the concrete Butler and projects its identity and
ingress boundary.

[See the full communication model →](architecture/communication-model.md)

## This is a real project, not a diagram exercise

The architecture grew out of a functioning home and the problems encountered
while operating it: voice control, appliances, media, safe power sequencing,
energy telemetry, physical-state verification, remote access and eventually
communication with a real Android client.

IGNITION-001 is the first coordinated released baseline proven end to end from
Android through the Butler network.

[See what IGNITION-001 actually proved →](milestones/ignition-001.md)

## Choose how deep you want to go

If you are evaluating the engineering work, start with the
[Project Showcase](SHOWCASE.md).

If you want to understand how the architecture became what it is, read
[Project Origin](PROJECT_ORIGIN.md) and the [Project History](history/index.md).

If you want contracts and boundaries, go straight to the
[Architecture Overview](architecture/overview.md), [Bifröst API](api/bifrost.md),
[Midgard](architecture/midgard.md) and [Asgard](architecture/asgard.md).

If you want to build or contribute, use the [Agent Guide](agent/index.md) and
follow the same canonical documentation used by humans.

## Maturity is explicit

This site distinguishes between:

- **Available**: public, documented and usable;
- **In testing**: implemented or privately exercised, but not a release promise;
- **Designed to enable**: a supported direction without an implementation claim.

That means the strange ideas are allowed to be strange without pretending they
already ship. Explore them anyway.

[Open Ideas & Experiments →](explore/index.md)

---

**Documentation site:** `0.1.0.dev0`  
Canonical source: versioned Markdown in the public repository.
