# ADR-006 - Separate Interactive Responses from Proactive Notification Policy

## Status

Accepted

## Context

Keriol Home communicates through both interactive responses and proactive notifications.

An interactive response follows an explicit user request. The user is already engaged and expects Alfred to answer.

A proactive notification originates from a domain event such as a media update, RSVP submission, appliance verification or future security, presence and energy event.

Treating both flows identically creates two problems:

- quiet-hour rules could incorrectly suppress a requested response;
- domain services could independently decide when and how to interrupt the user.

Notification policy and physical delivery were also becoming duplicated across integration-specific workflows.

## Decision

Interactive responses and proactive notifications use separate paths.

Interactive flow:

    Frontend -> Alfred -> Tool Registry -> Domain Tool -> Alfred -> Giorgio

Proactive flow:

    Domain Event -> Queue or Dispatcher -> Osvaldo -> Giorgio -> Shared Home Assistant Delivery

Interactive responses do not require Osvaldo's permission.

Osvaldo owns proactive communication policy and may:

- allow immediate delivery;
- defer delivery;
- aggregate related events;
- deny delivery;
- select the applicable speech mode.

The originating domain provides the event and its context. It does not own quiet hours, aggregation or physical notification delivery.

Giorgio owns speech and SSML rendering but does not decide whether delivery is allowed.

Shared Home Assistant delivery owns the physical notification call but does not own policy.

## Current Applications

The proactive policy path is used by:

- Plex update notifications;
- RSVP notifications;
- snoozable reminders;
- asynchronous laundry verification.

Future presence, security, camera, energy, climate, NAS and maker events must use the same policy path.

## Alternatives Considered

### Apply Quiet Hours to Every Alfred Response

Rejected because explicit user requests should receive a response even during quiet hours.

### Let Each Domain Implement Notification Rules

Rejected because policy would become duplicated and inconsistent across integrations.

### Put Policy Inside Home Assistant Delivery

Rejected because delivery is a transport concern and should not decide whether an event is appropriate.

### Put Policy Inside Alfred Core

Rejected because proactive events may originate without an active Alfred conversation.

## Consequences

### Positive

- Interactive responses remain predictable.
- Proactive behavior is quieter and explainable.
- Quiet hours and aggregation are consistent across domains.
- Speech rendering and physical delivery are reusable.
- New domains can emit events without reimplementing policy.
- Presence and house modes can later enrich one central policy layer.

### Negative

- Proactive workflows depend on the policy and queue services.
- Event metadata must be sufficient for future policy decisions.
- Delivery success must be handled separately from policy approval.

## Safety Rules

- Policy approval is not delivery success.
- Physical delivery results must be checked.
- Domains must not bypass Osvaldo for unsolicited communication.
- Test notifications require explicit confirmation.
- Sensitive event data must not be exposed in public documentation or logs.

## Follow-up Rules

- Add presence and house-mode context only after presence confidence is reliable.
- Keep domain events separate from rendered speech.
- Keep delivery transport separate from notification policy.
- Route new proactive domains through Osvaldo rather than adding integration-specific exceptions.
