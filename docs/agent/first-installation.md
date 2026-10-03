---
title: First Installation Assistance
kind: agent-guide
scope: public
status: current
---

# First Installation Assistance

Use this path when the user is installing a Butler for the first time.

This is different from feature design. The goal is not to modify architecture:
it is to reach a known-good released baseline one boundary at a time.

## Entry rule

Prefer released/public installation instructions and immutable release evidence
over development `main` unless the user explicitly wants a development setup.

Do not silently upgrade, install extra tooling or switch to a development branch
to make an installation succeed.

## Security rule

Never ask the user to paste secrets, API keys, Home Assistant tokens, signing
keys or production credentials into chat.

Use environment variables, ignored local files or the secret/configuration
mechanisms documented by the owning repository.

## Stage 1 — Base Wilfred runtime

Start with the public Wilfred runtime before adding external providers.

Authoritative guides:

- [Wilfred README](https://github.com/keriol/butler-wilfred)
- [Installation and first run](https://github.com/keriol/butler-wilfred/blob/main/docs/installation.md)
- [Public onboarding](https://github.com/keriol/butler-wilfred/blob/main/docs/onboarding.md)
- [Docker distribution](https://github.com/keriol/butler-wilfred/blob/main/docs/docker.md)

First prove:

```text
Wilfred installed
    ↓
wilfred status
    ↓
wilfred tools
    ↓
deterministic demo.echo
```

Do not configure AI, Home Assistant or the external-client network until this
boundary is healthy.

If this stage fails, diagnose Wilfred/runtime packaging first.

Wilfred issue tracker:
https://github.com/keriol/butler-wilfred/issues

## Stage 2 — Optional AI / HTTP transport

Only after deterministic local behavior works:

- add the optional planner/provider if the user wants AI-backed goals;
- add the optional HTTP transport if the user needs an API;
- verify local health before exposing anything beyond loopback.

Do not treat planner success as execution-policy bypass.

## Stage 3 — Optional Home Assistant Plugin

If the user wants smart-home integration, add HAP only after the Butler runtime
is healthy.

Ownership:

```text
Butler runtime -> HAP -> Home Assistant
```

Verify READ-only integration/readiness first.

Only after a valid READ path exists should an ACTION be tested.

For observable actions use:

```text
READ -> ACTION -> READ -> VERIFY
```

HAP repository:
https://github.com/keriol/home-assistant-plugin

HAP issue tracker:
https://github.com/keriol/home-assistant-plugin/issues

Home Assistant remains the physical orchestration owner.

## Stage 4 — Optional external client network

Only users who need an external/mobile client need this layer.

Canonical topology:

```text
Interphone / external client
        ↓
     Bifröst
        ↓
     Midgard
      ↙   ↘
   Core   Butler-owned Asgard
             ↓
        concrete Butler
```

Read before setup:

- [Bifröst API](../api/bifrost.md)
- [Midgard](../architecture/midgard.md)
- [Asgard](../architecture/asgard.md)
- [IGNITION-001](../milestones/ignition-001.md)

Keep the layers separate during diagnosis:

1. Bifröst endpoint reachable/authenticated;
2. Midgard routing healthy;
3. Core-facing request works;
4. concrete Butler/Asgard request works;
5. Interphone/client compatibility and rendering works.

Do not skip directly to Android debugging if the Bifröst/Midgard server path is
not already proven.

## Stage 5 — Evidence and handoff

At each stage record:

- what was installed;
- exact released/development version;
- what command/request was used;
- what observable result proved success;
- which boundary failed if it did not succeed.

A successful HTTP response or dispatch is not proof of physical success.

## Escalation to development work

If installation fails because released documentation, packaging or compatibility
is wrong, that is no longer ordinary installation assistance.

Switch to the normal development workflow:

```text
GitHub Issue -> branch -> fix -> tests -> main
```

Link the installation evidence to the issue in the owning repository rather
than working around the defect locally.

## Related GitHub work

- Wilfred public onboarding: https://github.com/keriol/butler-wilfred/issues/76
- Wilfred first-install reconciliation: https://github.com/keriol/butler-wilfred/issues/125
- IGNITION-001 coordination: https://github.com/keriol/Iot-home-automation/issues/17
