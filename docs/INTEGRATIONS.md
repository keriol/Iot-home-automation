# Integrations

## Overview

This project integrates several Home Assistant native integrations, HACS custom integrations and external services.

The repository does not include third-party custom component source code. It only documents which integration categories are used.

## Core Integrations

| Area | Integration Type | Purpose |
|---|---|---|
| Voice | Alexa Devices | TTS, announcements and voice-driven commands |
| Voice | Home Assistant Assist | Local intent handling |
| Media | Plex | Media search and playback control |
| Lighting | Hue | Smart lighting |
| Lighting | Magic Home / flux_led | LED control |
| Power | Tapo | Smart plug control |
| Climate | Tuya / thermostat integrations | Climate monitoring and control |
| Infrared | Broadlink | IR-based device control |
| Appliances | hOn | Washing machine monitoring |
| Cameras | RTSP / Imou | Camera stream integration |
| Presence | Bermuda BLE | BLE-based presence detection |
| Energy | MQTT sensors | Local photovoltaic and battery telemetry |
| Security / Access | Cloudflare Tunnel | Public HTTPS integration layer |
| Security / Access | Tailscale | Private remote administration |

## HACS / Custom Components

The live Home Assistant environment uses custom components for selected integrations.

Custom component source code is not copied into this repository because it belongs to upstream projects. The portfolio documents usage, architecture and sanitized configuration examples only.

## Design Principle

Integrations are selected using a local-first preference whenever possible. Cloud integrations are used when local alternatives are not available or when they provide useful user-facing capabilities.
