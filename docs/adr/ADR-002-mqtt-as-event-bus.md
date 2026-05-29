# ADR-002 - MQTT as Event Bus

## Status

Accepted

## Context

The project collects and coordinates events from heterogeneous systems:

- Energy telemetry
- Sensors
- Presence detection
- Home Assistant entities
- Python helper scripts
- Future automation services

A lightweight and decoupled communication layer is required.

## Decision

MQTT is used as the main event bus for telemetry and decoupled automation data.

Mosquitto is used as the MQTT broker.

## Responsibilities

MQTT is used for:

- Publishing sensor telemetry
- Decoupling Python scripts from Home Assistant
- Exposing local energy data
- Supporting future event-driven automations
- Creating a stable integration boundary between producers and consumers

## Alternatives Considered

### Direct Home Assistant API Calls

Useful for some workflows, but less decoupled and less suitable for continuous telemetry.

### File-Based Data Exchange

Rejected because it is harder to monitor, less real-time and less appropriate for event-driven systems.

### Database-Centric Integration

Rejected for real-time automation because it adds unnecessary persistence and coupling.

## Consequences

### Positive

- Lightweight protocol
- Works well with Home Assistant
- Easy to publish from Python
- Supports decoupled architecture
- Good fit for IoT telemetry
- Enables future consumers without changing producers

### Negative

- Requires topic naming discipline
- Requires broker availability
- Retained messages and discovery payloads must be managed carefully
- Security configuration must be handled correctly

## Follow-up Rules

- Use MQTT for telemetry and event boundaries.
- Avoid publishing secrets or personal data.
- Keep topic names clear and consistent.
- Prefer sanitized examples in the public repository.
- Use Home Assistant MQTT integration to consume stable sensor data.
