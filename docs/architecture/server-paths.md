# Server Paths

This document describes the sanitized server layout used by the project.

## Real Local Layout

| Component | Host Path | Container Path |
|---|---|---|
| Home Assistant config | `/opt/home-automation/homeassistant` | `/config` |
| Mosquitto config | `/opt/home-automation/mosquitto/config` | `/mosquitto/config` |
| Mosquitto data | `/opt/home-automation/mosquitto/data` | `/mosquitto/data` |
| Mosquitto logs | `/opt/home-automation/mosquitto/log` | `/mosquitto/log` |
| Node-RED data | `/opt/home-automation/nodered` | `/data` |
| Cloudflared | No bind mount detected | Container-managed/runtime config |

## Public Sanitization Map

| Real Path | Public Placeholder |
|---|---|
| `/opt/home-automation/homeassistant` | `/opt/home-assistant/config` |
| `/opt/home-automation/mosquitto` | `/opt/mosquitto` |
| `/opt/home-automation/nodered` | `/opt/node-red/data` |
| `/opt/home-automation` | `/opt/home-automation` |
| Local media folders | `/mnt/media` |
| Downloads | `/mnt/downloads` |
| SSH keys and credentials | Never published |

## Rules

- Do not publish real secrets, tokens or credentials.
- Do not publish Home Assistant `.storage`.
- Do not publish databases, logs or backups.
- Do not publish tunnel IDs or private network details.
- Publish architecture, patterns and sanitized examples only.
