"""
Sanitized example: asynchronous laundry command verification.

This example demonstrates the pattern used by Alfred the Butler:

- do not treat command dispatch as success
- verify the expected appliance state out of band
- refresh the integration state before each check
- notify only when the expected state is observed
- ask for manual verification after a timeout

No real Home Assistant URL, token, entity ID, device ID or private endpoint is included.
"""

from __future__ import annotations

import logging
import threading
import time
from typing import Any, Callable

LOGGER = logging.getLogger("example.laundry.async_verification")

VERIFY_INTERVAL_SECONDS = 15
VERIFY_MAX_SECONDS = 90


class HomeAssistantClient:
    """Minimal sanitized Home Assistant client abstraction."""

    def get_state(self, entity_id: str) -> dict[str, Any]:
        """Return a sanitized Home Assistant state object."""
        raise NotImplementedError

    def call_service(
        self,
        domain: str,
        service: str,
        data: dict[str, Any],
    ) -> None:
        """Call a sanitized Home Assistant service."""
        raise NotImplementedError


def is_empty_remaining_time(value: str | None) -> bool:
    if value is None:
        return True

    return str(value).strip().lower() in {
        "",
        "0",
        "0:00:00",
        "00:00:00",
        "unknown",
        "unavailable",
        "none",
    }


def is_idle(
    remaining_time: str | None,
    program_phase: str | None,
) -> bool:
    return is_empty_remaining_time(remaining_time) and program_phase in {
        "0",
        "ready",
        "unknown",
        "unavailable",
        None,
    }


def refresh_laundry_state(client: HomeAssistantClient) -> None:
    """Ask the integration to refresh washer details before reading sensors."""
    refresh_buttons = [
        "button.example_washer_get_settings_details",
        "button.example_washer_get_programs_details",
    ]

    for entity_id in refresh_buttons:
        LOGGER.info("Requesting washer refresh through %s", entity_id)

        client.call_service(
            "button",
            "press",
            {
                "entity_id": entity_id,
            },
        )

    time.sleep(5)


def start_confirmed(client: HomeAssistantClient) -> bool:
    remaining = client.get_state("sensor.example_washer_remaining_time")
    phase = client.get_state("sensor.example_washer_program_phase")

    return not is_idle(
        remaining.get("state"),
        phase.get("state"),
    )


def stop_confirmed(client: HomeAssistantClient) -> bool:
    remaining = client.get_state("sensor.example_washer_remaining_time")
    phase = client.get_state("sensor.example_washer_program_phase")

    return is_idle(
        remaining.get("state"),
        phase.get("state"),
    )


def notify_user(client: HomeAssistantClient, message: str) -> None:
    LOGGER.info("Sending verification notification: %s", message)

    client.call_service(
        "notify",
        "send_message",
        {
            "entity_id": "notify.example_living_room_echo",
            "message": message,
        },
    )


def verify_laundry_state_later(
    client: HomeAssistantClient,
    verification_name: str,
    is_confirmed: Callable[[HomeAssistantClient], bool],
    success_message: str,
    manual_check_message: str,
) -> None:
    LOGGER.info(
        "Scheduled async verification: type=%s interval=%s max=%s",
        verification_name,
        VERIFY_INTERVAL_SECONDS,
        VERIFY_MAX_SECONDS,
    )

    for elapsed_seconds in range(
        VERIFY_INTERVAL_SECONDS,
        VERIFY_MAX_SECONDS + 1,
        VERIFY_INTERVAL_SECONDS,
    ):
        LOGGER.info(
            "Verification attempt: type=%s elapsed=%s",
            verification_name,
            elapsed_seconds,
        )

        time.sleep(VERIFY_INTERVAL_SECONDS)

        refresh_laundry_state(client)

        if is_confirmed(client):
            notify_user(client, success_message)
            return

        LOGGER.info(
            "Verification not confirmed yet: type=%s elapsed=%s",
            verification_name,
            elapsed_seconds,
        )

    notify_user(client, manual_check_message)


def schedule_verification(
    client: HomeAssistantClient,
    verification_name: str,
    is_confirmed: Callable[[HomeAssistantClient], bool],
    success_message: str,
    manual_check_message: str,
) -> None:
    thread = threading.Thread(
        target=verify_laundry_state_later,
        args=(
            client,
            verification_name,
            is_confirmed,
            success_message,
            manual_check_message,
        ),
        daemon=True,
    )

    thread.start()


def schedule_start_verification(
    client: HomeAssistantClient,
    program_name: str,
) -> None:
    schedule_verification(
        client=client,
        verification_name="start",
        is_confirmed=start_confirmed,
        success_message=f"Washer start verified. Program: {program_name}.",
        manual_check_message=(
            "The washer start command was sent, but automatic confirmation "
            "was not reached in time. Please verify manually."
        ),
    )


def schedule_stop_verification(client: HomeAssistantClient) -> None:
    schedule_verification(
        client=client,
        verification_name="stop",
        is_confirmed=stop_confirmed,
        success_message="Washer stop verified.",
        manual_check_message=(
            "The washer stop command was sent, but automatic confirmation "
            "was not reached in time. Please verify manually."
        ),
    )
