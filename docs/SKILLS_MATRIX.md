# Skills Matrix

## Overview

This portfolio demonstrates software engineering, IoT integration, automation, networking and AI-assisted development through a real smart-home proving ground and the reusable Butler ecosystem extracted from it.

The matrix describes **skills demonstrated by documented architecture and evidence**. It does not imply that every private Keriol capability is publicly available in Wilfred.

## Technical Skills

| Area | Skills / Technologies Demonstrated |
|---|---|
| Home Automation | Home Assistant orchestration, automations, scripts, dashboards, integration ownership |
| Butler Architecture | Butler Core / Wilfred / Alfred layering, provider-neutral contracts, capability/domain ownership |
| Capability Design | typed tools, capabilities, domains, goals, deterministic-first resolution, planner fallback boundaries |
| IoT Integration | heterogeneous sensors, smart plugs, lighting, appliances, climate, cameras and IR devices |
| Messaging | MQTT, Mosquitto, event-driven telemetry and integration boundaries |
| Workflow Automation | Home Assistant workflows, Node-RED multi-event flows, verified action patterns |
| Programming | Python services, typed APIs, integration adapters, validation and telemetry parsing |
| Media Automation | Plex-oriented media intelligence, Android TV integration and home-theater workflows |
| Energy Monitoring | local photovoltaic telemetry, battery state, MQTT publication and dashboard integration |
| Presence Engineering | BLE/Bermuda experimentation, reliability analysis and occupancy-design constraints |
| Networking | Docker networking, DNS, VPN and HTTPS tunnel architecture |
| Remote Access | Tailscale private administration and Cloudflare Tunnel for selected public integrations |
| Security | local-first design, permission/confirmation boundaries, public/private separation and sanitization |
| DevOps / Infrastructure | Linux services, Docker, GitHub Issues/Git workflow, release evidence and validation discipline |
| Documentation | ADRs, roadmap, historical records, analysis trails, case studies and public-safe architecture docs |
| AI Workflow | AI-assisted research, troubleshooting, design review and documentation under human ownership |

## Engineering Practices

| Practice | Demonstrated Through |
|---|---|
| Local-first architecture | local device/service ownership where practical, with cloud providers kept behind explicit integration boundaries |
| Deterministic-first behavior | known requests resolved before open-goal planning or AI fallback |
| Verified physical actions | `READ -> ACTION -> READ -> VERIFY`; dispatch alone is not accepted as proof of success |
| Capability ownership | domain behavior moves toward capability/plugin owners instead of accumulating in conversation code |
| Provider neutrality | Butler Core remains service-agnostic; frontend/provider concerns stay outside Core |
| Progressive delivery | focused issues, branches, commits, validation and evidence before integration |
| Observability | state reads, logs, dashboards, telemetry and post-action verification |
| Risk management | confirmation for appropriate actions, explicit safety boundaries and cautious physical-control language |
| Security awareness | secrets, private endpoints, operational identifiers and private implementation excluded from public docs |
| Knowledge management | GitHub issues, Git history, ADRs, analysis trails, worklogs and historical records with clear authority boundaries |
| Iterative troubleshooting | hardware, network, BLE, energy, appliance and voice-delivery investigations grounded in observable evidence |

## Maturity-Aware Examples

The portfolio uses the following language when describing demonstrated work:

- **Available** — public, documented and usable in the relevant public component.
- **In testing** — validated privately or under active validation; not a public release promise.
- **Designed to enable** — architecturally supported direction without an implementation claim.

Examples:

| Area | Portfolio maturity treatment |
|---|---|
| Wilfred public runtime | Available as the current Public Alpha baseline |
| Verified laundry workflow patterns | Private proving-ground evidence used to demonstrate engineering lessons |
| Local energy telemetry | In testing |
| Reliable occupancy/presence automation | Designed to enable |
| Alexa/Hermes delivery path | Private proving-ground / in-testing evidence, not a public Wilfred frontend claim |

## Laundry Workflow Engineering Evidence

The laundry workflow remains one of the strongest private proving-ground examples because it forced the system to distinguish command dispatch from physical success.

| Area | Skills Demonstrated |
|---|---|
| Voice UX | session design, reprompts, help discovery, yes/no flows and pagination |
| Backend Integration | typed service boundaries, request routing and validation |
| Home Assistant | service invocation through owned orchestration boundaries and explicit state reads |
| Appliance Control | allowlisted start/stop workflows and cautious command semantics |
| Async Processing | deferred verification, polling windows, retries and timeout/fallback behavior |
| State Validation | separating successful request dispatch from confirmed physical state |
| Catalog Search | deterministic keyword search, aliases and pagination for known program catalogs |
| Safety | no unsafe fuzzy matching for physical actions, capability checks and confirmation boundaries |
| Notifications | policy-aware follow-up and provider/frontend delivery separation |
| Documentation | sanitized architecture, diagrams, case studies and lessons without publishing private source |

## Portfolio Value

The project demonstrates the ability to:

- design a real-world IoT architecture with clear owner boundaries;
- extract reusable runtime concepts from a private proving ground;
- integrate heterogeneous devices and protocols without coupling the core runtime to providers;
- design deterministic and AI-assisted paths with explicit fallback boundaries;
- verify observable physical outcomes instead of trusting command acknowledgements;
- troubleshoot hardware, network, integration and delivery failures methodically;
- maintain evidence-backed public documentation while preserving private implementation boundaries;
- preserve both current architecture and the historical reasoning that produced it.
