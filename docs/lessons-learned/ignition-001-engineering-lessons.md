---
title: IGNITION-001 Engineering Lessons
kind: lessons-learned
scope: public
status: released-evidence
baseline: ignition-001
---

# IGNITION-001 Engineering Lessons

IGNITION-001 did more than prove component compatibility. It exposed several
engineering rules that now shape the Butler communication architecture.

## 1. Request correlation must survive the whole trip

A client-visible request identifier is useful only if it remains stable through
transport, routing and the concrete Butler boundary.

The released proving confirmed a non-empty correlation identifier at the Android
client after the round trip.

## 2. Butler identity must come from the Butler

Bifröst and Midgard must never fabricate the responding Butler identity.

The concrete Butler owns its canonical identity. Asgard projects it. Midgard
routes using that projection, and Bifröst transports the response.

Ignition proved canonical:

```text
Source Butler: Alfred
```

at the Android client.

## 3. Core-facing and Butler-facing requests are complementary

The network supports both:

```text
Bifröst -> Midgard -> Core
```

and:

```text
Bifröst -> Midgard -> Asgard -> concrete Butler
```

This prevents every external request from requiring a concrete Butler while
preserving a governed boundary for Butler-owned behavior.

## 4. Dispatch is not physical success

For observable actions the preferred lifecycle remains:

```text
READ -> ACTION -> READ -> VERIFY
```

Ignition proved this rule through a real Home Assistant action from the Android
client.

## 5. Client acknowledgement and physical completion have different budgets

A real media playback request exposed a false client failure:

- the Android HTTP request exceeded the client transport timeout;
- the physical action later completed successfully.

The problem was not the action. The problem was coupling the HTTP response budget
to the physical verification budget.

The resulting rule is:

```text
client acknowledgement != physical completion
```

Bifröst-originated interactions therefore preserve interaction origin so a
capable runtime can return a bounded acknowledgement while long-running verified
work continues asynchronously.

## 6. Transport should remain replaceable

Bifröst transports client protocol concerns. It does not acquire domain behavior,
Butler identity or cross-Butler routing policy.

This makes another client possible without cloning Alfred or Midgard knowledge.

## 7. Historical proving seams must not become architecture by accident

An early proving path connected Bifröst directly to Asgard.

That path was useful for bootstrapping, but the canonical topology is:

```text
Bifröst -> Midgard -> Asgard
```

Historical proving code is evidence, not automatically the final ownership
model.

## 8. Self-description should be owner-declared

Clients should not infer runtime anatomy from component names.

Core plugins, Butler identity, entities, capabilities and Butler-local components
must come from authoritative owner metadata and then be aggregated/transported
by Midgard/Bifröst.

## 9. Interactive reply and proactive delivery are different problems

The request/reply communication stack is bidirectional by design.

A future ordinary interactive reply can return through the active communication
boundary, while proactive/asynchronous communication has no active call stack
and therefore requires separate delivery policy/provider work.

This distinction remains important even where the full interactive-output design
is still post-Ignition work.


## GitHub evidence trail

Selected work behind these lessons:

- [ALF-220 — preserve Bifröst interaction origin for deferred client actions](https://github.com/keriol/alfred/issues/361)
- [ALF-184 — Alfred 0.5.0 Butler-to-Android proving release](https://github.com/keriol/alfred/issues/300)
- [MID-003 — Midgard routing observability through Georges](https://github.com/keriol/butler-core-midgard-plugin/issues/5)
- [BIF-011 — composed client node manifest](https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues/20)
- [DOC-012 — consolidate Ignition architecture and engineering lessons](https://github.com/keriol/Iot-home-automation/issues/25)

These links explain implementation/design lineage. Current capability and release
claims still follow the source-of-truth rules above.
