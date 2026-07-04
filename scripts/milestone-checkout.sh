#!/usr/bin/env bash
set -euo pipefail

cd "$(cd "$(dirname "$0")/.." cd /home/server/home-automation-portfoliocd /home/server/home-automation-portfolio pwd)"

cat > docs/PROJECT_MODEL.md <<'EOF'
HOME AUTOMATION PROJECT MODEL (<8K)

STARTUP
- Verify HA/MQTT/Node-RED/cloudflared healthy.
- Backup before risky changes.
- One feature at a time.
- Review priorities.
- Keep short worklog.
- Local-first, public-safe, no secrets.
- Update PRIVATE model before PUBLIC snapshot.

STACK

Core:
[x] Home Assistant Docker
[x] Mosquitto MQTT Docker
[x] Node-RED
[x] HACS
[x] Python helpers/scripts
[x] Plex API
[x] QNAP NAS

Voice:
[x] Alexa Devices integration
[x] Echo TTS/text/sound
[x] Home Assistant Assist
[x] Plex voice control
[x] Laundry voice status query
[x] Laundry program catalog voice query
[x] Emulated Hue Alexa triggers
[x] Cloudflare HTTPS endpoint
[x] FastAPI Alexa bridge MVP
[x] Persistent Alexa bridge service
[ ] Custom Alexa Skill
[ ] Safe appliance control

Network:
[x] LAN
[x] Tailscale VPN
[x] Cloudflare Tunnel
[x] HTTPS endpoint
[x] Alexa bridge hostname
[x] cloudflared autorestart
[x] AdGuard Home
[x] Emulated Hue on host port 80
[ ] Cloudflare Access policy

Devices:
[x] Hue
[x] Magic Home LED
[x] Broadlink
[x] Sonoff/eWeLink
[x] Tuya thermostats
[x] Imou RTSP
[x] hOn washing machine
[x] Tapo smart plug
[x] Dolby smart power
[x] Echo Pop TTS

Energy:
[x] ZCS local telemetry
[x] Battery SOC
[x] MQTT sensors
[x] PV production dashboard
[x] Grid export dashboard
[ ] Grid import
[ ] Charge/discharge tracking
[ ] Long-term statistics
[ ] Surplus notifications

Presence:
[x] BT500 BLE adapter
[x] Bermuda
[x] Primary phone pilot
[ ] Secondary phone pilot
[ ] delay_off stabilization
[ ] casa_vuota logic

Climate:
[x] Tapo H100
[x] T310 sensor
[ ] Bedroom dashboard
[ ] Bedroom automations

Security:
[ ] Vacation mode
[ ] Alerts

Frigate:
[ ] Indoor pilot

Home Theater:
[x] Safe-power logic
[x] Plex voice
[x] Tapo migration
[x] eARC mitigation
[ ] Cinema scenes
[ ] Bravia automation

Smart Appliances:
[x] hOn integration
[x] Laundry Assist query
[x] Laundry Alexa query
[x] Italian program catalog
[x] White laundry routines
[x] HTTPS bridge foundation
[ ] Safe remote start
[ ] Safe stop/pause
[ ] PV-aware reminders

Dashboards:
[x] Energy v1
[ ] Security
[ ] Climate
[ ] Advanced energy

Backup:
[ ] QNAP incremental backup

Portfolio:
[x] Public GitHub repository
[x] Architecture docs
[x] ADR docs
[x] Mermaid diagrams
[x] Skills matrix
[x] Showcase
[x] Metrics
[x] Sanitized examples
[x] AI workflow docs
[x] Worklog structure
[x] Project model export
[x] Laundry Voice MVP case study
[x] Alexa HTTPS Bridge case study
[ ] Additional case studies
[ ] Screenshot gallery

ARCHITECTURE
- HA = orchestration/dashboard.
- Python = complex/stateful logic, APIs, catalogs.
- Node-RED = visual multi-event flows.
- MQTT = event bus.
- One owner per feature.
- Avoid duplicated logic.

VOICE STRATEGY
- Assist handles local intents.
- Alexa Devices handles TTS/text/sound.
- Emulated Hue provides local Alexa triggers.
- Alexa routines trigger HA workflows.
- HTTPS bridge validated via Cloudflare + FastAPI.
- Bridge enables future Alexa Custom Skill.
- Bridge reusable for Plex search/playback and appliance catalogs.
- Prefer HA-owned laundry catalog over native hOn/Alexa mappings.

LAUNDRY MVP (2026-05-31)
- Runtime status helper created.
- Program catalog extracted and translated.
- Assist laundry status intent working.
- Echo Pop laundry announcements working.
- Emulated Hue enabled on port 80.
- Alexa routines validated.
- White program catalog served from HA.

Rules:
- If remaining_time <= 0, avoid stale runtime data.
- Voice names use Italian translations.
- Start commands use internal hOn codes only.
- No fuzzy matching for start/stop commands.

ALEXA HTTPS BRIDGE MVP (2026-06-01)
- FastAPI bridge created.
- Home Assistant REST integration validated.
- Laundry status endpoint implemented.
- Cloudflare hostname published.
- HTTPS endpoint validated externally.
- Persistent systemd deployment completed.
- End-to-end path validated:

  Alexa
  → HTTPS
  → Cloudflare Tunnel
  → FastAPI
  → Home Assistant

Bridge rules:
- Do not expose HA directly.
- Read-only first.
- Appliance control requires allowlists and safety validation.

REMOTE ACCESS

Private:
- Tailscale/VPN for admin access.
- Prefer VPN over exposed management services.

Public:
- Cloudflare Tunnel for HTTPS endpoints.
- Alexa HTTPS bridge validated.
- Future use: Alexa Skill, webhooks, RSVP APIs.

PORTFOLIO RULES
- Public-safe docs only.
- Never commit secrets, tokens, .storage, DBs, logs, backups, IDs, private endpoints, Wi-Fi names or credentials.
- Document decisions, not only code.
- Prefer sanitized real examples.
- Worklog separate from model.
- Keep model under 8K chars.

CHECKOUT PROCEDURE
1. Update worklog.
2. Update diagrams if architecture changed.
3. Add sanitized examples.
4. Add/update case studies.
5. Update PRIVATE model.
6. Save PRIVATE model.
7. Export PUBLIC snapshot.
8. Verify no sensitive data.
9. Commit.
10. Push.

NEXT
1. Alexa Developer Console Custom Skill.
2. LaundryStatusIntent integration.
3. Laundry catalog intents.
4. Plex HTTPS voice integration.
5. Safe remote start validation.
6. Safe stop/pause validation.
7. Presence stabilization.
8. Energy validation.
9. Additional portfolio case studies.
10. Screenshot gallery.
11. PUBLIC snapshot export.
EOF

./scripts/export-project-model.sh

echo
echo "Model chars:"
wc -m docs/PROJECT_MODEL.md docs/project-model/project-model-public.md

echo
echo "Git status:"
git status --short
