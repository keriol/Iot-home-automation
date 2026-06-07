# Home Automation Project Status

Last Updated: 2026-06-07

## Infrastructure

| Component | Status |
|---|---|
| Home Assistant Docker | ✅ Operational |
| Mosquitto MQTT | ✅ Operational |
| Node-RED | ✅ Operational |
| HACS | ✅ Operational |
| Cloudflare Tunnel | ✅ Operational |
| Tailscale VPN | ✅ Operational |

## Voice Assistants

| Feature | Status |
|---|---|
| Alexa Devices Integration | ✅ |
| TTS Notifications | ✅ |
| Text Commands | ✅ |
| Voice Announcements | ✅ |
| Home Assistant Assist Custom Intents | ✅ |
| Plex Voice Commands | ✅ |
| Alexa Custom Skill HTTPS Bridge | ✅ |
| Alfred the Butler Skill MVP | ✅ |
| Laundry Voice Status | ✅ |
| Laundry Catalog Queries | ✅ |
| Laundry Start/Stop MVP | ✅ |
| Alexa Skill Cleanup | 🔄 |

## Energy Platform

| Feature | Status |
|---|---|
| ZCS / PV Real Telemetry | 🔄 Not validated |
| MQTT Energy Publishing | 🔄 Partial |
| PV Production Real Data | 🔄 Not working yet |
| Battery SOC Real Data | 🔄 Not validated |
| Energy Dashboard v1 | 🔄 Partial |
| Grid Export Mapping | 🔄 Not validated |
| Grid Import Mapping | 🔄 |
| Battery Charge/Discharge Mapping | 🔄 |
| Long-Term Statistics | 🔄 |
| Surplus Notifications | 🔄 |

## Presence Detection

| Feature | Status |
|---|---|
| Bluetooth Presence | 🔄 Not reliable yet |
| ASUS BT500 | 🔄 Under validation |
| Bermuda BLE | 🔄 Under validation |
| Primary Phone BLE Pilot | 🔄 Not stable |
| Secondary Phone BLE Pilot | 🔄 |
| delay_off Stabilization | 🔄 |
| Empty Home Logic | 🔄 |
| Voice Presence Overrides | 🔄 |

## Media Platform

| Feature | Status |
|---|---|
| Plex Voice Search | ✅ |
| Plex Resume Playback | ✅ |
| Dynamic Media Selection | ✅ |
| Android TV Playback | ✅ |
| Native Smart Plug Control | ✅ |
| Home Theater Safe Power | ✅ |
| eARC Mitigation | ✅ |
| Cinema Scenes | 🔄 |
| TV Input Automation | 🔄 |
| Plex HTTPS Voice Intents | 🔄 |

## Smart Appliances

| Feature | Status |
|---|---|
| Washing Machine Integration | ✅ |
| Remaining Time Sensor | ✅ |
| Program Details | ✅ |
| Real Laundry Program Catalog | ✅ |
| Laundry Voice Query | ✅ |
| Laundry Catalog Voice Queries | ✅ |
| Laundry Remote Start MVP | ✅ |
| Laundry Remote Stop MVP | ✅ |
| Safe Control Hardening | 🔄 |
| Async Start/Stop Verification | ✅ |
| True Keyword Program Search | ✅ |
| PV-Aware Laundry Reminder | 🔄 |

## Cameras and Security

| Feature | Status |
|---|---|
| RTSP Camera Stream | ✅ |
| Camera Dashboard | 🔄 |
| ONVIF Cleanup | 🔄 |
| Frigate Pilot | 🔄 |
| Vacation Mode | 🔄 |
| Security Dashboard | 🔄 |

## Networking

| Feature | Status |
|---|---|
| VPN Private Access | ✅ |
| HTTPS Endpoint | ✅ |
| cloudflared Auto-Restart | ✅ |
| Cloudflare Access Policy | 🔄 |

## Portfolio Progress

| Item | Status |
|---|---|
| GitHub Repository | ✅ |
| README | ✅ |
| Roadmap | ✅ |
| Lessons Learned | ✅ |
| Architecture Docs | 🔄 |
| Case Studies | 🔄 |
| Diagrams | 🔄 |
| Sanitized Examples | 🔄 |
| Public Project Model Snapshot | ✅ |

## Current Priorities

1. Backup baseline
2. Cloudflare Access policy
3. Alexa Developer Console cleanup for help, yes/no and exit routing
4. Validate active-cycle laundry menu during real running cycles
5. Connect proactive laundry prompts to presence/home-context logic
6. Bluetooth/presence stabilization
7. Real PV/ZCS telemetry validation
8. Empty home logic
9. Battery charge/discharge mapping
10. Portfolio completion

## Notable Achievements

- MQTT event bus architecture operational.
- Plex voice control integrated with Home Assistant.
- Home theater safe-power workflow implemented.
- Cloudflare Tunnel and Tailscale both operational.
- Alexa Custom Skill bridge validated through public HTTPS without exposing Home Assistant.
- Alfred the Butler can query laundry status, list catalog programs and dispatch validated start/stop commands.
- Laundry start uses a real local program catalog with validated hOn codes and default parameters.
- Native smart-home orchestration platform running on self-hosted infrastructure.

## Known Gaps

- Bluetooth presence is not reliable yet.
- Real photovoltaic/ZCS telemetry still needs validation and correction.
- Laundry start/stop now includes asynchronous verification; safer control hardening remains a follow-up.

## 2026-06-07 Update - Alfred Laundry Workflow

The Alfred the Butler laundry workflow has moved from MVP command handling to a validated voice-driven appliance workflow.

Completed:

- Alexa Custom Skill laundry session with reprompts
- launch and fallback help guidance
- true keyword search across the laundry program catalog
- paginated spoken search results
- validated remote start for allowlisted catalog programs
- remote stop command
- hOn generic program-name fallback through a Home Assistant helper
- asynchronous start and stop verification
- hOn state refresh before each verification attempt
- 15-second verification polling up to 90 seconds
- manual verification fallback if expected state is not confirmed
- living-room Echo notification for async verification results

Validated behavior:

- start verification may fail on the first check while hOn lags, then later confirms the washer is running
- stop verification may require multiple checks, then later confirms the washer is stopped

Remaining:

- validate active-cycle menu during more real washing cycles
- clean Alexa Developer Console model for help, yes/no and exit routing
- connect proactive prompts to stronger presence/home-context logic
- monitor upstream hOn behavior for remote-start program naming
