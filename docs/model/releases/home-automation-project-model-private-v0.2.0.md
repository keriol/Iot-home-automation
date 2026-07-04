HOME AUTOMATION PROJECT MODEL - PRIVATE (<8K)

STATUS
- Active model lives in ChatGPT project instructions.
- This file is the private repo model snapshot.
- history/ keeps archived old models.
- worklog/ keeps dated progress.
- PUBLIC snapshot is generated after PRIVATE update by scripts/export-project-model.sh.

STARTUP
- Verify HA/MQTT/Node-RED/cloudflared before changes.
- Backup before risky changes. One feature at a time.
- Local-first, public-safe, no secrets.
- PRIVATE model first, PUBLIC snapshot second.
- Checkout = verify services, compile, restart, test endpoints, sanitize, update docs/model, run public export, diff/commit/push.

VISION
- Alfred the Butler is the AI Agent of Keriol Home.
- User entrypoint: "Alexa, apri Alfred the Butler".
- Alfred is not the smart home software; Alfred knows how to talk to every smart home service.
- New projects extend Alfred through tools, not core complexity.
- Motto: "Alfred non è il software della casa. Alfred è colui che sa parlare con tutti i software della casa."

STACK SNAPSHOT
Core: HA Docker, Mosquitto, Node-RED, HACS, Python/FastAPI, QNAP, Plex available.
Voice: Alexa Devices, Assist, Echo TTS, Cloudflare HTTPS, Alexa Skill MVP, Laundry voice.
Network: LAN, Tailscale, Cloudflare Tunnel, AdGuard. Cloudflare Access pending.
Devices: Hue/MagicHome/Broadlink/Sonoff/Tuya/Imou/hOn/Tapo/Dolby integrated.
Portfolio: public repo/docs/ADR/examples/worklog/model export exists.

ARCHITECTURE
User -> Alexa/Web/Telegram/App -> FastAPI -> Alfred Agent -> Tool Registry -> Integrations.
- Alfred uses registered tools only.
- HA = orchestration, dashboards, simple automations and physical commands.
- Python/FastAPI = Alfred Core, APIs, Tool Registry, validation, planning and workflows.
- Node-RED = visual multi-event flows.
- MQTT = event bus.
- One owner per feature. Avoid duplicated logic.

ALFRED AGENT MVP
Implemented:
- Alfred Core.
- Tool Registry.
- Deterministic-first routing.
- AI planner fallback via OpenAI Responses API.
- Registered READ tools.
- Domain mismatch guard.
- JSONL Alfred request logging.
- FastAPI endpoints: POST /alfred/ask, GET /alfred/tools, GET /alfred/ai/status.

Current path:
- Alexa -> Cloudflare -> FastAPI /alexa -> legacy Alexa intent logic.

Target path:
- Alexa -> Cloudflare -> FastAPI -> AlfredCore.ask -> Tool Registry -> Tools.

Pending:
- Alexa free-text AI Agent bridge.
- Memory JSON -> SQLite.
- AI Budget Manager.
- Dashboard for tools, logs, AI cost and health.

ALFRED RULES
- Prefer deterministic logic over AI.
- Cheap model for routing/tool selection.
- Strong models only when required.
- Send minimum necessary context.
- Never hallucinate. If no suitable tool exists, say so.
- Use tools for live data.
- READ before ACTION.
- ACTION/DANGEROUS tools require confirmation when appropriate.
- Verify physical state after commands.
- Keep responses cautious when data is stale/unavailable.

TOOL REGISTRY
Metadata: name, description, parameters, category, permission READ/ACTION/DANGEROUS, timeout.
Registered READ tools:
- get_laundry_status
- search_laundry_programs
- get_server_status
- get_rsvp_summary
- get_rsvp_guest_status
Planned/legacy tools:
- start_laundry
- stop_laundry
- notify_home_assistant
- get_plex_status
- search_plex_media
- get_plex_recent_activity
- Bambu tools
- UPS/Energy tools
- NAS tools
- Calendar/Weather tools

VOICE
- Alexa is only a frontend.
- Invocation: "Alexa, apri Alfred the Butler".
- Sessions stay open after functional replies.
- Close only on explicit exit/thanks or timeout.
- Launch style: "Ti passo Alfred".
- Alexa+ Early Access devices may not invoke unpublished dev skills by voice; simulator/classic Alexa remains safer.

LAUNDRY
- READ/search tools are registered.
- Physical control still relies on existing Alexa/HA logic until ACTION tools are registered.
- Catalog: 143 validated HA programs.
- Exact aliases only for physical control.
- Python validates requests; HA owns physical wrapper.
- Dispatch != success; verify physical state.
- hOn stale/unavailable states require cautious wording.
- Future: register start_laundry/stop_laundry as ACTION/DANGEROUS tools.

RSVP
- READ tools expose summary and guest status.
- get_rsvp_summary reads generated report/state.
- get_rsvp_guest_status reads source RSVP JSONs.
- Do not expose private contact data.
- Public docs must not include real guest names, tokens, raw RSVP data, private paths or endpoints.
- Future: notify Home Assistant/Alexa on new or updated RSVP.

SERVER
- get_server_status is READ only.
- Reports reachability, uptime, load, disk/RAM summary and key service/container status.
- Uses safe read-only commands only.
- No secrets, tokens, raw logs or private payloads.

PLEX
- Plex service/API exists in the stack.
- Alfred Plex tool is not implemented yet.
- Next READ tools: get_plex_status, search_plex_media, get_plex_recent_activity.
- ACTION tools such as library scan require explicit confirmation.

NOTIFICATIONS / SECURITY
- Release notifications: notify.echo_pop_salotto_parla.
- Debug notifications: notify.bagno_parla.
- Proactive notifications use normal Alexa voice.
- Skill SSML only inside Alfred conversations.
- Private access via Tailscale.
- Public integrations via Cloudflare Tunnel.
- Never expose HA directly.
- Never commit secrets, tokens, IDs, logs, backups, private endpoints or credentials.
- Public snapshots sanitize domains, paths, guest data and operational details.

HISTORY
- Old pre-Alfred model archived under history/.
- Archive covers early HA stack, Assist/Plex voice, Bravia/Dolby safe-power, hOn early phase, access roadmap and portfolio plan.
- Archive is reference only, not active operating context.

CHECKOUT
1. Verify services.
2. Compile bridge.
3. Restart service.
4. Test /alfred/tools, /alfred/ask, /alfred/ai/status.
5. Test legacy Alexa endpoints.
6. Update worklog/docs/private model.
7. Remove pycache.
8. Run scripts/export-project-model.sh.
9. Sanitize docs/examples/scripts.
10. Review diff, commit, push.

NEXT
1. Document Alfred Agent MVP as ADR/worklog.
2. Run public sanitized snapshot export.
3. Add Plex READ tool.
4. Add Alexa generic free-text bridge to AlfredCore.ask.
5. Register Laundry ACTION tools with confirmation/verification.
6. Add Home Assistant notification tool.
7. Add dashboard for tools, logs, AI usage and health.
8. Add Memory JSON -> SQLite.
9. Add Bambu/UPS/Energy/NAS/Calendar/Weather tools.
10. Add presence, energy and proactive notifications.
