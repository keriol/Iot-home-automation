#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_CHARS = 8000

PUBLIC_CONTEXT = (
    ROOT
    / "docs"
    / "project-model"
    / "project-model-public.md"
)

REQUIRED_MARKERS = [
    "HOME AUTOMATION PROJECT CONTEXT - PUBLIC",
    "SOURCES OF TRUTH",
    "Butler Core -> Wilfred -> Alfred",
    "Butler Core",
    "Wilfred",
    "Alfred the Butler",
    "Osvaldo",
    "Charon",
    "Umberto",
    "CAPABILITY MATURITY",
    "OPEN WORKSHOP",
    "HOME ASSISTANT BOUNDARY",
    "PUBLIC BOUNDARY",
    "REFERENCE MAP",
    "CURRENT DIRECTION",
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


def main() -> int:
    if not PUBLIC_CONTEXT.is_file():
        fail(f"Missing public context: {PUBLIC_CONTEXT}")

    text = PUBLIC_CONTEXT.read_text(encoding="utf-8")

    print(f"{PUBLIC_CONTEXT}: {len(text)} chars")

    if len(text) >= MAX_CHARS:
        fail(f"{PUBLIC_CONTEXT} violates the <8K requirement")

    for marker in REQUIRED_MARKERS:
        if marker not in text:
            fail(f"Public context missing marker: {marker}")

    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, text):
            fail(
                "Public context contains private pattern: "
                f"{pattern}"
            )

    print(
        "OK: public project context passed "
        "architecture and safety validation"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
