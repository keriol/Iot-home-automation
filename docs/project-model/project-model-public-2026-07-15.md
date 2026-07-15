HOME AUTOMATION PROJECT MODEL - PUBLIC (<8K)
UPDATED: 2026-07-15

PURPOSE

Active operational model of Keriol Home. ADRs, worklogs, Umberto and archives preserve history, decisions and implementation detail.

WORKFLOW

* Git-first for tracked code and documentation.
* One focused feature per commit; include related ALF task IDs.
* PRIVATE implementation first; PUBLIC sanitized snapshot second.
* The private Alfred repository is local-only and has no remote.
* Never push private acquisition code or operational details.
* No manual .bak files for Git-tracked content.
* Before changes verify Home Assistant, MQTT, Node-RED, Alfred and cloudflared.
* Use the production virtualenv for compile and tests.
* Dispatch is not success: verify physical state.

VISION

* Alfred the Butler is the AI Agent of Keriol Home.
* Entrypoint: "Alexa, apri Alfred the Butler".
* Alfred knows how to talk to every service without becoming the smart-home software itself.
* Extend Alfred through registered tools, workflows and domain events.
* Motto: "Alfred non è il software della casa. Alfred è colui che sa parlare con tutti i software della casa."

ROLES

* Alfred = orchestrator, deterministic router, AI fallback and tool executor.
* Giorgio = speech and SSML renderer.
* Osvaldo = proactive policy: allow, defer, deny, quiet hours, aggregation and speech mode.
* Charon = Plex and media curator for discovery, quality, playback and lifecycle.
* Umberto = development ledger and checkout coordinator.
* Interactive: frontend -> Alfred -> Tool Registry -> domain -> Alfred -> Giorgio.
* Proactive: event -> queue/dispatcher -> Osvaldo -> Giorgio -> shared HA delivery.

ARCHITECTURE

User -> Alexa/Web/Telegram/App -> FastAPI -> Alfred Core -> Tool Registry -> Integrations.

* Home Assistant owns physical orchestration, dashboards and device wrappers.
* Python/FastAPI owns Alfred Core, validation, planning, workflows, APIs and tools.
* Node-RED owns visual multi-event flows. MQTT is the event bus.
* One owner layer per feature. READ before ACTION.
* ACTION and DANGEROUS require confirmation when appropriate.
* Physical actions require post-dispatch verification.

STACK

Home Assistant Docker, Mosquitto, Node-RED, HACS, Python/FastAPI, QNAP, Plex, Tautulli, Alexa, Assist, Echo TTS, Cloudflare Tunnel, Tailscale, AdGuard and private local media services.

RUNTIME STATUS

* Core containers and services are active.
* Alfred health, tool registry and AI status endpoints respond successfully.
* Alfred uses gpt-5-mini as enabled AI fallback.
* Production runtime uses the local Python 3.12 virtualenv.
* Checkout evidence on 2026-07-15: compile and all test suites passed.

ALFRED STATUS

Implemented:

* Alfred Core, Tool Registry and FastAPI routes.
* Deterministic-first routing with OpenAI fallback.
* Cheap-model preference, domain guard, permissions and JSONL logging.
* /alfred/ask, /alfred/tools and /alfred/ai/status.
* Alexa free-text backend bridge with legacy intents still active.
* Shared Home Assistant delivery and Giorgio rendering.
* Osvaldo policy for RSVP, Plex, notifications and laundry verification.
* Contextual pending actions, snooze and confirmation routing.
* Alexa carrier phrases removed before media-title parsing.
* Contextual yes routed to Alfred when a media action is pending.
* Plex search, activity, scans and Bravia playback tools.
* Charon quality policy, discovery, pending offers and verified private execution.
* RSVP metrics and notifications.
* Interactive voice override: auto, normal and whisper.
* Umberto SQLite service, CLI, Markdown export and commit links.

REGISTERED CAPABILITIES

READ:

* Laundry status and validated-program search.
* Server health.
* RSVP summary and metrics.
* Plex status, libraries, activity and media search.
* Pending and snoozed actions.
* Charon media policy and discovery.
* Interactive voice state.

ACTION:

* Confirmed Plex scans.
* Plex update evaluation and playback offers.
* Pending-action state changes.
* Charon proposal and confirmed private execution.
* Plex playback on Bravia with optional courtesy lights.
* RSVP and snoozable notifications.
* Voice override.

DOMAINS

* Voice: Alexa is becoming a thin frontend; legacy intents remain until free-text is reliable on real devices.
* Notifications: proactive events pass through Osvaldo; interactive replies bypass it.
* Laundry: 143 validated programs. READ/search are tools; start/stop remain legacy until confirmed tools exist.
* RSVP: reports refresh after submissions; shared services expose metrics and notifications. Never expose guest data publicly.
* Plex/Charon: search, scans, playback, cooldown, pending offers and quality policy are active.
* Media lifecycle: private foundation exists; legal availability, monitoring, import, retention and lifecycle completion remain scheduled.
* Presence: reliable people/home state, guests and vacation mode remain future work.
* Security/cameras: inventory, events, dashboard and alerts remain planned.
* Energy/UPS: add READ tools for production, consumption, grid, battery and health.
* Climate: combine environment, presence and weather; advisory first.
* NAS/network/backup: add health, capacity and backup visibility. Git is not a runtime backup.
* Bambu: future READ tools; pause/cancel require confirmation.
* Calendar/weather: future live READ domains.
* Operations: future dashboard for tools, health, logs and AI cost.

UMBERTO

* Umberto is the development ledger of the project.
* The SQLite planner is the source of truth for milestones, tasks, dependencies, status and commits.
* session-start determines current work.
* This model does not duplicate task lists or detailed operational roadmap state.

RULES

* Prefer deterministic logic over AI.
* Use stronger models only when necessary.
* Send minimum necessary context.
* Never hallucinate unavailable state.
* Use tools for live information.
* Never claim ACTION success without verification.
* Proactive behavior must remain useful, quiet and explainable.
* Review public documentation before push.
* Private acquisition details never leave the local repository.

ROADMAP THEMES

* Finish Alexa thin-frontend migration and device validation.
* Complete QNAP/Plex notifications through Osvaldo.
* Complete Plex playback verification end-to-end.
* Build Umberto checkout automation.
* Harden PRIVATE-to-PUBLIC sanitization.
* Complete Charon availability, lifecycle and retention.
* Build presence and house modes.
* Add NAS, energy/UPS, calendar and weather READ tools.
* Add security, climate and Bambu domains.

CHECKOUT

1. Verify core services and containers.
2. Compile and test with the production virtualenv.
3. Remove generated Python caches.
4. Test Alfred endpoints and Alexa legacy/free-text paths.
5. Update Umberto evidence.
6. Update worklog, ADR/docs and PRIVATE model.
7. Generate and review the PUBLIC sanitized diff.
8. Commit PRIVATE locally without push.
9. Commit and push only the reviewed PUBLIC portfolio.
10. Confirm clean trees and healthy services.

ARCHIVE POINTER

Historical details, completed milestones, commands, device inventory and superseded decisions live in archives, worklogs and ADRs.
