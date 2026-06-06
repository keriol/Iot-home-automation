import os
from typing import Any

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()

app = FastAPI()

HA_BASE_URL = os.getenv("HA_BASE_URL")
HA_TOKEN_FILE = os.getenv("HA_TOKEN_FILE")

if not HA_BASE_URL or not HA_TOKEN_FILE:
    raise RuntimeError("Configure HA_BASE_URL and HA_TOKEN_FILE")

with open(HA_TOKEN_FILE, "r", encoding="utf-8") as token_file:
    HA_TOKEN = token_file.read().strip()

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

ENTITIES = {
    "status": os.getenv("LAUNDRY_STATUS_ENTITY", "binary_sensor.example_washer_status"),
    "remote": os.getenv("LAUNDRY_REMOTE_ENTITY", "binary_sensor.example_washer_remote"),
    "remaining": os.getenv("LAUNDRY_REMAINING_ENTITY", "sensor.example_washer_remaining"),
    "program": os.getenv("LAUNDRY_PROGRAM_ENTITY", "sensor.example_washer_program"),
}

START_SCRIPT = os.getenv("LAUNDRY_START_SCRIPT", "laundry_start_program")
HON_DEVICE = os.getenv("HON_WASHER_DEVICE", "EXAMPLE_HON_DEVICE_ID")

CATALOG = [
    {
        "code": "example_white_steam",
        "name": "Example White Steam",
        "aliases": ["example white steam", "white steam"],
        "categories": ["whites", "steam"],
        "defaults": {"temp": 60, "spinSpeed": 1200},
    },
    {
        "code": "example_colours",
        "name": "Example Colours",
        "aliases": ["example colours", "colours"],
        "categories": ["colours"],
        "defaults": {"temp": 40, "spinSpeed": 1000},
    },
    {
        "code": "example_stains",
        "name": "Example Stains",
        "aliases": ["example stains", "stains"],
        "categories": ["stains"],
        "defaults": {"temp": 40, "spinSpeed": 1200},
    },
]

CATEGORY_ALIASES = {
    "white": "whites",
    "whites": "whites",
    "colour": "colours",
    "colours": "colours",
    "color": "colours",
    "colors": "colours",
    "stain": "stains",
    "stains": "stains",
    "steam": "steam",
}


def ha_get(entity_id: str) -> dict[str, Any]:
    response = requests.get(
        f"{HA_BASE_URL}/api/states/{entity_id}",
        headers=HEADERS,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def ha_call(domain: str, service: str, data: dict[str, Any]) -> None:
    response = requests.post(
        f"{HA_BASE_URL}/api/services/{domain}/{service}",
        headers=HEADERS,
        json=data,
        timeout=10,
    )
    response.raise_for_status()


def alexa_response(text: str, end: bool = False) -> dict[str, Any]:
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": f"<speak><voice name=\"Giorgio\">{text}</voice></speak>",
            },
            "shouldEndSession": end,
        },
    }


def empty(value: str | None) -> bool:
    return str(value or "").strip().lower() in {
        "",
        "0",
        "0:00:00",
        "00:00:00",
        "unknown",
        "unavailable",
        "none",
    }


def normalize(value: str | None) -> str:
    text = str(value or "").lower().strip()
    for old in ["+", "-", "'", "’"]:
        text = text.replace(old, " ")
    for word in ["program", "programme", "washing", "machine", "the", "for", "with", "plus"]:
        text = text.replace(f" {word} ", " ")
    return " ".join(text.split())


def slot(intent: dict[str, Any], name: str) -> str | None:
    item = intent.get("slots", {}).get(name, {})
    return item.get("value") if isinstance(item, dict) else None


def find_program(spoken_name: str | None) -> dict[str, Any] | None:
    normalized = normalize(spoken_name)

    for program in CATALOG:
        names = [program["name"], *program["aliases"]]

        if normalized in {normalize(name) for name in names}:
            return program

    return None


