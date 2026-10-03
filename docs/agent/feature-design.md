---
title: Feature Design Workflow
kind: agent-guide
scope: public
status: current
---

# Feature Design Workflow

Use this sequence before proposing Butler code.

## 1. Classify the request

Identify:

- requested outcome;
- affected domain/capability;
- client-facing vs runtime-facing behavior;
- READ vs ACTION vs DANGEROUS behavior;
- public/reusable vs private/Keriol-specific scope.

## 2. Find the owner

Prefer one owner layer/component per feature.

Typical ownership:

- Butler Core: provider-neutral contracts/execution foundations;
- Bifröst: external client/API transport and correlation;
- Midgard: provider-neutral communication and cross-Butler routing;
- Butler-owned Asgard: concrete Butler ingress and identity;
- HAP: reusable Home Assistant integration behavior;
- Wilfred: public runtime composition;
- Alfred: private Keriol composition/policy/domain behavior;
- Interphone: Android presentation and client interaction.

If ownership is ambiguous, resolve that before implementation.

## 3. Read only relevant documentation

Read:

- the owning component page/repository;
- directly related architecture/API pages;
- relevant ADRs;
- relevant proven baselines/milestones.

Avoid loading unrelated domain detail into the design.

## 4. Inspect active work

Search GitHub Issues and open PRs in the owning repository before creating a new
task or design.

Do not create duplicate ownership or competing implementations.

## 5. Define boundaries

State explicitly:

- inputs/outputs;
- ownership;
- dependencies;
- permissions/confirmation;
- failure behavior;
- observability;
- public/private constraints.

## 6. Define evidence before code

Specify:

- unit/contract tests;
- integration tests;
- E2E path if relevant;
- observable post-action verification;
- release/runtime evidence required.

## 7. Implement through the normal workflow

Use:

```text
GitHub Issue -> branch -> commit -> main -> close
```

One focused feature per commit where practical.

## 8. Update documentation

If the change alters durable architecture, API surface, ownership or a proven
baseline, update the canonical documentation in the same development flow.
