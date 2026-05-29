# Docker Stack

This project runs the main smart-home services as Docker containers.

## Containers

| Container | Image | Role | Public Ports |
|---|---|---|---|
| homeassistant | ghcr.io/home-assistant/home-assistant:stable | Smart-home orchestration, dashboards and integrations | Host/network mode or not publicly documented |
| mosquitto | eclipse-mosquitto:2 | MQTT broker and event bus | 1883, 9001 |
| nodered | nodered/node-red:latest | Visual automation flows | 1880 |
| cloudflared | cloudflare/cloudflared:latest | HTTPS tunnel for selected public integrations | No direct public host port |
| adguard | adguard/adguardhome | Local DNS and filtering | 53, 80, 443, 3000 and related DNS/TLS ports |

## Design Notes

- Home Assistant is the orchestration layer.
- Mosquitto is the event bus.
- Node-RED is used for visual multi-event flows.
- Cloudflare Tunnel exposes only selected HTTPS integrations.
- AdGuard provides local DNS and filtering.
- Management access should prefer VPN/private network access.

## Public Safety

Real hostnames, IP addresses, tunnel identifiers, credentials, tokens and private network details are not published.
