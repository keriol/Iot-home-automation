# Roadmap

## Security and Access

- [x] Tailscale private access
- [x] Cloudflare Tunnel HTTPS endpoint
- [x] cloudflared autorestart
- [ ] Cloudflare Access policy
- [ ] Backup baseline

## Energy

- [x] ZCS local telemetry
- [x] Battery SOC
- [x] MQTT sensors
- [x] Energy Dashboard v1
- [ ] Grid import
- [ ] Battery charge/discharge
- [ ] Long-term statistics
- [ ] Surplus notifications

## Presence

- [x] ASUS BT500 validated
- [x] Bermuda installed
- [x] Phone BLE pilot
- [ ] Second phone BLE
- [ ] delay_off stabilization
- [ ] casa_vuota logic
- [ ] Voice overrides

## Media and Home Theater

- [x] Bravia/Dolby safe-power logic
- [x] Native smart plug migration
- [x] Plex voice control
- [x] eARC mitigation
- [ ] Cinema scenes
- [ ] TV input automation

## Appliances

- [x] hOn washing machine integrated
- [ ] Laundry voice query
- [ ] Remote start research
- [ ] PV-aware laundry reminder

## Portfolio

- [x] Repository skeleton
- [ ] Architecture diagrams
- [ ] Case studies
- [ ] Sanitized examples

## 2026-06-07 Update - Alfred Laundry Workflow

The Alfred the Butler laundry workflow has progressed beyond the initial voice-query phase.

Completed:

- Alexa Custom Skill laundry status and remaining-time query
- validated laundry program catalog
- true keyword search across program names, codes and categories
- paginated spoken results for long catalog searches
- validated remote start for allowlisted programs
- remote stop command
- hOn generic program-name fallback using an Alfred/Home Assistant helper
- asynchronous start and stop verification
- hOn state refresh before each verification attempt
- verification polling every 15 seconds up to 90 seconds
- manual verification fallback if the expected state is not confirmed

Remaining roadmap items:

- validate active-cycle menu during more real washing cycles
- clean Alexa Developer Console model for help, yes/no and exit routing
- connect proactive laundry prompts to stronger presence/home-context logic
- add PV-aware laundry suggestions
- monitor upstream hOn behavior for remote-start program naming
