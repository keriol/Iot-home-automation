# Lessons Learned

## Local-first is not a slogan

Cloud integrations are useful, but critical automations should prefer local control when possible.

## MQTT keeps the system modular

MQTT acts as a stable boundary between telemetry producers, Home Assistant sensors and future automations.

## Voice assistants are front-ends, not the brain

Alexa and Assist are useful entry points, but Home Assistant remains the orchestration layer.

## Presence is harder than expected

BLE presence requires reliable hardware, careful filtering and stabilization delays.

## Public repositories need aggressive sanitization

Architecture, patterns and lessons are safe to publish. Secrets, tokens, entity IDs, private domains, IPs, NAS paths and real device details are not.
