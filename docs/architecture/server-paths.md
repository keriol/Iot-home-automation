# Deployment Layout

This document describes a **public-safe example layout** for the services used by Keriol Home.

It intentionally does not publish the real host filesystem layout. Paths below are documentation placeholders that illustrate separation of concerns without exposing machine-specific deployment details.

## Sanitized Example Layout

| Component | Public Example Path | Container Path / Role |
|---|---|---|
| Home Assistant config | `/opt/home-assistant/config` | `/config` |
| Mosquitto config | `/opt/mosquitto/config` | `/mosquitto/config` |
| Mosquitto data | `/opt/mosquitto/data` | `/mosquitto/data` |
| Node-RED data | `/opt/node-red/data` | `/data` |
| Media storage | `/mnt/media` | Media-library storage example |
| Cloudflared | Runtime-managed configuration | HTTPS tunnel for selected public integrations |

These paths are examples only. They must not be interpreted as the real Keriol Home server layout.

## Public-Safety Rules

- Do not publish real host paths or machine-specific deployment layout.
- Do not publish secrets, tokens or credentials.
- Do not publish Home Assistant `.storage`.
- Do not publish databases, logs, runtime backups or private environment files.
- Do not publish tunnel IDs, private hostnames, IP addresses or private network topology.
- Do not publish private media-acquisition implementation or storage paths that reveal it.
- Publish architecture, patterns and deliberately sanitized examples only.
