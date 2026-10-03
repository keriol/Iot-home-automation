---
title: Agent Guide
kind: agent-guide
scope: public
status: current
---

# Agent Guide

This section tells coding/planning agents how to navigate Butler documentation
without duplicating the documentation itself.

## Start here

Read in this order:

1. [Sources of truth](source-of-truth.md)
2. [Feature design workflow](feature-design.md)
3. [Architecture overview](../architecture/overview.md)
4. the owning component/API page for the requested work
5. relevant ADRs, milestones and GitHub issues

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
