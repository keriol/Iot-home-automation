HOME AUTOMATION PROJECT CONTEXT - PUBLIC (<8K>)
UPDATED: 2026-09-17

PURPOSE

Public-safe derived architectural context for Keriol Home and the reusable Butler ecosystem.

This file is not a task ledger, roadmap database, release evidence store or runtime-status source. It provides compact context about architecture, responsibilities, maturity and engineering principles.

SOURCES OF TRUTH

* GitHub Issues are authoritative for development tasks, priorities, dependencies, planning and active status.
* Git main is authoritative for merged implementation and versioned documentation.
* Commits, tags, workflows and releases provide implementation and release evidence.
* Live systems are authoritative for deployed behavior, service health and physical state.
* This file is a derived public snapshot refreshed after meaningful architectural, boundary or release changes.

VISION

Keriol Home is the private real-world proving ground behind a reusable public Butler stack.

Butler Core -> Butler runtimes / reusable plugins

* Butler Core provides provider-neutral contracts and execution foundations.
* Wilfred is the reusable public Butler runtime built on Butler Core.
* Alfred the Butler is the private Keriol Home sibling runtime/deployment and proving ground.
* Home Assistant Plugin (HAP) is the reusable public Home Assistant integration package built on Core-owned contracts and consumable by Butler runtimes.
* Home Assistant remains the owner of devices, integrations, dashboards and physical orchestration.
* Reusable Alfred behavior moves outward only after generalization, tests and sanitization.

Motto: "Alfred non è il software della casa. Alfred è colui che sa parlare con tutti i software della casa."

CURRENT PUBLIC BASELINE

* Butler Core 0.2.0 is the current released Core baseline.
* Core 0.2.0 provides the provider-neutral execution, asynchronous-job, tracing and domain/capability contribution baseline used by higher-level Butler consumers.
* Wilfred 0.2.2 is the current released Public Alpha baseline and adopts the Core 0.2.0 domain/capability/plugin contribution contracts while preserving Wilfred-owned runtime behavior.
* Wilfred main is on the 0.2.3.dev0 development line; development state is not a release claim.
* Home Assistant Plugin lives at https://github.com/keriol/home-assistant-plugin and is currently on its 0.2.0.dev0 development line while the consumer-neutral Core boundary is consolidated.
* HAP is the canonical task namespace for current Home Assistant Plugin work. Historical WHA/WILF identifiers remain useful only as historical aliases.
* Alfred 0.4.0 is the current private released baseline; post-0.4.0 development continues privately.

Release claims use explicit tag/release evidence. Open branches and issues describe development direction only.

CAPABILITY MODEL

Wilfred is capability-first.

* integration/provider = connection to an external service;
* tool = typed executable operation;
* capability = something the Butler knows how to do;
* domain = owner of related knowledge and behavior;
* goal = requested outcome.

Plugins package tools and domain behavior. Conversation code must not own domain knowledge.

Known requests resolve deterministically first. Open goals may fall back to planning or AI.

Policy, permissions, confirmation and validation still govern execution.

Observable actions follow:

READ -> ACTION -> READ -> VERIFY

Dispatch is not proof of physical success.

PUBLIC BUTLER STACK

Butler Core:

* provider-neutral contracts and small execution primitives;
* tool/registry, planner, deterministic-resolution and execution contracts;
* provider-neutral asynchronous job requests/results and lifecycle protocols;
* structured tracing with trace context, status/severity/levels and fail-safe tracer abstraction;
* reusable domain, capability, plugin/contribution and goal-expectation declarations with conformance helpers;
* provider-neutral readiness/capability-availability and explicit user-authorization development contracts may exist on Core main after the released 0.2.0 baseline, but remain development state until released;
* provider-neutral output contracts;
* no plugin discovery/loading/lifecycle, concrete domain behavior, provider configuration, frontend rendering or deployment-specific behavior;
* no Keriol, Alexa or Home Assistant device-specific behavior;
* provider-neutral and service-agnostic.

Wilfred:

* public reusable Butler runtime;
* deterministic-first resolution;
* registered tools and workflows;
* planning interfaces and confirmation boundaries;
* verified execution and output contracts;
* plugin loading and standalone interfaces;
* released 0.2.2 adoption of Core-owned domain, capability, plugin and goal-expectation declarations;
* owns runtime discovery/loading/composition behavior rather than delegating those responsibilities to Core.

Home Assistant Plugin (HAP):

* official public Home Assistant integration package;
* canonical repository: https://github.com/keriol/home-assistant-plugin;
* built around Core-owned Butler contracts rather than a dependency on Wilfred;
* explicit typed interaction with Home Assistant;
* configuration-driven authorization;
* plugin-owned setup/discovery and provider introspection are under active development;
* Home Assistant remains the physical orchestration owner;
* Wilfred and Alfred may consume HAP independently without becoming runtime dependencies of one another.

PRIVATE PROVING GROUND

Alfred:

* private Keriol composition, context, routing and AI fallback;
* sibling Butler runtime to Wilfred, not a Wilfred runtime wrapper or downstream runtime dependency;
* exercises reusable Butler behavior against a real operating home;
* keeps household-specific policy, integrations and experimental behavior private.

Osvaldo:

* proactive communication policy;
* allow, defer, aggregate, deny and quiet-hours behavior;
* policy owner, not delivery provider.

Charon:

* media intelligence and lifecycle behavior;
* discovery, identity, quality, playback and observation concerns.

Hermes:

