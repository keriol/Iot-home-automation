# ADR-008 - Butler Core, Wilfred and Alfred Layering

## Status

Accepted

## Context

Keriol Home originally evolved around a private Alfred agent, a FastAPI service and a registered-tool architecture.

As the implementation matured, several concerns proved reusable outside the household deployment:

- execution contracts
- tool definitions
- permission and confirmation semantics
- planning interfaces
- workflow execution
- output contracts
- plugin-based integrations

Keeping those concerns embedded only in Alfred would couple reusable runtime behavior to one private smart-home deployment.

At the same time, pretending that every capability validated in Alfred already belongs to the public runtime would overstate the maturity and scope of Wilfred.

## Decision

The Butler architecture is separated into three explicit layers.

### Butler Core

Butler Core owns provider-neutral contracts and execution primitives.

It must not depend on Keriol Home, Home Assistant, Alexa or other deployment-specific services.

### Wilfred

Wilfred is the reusable public Butler runtime built on Butler Core.

It owns general runtime behavior such as registered capabilities, workflows, planning integration, confirmation boundaries, output handling and plugin loading.

Wilfred must remain usable independently of Alfred.

### Alfred

Alfred is the private Keriol Home Butler deployment.

Wilfred provides Alfred's reusable runtime base.

Alfred may add private policies, integrations, domain services and experimental capabilities required by Keriol Home.

Some legacy Alfred paths predate Wilfred and may continue to exist temporarily while migration proceeds.

## Home Assistant Boundary

Home Assistant remains the owner of physical orchestration, integrations, dashboards and device wrappers.

Wilfred and Alfred invoke explicit capabilities rather than becoming the smart-home platform.

For observable physical actions, the preferred workflow is:

    READ -> ACTION -> READ -> VERIFY

Successful dispatch is not equivalent to verified physical success.

## Capability Maturity

Public documentation uses three maturity labels:

- **Public**
- **Private validated**
- **Candidate**

Private validated means a capability is implemented and exercised in the real Alfred deployment.

Candidate means the capability may later be generalized into Wilfred or an official plugin.

Candidate status is not a release promise.

## Consequences

### Positive

- Reusable runtime behavior is no longer tied to one household.
- Alfred can continue evolving quickly as a real-world proving ground.
- Wilfred exposes only capabilities that have been intentionally generalized.
- Butler Core remains small and provider-neutral.
- Public documentation can describe private validation without overstating public availability.
- Home Assistant retains clear ownership of physical orchestration.

### Negative

- Some features temporarily exist in different maturity states across Alfred and Wilfred.
- Documentation must state those maturity differences explicitly.
- Legacy Alfred paths require gradual convergence rather than an artificial instant rewrite.

## Historical Documentation

Older ADRs, worklogs and milestone snapshots describe the architecture that existed at the time.

They should normally remain historical rather than being rewritten to pretend that Wilfred existed before it was extracted.

This ADR supersedes the current-architecture portions of ADR-007 where they describe Alfred Core as the reusable runtime boundary.
