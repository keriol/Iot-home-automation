HOME AUTOMATION PROJECT MODEL - PUBLIC (<8K)
UPDATED: 2026-07-11

PURPOSE

Active model of Keriol Home: architecture, current capabilities and roadmap. ADRs, worklogs and archive keep history and implementation detail.

WORKFLOW

* Git-first for code, docs, private model and public snapshot.
* Tracked files: branch, focused diff, tests, commit, merge and push.
* No manual .bak copies for Git-tracked files.
* Manual backups only for non-versionable data, databases, runtime state and infrastructure.
* One feature per commit. Private source first, public sanitized snapshot second.
* Before changes verify HA, MQTT, Node-RED and cloudflared.

VISION

* Alfred the Butler is the AI Agent of Keriol Home.
* Entrypoint: "Alexa, apri Alfred the Butler".
* Alfred is not the smart-home software; Alfred knows how to talk to every service.
* Extend Alfred through registered tools, not core complexity.
* Motto: "Alfred non è il software della casa. Alfred è colui che sa parlare con tutti i software della casa."

ROLES

* Alfred = orchestrator and tool router.
* Giorgio = Alfred voice/SSML.
* Osvaldo = proactive policy: allow/defer/deny, quiet hours, aggregation and speech mode.
* Charon = Plex/media curator.
* Interactive: frontend -> Alfred -> Giorgio.
* Proactive: event -> queue/dispatcher -> Osvaldo -> Giorgio -> shared HA delivery.

ARCHITECTURE

User -> Alexa/Web/Telegram/App -> FastAPI -> AlfredCore -> Tool Registry -> Integrations.

* HA owns orchestration, dashboards and physical wrappers.
* Python/FastAPI owns Alfred Core, APIs, validation, planning, workflows and tools.
* Node-RED owns visual multi-event flows. MQTT is the event bus.
* One owner per feature. READ before ACTION.
* ACTION/DANGEROUS require confirmation when appropriate.
* Dispatch is not success: verify physical state.

STACK

HA Docker, Mosquitto, Node-RED, HACS, Python/FastAPI, QNAP, Plex, Tautulli, Alexa, Assist, Echo TTS, Cloudflare Tunnel, Tailscale and AdGuard.

ALFRED STATUS

Implemented:

* Alfred Core, Tool Registry and FastAPI routes.
* Deterministic-first routing with OpenAI fallback.
* Cheap-model preference, domain guard, permissions, timeouts and JSONL logging.
* /alfred/ask, /alfred/tools and /alfred/ai/status.
* Alexa free-text backend bridge; legacy intents remain active.
* Shared HA delivery and Giorgio renderer.
* RSVP, Plex, snoozable notifications and laundry async verification use Osvaldo.
* Plex notification workflow flattened; obsolete adapters/helpers removed.

REGISTERED TOOLS

READ: laundry status/search, server status, RSVP summary/guest status, Plex status/libraries/activity/search.

ACTION: confirmed Plex library/path scan.

Pending actions support playback offers.

DOMAINS

* Voice/notifications: Alexa is a frontend; proactive notifications pass through Osvaldo; snoozable queue handles quiet hours and aggregation. Production and debug notification targets are separated.
* Laundry/appliances: 143 validated programs; READ/search tools active; start/stop remain legacy until Alfred ACTION tools exist. Pattern: validate -> confirm -> act -> verify.
* RSVP: READ summary/guest tools; reports refresh after submissions; proactive notifications use Osvaldo. Never expose guest data or private paths publicly.
* Media/Charon: Plex and Tautulli integrated; READ/search and confirmed scan tools active; update workflow handles recent viewing, cooldown and playback offers. Future: recommendations, missing-title analysis and home-theater scenes.
* Presence: build reliable people/home state, casa_vuota, guests and vacation mode using HA, network/Bluetooth and future sensors. Critical automations require high confidence.
* Security/cameras: HA camera inventory, ONVIF validation, event model, dashboard and alerts. Evaluate Frigate only where object detection adds value.
* Energy/UPS: polling exists; future READ tools for production, consumption, grid exchange, UPS/battery and health, then anomaly/outage/surplus workflows.
* Climate: combine temperature, humidity, presence, weather and room use. Start advisory, automate cautiously.
* Network/NAS/backup: LAN, Tailscale, Cloudflare Tunnel, AdGuard and QNAP are core. HA is never exposed directly. Add NAS health, capacity and backup status tools. Git is not backup for runtime data.
* Bambu: future READ tools for state, job, progress, temperatures and errors. Pause/cancel require confirmation.
* Calendar/weather: planned READ domains using live tools.
* Server/operations: get_server_status is READ-only. Future dashboard covers tools, health, logs and AI cost.

ALFRED RULES

* Prefer deterministic logic over AI.
* Use stronger models only when required.
* Send minimum necessary context.
* Never hallucinate; say when no suitable tool exists.
* Use tools for live data and be cautious with stale sources.
* Never claim ACTION success without verification.
* Proactive behavior must remain useful, quiet and explainable.

ROADMAP

Near term:

1. Complete Alexa Developer Console free-text model and device tests.
2. Register Laundry start/stop as ACTION/DANGEROUS with confirmation and verification.
3. Add general HA notification tool.
4. Remove pre-Git .bak files.
5. Review Plex mark_notified with dedicated tests.

Platform:
6. Add tools/logs/AI-cost/health dashboard.
7. Add Memory JSON -> SQLite and AI Budget Manager.
8. Build presence foundation and house modes.
9. Add NAS, UPS/Energy, Calendar and Weather READ tools.

Expansion:
10. Build Charon catalog/recommendation tools.
11. Add camera/security pilot and presence-aware alerts.
12. Add climate intelligence.
13. Add Bambu READ tools and confirmed ACTIONs.
14. Add cross-domain proactive workflows.

CHECKOUT

1. Verify core services and containers.
2. Compile, remove pycache and restart.
3. Test Alfred endpoints and Alexa legacy/free-text paths.
4. Update worklog, ADR/docs and the private source model; validate below 8K.
5. Run the sanitizing export and review the public diff.
6. Commit the private source and publish the reviewed portfolio.
7. Confirm clean trees and healthy services.

ARCHIVE POINTER

Historical details, completed milestones, old commands, Alexa history, device inventory and superseded decisions live in archive/worklog/ADRs.
