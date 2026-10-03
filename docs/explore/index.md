---
title: Ideas, Experiments and Rabbit Holes
kind: exploration
scope: public
status: current
---

# Ideas, experiments and rabbit holes

Not everything interesting belongs in a release.

This is the part of the project where validated private behavior, future
architecture and deliberately unfinished ideas can be explored without pretending
they already ship.

## How to read this section

- **In testing** means implementation or real-world validation exists somewhere,
  but it is not a public release promise.
- **Designed to enable** means the architecture deliberately leaves room for the
  idea, but implementation is not claimed.
- Open GitHub issues describe work, not automatically capability.

## In testing

### A Butler that knows when to speak

Osvaldo separates proactive communication policy from delivery.

The interesting question is not *can the system send a notification?* It is
*should it interrupt you now, defer it, aggregate it, or stay quiet?*

[See the showcase →](../SHOWCASE.md#3-proactive-communication-policy)

### Media as a domain, not a pile of commands

Charon explores media identity, discovery, lifecycle, playback and observed
state as one owned domain rather than scattered conversational logic.

[Media intelligence & Plex workflows →](../SHOWCASE.md#4-media-intelligence-and-plex-workflows)

### Appliances that can be reasoned about

Laundry proving work explores how a Butler can expose state, program knowledge,
safe actions and physical verification without turning the conversation layer
into the appliance implementation.

[Laundry workflow →](../SHOWCASE.md#2-alfred-laundry-voice-workflow)

### Local energy intelligence

Local photovoltaic, grid and battery telemetry is being validated as a durable
local-first data source for future reasoning.

[Energy telemetry →](../SHOWCASE.md#6-local-energy-telemetry)

## Designed to enable

### Presence without building a surveillance system

The preferred direction is deliberately small:

```text
occupied / empty / uncertain
```

The goal is useful context, not continuous room-level tracking.

[Privacy-preserving presence →](../SHOWCASE.md#7-privacy-preserving-presence)

### A reusable standalone Asgard

Ignition proved the Asgard boundary inside Alfred. Extracting a standalone
reusable Asgard remains a post-Ignition direction, not a released package.

[Asgard →](../architecture/asgard.md)

### Pairing and trusted client enrollment

Bifröst discovery exists as a client/network concept, while automatic
pairing/device credentials remain beyond the released 0.1.0 baseline.

[Bifröst API →](../api/bifrost.md)

### Richer interactive and proactive clients

The released network proves request/reply from Android. Proactive Android
delivery, richer continuation/confirmation UX and polished voice interaction are
explicitly post-Ignition directions.

[IGNITION-001 deferred scope →](../milestones/ignition-001.md#deferred)

## Why keep the weird ideas visible?

Because architecture becomes sterile if it documents only the parts that already
worked.

The useful question is whether an idea has:

1. an owner;
2. a clean boundary;
3. an evidence level;
4. a path to proving or rejecting it.

If it does, it can remain visible without being marketed as finished.

For active work, follow the linked GitHub Issues from the relevant architecture
page.
