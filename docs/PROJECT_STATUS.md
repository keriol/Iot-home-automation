# Home Automation Project Status

Last Updated: 2026-10-03

## Overview

The Butler documentation distinguishes two different evidence surfaces:

1. **Released Public Ecosystem** — components released in public repositories and
   usable without access to the private Keriol deployment.
2. **Development & Proving Ground** — Alfred/Keriol behavior exercised privately
   to validate ideas before possible public extraction.

These must not be mixed into one availability claim.

Home Assistant remains the physical orchestration owner.

## Released Public Ecosystem

| Component | Status | Released baseline |
| --- | --- | --- |
| Butler Core | Available | `0.3.0` |
| Wilfred | Available / Public Alpha | `0.2.2` |
| Home Assistant Plugin | Available | `0.3.0` |
| Bifröst | Available | `0.1.0` |
| Midgard | Available | `0.1.0` |
| Butler Interphone | Available | `0.1.0` |

Current development lines on `main` are not release claims.

See [Released Public Ecosystem](ecosystem/released.md).

## Ignition and the Asgard exception

IGNITION-001 released and proved the public client/communication stack:

```text
Interphone -> Bifröst -> Midgard -> Butler Core -> HAP -> Home Assistant
```

It also proved the concrete-Butler branch:

```text
Interphone -> Bifröst -> Midgard -> Butler-owned Asgard -> Alfred
```

Asgard is therefore part of the documented released architecture.

However, for IGNITION-001:

- Asgard compatibility version is `0.1.0`;
- the implementation is owned internally by Alfred;
- no independent public Asgard package/repository/tag is claimed.

This makes Asgard a **released architectural compatibility boundary**, not an
installable standalone public component.

## Development & Proving Ground

Alfred is the private Keriol Butler runtime and real-world proving ground.

It is not a public distribution and must not be presented as a prerequisite for
using Wilfred or the released public ecosystem.

Public-safe documentation may describe development themes such as:

- verified physical actions;
- appliance/domain semantics;
- proactive communication policy;
- media-domain reasoning;
- frontend/delivery experiments;
- energy, climate and presence ideas;
- interaction patterns that may later graduate into reusable contracts.

Unless public release evidence exists elsewhere, those areas are **In testing**
or **Designed to enable**.

See [Development & Proving Ground](ecosystem/development.md).

## Public/private extraction rule

A private Alfred behavior becomes public only after:

- stable ownership;
- generalization;
- independent tests;
- sanitization;
- public documentation;
- clean installation/runtime evidence;
- explicit release evidence in an owning public repository.

Working privately is not the same as being publicly available.

## Safety model

Current design rules include:

- one owner layer/domain per feature;
- deterministic behavior before AI fallback for known requests;
- explicit confirmation for sensitive actions when appropriate;
- successful dispatch is not proof of physical success;
- observable actions use `READ -> ACTION -> READ -> VERIFY` where practical;
- frontend presentation stays outside Butler Core;
- AI receives only the context needed for the task.

## Sources of truth

- GitHub Issues: tasks, priorities, dependencies and active status;
- repository `main`: merged implementation and documentation;
- tags/releases/workflows: release evidence;
- live systems: deployed/runtime truth;
- this documentation corpus: durable architecture, boundaries and engineering knowledge.

## Documentation status

The repository-backed documentation corpus is the active durable project model.

Historical material remains available for evolution/context but does not override
current release or runtime evidence.
