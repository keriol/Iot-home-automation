---
title: Agent Guide
kind: agent-guide
scope: public
status: current
---

# Agent Guide

This section tells coding/planning agents how to navigate Butler documentation
without duplicating the documentation itself.

## Choose the path first

### New feature / architecture work

Read:

1. [Sources of truth](source-of-truth.md)
2. [Feature design workflow](feature-design.md)
3. [Architecture overview](../architecture/overview.md)
4. the owning component/API page
5. relevant ADRs, milestones and GitHub issues

### First installation / onboarding assistance

Read:

1. [Sources of truth](source-of-truth.md)
2. [First Installation Assistance](first-installation.md)
3. the released installation documentation of the owning runtime/integration

Do not use the feature-design path to improvise around a broken installation.

## Release boundary

Before proposing installation or capability claims, distinguish:

- [Released Public Ecosystem](../ecosystem/released.md): public, released and usable components;
- [Development & Proving Ground](../ecosystem/development.md): Alfred/private proving, not a Wilfred availability claim.

Asgard is the explicit exception: the boundary is part of the released Ignition architecture, while its Ignition implementation remains Alfred-owned and non-standalone.

## Component discovery

| Need | Read first | Likely owner |
| --- | --- | --- |
| External client/API integration | [Bifröst API](../api/bifrost.md) | Bifröst |
| Cross-Butler routing | [Midgard](../architecture/midgard.md) | Midgard |
| Concrete Butler ingress/identity | [Asgard](../architecture/asgard.md) | Butler-owned Asgard |
| Provider-neutral execution/contracts | [Architecture overview](../architecture/overview.md) | Butler Core |
| Home Assistant integration | Architecture overview + HAP repository docs | Home Assistant Plugin |
| Public reusable Butler runtime | Wilfred repository docs | Wilfred |
| Private Keriol behavior | private Alfred repository docs | Alfred |
| Android client | Interphone repository docs | Butler Interphone |

The table is a discovery aid, not a substitute for the owning repository.

## Evidence mindset

Before implementation, define what evidence will prove the feature works.

For observable actions prefer:

```text
READ -> ACTION -> READ -> VERIFY
```

A successful dispatch or HTTP acknowledgement is not physical-success evidence.
