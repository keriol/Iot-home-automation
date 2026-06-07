# Alexa Laundry Async Verification Diagrams

This page documents the public-safe architecture behind Alfred the Butler's laundry voice workflow.

No real endpoint, token, device ID, user ID, skill ID, MAC address or private entity name is included.

## End-to-End Voice Path

    User voice command
        |
        v
    Alexa Custom Skill
        |
        v
    Public HTTPS tunnel
        |
        v
    FastAPI Alexa bridge
        |
        v
    Home Assistant REST API
        |
        v
    HA laundry command wrapper
        |
        v
    hOn washer integration
        |
        v
    Washing machine

Async verification branch:

    FastAPI Alexa bridge
        |
        v
    Async verification worker
        |
        +--> Home Assistant REST API
        |
        +--> Echo / HA notification

## Command Dispatch vs Confirmed State

| Step | Component | Action |
|---|---|---|
| 1 | User | Asks Alfred to start or stop the washer |
| 2 | Alexa Custom Skill | Sends an intent request to the FastAPI bridge |
| 3 | FastAPI bridge | Validates command and dispatches it to Home Assistant |
| 4 | Home Assistant | Calls the hOn command wrapper |
| 5 | FastAPI bridge | Immediately replies that the command was sent |
| 6 | Async worker | Starts verification outside the Alexa session |
| 7 | Async worker | Refreshes hOn state before each check |
| 8 | Async worker | Reads washer sensors every 15 seconds |
| 9 | Async worker | Notifies success only after expected state is observed |
| 10 | Async worker | Requests manual verification if no confirmation arrives within 90 seconds |

Verification loop:

    Wait 15 seconds
        |
        v
    Refresh hOn details
        |
        v
    Read remaining time and program phase
        |
        +--> Expected state found
        |       |
        |       v
        |   Notify verified result
        |
        +--> Expected state not found
                |
                v
            Continue until 90 seconds
                |
                v
            Ask for manual verification

## Search Pagination Flow

    Search requested
        |
        +--> 0 results
        |       |
        |       v
        |   Suggest alternative keywords
        |
        +--> 1 to 5 results
        |       |
        |       v
        |   Read all results and keep session open
        |
        +--> More than 5 results
                |
                v
            Read first 5 and ask "Continuo?"
                |
                +--> User says yes
                |       |
                |       v
                |   Read next 5
                |
                +--> User says no
                |       |
                |       v
                |   Stop list, keep skill open
                |
                +--> Timeout
                        |
                        v
                    Clear pending list

## hOn Generic Program Name Fallback

hOn may expose generic program names after remote start.

Examples:

- home_assistant
- HOME_ASSISTANT
- No program

Fallback flow:

    Alfred receives validated start command
        |
        v
    Alfred saves requested display name in Home Assistant helper
        |
        v
    Alfred dispatches hOn start command
        |
        v
    Later status reads hOn program name
        |
        +--> hOn exposes real program name
        |       |
        |       v
        |   Use hOn program name
        |
        +--> hOn exposes generic program name
                |
                v
            Use Alfred stored requested display name

## Why This Matters

Command dispatch and confirmed physical state are separate events.

Alfred therefore avoids saying that the washer has started or stopped only because the command was accepted. The assistant waits for sensor confirmation, then notifies the user.
