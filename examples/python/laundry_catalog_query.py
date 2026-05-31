#!/usr/bin/env python3
"""
Sanitized example - laundry program catalog query helper.

Purpose:
- Query a local washing machine program catalog.
- Support Italian voice-style queries.
- Keep human names separate from internal program codes.

The catalog is expected to be a JSON file generated from integration data.
This example intentionally does not include real device IDs or private paths.
"""

import json
import re
import sys
import unicodedata
from pathlib import Path


CATALOG_PATH = Path("laundry_programs.example.json")

CATEGORY_ALIASES = {
    "whites": ["bianchi", "bianco", "white", "whites"],
    "stains": ["macchie", "macchia", "macchie ostinate", "antimacchia", "sporco difficile", "stain", "stains"],
    "delicates": ["delicati", "delicato", "lana", "seta", "delicate", "wool", "silk"],
    "rapid": ["rapidi", "rapido", "veloce", "quick", "rapid"],
}


def normalize(value):
    value = (value or "").lower().strip()
    value = unicodedata.normalize("NFD", value)
    value = "".join(ch for ch in value if unicodedata.category(ch) != "Mn")
    value = re.sub(r"[^a-z0-9\s_]", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value


def detect_category(text):
    normalized = normalize(text)

    for category, aliases in CATEGORY_ALIASES.items():
        if any(normalize(alias) in normalized for alias in aliases):
            return category

    return None


def load_catalog():
    with CATALOG_PATH.open("r", encoding="utf-8") as catalog_file:
        return json.load(catalog_file)


def list_programs(category, programs):
    result = [
        program
        for program in programs
        if category in program.get("categories", [])
    ]

    names = [
        program.get("name_it") or program.get("name") or program.get("code")
        for program in result
    ]

    return {
        "intent": "list_programs",
        "category": category,
        "count": len(result),
        "programs": result,
        "speech_it": "Ho trovato " + str(len(result)) + " programmi: " + ", ".join(names) + ".",
    }


def main():
    query = " ".join(sys.argv[1:]).strip()
    programs = load_catalog()
    category = detect_category(query)

    if category:
        print(json.dumps(list_programs(category, programs), ensure_ascii=False, indent=2))
        return

    print(json.dumps({
        "intent": "unknown",
        "speech_it": "Non ho capito quale categoria di programmi vuoi cercare.",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