* private delivery framework/provider boundary;
* routes provider-neutral output toward provider-specific delivery;
* delivery does not acquire domain or communication-policy ownership.

Alexa:

* current voice frontend and first Hermes target;
* speech and SSML are frontend details;
* the configured Giorgio voice used for Alfred Alexa speech notifications is a frontend rendering parameter, not an architectural component.

Detailed Keriol implementation and operational state remain private.

INTERACTION

Reusable public runtime path:

Client -> Wilfred -> Registered Capability / Plugin -> Service

Keriol proving-ground path:

Frontend -> Alfred -> Registered Capability / Plugin -> Service

Reusable Home Assistant path:

Butler Runtime -> HAP -> Home Assistant

Proactive communication path:

Domain Event -> Osvaldo Policy -> Hermes Delivery -> Provider / Frontend

HOME ASSISTANT BOUNDARY

* Home Assistant remains the smart-home platform.
* Home Assistant owns physical orchestration, device wrappers, integrations, dashboards and device state.
* Wilfred and Alfred reason, route and invoke capabilities rather than replacing Home Assistant.
* Reusable Home Assistant integration belongs in Home Assistant Plugin (HAP), not in Butler Core and not exclusively in Wilfred.
* HAP owns reusable Home Assistant transport/configuration/state/action behavior while each Butler runtime owns its own composition, policy and semantic routing.

ARCHITECTURE RULES

* One owner layer/domain per feature.
* Home Assistant owns physical orchestration.
* Butler Core stays provider-neutral and service-agnostic.
* Core contribution contracts do not imply Core owns runtime plugin discovery/loading/lifecycle.
* Wilfred and Alfred remain sibling runtimes; neither is the architectural runtime base of the other.
* Reusable platform integrations should depend on Core-owned contracts rather than a concrete Butler runtime when the integration can be consumer-neutral.
* Deterministic behavior precedes AI fallback for known requests.
* AI receives only the minimum necessary context.
* ACTION/DANGEROUS operations require confirmation when appropriate.
* Observable actions verify post-action state.
* Frontends remain replaceable.
* Presentation stays out of Core.
* Delivery providers do not own domain policy.
* Private validation never automatically becomes a public roadmap commitment.

CAPABILITY MATURITY

Available:

Public, documented and usable in the relevant public repository/component.

In testing:

Implemented and exercised privately or under active validation, but not a public release promise.

Designed to enable:

Architecturally supported direction without an implementation claim.

Open issues or branches never justify an Available claim by themselves.

PUBLIC EXTRACTION

A private capability is not automatically a Wilfred feature.

Public extraction requires:

* a reusable contract and correct owner layer/domain;
* removal of Keriol-specific assumptions;
* explicit permissions/confirmation/failure semantics;
* independent tests;
* sanitization and public-safe documentation;
* clean installation/runtime evidence.

Some private capabilities will intentionally remain private.

PUBLIC BOUNDARY

Public material may contain:

* architecture;
* ADRs;
* reusable engineering lessons;
* sanitized case studies;
* maturity claims backed by evidence;
* public-safe conceptual diagrams.

Public material must not contain:

* readable private Alfred implementation;
* secrets, credentials or private endpoints;
* personal data;
* unnecessary real entity/device identifiers;
* sensitive operational state;
* private acquisition implementation;
* machine-specific private server paths unless intentionally public and necessary.

Historical documents may preserve superseded architecture when clearly historical.

REFERENCE MAP

* Butler Core: https://github.com/keriol/butler-core
* Wilfred: https://github.com/keriol/butler-wilfred
* Home Assistant Plugin: https://github.com/keriol/home-assistant-plugin
* Keriol Home portfolio: https://github.com/keriol/Iot-home-automation

STACK

* Butler: Butler Core, Wilfred, Home Assistant Plugin and the private Alfred proving ground.
* Automation: Home Assistant, MQTT, Node-RED, HACS.
* Services: Python/FastAPI and provider integrations.
* Media/storage validation: Plex, Tautulli and network storage.
* Frontends/networking: voice frontends, Assist, Cloudflare Tunnel and Tailscale.

Exact household inventory is intentionally outside this public context.

CURRENT DIRECTION

* Keep Wilfred on Core-owned public contracts while preserving Wilfred-owned runtime discovery/loading/composition behavior.
* Continue capability-first/domain consolidation in Wilfred.
* Continue HAP consumer-neutral consolidation so Wilfred and Alfred can consume the same public Home Assistant integration independently.
* Continue converging reusable Alfred behavior onto Wilfred, Butler Core or independent public plugins while keeping Keriol-specific behavior private.
* Mature Hermes/Alexa privately before considering reusable/public extraction.
* Keep Home Assistant as the physical orchestration owner.
* Keep release baseline and development baseline distinct.
* Keep maturity explicit instead of presenting experiments or open branches as shipped features.

DEVELOPMENT GOVERNANCE

GitHub is the development source of truth.

The former Umberto development ledger is retired and archive-only. Historical Umberto records may remain useful for recovery and traceability but never override GitHub Issues, Git or runtime evidence.

CONTEXT MAINTENANCE

Refresh this file for durable architecture, ownership, public/private boundary, maturity-model or release-baseline changes.

Task state belongs in GitHub Issues. Implementation evidence belongs in Git. Release evidence belongs in tags/releases/workflows. Runtime evidence belongs in live systems.

HISTORICAL CONTEXT

Dated project-context snapshots preserve the architecture and terminology of their time and are not rewritten retroactively.
