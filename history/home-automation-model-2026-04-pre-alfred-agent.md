# Home Automation Project Model History
Snapshot: pre-Alfred Agent
Status: archived reference

This file preserves the older project model before Alfred Agent became the central architecture.
Do not use this as active operating context.

Historical state:
- Home Assistant Docker, Mosquitto, Node-RED, HACS.
- Alexa Devices, Echo TTS, Assist custom intents.
- Plex voice/conversational control.
- hOn washing machine.
- Magic Home LED.
- Tapo plug for Dolby/home theater.
- Hue/Broadlink/Sonoff/Tuya/Imou integrations.
- Remote HA dashboards.
- Planned: private VPN/Tailscale access, HTTPS public endpoint, QNAP backup, public-safe GitHub portfolio, camera/security dashboards, presence, energy/PV notifications.

Historical rules still valid:
- Backup before risky changes.
- Prefer local integrations.
- Notify first, automate later.
- Avoid duplicate logic.
- Never commit secrets, tokens, private endpoints, device IDs or personal data.
- HA handles simple orchestration.
- Python handles complex logic/API parsing/ranking/stateful workflows.
- Node-RED handles visual multi-event flows.
- MQTT acts as event bus.
- One owner layer per feature.

Historical milestones:
- Alexa Devices integration working.
- Plex voice/Assist workflow working.
- hOn washer integrated.
- Magic Home LED integrated.
- Tapo plug migrated to Dolby/home-theater power.
- Alexa text commands removed from Dolby power path.
- Bravia/Dolby safe-power logic tested successfully.
- Initial public-safe portfolio plan defined.

Superseded by:
- Alfred the Butler identity.
- Alexa Skill MVP.
- FastAPI Alfred Agent.
- Tool Registry.
- Deterministic-first routing.
- AI planner fallback.
- Registered READ tools.
- Private/public model split.
- Sanitized public documentation workflow.
