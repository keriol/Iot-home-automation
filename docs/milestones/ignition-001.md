# IGNITION-001 — Butler-to-Android Network Baseline

> One small step for a man, one giant step for a Butler.

**Status:** released / closed

Ignition Phase 1 is the first coordinated compatibility checkpoint that reaches
from a real Android client into the Butler communication network.

## Compatibility BOM

Exact proven release set:

| Component | Ignition version | Role |
| --- | --- | --- |
| Butler Interphone | 0.1.0 | Android client |
| Bifröst | 0.1.0 | external/client bridge |
| Midgard | 0.1.0 | communication and cross-Butler routing |
| Butler Core | 0.3.0 | provider-neutral execution/contracts |
| Home Assistant Plugin | 0.3.0 | reusable Home Assistant integration |
| Alfred | 0.5.0 | private proving runtime |
| Asgard | 0.1.0 | Alfred-owned internal Butler ingress compatibility version |

Wilfred is intentionally not part of this BOM.

Asgard 0.1.0 is shipped inside Alfred 0.5.0. It has no independent package,
repository, tag or artifact lifecycle in IGNITION-001.

## Public path

```text
Android
  -> Interphone 0.1.0
  -> Bifröst 0.1.0
  -> Midgard 0.1.0
  -> Butler Core 0.3.0
  -> HAP 0.3.0
  -> Home Assistant
```

## Private proving path

```text
Android
  -> Interphone 0.1.0
  -> Bifröst 0.1.0
  -> Midgard 0.1.0
  -> Butler-owned Asgard 0.1.0
  -> Alfred 0.5.0
```

## Version semantics

The versions above are the first versions declared network-capable for this
Android communication baseline.

That statement means:

- the component participates in the canonical network architecture from that
  release onward;
- IGNITION-001 records the exact set actually proven together;
- a later component version is not automatically claimed compatible without
  new integration evidence;
- Core and HAP remain Android-agnostic despite being validated inside this
  Android-reaching network.

## Live proving evidence

The final candidate set was assembled on the canonical private proving
environment and exercised from the signed Android client.

Observed evidence includes:

- client compatibility manifest accepted with no blocking Ignition cards;
- Android -> Core/HAP state READ;
- governed Home Assistant ACTION;
- post-action state READ confirming the expected physical-state transition;
- Android -> Bifröst -> Midgard -> Asgard -> Alfred request/reply;
- non-empty request correlation identity visible on the client;
- canonical `Source Butler: Alfred` returned to the client;
- long-running media playback retested after propagating Bifröst interaction
  origin, allowing deferred work to acknowledge within the client transport
  budget while physical playback completes asynchronously;
- final private runtime health and exact BOM version alignment verified after
  deployment.

Private topology, credentials and household identifiers are intentionally not
part of this public evidence record.

## Release evidence

The released baseline was closed only after:

- green component CI;
- build/package validation;
- public/private sanitization audit;
- signed Interphone APK validation;
- Android in-place install and client smoke;
- Android -> Core/HAP READ proof;
- Android -> Home Assistant ACTION followed by post-action READ/VERIFY when
  observable;
- Android -> Midgard -> Asgard -> Alfred proof;
- preserved request correlation;
- canonical source Butler identity on the concrete-Butler path;
- verified final tag targets and release assets.

All live behavior gates above completed and the coordinated releases were
published and verified. IGNITION-001 is therefore a closed compatibility
baseline rather than an open release candidate.

## External I/O boundary

IGNITION-001 proves client input and request/reply output through the reusable
network boundary.

A later proactive output direction is architecturally supported:

```text
Alfred/domain
  -> Georges
  -> Osvaldo
  -> Hermes
  -> Bifröst
  -> Interphone
```

That proactive path remains **Designed to enable**, not an IGNITION-001
implementation claim.

## Publication boundary

Intended public Ignition components:

- Butler Interphone;
- Bifröst;
- Midgard;
- Butler Core;
- Home Assistant Plugin.

Private proving components:

- Alfred;
- Alfred-owned Asgard;
- Keriol deployment configuration and runtime evidence containing private
  topology or household data.

## Deferred

The following are explicitly outside Ignition Phase 1:

- reusable standalone Asgard;
- Wilfred network attachment;
- automatic pairing/device credentials;
- Material 3 Expressive UI;
- proactive Android notifications;
- structured interactive continuation/confirmation UI;
- polished voice interaction.

## Development authority

This milestone describes the coordinated compatibility checkpoint.

Per-component implementation and release evidence remain authoritative in their
own repositories. GitHub Issues own active status; Git tags/releases/workflows
own release evidence; live systems own runtime truth.
