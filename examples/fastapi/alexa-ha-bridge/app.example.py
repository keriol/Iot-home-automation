import os
from typing import Any

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()

app = FastAPI()

HA_BASE_URL = os.getenv("HA_BASE_URL")
HA_TOKEN_FILE = os.getenv("HA_TOKEN_FILE")

if not HA_BASE_URL:
    raise RuntimeError("HA_BASE_URL is not configured")

if not HA_TOKEN_FILE:
    raise RuntimeError("HA_TOKEN_FILE is not configured")

with open(HA_TOKEN_FILE, "r", encoding="utf-8") as token_file:
    HA_TOKEN = token_file.read().strip()

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}


def alexa_response(text: str, should_end_session: bool = True) -> dict[str, Any]:
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": text,
            },
            "shouldEndSession": should_end_session,
        },
    }


def get_ha_state(entity_id: str) -> dict[str, Any]:
    response = requests.get(
        f"{HA_BASE_URL}/api/states/{entity_id}",
        headers=HEADERS,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def is_empty_remaining_time(value: str | None) -> bool:
    if value is None:
        return True

    normalized = str(value).strip().lower()

    return normalized in {
        "",
        "0",
        "0:00:00",
        "00:00:00",
        "unknown",
        "unavailable",
        "none",
    }


def is_unknown(value: str | None) -> bool:
    if value is None:
        return True

    return str(value).strip().lower() in {
        "",
        "unknown",
        "unavailable",
        "none",
    }


def build_laundry_status_text() -> str:
    washer_status = get_ha_state("binary_sensor.washing_machine_status")

    if washer_status.get("state") != "on":
        return "The washing machine is currently not connected."

    remaining = get_ha_state("sensor.washing_machine_remaining_time")
    program = get_ha_state("sensor.washing_machine_program_name")
    remote = get_ha_state("binary_sensor.washing_machine_remote_control")

    remaining_state = remaining.get("state")
    program_state = program.get("state")
    remote_state = remote.get("state")

    if is_empty_remaining_time(remaining_state):
        text = "The washing machine is connected and ready."

        if remote_state == "on":
            text += " Remote control is enabled."

        return text

    if is_unknown(program_state):
        program_state = "current program"

    return f"Washing machine program: {program_state}. Remaining time: {remaining_state}."


@app.get("/")
def root() -> dict[str, Any]:
    return {
        "status": "ok",
        "service": "alexa-ha-bridge",
        "routes": [
            "GET /",
            "GET /health",
            "GET /laundry/status",
            "POST /alexa",
            "POST /alexa/laundry",
        ],
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/laundry/status")
def laundry_status() -> dict[str, str]:
    try:
        return {
            "status": "ok",
            "text": build_laundry_status_text(),
        }
    except Exception:
        return {
            "status": "error",
            "text": "Unable to read washing machine status right now.",
        }


@app.post("/alexa")
@app.post("/alexa/laundry")
async def alexa_laundry(request: Request) -> dict[str, Any]:
    body = await request.json()

    request_data = body.get("request", {})
    request_type = request_data.get("type")

    if request_type == "LaunchRequest":
        return alexa_response(
            "The home assistant bridge is ready. You can ask for laundry status.",
            should_end_session=False,
        )

    if request_type == "SessionEndedRequest":
        return {}

    if request_type != "IntentRequest":
        return alexa_response("Unsupported request.")

    intent_name = request_data.get("intent", {}).get("name")

    if intent_name in ["LaundryStatusIntent", "HelloWorldIntent"]:
        try:
            return alexa_response(build_laundry_status_text())
        except Exception:
            return alexa_response("Unable to read washing machine status right now.")

    if intent_name == "AMAZON.HelpIntent":
        return alexa_response("You can ask for laundry status.")

    if intent_name in ["AMAZON.CancelIntent", "AMAZON.StopIntent"]:
        return alexa_response("OK.")

    if intent_name == "AMAZON.FallbackIntent":
        return alexa_response("I did not understand. You can ask for laundry status.")

    return alexa_response("This command is not supported yet.")
