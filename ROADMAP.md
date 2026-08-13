# Roadmap

Keriol Home evolves as a local-first smart-home platform with a reusable public Butler stack and a private real-world deployment.

The roadmap distinguishes public runtime work from capabilities that are already validated privately in Alfred.

## Current Foundation

### Smart-home platform

- Home Assistant owns physical orchestration, dashboards, device wrappers and integration state.
- MQTT is the event and telemetry bus.
- Node-RED owns visual multi-event flows where it is the clearest implementation layer.
- Python services own complex validation, planning, APIs and stateful workflows.
- Tailscale provides private administration.
- Cloudflare Tunnel provides narrow public integration entrypoints where required.

### Public Butler stack

- Butler Core `0.1.3` provides provider-neutral contracts and execution primitives.
- Wilfred `0.2.0.dev0` is the active development line toward the Public Alpha.
- Wilfred supports registered tools, workflows, planning, confirmation boundaries, output contracts and standalone HTTP APIs.
- Docker distribution and runtime verification are implemented for the Public Alpha path.
- `wilfred-home-assistant` provides the official public Home Assistant plugin.
- Home Assistant actions use explicit READ and ACTION capabilities.
- Verified workflows support READ -> ACTION -> READ -> VERIFY semantics.

### Private Keriol deployment

- Alfred is the private Keriol Home Butler deployment and real-world proving ground.
- Wilfred provides Alfred's reusable Butler runtime base.
- Butler Core provides the shared contracts underneath Wilfred and Alfred.
- Some older Alfred paths predate Wilfred and are still converging onto the reusable runtime.
- Osvaldo governs proactive communication policy.
- Charon owns media-domain intelligence.
- Umberto coordinates development ledger and checkout evidence.
- Alexa is currently a frontend; speech and SSML rendering remain frontend-specific implementation details.

## Near Term

### Wilfred Public Alpha

- Complete the `0.2.0` release checkout.
- Publish and verify the stable public container distribution.
- Finalize compatible Butler Core, Wilfred and official Home Assistant plugin versions.
- Verify installation and runtime behavior from clean environments.
- Complete public launch documentation close to the actual release.
- Keep crowdfunding activation disabled until the real verified `0.2.0` release.

### Alfred convergence

- Continue moving reusable Alfred behavior onto Wilfred and Butler Core.
- Preserve Keriol-specific policy and integrations in Alfred.
- Keep legacy compatibility paths only while they are still required.
- Label private capabilities clearly rather than presenting them as already public.

### Home Assistant plugin

- Stabilize the official plugin for the Public Alpha.
- Keep entity mapping and authorization configuration-driven.
- Preserve READ before ACTION where state is relevant.
- Verify physical state after actions when observable.
- Keep Home Assistant as the owner of device orchestration.

## Private Validated Domains

These capabilities are useful portfolio evidence even when they are not yet public Wilfred functionality.

### Voice and interaction

- Alexa Custom Skill and free-text interaction paths.
- Deterministic routing with AI fallback.
- Contextual confirmations.
- Fast acknowledgement before slower AI-backed responses.
- Frontend-specific speech and SSML rendering.

### Appliances

- Washing-machine status and program catalog.
- Allowlisted start and stop actions.
- Asynchronous physical-state verification.
- Proactive follow-up after verified state changes.
- Future energy-aware appliance suggestions.

### Media

- Plex and Tautulli integration.
- Charon discovery and media-domain policy.
- Search, scan and playback workflows.
- Pending playback offers and lifecycle analysis.
- Future recommendation and catalog-quality capabilities.

### Proactive communication

- Osvaldo allow, defer, aggregate and deny policy.
- Quiet-hours and snoozable delivery behavior.
- Shared delivery paths without domain-specific policy duplication.

### Climate

- Room temperature and humidity sensing.
- Infrared and native climate-control paths.
- Advisory and experimental closed-loop climate strategies.
- Conservative verification where device feedback is incomplete.

### Energy

- Local photovoltaic telemetry.
- Battery state visibility.
- MQTT-based power and energy sensors.
- Surplus and abnormal-consumption analysis candidates.

### Presence and security

- BLE presence experiments.
- Home and away state development.
- Camera and security integration review.
- Presence-aware notification candidates.

### Maker and operations

- Future 3D-printer READ and confirmed ACTION capabilities.
- Server and NAS observability.
- Backup and service-health visibility.

## Public Extraction Principle

A capability validated in Alfred is not automatically a Wilfred feature.

Public extraction requires:

1. a reusable contract;
2. removal of Keriol-specific assumptions;
3. explicit permissions and confirmation semantics;
4. tests independent of the private deployment;
5. public-safe documentation;
6. clean installation and runtime verification.

Until then, the capability remains **Private validated** or **Candidate**.

## Documentation

- Keep current architecture documents aligned with implementation.
- Preserve historical ADRs, worklogs and milestone snapshots as historical records.
- Keep the public/private boundary explicit.
- Remove legacy readable implementation snapshots from the public portfolio and purge private-derived source from public history.
- Keep the public project model current without rewriting historical snapshots.
