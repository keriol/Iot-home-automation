---
title: Released Public Ecosystem
kind: ecosystem
scope: public
status: current
---

# Released Public Ecosystem

This page lists the Butler components that are released in public repositories
and can be evaluated or installed without access to the private Keriol Home
runtime.

## Public released components

| Component | Role | Released baseline |
| --- | --- | --- |
| Butler Core | Provider-neutral contracts and execution foundations | 0.3.0 |
| Wilfred | Reusable public Butler runtime | 0.2.2 |
| Home Assistant Plugin | Reusable Home Assistant integration | 0.3.0 |
| Bifröst | External/client API boundary | 0.1.0 |
| Midgard | Provider-neutral communication and cross-Butler routing | 0.1.0 |
| Butler Interphone | Android client | 0.1.0 |
| [Butler Asgard Plugin](https://github.com/keriol/butler-asgard-plugin) | Butler-owned identity and ingress boundary | [0.1.0 Public Alpha](https://github.com/keriol/butler-asgard-plugin/releases/tag/v0.1.0) |

Development-line versions on `main` are not release claims.

## What you can build today

A public installation can start from Wilfred and grow incrementally:

```text
Wilfred
  |
  +-> optional Home Assistant Plugin
  |
  +-> optional Bifröst + Midgard
  |
  +-> optional Butler Interphone
```

For a first installation, use
[Install a Butler in your home](../install/index.md).

## Asgard: standalone Public Alpha after Ignition

[Butler Asgard Plugin 0.1.0](https://github.com/keriol/butler-asgard-plugin/releases/tag/v0.1.0)
is now a publicly released, standalone Python package for per-Butler identity
projection and governed ingress composition. The release contains a wheel and
source archive and is not a claim that it is published on PyPI.

The historical IGNITION-001 bill of materials is **unchanged**: that release
used an internal Alfred-owned Asgard compatibility boundary, not the later
standalone distribution. Alfred privately adopted the earlier standalone
`0.1.0.dev0` development revision through its own adapter.

The Public Alpha does **not** provide network transport or Midgard routing,
profile-image loading/projection, an independently proven second Butler
consumer, or runtime-owned policy and authentication.

See [Asgard](../architecture/asgard.md).

## Not included here

Private Keriol behavior and Alfred-specific domains are intentionally not part of
the released public ecosystem list.

Those belong to the
[Development & Proving Ground](development.md) section.
