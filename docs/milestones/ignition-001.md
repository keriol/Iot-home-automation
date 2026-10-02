# IGNITION-001 — Butler-to-Android Network Baseline

**Status:** release candidate / combined proving

Ignition Phase 1 is the first coordinated compatibility checkpoint that reaches
from a real Android client into the Butler communication network.

## Compatibility BOM

Target release set:

| Component | Ignition version | Role |
| --- | --- | --- |
| Butler Interphone | 0.1.0 | Android client |
| Bifröst | 0.1.0 | external/client bridge |
| Midgard | 0.1.0 | communication and cross-Butler routing |
| Butler Core | 0.3.0 | provider-neutral execution/contracts |
| Home Assistant Plugin | 0.3.0 | reusable Home Assistant integration |
| Alfred | 0.5.0 | private proving runtime |

Wilfred is intentionally not part of this BOM.

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
  -> Butler-owned Asgard
  -> Alfred 0.5.0
```

The Asgard implementation used here remains private and is frozen by the Alfred
release source revision rather than by an independent package version.

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

## Release evidence required

Ignition is complete only after the exact candidate set has:

- green component CI;
- build/package validation;
- public/private sanitization audit;
- signed Interphone APK validation;
- Android in-place install and cold-start/reconnect smoke;
- Android -> Core/HAP READ proof;
- Android -> Home Assistant ACTION followed by post-action READ/VERIFY when
  observable;
- Android -> Midgard -> Asgard -> Alfred proof;
- preserved request correlation;
- canonical source Butler identity on the concrete-Butler path;
- verified final tag targets and release assets.

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
