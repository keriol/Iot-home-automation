# Home Automation Project Model - Public Snapshot

## Principles

- Local-first whenever possible.
- Public HTTPS only through narrow bridge endpoints.
- Do not expose Home Assistant directly.
- Use VPN/Tailscale for private administration.
- Use Cloudflare Tunnel for public integrations.
- One owner layer per feature.
- Avoid duplicated logic across Home Assistant, Python, Node-RED and MQTT.
- Notify first, automate later.
- Never commit secrets, tokens, debug payloads, private endpoints, real device IDs or personal data.

## Stack

Working:

- Home Assistant Docker
- Mosquitto MQTT Docker
- Node-RED
- HACS
- Python helpers/scripts
- Plex API
- QNAP NAS
- Alexa Devices integration
- Echo TTS/text/sound
- Home Assistant Assist
- Emulated Hue Alexa triggers
- Cloudflare Tunnel
- FastAPI Alexa bridge
- hOn washing machine
- Tapo smart plug
- Hue
- Magic Home LED
- Broadlink
- Sonoff/eWeLink
- Tuya thermostats
- Imou RTSP
- ZCS local telemetry
- Battery SOC
- MQTT sensors
- PV production dashboard
- Grid export dashboard

Planned:

- Cloudflare Access policy
- Safe appliance control
- Presence stabilization
- Security dashboard
- Climate dashboard
- Frigate indoor pilot
- QNAP incremental backup
- Additional portfolio case studies
- Screenshot gallery

## Architecture

```mermaid
flowchart LR
    Alexa[Alexa Custom Skill] --> CF[Cloudflare Tunnel HTTPS]
    CF --> API[FastAPI Bridge]
    API --> HA[Home Assistant REST API]
    HA --> Devices[Smart Home Entities]
```

Layer ownership:

- Home Assistant: orchestration, dashboards, simple automations.
- Python/FastAPI: complex/stateful logic, APIs, external voice bridge, catalog parsing.
- Node-RED: visual multi-event flows where YAML would be hard to maintain.
- MQTT: stable event bus for sensors and decoupled integrations.

## Voice Strategy

Working:

- Alexa Devices integration for TTS/text/sound.
- Home Assistant Assist for local intents.
- Emulated Hue for local Alexa-triggered routines.
- HTTPS bridge via Cloudflare + FastAPI.
- Laundry status query through Alexa Custom Skill MVP.
- Plex voice control through Home Assistant helpers.

Roadmap:

- Clean Alexa interaction model.
- Add laundry catalog intents.
- Add Plex HTTPS voice integration.
- Add safe appliance control only after allowlists and safety validation.
- Future assistant platform name: Maggiordomo.
- Assistant persona/alias: Albert.

## Alexa Custom Skill MVP

Completed:

- Custom Alexa skill created in Alexa Developer Console.
- Invocation name validated in development.
- HTTPS endpoint configured through Cloudflare Tunnel.
- FastAPI bridge runs persistently through systemd/Uvicorn on port 5055.
- Alexa-compatible route added:
  - `POST /alexa`
- Compatibility route kept:
  - `POST /alexa/laundry`
- Health/status routes:
  - `GET /`
  - `GET /health`
  - `GET /laundry/status`
- Alexa LaunchRequest validated end-to-end.
- Session kept open after launch using `shouldEndSession=false`.
- Laundry status query validated through Alexa Custom Skill.
- Cloudflare wildcard certificate required Alexa wildcard certificate setting.
- Temporary workaround: starter `HelloWorldIntent` maps to laundry status until interaction model cleanup.

Public endpoint format:

```text
https://<public-alexa-bridge-host>/alexa
```

Security rules:

- Do not commit real endpoint.
- Do not commit Alexa debug JSON.
- Do not commit user IDs, device IDs, skill IDs, access tokens or Home Assistant tokens.

Future Alexa checklist:

1. Set invocation name.
2. Set HTTPS endpoint.
3. Select correct SSL certificate type.
4. Save.
5. Build model.
6. Test.

## Laundry MVP

Completed:

- hOn washing machine integrated in Home Assistant.
- Runtime status helper created.
- Program catalog extracted and translated.
- Assist laundry status intent working.
- Echo laundry announcements working.
- Alexa Custom Skill can query laundry status through HTTPS bridge.
- White laundry program catalog served from Home Assistant.

Rules:

- If remaining time is empty or zero, avoid stale runtime data.
- Voice names use Italian translations.
- Start commands must use internal hOn codes only.
- No fuzzy matching for start/stop commands.
- Appliance control remains read-only until safety checks are implemented.

## Plex Voice Control

Working:

- Plex integrated with Home Assistant and Bravia.
- Search and playback helpers available.
- Assist commands can search, play a selected result and resume media.
- Series resume logic:
  - resume partially watched episode
  - else first unwatched episode
  - else first episode

Roadmap:

- Reuse HTTPS bridge pattern for future Plex Custom Skill intents.
- Keep naming public-safe and avoid implying official Plex ownership.

## Home Theater

Working:

- Bravia TV integrated.
- Tapo smart plug migrated into Dolby/home theater safe-power role.
- Old indirect Alexa text-command path removed for Dolby power.
- Safe-power logic uses direct Home Assistant switch control.
- Bravia/Dolby eARC mitigation tested successfully.

Roadmap:

- Cinema scenes.
- Bravia automation refinement.
- Plex-aware lighting scenes.

## Energy

Working:

- ZCS local telemetry.
- Battery SOC.
- MQTT sensors.
- PV production dashboard.
- Grid export dashboard.

Planned:

- Grid import.
- Charge/discharge tracking.
- Long-term statistics.
- Surplus notifications.
- Maggiordomo proactive notifications.

Example future notification:

```text
Hai una notifica da Maggiordomo! Stai regalando corrente all'Enel.
```

## Presence

Working:

- BLE adapter.
- Bermuda.
- Primary phone pilot.

Planned:

- Secondary phone pilot.
- delay_off stabilization.
- casa_vuota logic.

## Security and Cameras

Working:

- Imou RTSP present.

Planned:

- Vacation mode.
- Alerts.
- Security dashboard.
- Frigate indoor pilot.

## Climate

Working:

- Tapo H100.
- Tapo T310 sensor.

Planned:

- Bedroom dashboard.
- Bedroom automations.

## Portfolio Rules

Include:

- Architecture docs.
- ADR docs.
- Mermaid diagrams.
- Case studies.
- Sanitized examples.
- AI workflow docs.
- Worklog structure.
- Public-safe project model snapshots.

Exclude:

- secrets.yaml
- `.storage`
- Home Assistant DB/logs/backups
- tokens
- real endpoints
- device IDs
- private hostnames/IPs
- Wi-Fi names
- NAS paths
- Node-RED credentials
- Alexa debug payloads
- personal data

## Next

1. Clean Alexa interaction model:
   - create/verify `LaundryStatusIntent`
   - move laundry utterances there
   - remove or empty template `HelloWorldIntent`
   - rebuild and retest
2. Add Plex HTTPS voice intents.
3. Add laundry catalog intents.
4. Validate safe remote start.
5. Validate safe stop/pause.
6. Stabilize presence.
7. Validate energy import/export logic.
8. Add Maggiordomo proactive notifications.
9. Add more portfolio case studies.
10. Add screenshot gallery.
