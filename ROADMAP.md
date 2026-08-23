# Roadmap

Keriol Home evolves as a local-first smart-home platform with a reusable public Butler stack and a private real-world proving ground.

The roadmap distinguishes **released/public baseline**, **current development direction**, and **private validated capability work**. Open issues and branches do not become portfolio feature claims until supported by merged, released or validated evidence.

## Current Foundation

### Smart-home platform

- Home Assistant owns physical orchestration, dashboards, device wrappers and integration state.
- MQTT is the event and telemetry bus.
- Node-RED owns visual multi-event flows where it remains the clearest implementation layer.
- Python services own complex validation, APIs and stateful workflows.
- Tailscale provides private administration.
- Cloudflare Tunnel provides narrow public integration entrypoints where required.

### Public Butler stack

- Butler Core `0.1.4` is the current released Core baseline used by Wilfred `0.2.1`.
- Butler Core `main` is on the `0.1.5.dev0` development line.
- Wilfred `0.2.1` is the current Public Alpha.
- Wilfred provides registered tools, deterministic-first resolution, planning interfaces, workflows, confirmation boundaries, verified execution, output contracts and standalone APIs.
- `wilfred-home-assistant` is the official public Home Assistant plugin and remains on its `0.1.0.dev0` development line.
- Home Assistant remains the owner of devices and physical orchestration.
- Observable actions follow READ -> ACTION -> READ -> VERIFY where practical.

### Private Keriol deployment

- Alfred `0.4.0` is the released private baseline; development continues on `main`.
- Alfred is the Keriol Home Butler deployment and real-world proving ground.
- Wilfred provides the reusable Butler runtime layer; Butler Core provides provider-neutral foundations.
- Osvaldo owns proactive communication policy.
- Charon owns media intelligence and lifecycle behavior.
- Hermes owns delivery framework/provider responsibilities.
- Alexa is a replaceable frontend; speech and SSML remain frontend-specific details.
- GitHub Issues and Git own development state. Historical Umberto data is archival only.

## Near Term

### Capability-first Wilfred consolidation

The next public consolidation direction is capability-first rather than version-driven.

Current tracked work includes:

- first-class capability and domain contracts;
- plugin-declared capability/domain ownership;
- runtime capability discovery and introspection;
- deterministic resolvers under capability ownership;
- capability discovery through CLI and HTTP surfaces;
- reusable developer validation and drift evidence;
- reproducible release BOM discipline as a gate for a future coherent release checkpoint.

These are development directions until their owning GitHub issues are completed and implementation evidence is merged.

### Alfred proving-ground convergence

- Continue moving reusable Alfred behavior toward Wilfred/Core only when ownership and contracts are genuinely reusable.
- Keep Keriol-specific policy, mappings and operations private.
- Exercise package-owned frontend contributions and provider-specific compilation privately before public extraction.
- Mature Alexa input/frontend boundaries separately from Hermes delivery responsibilities.
- Preserve deterministic behavior before AI fallback.
- Keep requested outcomes, policy, permissions, confirmation and observable verification explicit.

### Home Assistant plugin

- Migrate the official plugin to the capability-first model when the public Wilfred contracts are ready.
- Keep entity mapping and authorization configuration-driven.
- Preserve READ before ACTION where relevant state exists.
- Verify observable state after actions when practical.
- Never move physical orchestration ownership out of Home Assistant.

## Private Validated Domains

These capabilities are useful portfolio evidence even when they are not public Wilfred functionality.

### Voice and interaction

- Alexa Custom Skill and free-text interaction paths.
- Deterministic routing with AI fallback.
- Contextual confirmations.
- Fast acknowledgement before slower AI-backed responses.
- Frontend-specific speech and SSML rendering.
- Package/frontend contribution experiments remain private until maturity criteria are satisfied.

### Appliances

- Washing-machine status and program catalog.
- Allowlisted start and stop actions.
- Asynchronous physical-state verification.
- Proactive follow-up after verified state changes.
- Future energy-aware appliance suggestions remain candidates.

### Media

- Plex integration and media-domain intelligence through Charon.
- Search, scan, acquisition-lifecycle and playback workflows in the private proving ground.
- Pending offers, async completion and lifecycle analysis.
- Public documentation describes architecture and lessons, not private acquisition implementation.

### Proactive communication

- Osvaldo allow, defer, aggregate and deny policy.
- Quiet-hours and snoozable-delivery behavior.
- Requested replies are treated separately from generic proactive communication.
- Hermes handles delivery/provider concerns without acquiring domain policy ownership.

### Climate

- Room temperature and humidity sensing.
- Infrared and native climate-control paths.
- Advisory and experimental closed-loop strategies.
- Conservative verification where device feedback is incomplete.

### Energy

- Local photovoltaic telemetry.
- Battery state visibility.
- MQTT-based power and energy sensors.
- Surplus and abnormal-consumption analysis candidates.

### Presence and security

- BLE presence experiments.
- Home/away occupancy direction with privacy constraints.
- Camera and security integration review.
- Presence-aware notification candidates.

### Maker and operations

- Future 3D-printer READ and confirmed ACTION capabilities.
- Server and NAS observability.
- Backup and service-health visibility.
- Developer validation tooling is being proven privately before any reusable extraction.

## Public Extraction Principle

A capability validated in Alfred is not automatically a Wilfred feature.

Public extraction requires:

1. a reusable contract;
2. removal of Keriol-specific assumptions;
3. explicit permissions and confirmation semantics;
4. tests independent of the private deployment;
5. public-safe documentation;
6. clean installation/runtime evidence;
7. stable ownership demonstrated through real use.

Until then, the capability remains **Private validated**, **Candidate**, **In testing**, or **Designed to enable**.

## Release Discipline

Version numbers are checkpoints, not task containers.

- One issue or commit does not imply a release.
- Release scope comes from explicit GitHub/Git/tag/release evidence.
- Public release claims must distinguish source state, artifact state and observable verification.
- Wilfred `0.2.1` remains the current Public Alpha until a later release is explicitly completed and verified.

## Documentation Maintenance

- GitHub Issues are authoritative for development planning/status.
- Git `main` is authoritative for merged implementation/documentation state.
- Tags/releases/workflows provide release evidence.
- Live systems provide runtime evidence.
- The portfolio is a derived public-safe view, not another development ledger.
- Current architecture documents should be refreshed after meaningful architecture, maturity or release changes.
- Historical ADRs, worklogs and dated snapshots remain historical.
- The current public project model may evolve; historical project-model snapshots are not rewritten.
- Private implementation, endpoints, credentials, machine paths and acquisition internals remain outside the public portfolio.
