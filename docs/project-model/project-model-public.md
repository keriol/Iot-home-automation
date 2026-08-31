HOME AUTOMATION PROJECT CONTEXT - PUBLIC (<8K>)
UPDATED: 2026-08-31

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

Butler Core -> Wilfred -> Alfred

* Butler Core provides provider-neutral contracts and execution foundations.
* Wilfred is the reusable public Butler runtime built on Butler Core.
* Alfred the Butler is the private Keriol Home deployment and proving ground.
* Home Assistant remains the owner of devices, integrations, dashboards and physical orchestration.
* Reusable Alfred behavior moves outward only after generalization, tests and sanitization.

Motto: "Alfred non è il software della casa. Alfred è colui che sa parlare con tutti i software della casa."

CURRENT PUBLIC BASELINE

* Butler Core 0.2.0 is the current released Core baseline.
* Core 0.2.0 adds the provider-neutral execution, asynchronous-job, tracing and domain/capability contribution baseline used by higher-level Butler runtimes.
* Wilfred 0.2.1 remains the current Public Alpha.
* Wilfred 0.2.1 must not be described as already adopting every Core 0.2.0 contract; consumer adoption is evidenced separately in the Wilfred repository.
* wilfred-home-assistant is the official Home Assistant plugin and is currently on its 0.1.0.dev0 development line.
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
* reusable domain, capability, contribution/plugin and goal-expectation declarations with conformance helpers;
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
* capability-first/domain adoption continues as a Wilfred-owned implementation concern even though Core 0.2.0 now provides reusable declarations.

wilfred-home-assistant:

* official public Home Assistant plugin;
* explicit typed interaction with Home Assistant;
* configuration-driven authorization;
* Home Assistant remains the physical orchestration owner.

PRIVATE PROVING GROUND

Alfred:

* private Keriol composition, context, routing and AI fallback;
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

Reusable public path:

Client -> Wilfred -> Registered Tool / Plugin -> Service

Keriol proving-ground path:

Frontend -> Alfred -> Wilfred Runtime -> Registered Capability -> Domain / Integration

Proactive communication path:

Domain Event -> Osvaldo Policy -> Hermes Delivery -> Provider / Frontend

HOME ASSISTANT BOUNDARY

* Home Assistant remains the smart-home platform.
* Home Assistant owns physical orchestration, device wrappers, integrations, dashboards and device state.
* Wilfred and Alfred reason, route and invoke capabilities rather than replacing Home Assistant.
* Public Home Assistant integration belongs in wilfred-home-assistant.

ARCHITECTURE RULES

* One owner layer/domain per feature.
* Home Assistant owns physical orchestration.
* Butler Core stays provider-neutral and service-agnostic.
* Core contribution contracts do not imply Core owns runtime plugin discovery/loading/lifecycle.
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
* Home Assistant plugin: https://github.com/keriol/wilfred-home-assistant
* Keriol Home portfolio: https://github.com/keriol/Iot-home-automation

STACK

* Butler: Butler Core, Wilfred and the private Alfred proving ground.
* Automation: Home Assistant, MQTT, Node-RED, HACS.
* Services: Python/FastAPI and provider integrations.
* Media/storage validation: Plex, Tautulli and network storage.
* Frontends/networking: voice frontends, Assist, Cloudflare Tunnel and Tailscale.

Exact household inventory is intentionally outside this public context.

CURRENT DIRECTION

* Adopt Core 0.2.0 contribution contracts in Wilfred without moving runtime discovery/loading ownership into Core.
* Continue capability-first/domain consolidation in Wilfred.
* Continue converging reusable Alfred behavior onto Wilfred/Core while keeping Keriol-specific behavior private.
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
