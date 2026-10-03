# Project Showcase

## How to read this page

The showcase is intentionally split into two worlds.

### Released Public Ecosystem

These examples are backed by public repositories and release evidence.

### Development & Proving Ground

These examples come from Alfred/Keriol private validation. They explain problems,
patterns and lessons without claiming that Wilfred already ships the behavior or
exposing private implementation details.

Maturity labels:

- **Available** — public, documented and released/usable;
- **In testing** — exercised privately or under active validation;
- **Designed to enable** — supported direction without an implementation claim.

---

# Released Public Ecosystem

## Butler foundations and reusable runtime

**Status: Available**

Current public building blocks:

- Butler Core `0.3.0`;
- Wilfred `0.2.2`;
- Home Assistant Plugin `0.3.0`;
- Bifröst `0.1.0`;
- Midgard `0.1.0`;
- Butler Interphone `0.1.0`.

Core owns provider-neutral contracts. Wilfred is the reusable public runtime.
HAP owns reusable Home Assistant integration behavior. Bifröst and Midgard own
the released client/communication boundaries.

[Released Public Ecosystem](ecosystem/released.md)

## IGNITION-001

**Status: Available / released compatibility baseline**

IGNITION-001 proved:

```text
Interphone -> Bifröst -> Midgard -> Butler Core -> HAP -> Home Assistant
```

and the concrete-Butler branch:

```text
Interphone -> Bifröst -> Midgard -> Butler-owned Asgard -> Alfred
```

Released/proven properties include:

- preserved request correlation;
- canonical source-Butler identity;
- client-safe node self-description;
- observable `READ -> ACTION -> READ -> VERIFY`;
- separation of client transport, cross-Butler routing and Butler identity.

### Asgard exception

Asgard is part of the released architectural compatibility model because the
boundary was proven by IGNITION-001.

The Ignition implementation is Alfred-owned and has compatibility version
`0.1.0`; no standalone public Asgard package is claimed.

[IGNITION-001](milestones/ignition-001.md) ·
[Asgard](architecture/asgard.md)

---

# Development & Private Proving Ground

The following examples are **not public Wilfred feature claims**.

They describe private proving themes and reusable lessons.

## Verified appliance interaction

**Status: In testing**

Private household workflows exercise status reads, controlled actions and
physical-state verification.

The durable public lesson is:

```text
READ -> ACTION -> READ -> VERIFY
```

Successful dispatch alone is not treated as physical success.

[Development & Proving Ground](ecosystem/development.md)

## Proactive communication policy

**Status: In testing**

Private proving separates:

- domain event ownership;
- communication policy;
- provider/delivery responsibility;
- frontend presentation.

The reusable question is not only whether a system can send something, but
whether it should interrupt, defer, aggregate or remain quiet.

## Media-domain reasoning

**Status: In testing**

Private proving explores media identity, discovery, playback/lifecycle reasoning
and observed-state verification as domain-owned behavior rather than scattered
conversation logic.

No private acquisition implementation is published here.

## Home-theater safe-power lessons

**Status: In testing / privately validated**

Real device startup sequencing demonstrated why physical orchestration and
recovery belong where state can be observed, typically Home Assistant.

## Local energy intelligence

**Status: In testing**

Local photovoltaic/grid/battery telemetry has been used as a proving source for
future household reasoning, but long-duration general-public readiness is not
claimed.

## Privacy-preserving presence

**Status: Designed to enable**

The preferred direction is intentionally small:

`occupied / empty / uncertain`

without requiring continuous room-level tracking.

## Frontend and delivery experiments

**Status: In testing / Designed to enable**

Voice and other private delivery paths are used to test replaceable frontend and
delivery concepts.

A working Alfred path does not imply that Wilfred currently ships that frontend
integration.

---

# Engineering themes that cross both worlds

- Home Assistant owns physical orchestration;
- Butler Core remains provider-neutral;
- deterministic paths precede AI fallback where appropriate;
- capability/domain ownership is explicit;
- dispatch and observed success are separate;
- frontends remain replaceable;
- public/private boundaries are architectural;
- private proving can inform public design without becoming public availability.

For implementation/installable status, always return to the
[Released Public Ecosystem](ecosystem/released.md).
