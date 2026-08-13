HOME AUTOMATION PROJECT CONTEXT - PUBLIC (<8K>)
UPDATED: 2026-08-13

PURPOSE

Public-safe derived architectural context for Keriol Home and the reusable Butler ecosystem.

This file is not a task ledger, roadmap database or runtime-status source. It provides compact context about architecture, responsibilities, maturity and engineering principles.

SOURCES OF TRUTH

* Git is authoritative for versioned public code, documentation, ADRs and repository history.
* Umberto is authoritative for active development state, milestones, dependencies and evidence.
* Live systems are authoritative for operational behavior and physical state.
* This file is a derived public snapshot refreshed after meaningful architectural, boundary or release changes.

VISION

Keriol Home is the private real-world proving ground behind a reusable public Butler stack.

Home Assistant remains the owner of physical orchestration, dashboards, integrations and device wrappers.

The Butler knows how to talk to services without becoming the smart-home platform itself.

Motto: "Alfred non è il software della casa. Alfred è colui che sa parlare con tutti i software della casa."

BUTLER LAYERING

Butler Core -> Wilfred -> Alfred

* Butler Core provides provider-neutral contracts and execution foundations.
* Wilfred is the reusable public Butler runtime built on Butler Core.
* Alfred the Butler is the private Keriol Home deployment and real-world proving ground.
* Some older Alfred paths predate Wilfred and are progressively converging onto the reusable runtime.
* wilfred-home-assistant is the official public Home Assistant plugin.

PUBLIC BUTLER STACK

Butler Core:

* provider-neutral contracts;
* shared execution foundations;
* planning and output contracts;
* no dependency on a specific smart-home platform or frontend.

Wilfred:

* registered tools and capabilities;
* deterministic execution and planning interfaces;
* workflows and verified execution;
* confirmation boundaries;
* output contracts;
* standalone HTTP APIs;
* plugin loading;
* container distribution.

wilfred-home-assistant:

* official public Home Assistant integration;
* explicit READ and ACTION capabilities;
* configuration-driven authorization;
* Home Assistant remains the physical orchestration owner.

PRIVATE PROVING GROUND

Alfred validates Butler behavior against a real operating smart home.

Sanitized private validation areas include:

* voice and interaction;
* proactive communication;
* appliances;
* media;
* energy;
* climate;
* presence;
* service observability;
* household operations.

Osvaldo validates proactive communication policy such as allow, defer, aggregate, deny and quiet-hours behavior.

Charon validates media-domain intelligence including discovery, quality, playback and lifecycle concepts.

Umberto coordinates the structured development ledger, multi-repository planning and checkout evidence.

Detailed Keriol implementation and operational state remain private.

INTERACTION

Reusable public path:

Client -> Wilfred -> Registered Tool / Plugin -> Service

Keriol proving-ground path:

Frontend -> Alfred -> Wilfred Runtime -> Registered Capability -> Service

Physical action model:

READ -> ACTION -> READ -> VERIFY

ARCHITECTURE RULES

* One owner layer per feature.
* READ before ACTION where current state matters.
* Sensitive actions require confirmation when appropriate.
* Successful dispatch does not prove physical success.
* Verify observable post-action state.
* Prefer deterministic behavior before AI fallback.
* Give AI only the context required for the task.
* Frontends remain replaceable.
* Presentation concerns stay outside Butler Core.
* Butler Core remains provider-neutral and service-agnostic.

CAPABILITY MATURITY

Public:

Implemented in Butler Core, Wilfred or an official public plugin.

Private validated:

Implemented and exercised in Keriol Home but not necessarily available publicly.

Candidate:

Private functionality that may later be generalized. Candidate status is not a release promise.

OPEN WORKSHOP

The public Butler repositories intentionally expose a smaller surface than the real-world workshop behind them.

Keriol Home continuously produces new domains, workflows, interaction patterns and plugin candidates.

Some will remain household-specific.

Some may graduate into Wilfred.

Some may become reusable or official plugins.

Crossing that boundary requires reusable contracts, tests, sanitization, documentation and clean installation/runtime evidence.

For builders, founders and early adopters, the public repositories therefore show the components that have already earned their way out of the proving ground while the portfolio shows the engineering process behind them.

HOME ASSISTANT BOUNDARY

* Home Assistant remains the smart-home platform.
* Wilfred does not replace Home Assistant.
* Alfred does not replace Home Assistant.
* Public Home Assistant integration belongs in the official Wilfred plugin.
* Physical orchestration and device wrappers stay with Home Assistant.

PUBLIC BOUNDARY

Public material may contain:

* architecture;
* ADRs;
* reusable engineering lessons;
* sanitized case studies;
* capability maturity;
* public-safe diagrams and conceptual flows.

Public material must not contain:

* readable private-derived implementation, even when identifiers are sanitized;
* secrets or credentials;
* personal data;
* private endpoints;
* unnecessary real entity IDs;
* sensitive operational details;
* private acquisition implementation.

Historical documents may preserve superseded architecture when they are clearly historical.

REFERENCE MAP

* Butler Core: https://github.com/keriol/butler-core
* Wilfred: https://github.com/keriol/butler-wilfred
* Home Assistant plugin: https://github.com/keriol/wilfred-home-assistant
* Keriol Home portfolio: https://github.com/keriol/Iot-home-automation

STACK

* Butler: Butler Core, Wilfred and the private Alfred proving ground.
* Automation: Home Assistant, MQTT, Node-RED, HACS.
* Services: Python 3.12 and FastAPI.
* Media/storage validation: Plex, Tautulli and network storage.
* Frontends/networking: voice frontends, Assist, Cloudflare Tunnel and Tailscale.

Exact household inventory is intentionally outside this public context.

CURRENT DIRECTION

* Finish Wilfred 0.2.0 Public Alpha readiness.
* Continue convergence of reusable Alfred behavior onto Wilfred and Butler Core.
* Graduate suitable private capabilities into reusable tools, workflows or plugins.
* Keep Home Assistant as the physical orchestration owner.
* Keep capability maturity explicit instead of presenting experiments as shipped features.

CONTEXT MAINTENANCE

Refresh this file for significant architectural, ownership, public/private boundary or release-baseline changes.

Task state, individual commits, test results and temporary service health belong to Umberto, Git or live runtime evidence.

HISTORICAL CONTEXT

Dated project-context snapshots preserve the architecture and terminology of their time and are not rewritten retroactively.
