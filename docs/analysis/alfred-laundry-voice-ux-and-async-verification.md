# Alfred Laundry - Portfolio Analysis

## Summary

Alfred the Butler evolved from a basic laundry status query into a full voice-driven appliance workflow.

The feature now demonstrates:

- Alexa Custom Skill integration
- public HTTPS bridge pattern
- Home Assistant orchestration
- validated remote appliance control
- real catalog search
- voice UX pagination
- asynchronous command verification
- cautious handling of slow cloud/device state

## Problem

Remote appliance integrations can be slow, generic or inconsistent.

For the hOn washing machine, command dispatch may succeed before Home Assistant sensors reflect the real physical state. In some cases hOn exposes generic program names such as `home_assistant` or `No program`.

A naive voice assistant would say "started" or "stopped" immediately after sending the command. That is unsafe and misleading.

## Solution

The workflow separates three concepts:

1. command dispatch
2. observed state
3. user-facing confirmation

Alfred answers immediately after sending a command, but does not claim physical success until a background verification confirms the expected state.

## Design Strengths

### 1. Dispatch is not treated as success

The system avoids claiming that a physical action succeeded only because a command was accepted.

This is important for appliance control, where state changes may lag or fail.

### 2. Asynchronous verification

The bridge starts a background verification task.

Verification behavior:

- refresh hOn state before every check
- poll every 15 seconds
- stop after 90 seconds
- notify only after expected state is observed
- ask for manual verification if confirmation is not reached

### 3. Local orchestration with public-safe entrypoint

Alexa traffic reaches only the FastAPI bridge through a public HTTPS tunnel.

Home Assistant is not exposed directly.

### 4. Catalog validation before control

Start commands are allowlisted through a validated laundry catalog.

Unknown or fuzzy-matched program names are rejected for safety.

### 5. Human-readable fallback for unreliable hOn labels

Alfred stores the validated requested program name in Home Assistant before calling hOn.

If hOn reports a generic name, Alfred uses the stored requested display name for voice status.

### 6. Voice UX designed for real use

Long search results are paginated.

- first 5 results are spoken immediately
- "sì" continues
- "no" stops the list without closing the skill
- reprompts keep the conversation alive

### 7. Public-safe documentation pattern

Implementation details are documented with sanitized examples, diagrams and lessons learned.

No raw payloads, private endpoints, tokens or device identifiers are published.

## Technical Highlights

| Area | Implementation |
|---|---|
| Voice frontend | Alexa Custom Skill |
| Public ingress | HTTPS tunnel |
| Backend | FastAPI bridge |
| Orchestration | Home Assistant |
| Appliance integration | hOn custom integration |
| Catalog | Home Assistant owned JSON copied to bridge |
| Verification | Python background worker |
| Notifications | Echo and Home Assistant notify service |
| Safety | allowlist, no fuzzy control, async verification |

## Validated Behavior

### Start

- first async check may not confirm due to hOn lag
- later check confirms washer running
- notification includes requested program and estimated remaining time

### Stop

- early checks may still report running state
- later check confirms idle state
- notification reports washer stopped

## Why This Is Portfolio-Friendly

This is not a trivial turn-on-a-light demo.

It shows real engineering tradeoffs:

- external cloud latency
- unreliable device state
- voice session constraints
- safe remote-control rules
- public and private boundary design
- observable verification
- user trust through cautious language

The result is a practical IoT workflow with production-style concerns.
