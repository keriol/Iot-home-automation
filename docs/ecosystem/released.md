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

## Post-Ignition standalone progress

After the Ignition release, a separately packaged `butler-asgard`
`0.1.0.dev0` development baseline was integrated into private Alfred
and exercised through the real Android Interphone client on 2026-10-10.

**Status: privately proven, not publicly released.**
This does not change the immutable IGNITION-001 release composition,
nor add Asgard to the public released-component table above.
Publication of the standalone repository remains subject to history and
metadata sanitization. Further Wilfred/Manfred consumer proving is future work.

## Not included here

Private Keriol behavior and Alfred-specific domains are intentionally not part of
the released public ecosystem list.

Those belong to the
[Development & Proving Ground](development.md) section.
