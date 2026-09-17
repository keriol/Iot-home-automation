# ADR-012 - Sibling Butler Runtimes and Independent Platform Plugins

## Status

Accepted

## Context

The Butler architecture originally evolved through a staged extraction path from the private Keriol Home deployment.

ADR-008 captured an important intermediate architecture in which Wilfred was treated as the reusable Butler runtime layer beneath Alfred. That model helped separate reusable runtime behavior from household-specific behavior while Butler Core was still comparatively small.

The architecture has since matured further.

Butler Core now owns the provider-neutral contracts shared by Butler runtimes and reusable plugins. Wilfred has adopted those contracts as the public reusable Butler runtime, while Alfred has continued evolving as the private Keriol runtime and proving ground without needing Wilfred as an architectural runtime dependency.

At the same time, the Home Assistant integration has matured beyond a Wilfred-owned plugin. Home Assistant Plugin (HAP) now has its own repository and depends on Core-owned contracts so multiple Butler runtimes can consume the same integration independently.

Keeping Alfred conceptually below Wilfred, or keeping reusable platform integrations owned by one runtime, would create unnecessary coupling and obscure component ownership.

## Decision

The Butler ecosystem uses a sibling-runtime architecture built on Butler Core.

### Butler Core

Butler Core owns provider-neutral contracts and small execution foundations shared by Butler runtimes and reusable plugins.

Core must remain service-agnostic and must not acquire concrete Home Assistant, Keriol, Alexa or other deployment-specific behavior.

Core contracts do not make Core responsible for runtime plugin discovery, loading, composition or concrete domain behavior.

### Wilfred

Wilfred is the public reusable Butler runtime built on Butler Core.

Wilfred owns its own runtime composition, plugin loading, deterministic-first resolution, planning/fallback integration, execution boundaries and standalone interfaces.

Wilfred is not the architectural runtime base of Alfred.

### Alfred

Alfred is the private Keriol Home Butler runtime and real-world proving ground built on Butler Core contracts.

Alfred owns Keriol-specific composition, context, routing, policy, private domains, integrations and AI fallback.

Alfred may reuse public Butler packages and plugins without depending on Wilfred as a runtime.

### Independent Platform Plugins

A reusable platform integration should depend on the lowest appropriate provider-neutral contracts rather than on a concrete Butler runtime when it can be consumer-neutral.

Home Assistant Plugin (HAP) is the first explicit example of this model.

The architectural relationship is:

```text
                 Butler Core
                /     |      \
               /      |       \
          Wilfred     HAP     Alfred
                       |
                 Home Assistant
```

Wilfred and Alfred may consume HAP independently. Neither runtime becomes a dependency of the other through that integration.

Future integrations for other automation managers may follow the same pattern when their behavior is reusable across Butler runtimes.

## Home Assistant Boundary

Home Assistant remains the owner of devices, integrations, dashboards, device state and physical orchestration.

HAP owns reusable Home Assistant transport, configuration, state and action behavior exposed through Butler-compatible contracts.

Each Butler runtime remains responsible for its own semantic routing, policy, permissions, confirmation and composition.

For observable physical actions, the preferred lifecycle remains:

    READ -> ACTION -> READ -> VERIFY

Successful dispatch is not proof of physical success.

## Public and Private Boundary

The sibling-runtime model does not make private Alfred behavior automatically public.

Reusable behavior may graduate from Alfred into Butler Core, Wilfred or an independent public plugin only after ownership is clear, private assumptions are removed, tests exist, public-safe documentation is available and clean installation/runtime evidence supports extraction.

Some Keriol-specific behavior will intentionally remain private.

## Consequences

### Positive

- Wilfred and Alfred can evolve independently while sharing stable Core contracts.
- Alfred no longer needs a conceptual or package dependency on Wilfred.
- Reusable platform integrations can serve multiple Butler runtimes without runtime-specific coupling.
- Home Assistant ownership remains separate from Butler runtime ownership.
- New runtimes and platform plugins can be added without changing the fundamental architecture.
- Public extraction has clearer destination choices: Core, a runtime, or an independent plugin.

### Negative

- Documentation must distinguish runtime responsibilities from shared Core contracts and plugin responsibilities more carefully.
- Similar composition concerns may exist independently in multiple runtimes and therefore require deliberate contract design to avoid accidental duplication.
- Plugin compatibility must be validated against the Core contracts and each consuming runtime rather than assumed through a single Wilfred-owned integration path.

## Supersession

This ADR supersedes ADR-008 for the current runtime relationship between Butler Core, Wilfred and Alfred.

ADR-008 remains an important historical record of the extraction phase in which Wilfred was treated as Alfred's reusable runtime base. Its historical decision text should not be rewritten retroactively.

ADR-008 continues to provide useful context for why reusable runtime behavior was extracted from Alfred, but this ADR defines the current architecture.
