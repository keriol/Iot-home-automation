# Lessons Learned - Alfred Laundry Voice UX and Async Verification

## 1. Voice assistants should not overclaim

A voice assistant must not say that a washer has started or stopped only because a command was sent.

Better user-facing wording:

- "Ho inviato il comando."
- "Verifico tra poco."
- "Ti avviso."

Only report success after observing the expected state.

## 2. Command dispatch and physical success are different events

For real appliances, dispatching a command is only the first step.

The system should distinguish:

- command accepted by the backend
- state observed through sensors
- final user-facing confirmation

This avoids false success messages.

## 3. Slow cloud integrations need verification windows

hOn can lag behind the physical appliance.

A fixed delay is fragile. Incremental verification works better:

- check every 15 seconds
- refresh state before each check
- stop after a maximum verification window
- request manual verification if still not confirmed

## 4. Refresh before reading state

Before verification, force hOn detail refresh through available Home Assistant buttons.

This reduces false negatives caused by stale sensor data.

## 5. Keep control paths deterministic

For appliance control:

- no fuzzy matching
- allowlisted catalog entries only
- one Home Assistant script wrapper for physical commands
- validate washer connected
- validate remote control enabled
- validate no active cycle before start

The system should reject uncertain commands instead of guessing.

## 6. Voice catalog search needs pagination

Reading long result lists aloud is poor UX.

Better pattern:

- read first 5 results
- ask "Continuo?"
- "sì" continues
- "no" stops the list without closing the skill

This keeps the skill conversational without overwhelming the user.

## 7. Generic integration labels need user-facing fallbacks

hOn may report generic program names after remote start.

Examples:

- home_assistant
- HOME_ASSISTANT
- No program

The bridge stores the requested human-readable display name before dispatching the command.

That stored value is used only as a presentation fallback, not as proof that the appliance is running.

## 8. Reprompts improve continuity

Functional responses should keep the session open and include a short reprompt.

The user should be able to continue without reopening the skill.

## 9. Help must be discoverable

The launch response now suggests asking:

- "che cosa puoi fare?"

This gives the user a clear recovery path when they do not remember supported commands.

## 10. Public documentation must be intentionally sanitized

Never publish:

- raw Alexa payloads
- skill IDs
- slot resolution IDs
- user IDs
- device IDs
- hOn raw payloads
- MAC addresses
- mobile IDs
- transaction IDs
- real endpoints
- private IPs
- tokens or secrets

Document patterns, decisions and lessons instead of production traces.

## 11. Portfolio value comes from real constraints

The strongest part of this feature is not the voice command itself.

The value is in handling real-world constraints:

- cloud latency
- stale sensors
- generic integration states
- Alexa session limits
- appliance safety
- public/private architecture boundaries
- user trust through cautious language

This turns a home automation feature into a credible integration case study.
