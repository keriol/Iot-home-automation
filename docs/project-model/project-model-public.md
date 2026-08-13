HOME AUTOMATION PROJECT MODEL - PUBLIC
UPDATED: 2026-08-13

PURPOSE

Public-safe current model of Keriol Home and its relationship to the reusable Butler projects.

Historical decisions and superseded architecture remain in ADRs, worklogs, milestones and dated project-model snapshots.

PRINCIPLES

* Local-first whenever practical.
* Home Assistant owns physical orchestration, dashboards, integrations and device wrappers.
* MQTT is the event and telemetry bus.
* Node-RED owns visual multi-event flows where appropriate.
* Python services own complex validation, planning, APIs and stateful workflows.
* One owner layer per feature.
* READ before ACTION where useful state exists.
* Dispatch is not physical success.
* Verify observable physical state after ACTION when practical.
* Frontends remain replaceable.
* Public documentation must distinguish public functionality from private validation.

BUTLER LAYERING

Butler Core -> Wilfred -> Alfred

* Butler Core provides provider-neutral contracts and execution primitives.
* Wilfred is the reusable public Butler runtime built on Butler Core.
* Alfred is the private Keriol Home Butler deployment built on the reusable runtime.
* Some older Alfred paths predate Wilfred and are progressively converging onto this layering.

PUBLIC COMPONENTS

Butler Core:
* public and provider-neutral;
* current stable line: 0.1.3;
* shared execution, planner and output contracts.

Wilfred:
* public reusable Butler runtime;
* current development line: 0.2.0.dev0;
* registered tools and capabilities;
* deterministic execution and planning interfaces;
* confirmation boundaries;
* workflows and verified execution;
* output contracts;
* standalone HTTP APIs;
* configured plugin loading;
* Docker distribution.

wilfred-home-assistant:
* official public Home Assistant plugin;
* Home Assistant REST reads and service actions;
* configuration-driven targets and authorized actions;
* READ and ACTION tools;
* compatible with verified workflows.

PRIVATE KERIOL DEPLOYMENT

Alfred the Butler:
* private user-facing Keriol Butler;
* Keriol-specific interaction and orchestration context;
* uses the reusable Wilfred / Butler Core foundations;
* may contain capabilities ahead of the public Wilfred distribution;
* legacy Alfred Core and Tool Registry terminology remains relevant to historical documentation but no longer defines the reusable runtime boundary.

Osvaldo:
* proactive communication policy;
* allow, defer, aggregate and deny behavior;
* quiet-hours and communication-mode policy.

Charon:
* media-domain intelligence;
* discovery, catalog policy, playback workflows and lifecycle analysis.

Umberto:
* development ledger and checkout coordination;
* task, milestone and evidence tracking.

VOICE AND FRONTENDS

* Alexa is the current primary voice frontend.
* Legacy deterministic intents and free-text paths coexist during migration.
* Speech and SSML rendering are frontend-specific implementation details.
* Frontend rendering is not an independent Keriol architectural component.
* Slow AI-backed paths may acknowledge a request before provider latency becomes noticeable.

INTERACTION FLOWS

Public Wilfred:

Client -> Wilfred -> Registered Tool / Plugin -> Service

Keriol Home:

Frontend -> Alfred -> Wilfred Runtime -> Registered Capability -> Service

Home Assistant action:

READ -> ACTION -> READ -> VERIFY

CAPABILITY MATURITY

Public:
* shipped or implemented in Butler Core, Wilfred or an official public plugin.

Private validated:
* implemented and exercised in the real Alfred deployment;
* not necessarily present in public Wilfred.

Candidate:
* private functionality that may later be generalized;
* not a release commitment.

CURRENT PRIVATE VALIDATION

* Alexa interaction and free-text routing.
* Laundry status, catalog, controlled actions and asynchronous verification.
* Proactive notification policy and snoozable behavior.
* Plex / media workflows and Charon policy.
* Server and service observability.
* Energy telemetry.
* Presence experiments.
* Climate-control experiments.
* Contextual confirmations and pending actions.


OPEN WORKSHOP / PUBLIC EXTRACTION

The public Butler repositories intentionally expose a smaller surface than the private Keriol proving ground.

Alfred the Butler is an active real-world workshop where new domains, workflows, interaction patterns and plugin candidates can be exercised before they are considered reusable.

* Some capabilities will remain specific to Keriol Home.
* Some may be generalized into Wilfred.
* Some may become official Wilfred plugins.
* Private validation alone does not make a capability public.
* Public extraction requires reusable contracts, tests, sanitization, documentation and clean installation evidence.

The workshop is intentionally open-ended: new projects and plugin candidates can emerge as real household needs expose useful reusable patterns.

For builders, founders and early adopters, the public repositories show the reusable pieces that have already crossed that boundary; this portfolio also documents the engineering proving ground behind them.

PUBLIC ALPHA DIRECTION

Wilfred 0.2.0 Public Alpha requires:

* final release checkout;
* compatible Butler Core / Wilfred / plugin versions;
* stable public artifacts;
* stable container publication;
* clean public-registry pull and runtime verification;
* final public documentation.

Crowdfunding activation remains after the real verified Wilfred 0.2.0 release.

HOME ASSISTANT BOUNDARY

* Home Assistant remains the smart-home platform.
* Wilfred does not replace Home Assistant.
* Alfred does not replace Home Assistant.
* Public Home Assistant integration belongs in the official Wilfred plugin.
* Keriol-specific Home Assistant assumptions remain private.

PUBLIC / PRIVATE DOCUMENTATION

Public:
* architecture;
* ADRs;
* sanitized case studies;
* reusable lessons;
* historical worklogs and snapshots;
* public-safe examples.

Private:
* secrets and credentials;
* personal data;
* private operational details;
* unnecessary real entity IDs and device identifiers;
* private service-specific implementation details.

HISTORICAL DOCUMENTATION

Dated project-model snapshots, worklogs and milestone documents describe the architecture that existed at the time.

They should not be rewritten merely to make Wilfred appear older than it is.

CURRENT DOCUMENTATION PRIORITY

* Align active portfolio documents with Butler Core -> Wilfred -> Alfred.
* Preserve historical records.
* Sanitize legacy examples against the current boundary.
* Keep capability maturity explicit.
