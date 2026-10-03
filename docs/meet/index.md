---
title: Meet Butler
kind: concept
scope: public
status: current
---

# Meet Butler

A smart home usually starts by teaching people the names of devices, entities,
apps and automations.

Butler turns that around.

## Talk to your home through a Butler

**The Butler knows the house. You describe the outcome you want.**

You should not have to remember whether the television belongs to one
integration, the lights to another, the washing machine to a vendor API and the
energy system to Home Assistant.

The Butler's job is to understand the request, find the capability that owns it,
apply policy and permissions, talk to the right system and, when possible,
verify what actually happened.

```text
You
  -> intent
  -> Butler
  -> capability / domain
  -> integration / service
  -> real world
```

The house remains made of many systems. The Butler is the layer that knows how
to speak with them without pretending to replace them.

## What this means in practice

Instead of thinking:

> Which app controls this? Which entity is it? Which API do I need?

the interaction becomes closer to:

> Make the living room ready for a movie.

or:

> Is the washing machine finished?

or:

> Turn that on, but tell me when it is actually on.

A Butler can use deterministic capabilities for known requests and planning or
AI where an open-ended goal genuinely needs it. Policy, permissions,
confirmation and verification still apply.

## A Butler is not the house

Home Assistant remains the physical orchestration owner in Keriol Home.

The Butler does not replace integrations, devices or automation platforms. It
reasons across them and invokes explicit capabilities.

That separation is a core architectural rule, not a marketing metaphor.

## Butler family

The public ecosystem currently includes:

- **Butler Core**, provider-neutral contracts and execution foundations;
- **Wilfred**, the reusable public Butler runtime;
- **Home Assistant Plugin**, the reusable Home Assistant integration;
- **Bifröst**, the external/client API boundary;
- **Midgard**, provider-neutral communication and cross-Butler routing;
- **Butler Interphone**, the Android client.

**Alfred** is the private Keriol Home Butler and real-world proving ground.

## Where to go next

If you want to understand the system, continue with
[Fundamental Concepts](fundamentals.md).

If you want the engineering detail, jump to the
[Architecture Overview](../architecture/overview.md).

If you want to see what has actually been built, browse the
[Portfolio](../portfolio/index.md).
