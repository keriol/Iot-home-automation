# Architecture Diagram

This diagram describes the high-level architecture of the platform.

User
 ├─ Voice Assistants
 │   └─ Home Assistant
 │       ├─ MQTT
 │       ├─ Node-RED
 │       ├─ Python Helpers
 │       ├─ Smart Lighting
 │       ├─ Smart Plugs
 │       ├─ TV & Home Theater
 │       ├─ Appliances
 │       └─ Cameras
 │
 ├─ Dashboards
 │   └─ Home Assistant
 │
 └─ Remote Access
     ├─ Tailscale VPN
     └─ Cloudflare Tunnel

Python Helpers
 ├─ Plex API
 └─ Energy Telemetry

MQTT
 ├─ Energy Sensors
 └─ Presence Sensors
