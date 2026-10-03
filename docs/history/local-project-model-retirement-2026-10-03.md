---
title: Retirement of the Local Project Model
kind: history
scope: public
status: historical
date: 2026-10-03
---

# Retirement of the Local Project Model

On 2026-10-03 the compact local Home Automation Project Model reached the end of
its active role.

It had served the project well through the period when Keriol Home was primarily
a Home Assistant-centered automation system and later while Alfred, Butler Core
and Wilfred were still being separated into clearer architectural layers.

## What the final local model still remembered

The last model still carried the project's early shape:

- Home Assistant, MQTT, Node-RED and HACS as the home-automation foundation;
- Plex voice control and media workflows;
- washing-machine integration;
- Bravia/Dolby safe-power sequencing;
- local lighting and appliance integration;
- early presence/security/energy priorities;
- Tailscale for private access and Cloudflare Tunnel for narrow public access;
- the original plan to create a public-safe GitHub portfolio;
- the principle that one layer should own each feature;
- the rule that secrets and private operational data must never enter public Git.

Those points remain historically useful because they show what the Butler
ecosystem grew out of.

## Why it was retired

By October 2026 the project had outgrown one compact model.

Durable knowledge was now spread across explicit, version-controlled owners:

- architecture documentation;
- Bifröst client/API documentation;
- Midgard and Asgard communication boundaries;
- Butler Core, Wilfred and HAP repositories;
- ADRs;
- compatibility milestones such as IGNITION-001;
- GitHub Issues;
- release/tag/workflow evidence;
- live-system proving.

Keeping a separate local model as an authority would have recreated the same
problem solved earlier when the development ledger moved to GitHub: two sources
could drift.

## Successor model

The successor is not another single file.

The **documentation corpus itself is the project model**.

```text
durable architecture / ownership
        -> versioned documentation

active work
        -> GitHub Issues

merged implementation
        -> repository main

release evidence
        -> tags / releases / workflows

runtime truth
        -> live systems
```

Agent entrypoints such as `AGENTS.md`, `docs/agent/` and `docs/llms.txt`
teach automated contributors how to navigate the same documentation rather than
maintaining a parallel AI-specific knowledge base.

## Historical preservation

The raw final local model is deliberately **not** published in the public
portfolio.

It contained operational details and identifiers appropriate to a private local
context but unnecessary for public architectural history.

This sanitized record preserves its architectural meaning without publishing
those details.

The earlier dated public-safe project-model snapshots remain immutable
historical artifacts.
