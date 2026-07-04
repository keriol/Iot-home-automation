SMART HOME PROJECT MODEL - PUBLIC SNAPSHOT (<8K)

STATUS
- Sanitized public snapshot for portfolio/docs.
- Private details removed: domains, tokens, private paths, raw logs, entity IDs, guest data, credentials and operational endpoints.
- Private active model, private repo model, history and worklog are kept separately.

VISION
This project is a local-first smart-home platform built around Home Assistant, Python/FastAPI, MQTT, Node-RED and voice frontends.

Long-term direction:
- Alfred the Butler is the assistant/agent layer.
- Alexa and other interfaces remain frontends.
- Alfred is not the home automation platform itself.
- Alfred knows how to talk to the right services through registered tools.
- New features extend Alfred through tools, not core complexity.

STACK OVERVIEW
Core: Home Assistant in Docker, MQTT broker, Node-RED, HACS, Python/FastAPI services, NAS/media storage, media server available.
Voice/notifications: Alexa devices, Home Assistant Assist, Echo TTS, HTTPS tunnel, custom Alexa skill MVP, laundry voice workflow.
Network: LAN-first, private remote access via VPN/Tailscale-style tooling, scoped HTTPS tunnel for public integrations, management services not directly exposed.
Integration categories: lights, smart plugs, bridges, smart appliances, cameras, media/home theater, environmental devices, TV/audio chain.

ARCHITECTURE
User -> Voice/Web/App -> FastAPI -> Alfred Agent -> Tool Registry -> Integrations.

Layer ownership:
- Home Assistant handles orchestration, dashboards, simple automations and physical commands.
- Python/FastAPI handles APIs, validation, planning, workflows and agent logic.
- Node-RED handles visual multi-event flows where useful.
- MQTT acts as event bus.
- Each feature has one clear owner layer.
- Avoid duplicated logic across YAML, Node-RED and Python.

ALFRED AGENT MVP
Implemented:
- Alfred Core.
- Tool Registry.
- Deterministic-first routing.
- AI planner fallback.
- Registered READ tools.
- Tool/domain guardrails.
- Sanitized request logging.
- API endpoints for asking Alfred, listing tools and checking AI status.

Current architecture:
- Existing intent-based voice flows remain compatible.
- New agent path is FastAPI -> Alfred Core -> Tool Registry -> integration tools.
- Free-text voice bridge is planned as the next step.

Design principles:
- Registered tools only.
- Deterministic logic before AI.
- AI fallback only when useful.
- Cheap model for routing/tool selection.
- Stronger models only when needed.
- Minimal context sent to AI.
- No hallucinated tools.
- If no suitable tool exists, Alfred says so.
- READ before ACTION.
- ACTION/DANGEROUS tools require confirmation.
- Physical actions require state verification.

TOOL REGISTRY
Each tool has:
- name.
- description.
- parameters.
- category.
- permission: READ, ACTION or DANGEROUS.
- timeout.

Initial registered tool domains:
- Laundry status/search.
- Server status.
- Internal reporting summaries.

Planned tool domains:
- Media/Plex status, search and recent activity.
- Notifications.
- Energy/device tools.
- NAS/media tools.
- Calendar/weather tools.

VOICE STRATEGY
- Alexa is a frontend, not the automation brain.
- Existing intent-based Alexa flows remain compatible.
- Target: free-text voice request -> FastAPI -> Alfred Agent -> Tool Registry -> integration tools.
- Voice sessions stay open after normal replies and close only on exit/thanks/timeout.
- Development voice testing may depend on device/runtime limitations, so simulator/classic paths remain useful.

LAUNDRY DOMAIN
Implemented:
- Laundry status query.
- Laundry program search.
- Catalog-driven program handling.
- Validation layer before physical commands.

Safety:
- Exact aliases only for physical start.
- No fuzzy matching for start/stop.
- Dispatch is not success.
- Physical state must be verified.
- Stale appliance data requires cautious wording.
- Start/stop tools should be ACTION/DANGEROUS and require confirmation.

MEDIA / PLEX DOMAIN
Current:
- Media server is available.
- Previous voice/media control is a historical milestone.
- Alfred media tools are planned.

Planned READ tools:
- Media server status.
- Media search.
- Recent activity.

Planned ACTION tools:
- Library refresh/scan only with explicit confirmation.

SERVER STATUS DOMAIN
Implemented:
- Safe read-only server status.
- Summary includes reachability, uptime, load, disk/RAM overview and service/container status.
- No raw logs, secrets or private payloads.

REPORTING DOMAIN
Implemented privately:
- Alfred can read generated report state and answer status questions.

Public constraints:
- Fake/sample data only.
- No real names.
- No raw data.
- No tokens.
- No private paths/endpoints.

HOME THEATER DOMAIN
Historical milestone:
- Local-first TV/audio safe-power automation.
- Smart plug migration removed dependence on cloud voice text commands.
- Guard logic prevents race conditions during TV/audio startup.
- Delayed shutdown avoids cutting power too early.
- Suitable as public case study after sanitization.

LIGHTING DOMAIN
Implemented:
- Smart lighting integrations.
- RGB/effects-capable LED integration.

Future:
- Cinema scenes.
- Media-aware ambient scenes.
- Alfred-triggered scene workflows.

ENERGY / PRESENCE / SECURITY ROADMAP
Planned:
- Reliable presence foundation.
- Energy surplus notifications.
- PV-aware suggestions.
- Security/camera dashboard.
- Vacation/security mode.
- Proactive notifications through Alfred.

Rule:
- Notify first, automate later.

SECURITY MODEL
- Never expose Home Assistant directly.
- Never commit secrets, tokens, credentials, raw logs, backups or private endpoints.
- Sanitize device IDs, private paths, domains and personal data.
- Use private access for admin services.
- Use HTTPS tunnel only for scoped public integrations.
- Keep portfolio examples generic and reproducible.

DOCUMENTATION MODEL
Private docs:
- Active model.
- Private repo model.
- Historical archive.
- Worklog.
- ADRs.
- Implementation notes.

Public docs:
- Sanitized architecture.
- Roadmap.
- ADRs.
- Worklog excerpts.
- Sanitized examples.
- Local-first decisions.
- Lessons learned.
- Case studies without private identifiers.

PUBLIC ROADMAP
1. Document Alfred Agent MVP as ADR.
2. Publish sanitized architecture snapshot.
3. Add media/Plex READ tool.
4. Add generic voice-to-agent bridge.
5. Add safe notification tool.
6. Add dashboard for tools, logs and health.
7. Add safe ACTION tool pattern with confirmations and verification.
8. Expand to energy, presence, NAS/media and device tools.

SUMMARY
The project evolved from Home Assistant automations into a modular assistant-oriented architecture.

Current milestone:
- FastAPI service.
- Alfred Agent MVP.
- Tool Registry.
- Deterministic routing.
- AI planner fallback.
- Safety permissions.
- Initial READ tools.
- Public-safe documentation path.
