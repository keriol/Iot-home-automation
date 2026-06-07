# Project Showcase

## Overview

This document highlights some of the most representative implementations within the platform.

The goal is to demonstrate practical engineering decisions, real-world integrations and iterative problem solving.

---

# 1. Plex Voice Control

## Status

Validated implementation.

## Objective

Control media playback using natural language voice commands.

## Technologies

- Home Assistant
- Assist
- Alexa
- Python
- Plex API

## Features

- Media search
- Dynamic content selection
- Resume playback
- Series continuation
- Android TV playback control

## Engineering Challenges

- Media identification
- Playback targeting
- Resume logic
- Voice intent mapping

## Outcome

A conversational media experience integrated into the smart-home platform.

---

# 2. Alfred Laundry Voice Control

## Status

Validated MVP.

## Objective

Expose washing-machine status, program catalog queries and controlled start/stop commands through an Alexa Custom Skill without exposing Home Assistant directly.

## Technologies

- Alexa Custom Skill
- Cloudflare Tunnel
- FastAPI
- Home Assistant REST API
- hOn washing machine integration
- Home Assistant script wrapper

## Features

- Laundry status query
- Last laundry query
- Real program catalog integration
- Category-based program lookup
- Validated program start by voice
- Remote stop command by voice
- Session-based Alfred UX with explicit exit intent

## Engineering Challenges

- Alexa intent and slot routing
- Safe appliance command validation
- Program name normalization without fuzzy matching
- hOn cloud/integration state lag
- Alexa session timing and follow-up UX
- Public HTTPS bridge without exposing Home Assistant

## Safety Decisions

- Unknown programs are rejected.
- Appliance control does not use fuzzy matching.
- Program start requires a validated catalog entry.
- Start uses default parameters from the local catalog.
- Alexa start/stop responses are quick and do not claim final success from dispatch alone.
- Laundry status remains the source of truth after start/stop commands.

## Outcome

A voice-controlled appliance workflow that demonstrates secure public integration, local orchestration and safety-aware command handling.

---

# 3. Home Theater Safe-Power Workflow

## Status

Validated implementation.

## Objective

Prevent audio initialization issues caused by startup timing between TV and home theater equipment.

## Technologies

- Home Assistant
- Smart plug automation
- State-based workflows

## Features

- Automated power sequencing
- Startup protection
- eARC mitigation
- Safe shutdown logic

## Engineering Challenges

- Race conditions
- Device state synchronization
- Startup timing

## Outcome

Reliable home theater startup without manual intervention.

---

# 4. Local Solar Energy Telemetry

## Status

Work in progress. Real telemetry still needs validation and correction.

## Objective

Collect local photovoltaic and battery data without relying exclusively on vendor cloud services.

## Technologies

- Python
- MQTT
- Home Assistant
- Solar inverter integration

## Target Features

- Local telemetry collection
- MQTT publication
- Battery monitoring
- Energy dashboards
- Import/export visibility
- Energy-aware automations

## Engineering Challenges

- Proprietary protocols
- Data discovery
- Register mapping
- Sensor validation
- Long-term statistics

## Current Outcome

The architecture direction is defined, but real photovoltaic/ZCS telemetry is not yet production-ready.

---

# 5. BLE Presence Detection

## Status

Work in progress. Presence is not reliable yet.

## Objective

Determine home occupancy using Bluetooth Low Energy devices.

## Technologies

- BLE
- Bermuda
- Home Assistant
- Bluetooth adapters

## Target Features

- Device detection
- Presence estimation
- Occupancy foundation
- Empty-home automations

## Engineering Challenges

- Signal instability
- Adapter compatibility
- Device variability
- False positives
- State stabilization

## Current Outcome

BLE presence remains a validation track and should not yet be treated as a reliable automation trigger.

---

# 6. PV-Aware Laundry Automation

## Status

Future feature.

## Objective

Use renewable energy and home context to suggest optimal appliance usage.

## Technologies

- Home Assistant
- Energy telemetry
- Appliance integration
- Presence detection
- Notification workflow

## Target Features

- Battery state awareness
- Occupancy awareness
- Laundry freshness reminders
- Smart recommendations
- Notify-first automation

## Engineering Challenges

- Requires reliable energy telemetry
- Requires reliable presence
- Requires safe appliance control hardening
- Needs user-friendly notification timing

## Current Outcome

The concept is documented, but implementation depends on stabilizing real PV data, reliable presence and safer appliance-control verification.

---

# Key Engineering Themes

Across all implementations, the project consistently applies:

- Local-first architecture
- Event-driven design
- Progressive automation
- Human-centered automation
- Security-aware remote access
- AI-assisted engineering workflow

## Alfred the Butler - Laundry Voice Workflow

Alfred the Butler exposes a washing-machine workflow through an Alexa Custom Skill and a FastAPI bridge.

Highlights:

- public HTTPS skill endpoint without exposing Home Assistant directly
- validated laundry program catalog
- Italian voice queries
- true keyword search
- paginated spoken results
- cautious start and stop commands
- asynchronous verification against real appliance state
- hOn refresh before each verification attempt
- manual verification fallback after timeout

This case study demonstrates real-world IoT integration concerns:

- cloud latency
- generic device states
- voice UX constraints
- appliance safety
- public and private boundary separation
- user trust through cautious feedback
