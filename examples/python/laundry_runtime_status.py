#!/usr/bin/env python3
"""
Sanitized example - washing machine runtime status helper.

Purpose:
- Read Home Assistant washing machine states.
- Generate a safe spoken status.
- Avoid stale data when no cycle is active.

Public-safe notes:
- No tokens are stored here.
- Entity IDs are placeholders.
- Use HA_TOKEN and HA_URL environment variables in real deployments.
"""

import json
import os
import urllib.request
from datetime import datetime


HA_URL = os.environ.get("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN = os.environ.get("HA_TOKEN", "")

ENTITIES = {
    "remote_control": "binary_sensor.<washer_remote_control>",
    "remaining_time": "sensor.<washer_remaining_time>",
    "start_time": "sensor.<washer_start_time>",
    "end_time": "sensor.<washer_end_time>",
    "temperature": "sensor.<washer_temperature>",
    "spin_speed": "sensor.<washer_spin_speed>",
}


def to_int(value):
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def parse_dt(value):
    if not value or value in ("unknown", "unavailable", "none"):
        return None

    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def format_minutes(value):
    minutes = to_int(value)

    if minutes is None or minutes <= 0:
        return None

    hours = minutes // 60
    mins = minutes % 60

    if hours == 0:
        return f"{mins} minuti"

    hour_label = "ora" if hours == 1 else "ore"

    if mins == 0:
        return f"{hours} {hour_label}"

    return f"{hours} {hour_label} e {mins} minuti"


def minutes_between(start, end):
    start_dt = parse_dt(start)
    end_dt = parse_dt(end)

    if not start_dt or not end_dt:
        return None

    minutes = round((end_dt - start_dt).total_seconds() / 60)
    return minutes if minutes > 0 else None


def get_state(entity_id):
    if not HA_TOKEN:
        raise RuntimeError("HA_TOKEN environment variable is required")

    request = urllib.request.Request(
        f"{HA_URL}/api/states/{entity_id}",
        headers={
            "Authorization": f"Bearer {HA_TOKEN}",
            "Content-Type": "application/json",
        },
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    return data.get("state", "unknown")


def build_speech(states):
    remaining_minutes = to_int(states["remaining_time"])
    active = remaining_minutes is not None and remaining_minutes > 0

    if not active:
        if states["remote_control"] == "on":
            return "La lavatrice è collegata e pronta al controllo remoto, ma non risulta un lavaggio in corso."

        return "La lavatrice è collegata, ma il controllo remoto non risulta attivo."

    parts = []

    duration = minutes_between(states["start_time"], states["end_time"])
    formatted_duration = format_minutes(duration)
    if formatted_duration:
        parts.append(f"durata stimata {formatted_duration}")

    formatted_remaining = format_minutes(remaining_minutes)
    if formatted_remaining:
        parts.append(f"tempo residuo {formatted_remaining}")

    if states["temperature"] not in ("unknown", "unavailable"):
        parts.append(f"temperatura {states['temperature']} gradi")

    spin = to_int(states["spin_speed"])
    if spin is not None:
        if spin == 0:
            parts.append("centrifuga disattivata")
        else:
            parts.append(f"centrifuga {spin} giri")

    return "Stato corrente della lavatrice: " + ", ".join(parts) + "."


def main():
    states = {
        key: get_state(entity_id)
        for key, entity_id in ENTITIES.items()
    }

    print(build_speech(states))


if __name__ == "__main__":
    main()
