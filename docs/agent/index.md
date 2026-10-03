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

Read [Sources of truth](source-of-truth.md), then choose the workflow that
matches the user's intent.

## Choose the path

### First installation / first run

Use [First Installation Assistance](first-installation.md).

This path is for getting a released public Butler working incrementally without
turning installation debugging into ad-hoc product development.

### Feature design / implementation

Use [Feature Design Workflow](feature-design.md), then read the owning
component/API page, relevant ADRs/milestones and GitHub Issues/PRs.

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
