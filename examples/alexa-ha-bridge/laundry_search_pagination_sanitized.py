"""
Sanitized example: voice-friendly laundry catalog search pagination.

Pattern:

- search across multiple catalog fields
- read only the first 5 results
- keep a short-lived pending list
- "yes" continues
- "no" stops the list without closing the whole skill

No real Alexa skill ID, slot ID, endpoint, token, user ID or device ID is included.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

PAGE_SIZE = 5
PENDING_TTL_SECONDS = 180

SEARCH_STOP_WORDS = {
    "the",
    "a",
    "an",
    "for",
    "with",
    "program",
    "programs",
    "wash",
    "washing",
}


PENDING_SEARCH: dict[str, Any] = {
    "active": False,
    "keyword": None,
    "results": [],
    "next_index": 0,
    "created_at": None,
}


def normalize(value: str | None) -> str:
    if value is None:
        return ""

    return str(value).strip().lower()


def search_tokens(keyword: str | None) -> list[str]:
    normalized = normalize(keyword)

    return [
        token
        for token in normalized.split()
        if token and token not in SEARCH_STOP_WORDS
    ]


def searchable_text(program: dict[str, Any]) -> str:
    fields: list[str] = []

    for key in ["name", "localized_name", "code"]:
        value = program.get(key)

        if value:
            fields.append(str(value))

    categories = program.get("categories") or []

    if isinstance(categories, list):
        fields.extend(str(category) for category in categories)

    return normalize(" ".join(fields))


def find_programs(
    catalog: list[dict[str, Any]],
    keyword: str | None,
) -> list[str]:
    tokens = search_tokens(keyword)

    if not tokens:
        return []

    scored: list[tuple[int, str]] = []

    for program in catalog:
        text = searchable_text(program)
        score = 0

        normalized_keyword = normalize(keyword)

        if normalized_keyword and normalized_keyword in text:
            score += 5

        for token in tokens:
            if token in text:
                score += 2

        name = program.get("localized_name") or program.get("name")

        if score > 0 and name:
            scored.append((score, str(name)))

    scored.sort(key=lambda item: (-item[0], item[1]))

    results: list[str] = []

    for _, name in scored:
        if name not in results:
            results.append(name)

    return results


def set_pending_search(keyword: str, results: list[str]) -> None:
    PENDING_SEARCH["active"] = True
    PENDING_SEARCH["keyword"] = keyword
    PENDING_SEARCH["results"] = results
    PENDING_SEARCH["next_index"] = PAGE_SIZE
    PENDING_SEARCH["created_at"] = datetime.now(timezone.utc)


def clear_pending_search() -> None:
    PENDING_SEARCH["active"] = False
    PENDING_SEARCH["keyword"] = None
    PENDING_SEARCH["results"] = []
    PENDING_SEARCH["next_index"] = 0
    PENDING_SEARCH["created_at"] = None


def has_pending_search() -> bool:
    if not PENDING_SEARCH["active"]:
        return False

    created_at = PENDING_SEARCH["created_at"]

    if not isinstance(created_at, datetime):
        clear_pending_search()
        return False

    age = datetime.now(timezone.utc) - created_at

    if age > timedelta(seconds=PENDING_TTL_SECONDS):
        clear_pending_search()
        return False

    return True


def build_initial_search_response(keyword: str, results: list[str]) -> str:
    if not results:
        clear_pending_search()
        return f"No programs found for {keyword}."

    visible = results[:PAGE_SIZE]
    program_list = ", ".join(visible)

    if len(results) <= PAGE_SIZE:
        clear_pending_search()
        return f"Found these programs for {keyword}: {program_list}."

    set_pending_search(keyword, results)

    return (
        f"Found {len(results)} programs for {keyword}. "
        f"The first {PAGE_SIZE} are: {program_list}. Continue?"
    )


def build_next_page_response() -> str:
    if not has_pending_search():
        return "There are no pending search results."

    results = list(PENDING_SEARCH["results"])
    keyword = PENDING_SEARCH["keyword"]
    next_index = int(PENDING_SEARCH["next_index"])

    visible = results[next_index:next_index + PAGE_SIZE]

    if not visible:
        clear_pending_search()
        return "No more programs to list."

    PENDING_SEARCH["next_index"] = next_index + len(visible)
    PENDING_SEARCH["created_at"] = datetime.now(timezone.utc)

    program_list = ", ".join(visible)
    remaining = len(results) - int(PENDING_SEARCH["next_index"])

    if remaining > 0:
        return f"Continuing programs for {keyword}: {program_list}. Continue?"

    clear_pending_search()
    return f"Last programs for {keyword}: {program_list}."


def handle_search_request(
    catalog: list[dict[str, Any]],
    keyword: str,
) -> str:
    results = find_programs(catalog, keyword)

    return build_initial_search_response(keyword, results)


def handle_yes() -> str:
    return build_next_page_response()


def handle_no() -> str:
    if has_pending_search():
        clear_pending_search()
        return "Search list stopped. You can ask for another search."

    return "Okay."
