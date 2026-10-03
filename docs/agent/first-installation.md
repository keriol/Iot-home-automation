---
title: First Installation Assistance
kind: agent-guide
scope: public
status: current
---

# First Installation Assistance

Use this path when the user is trying to install a public Butler for the first
time.

This is deliberately different from feature development. The goal is to reach a
small verified working system one boundary at a time.

## 1. Identify what is actually being installed

For a normal public first installation, start from **Wilfred**, the reusable
public Butler runtime.

Canonical installation documentation:

- [Wilfred onboarding](https://github.com/keriol/butler-wilfred/blob/main/docs/onboarding.md)
- [Installation and first run](https://github.com/keriol/butler-wilfred/blob/main/docs/installation.md)
- [Docker distribution](https://github.com/keriol/butler-wilfred/blob/main/docs/docker.md)

Do not treat private Alfred deployment instructions as public onboarding.

## 2. Prefer a released baseline

For a normal user installation, prefer a released Wilfred artifact and its
version-specific BOM/instructions.

Use development `main` only when the user explicitly wants development,
testing or contributor setup.

Do not silently mix versions from unrelated release/development lines.

## 3. Establish the base runtime first

Before enabling AI, Home Assistant or client networking, prove the deterministic
base runtime.

Minimum evidence:

```text
install
  -> CLI starts
  -> status/health succeeds
  -> tools can be listed
  -> demo.echo succeeds
```

If this boundary fails, diagnose it before adding another subsystem.

## 4. Add optional layers incrementally

Recommended order:

```text
Wilfred base runtime
        |
        +-> optional AI planner
        |
        +-> optional HTTP API
        |
        +-> Home Assistant Plugin
        |
        +-> Bifröst / Midgard client network
        |
        +-> Butler Interphone
```

A later layer must not be used to hide a broken earlier layer.

## 5. Home Assistant integration

When adding HAP:

- use the HAP repository documentation as the integration authority;
- keep Home Assistant credentials outside source control;
- start with READ/readiness checks;
- only attempt ACTION after the integration is healthy;
- for observable state-changing work prefer:

```text
READ -> ACTION -> READ -> VERIFY
```

Home Assistant remains the physical orchestration owner.

## 6. External client/network setup

Bifröst and Midgard are not prerequisites for proving that Wilfred itself
works.

Add them only when the user needs external Butler clients.

Read:

- [Bifröst API](../api/bifrost.md)
- [Midgard](../architecture/midgard.md)
- [Node Manifest and Self-Description](../architecture/node-manifest.md)

Then add Butler Interphone or another compatible client.

## 7. Secret handling

Never ask a user to paste API keys, Home Assistant tokens, Bifröst credentials,
private endpoints or signing secrets into chat.

Guide the user to:

- environment variables;
- ignored local configuration;
- GitHub Actions secrets;
- the secret/configuration mechanism documented by the owning repository.

When debugging, ask for sanitized errors and configuration shape rather than
secret values.

## 8. Diagnose one boundary at a time

Use the smallest failing boundary.

Examples:

```text
Python/venv
-> package install
-> Wilfred CLI
-> deterministic plugin
-> HTTP
-> HAP transport
-> Home Assistant state
-> Bifröst
-> Midgard
-> Android client
```

Do not reinstall unrelated tooling because a later integration failed.

## 9. Installation assistance is not feature development

If the requested solution requires changing product behavior or contracts,
switch to the [Feature Design Workflow](feature-design.md), search the owning
GitHub Issues/PRs, and create development work rather than patching around the
architecture during installation.

## Escalation

When a documented step appears wrong or stale, link the owning repository issue
tracker and open a documentation/product issue with the exact failing boundary
and evidence.

- [Wilfred issues](https://github.com/keriol/butler-wilfred/issues)
- [Home Assistant Plugin issues](https://github.com/keriol/home-assistant-plugin/issues)
- [Bifröst issues](https://github.com/keriol/Butler-Core-Bifrost-Plugin/issues)
- [Midgard issues](https://github.com/keriol/butler-core-midgard-plugin/issues)
- [Interphone issues](https://github.com/keriol/butler-interphone-android/issues)
