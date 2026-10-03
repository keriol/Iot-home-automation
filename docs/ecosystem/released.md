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

## The Asgard exception

Asgard belongs to the public architecture model because IGNITION-001 proved the
Butler-owned ingress/identity boundary end to end.

However, in the Ignition release:

- Asgard compatibility version is `0.1.0`;
- the implementation is owned internally by Alfred;
- there is no independent public Asgard package/repository/tag;
- a future standalone reusable Asgard remains post-Ignition direction.

Therefore:

```text
Asgard = documented public architectural boundary
      != standalone public installable package
```

See [Asgard](../architecture/asgard.md).

## Not included here

Private Keriol behavior and Alfred-specific domains are intentionally not part of
the released public ecosystem list.

Those belong to the
[Development & Proving Ground](development.md) section.
