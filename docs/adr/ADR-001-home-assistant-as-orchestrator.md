# ADR-001 - Home Assistant as Orchestrator

## Status

Accepted

## Context

The project integrates multiple smart-home domains:

- Voice assistants
- Energy monitoring
- Media playback
- Lighting
- Presence detection
- Cameras
- Appliances
- Remote access

A central orchestration layer is required to coordinate devices, expose dashboards and provide a stable automation surface.

## Decision

Home Assistant is used as the main orchestration layer.

It is responsible for:

- Device integrations
- Entity state management
- Dashboards
- Simple automations
- Scripts
- Voice intent execution
- User-facing smart-home control

## Alternatives Considered

### Node-RED as Main Orchestrator

Rejected as the primary layer because it is better suited for visual flows and multi-event logic, but less convenient as the main state registry and dashboard layer.

### Python-Only Automation

Rejected because it would require rebuilding state management, UI, integrations and automation primitives already provided by Home Assistant.

### Cloud-First Automation

Rejected for critical workflows because the project prefers local-first control and resilience.

## Consequences

### Positive

- Centralized device state
- Rich integration ecosystem
- Fast dashboard creation
- Strong automation primitives
- Works well with MQTT, Python and Node-RED
- Good fit for local-first smart-home logic

### Negative

- Complex YAML can become hard to maintain
- Some integrations depend on custom components
- Advanced logic may require external helpers

## Follow-up Rules

- Use Home Assistant for simple orchestration and dashboards.
- Use Python for complex logic, API parsing and stateful workflows.
- Use Node-RED for visual multi-event flows.
- Avoid duplicating the same logic across multiple layers.