def laundry_status_text() -> str:
    status = ha_get(ENTITIES["status"])

    if status.get("state") != "on":
        return "The washing machine is currently not connected."

    remaining = ha_get(ENTITIES["remaining"]).get("state")
    program = ha_get(ENTITIES["program"]).get("state")
    remote = ha_get(ENTITIES["remote"]).get("state")

    if empty(remaining):
        text = "The washing machine is connected and ready."

        if remote == "on":
            text += " Remote control is enabled."

        return text

    if empty(program):
        program = "current program"

    return f"Washing machine program: {program}. Remaining time: {remaining}."


def available_programs_text() -> str:
    categories = sorted({c for p in CATALOG for c in p["categories"]})
    return f"The example catalog has {len(CATALOG)} programs. Categories: {', '.join(categories)}."


def programs_by_category_text(value: str | None) -> str:
    category = CATEGORY_ALIASES.get(normalize(value))

    if not category:
        return "I did not understand the laundry category."

    names = [p["name"] for p in CATALOG if category in p["categories"]]

    if not names:
        return "I did not find programs for that category."

    return f"Programs for {value}: {', '.join(names)}."


def start_laundry_text(spoken_name: str | None) -> str:
    program = find_program(spoken_name)

    if not program:
        return "I did not find that program in the validated catalog, so I did not start the washing machine."

    if ha_get(ENTITIES["status"]).get("state") != "on":
        return "The washing machine is not connected. I did not start the program."

    if ha_get(ENTITIES["remote"]).get("state") != "on":
        return "Remote control is not enabled. I did not start the program."

    if not empty(ha_get(ENTITIES["remaining"]).get("state")):
        return "The washing machine already appears to have a running or selected program."

    ha_call(
        "script",
        START_SCRIPT,
        {
            "program_code": program["code"],
            "program_parameters": program["defaults"],
        },
    )

    return f"I sent the start command for {program['name']}. Ask for status in a few seconds."


def stop_laundry_text() -> str:
    if ha_get(ENTITIES["status"]).get("state") != "on":
        return "The washing machine is not connected. I did not send commands."

    ha_call("hon", "turn_off", {"device": HON_DEVICE})

    return "I sent the stop command. Ask for status in a few seconds."


@app.get("/")
def root() -> dict[str, Any]:
    return {"status": "ok", "service": "alexa-ha-bridge-example"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/laundry/status")
def laundry_status() -> dict[str, str]:
    return {"status": "ok", "text": laundry_status_text()}


@app.post("/alexa")
@app.post("/alexa/laundry")
async def alexa_laundry(request: Request) -> dict[str, Any]:
    body = await request.json()
    request_data = body.get("request", {})
    request_type = request_data.get("type")

    if request_type == "LaunchRequest":
        return alexa_response("Welcome. Ask me about laundry.", end=False)

    if request_type == "SessionEndedRequest":
        return {}

    if request_type != "IntentRequest":
        return alexa_response("Unsupported request.")

    intent = request_data.get("intent", {})
    name = intent.get("name")

    if name == "LaundryStatusIntent":
        return alexa_response(laundry_status_text())

    if name == "LaundryAvailableProgramsIntent":
        return alexa_response(available_programs_text())

    if name in {"LaundryProgramsByCategoryIntent", "LaundrySearchProgramsIntent"}:
        return alexa_response(programs_by_category_text(slot(intent, "LaundryCategory") or slot(intent, "LaundryKeyword")))

    if name in {"LaundryStartIntent", "StartLaundryIntent"}:
        return alexa_response(start_laundry_text(slot(intent, "LaundryProgram")))

    if name in {"LaundryStopIntent", "StopLaundryIntent"}:
        return alexa_response(stop_laundry_text())

    if name in {"AMAZON.HelpIntent", "SupportedFeaturesIntent"}:
        return alexa_response("You can ask for laundry status, programs, start, or stop.")

    if name in {"AlfredExitIntent", "AMAZON.CancelIntent", "AMAZON.StopIntent"}:
        return alexa_response("At your service.", end=True)

    return alexa_response("This command is not supported yet.")
