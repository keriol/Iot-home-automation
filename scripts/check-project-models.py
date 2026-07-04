#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_CHARS = 8000

PRIVATE_MODEL = ROOT / "docs/model/home-automation-project-model-private.md"
PUBLIC_TEMPLATE = ROOT / "docs/project-model/public-template.md"
PUBLIC_MODEL = ROOT / "docs/project-model/project-model-public.md"

REQUIRED_PUBLIC_MARKERS = [
    "Alfred Agent MVP",
    "Tool Registry",
    "AI planner fallback",
    "Registered tools only",
]

FORBIDDEN_OLD_MARKERS = [
    "[ ] Custom Alexa Skill",
    "[ ] Safe appliance control",
    "Plex voice control",
]

SENSITIVE_PATTERNS = [
    r"keriolhome\.online",
    r"/home/server",
    r"Camilla",
    r"Antony",
    r"media_player\.",
    r"input_boolean\.",
    r"switch\.",
    r"binary_sensor\.",
    r"button\.",
    r"notify\.",
    r"rsvp\.",
    r"alexa\.",
]

SECRET_PATTERN = re.compile(
    r"\b(SECRET|PASSWORD|PRIVATE_KEY|ACCESS_KEY)\b",
    re.IGNORECASE,
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"Missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def check_size(path: Path, text: str) -> None:
    size = len(text)
    print(f"{path.relative_to(ROOT)}: {size} chars")

    if size > MAX_CHARS:
        fail(f"{path.relative_to(ROOT)} exceeds {MAX_CHARS} chars")


def check_public_content(text: str) -> None:
    for marker in REQUIRED_PUBLIC_MARKERS:
        if marker not in text:
            fail(f"Public model missing marker: {marker}")

    for marker in FORBIDDEN_OLD_MARKERS:
        if marker in text:
            fail(f"Public model still contains old marker: {marker}")

    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            fail(f"Public model contains sensitive pattern: {pattern}")

    if SECRET_PATTERN.search(text):
        fail("Public model contains secret-like marker")


def main() -> int:
    private_text = read_text(PRIVATE_MODEL)
    public_template_text = read_text(PUBLIC_TEMPLATE)
    public_text = read_text(PUBLIC_MODEL)

    check_size(PRIVATE_MODEL, private_text)
    check_size(PUBLIC_TEMPLATE, public_template_text)
    check_size(PUBLIC_MODEL, public_text)

    check_public_content(public_text)

    print("OK: project models passed validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
