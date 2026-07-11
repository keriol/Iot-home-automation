#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_CHARS = 8000

PRIVATE_MODEL = Path(
    os.environ.get(
        "PRIVATE_MODEL_PATH",
        Path.home()
        / "alexa-ha-bridge"
        / "docs"
        / "model"
        / "home-automation-project-model-private.md",
    )
).expanduser().resolve()

PUBLIC_MODEL = (
    ROOT
    / "docs"
    / "project-model"
    / "project-model-public.md"
)

PRIVATE_MARKERS = [
    "HOME AUTOMATION PROJECT MODEL - PRIVATE ACTIVE",
    "Alfred the Butler",
    "Presence:",
    "Security/cameras:",
    "Energy/UPS:",
    "ROADMAP",
]

PUBLIC_MARKERS = [
    "HOME AUTOMATION PROJECT MODEL - PUBLIC",
    "Alfred the Butler",
    "Tool Registry",
    "Osvaldo",
    "Charon",
    "Presence:",
    "Security/cameras:",
    "Energy/UPS:",
    "Climate:",
    "ROADMAP",
]

SENSITIVE_PATTERNS = [
    r"PRIVATE ACTIVE",
    r"(?i)keriolhome\.online",
    r"/home/server",
    r"\bserver-keriol-home\b",
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    r"\bnotify\.",
    r"\bmedia_player\.",
    r"\binput_boolean\.",
    r"\bswitch\.",
    r"\bsensor\.",
    r"\bbinary_sensor\.",
    r"\bbutton\.",
    r"\brsvp\.",
    r"\balexa\.",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_model(path: Path) -> str:
    if not path.is_file():
        fail(f"Missing model: {path}")

    text = path.read_text(encoding="utf-8")
    print(f"{path}: {len(text)} chars")

    if len(text) >= MAX_CHARS:
        fail(f"{path} violates the <8K requirement")

    return text


def require_markers(
    label: str,
    text: str,
    markers: list[str],
) -> None:
    for marker in markers:
        if marker not in text:
            fail(f"{label} missing marker: {marker}")


def main() -> int:
    if ROOT in PRIVATE_MODEL.parents:
        fail("Private model must remain outside the public repository")

    private_text = read_model(PRIVATE_MODEL)
    public_text = read_model(PUBLIC_MODEL)

    require_markers("Private model", private_text, PRIVATE_MARKERS)
    require_markers("Public model", public_text, PUBLIC_MARKERS)

    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, public_text):
            fail(f"Public model contains private pattern: {pattern}")

    print("OK: private and public project models passed validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
