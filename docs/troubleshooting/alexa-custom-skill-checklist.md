# Alexa Custom Skill Troubleshooting Checklist

## Setup Order

Before opening the Test tab:

1. Set invocation name.
2. Set HTTPS endpoint.
3. Select the correct SSL certificate type.
4. Save.
5. Build model.
6. Test.

Alexa changes are not active until the model is rebuilt.

## Endpoint

Use the Alexa-compatible bridge route: `https://PUBLIC-ALEXA-BRIDGE-HOST/alexa`.

Do not point Alexa directly to Home Assistant.

Do not use a generic health/status route as the skill endpoint.

## SSL Certificate

If the public hostname uses a wildcard certificate such as `*.example.com`, select the Alexa Developer Console option for a sub-domain of a domain with a wildcard certificate.

## Session Handling

If the skill should support follow-up commands, functional responses must keep the session open.

Use `shouldEndSession: false` for normal feature intents.

Use `shouldEndSession: true` only for explicit exit/stop intents.

Recommended explicit exit intent: `AlfredExitIntent`.

Example exit phrases:

- thanks
- thanks Alfred
- that's enough
- close
- I do not need anything else

## Voice UX for Slow Devices

Do not make Alexa wait for slow device polling.

For appliance control:

1. Validate the request.
2. Send the command.
3. Reply quickly.
4. Ask the user to check status after a few seconds.

The status intent should be the source of truth after command dispatch.

Long polling can be useful for backend diagnostics, but it is usually poor Alexa UX.

## Debugging

### Check local FastAPI

- `curl -i http://localhost:5055/`
- `curl -i http://localhost:5055/health`
- `curl -i http://localhost:5055/laundry/status`

### Check Alexa route locally

- `curl -i -X POST http://localhost:5055/alexa -H "Content-Type: application/json" -d '{"request":{"type":"LaunchRequest"}}'`

### Check public HTTPS route

- `curl -i -X POST https://PUBLIC-ALEXA-BRIDGE-HOST/alexa -H "Content-Type: application/json" -d '{"request":{"type":"LaunchRequest"}}'`

### Check bridge logs

- `sudo journalctl -u alexa-ha-bridge.service -f`

Expected log when Alexa reaches the bridge: `POST /alexa HTTP/1.1" 200 OK`.

Useful fields to inspect:

- request type
- intent name
- slot values
- slot resolution status
- SessionEndedRequest

## Common Symptoms

### Alexa says it cannot reach the requested skill

Likely causes:

- endpoint not saved
- build not completed
- wrong endpoint path
- wrong SSL certificate option
- public tunnel not reachable

### Alexa opens the skill but the next phrase goes to Alexa global features

Likely cause:

- `LaunchRequest` response has `shouldEndSession: true`

Fix:

- use `shouldEndSession: false` when the launch response should keep the session open.

### Alexa closes the session after a functional response

Likely causes:

- backend returned `shouldEndSession: true`
- response took too long
- Alexa timed out
- user phrase matched a stop/cancel intent

Fix:

- keep functional intents open
- keep start/stop command handlers quick
- use a dedicated exit intent for closing

### Alexa says the command is not supported

Likely cause:

- the utterance matched a different intent than expected

Check:

- Skill I/O JSON input
- `request.intent.name`
- bridge logs

### A slot value is present but resolution says no match

Example: `ER_SUCCESS_NO_MATCH`.

Likely causes:

- missing custom slot synonym
- user included extra words in the slot
- utterance pattern captured too much text

Fix:

- add controlled synonyms to the custom slot
- add utterances that keep filler words outside the slot
- add deterministic backend normalization
- do not use fuzzy matching for appliance control

### A catalog phrase is routed to a search intent

Natural phrases such as "programs for whites" may be routed to a search-style intent instead of a category intent.

Fix options:

- improve utterances in the Alexa model
- add category aliases in the backend
- treat category-compatible search values as category lookups

### Appliance command is received but device status does not update immediately

Likely cause:

- cloud/integration sensor lag

Fix:

- do not claim final success from command dispatch alone
- ask the user to query status after a few seconds
- optionally add async verification notifications

### Home Assistant entities become unavailable

Likely causes:

- integration temporarily unavailable
- cloud API delay
- repeated start/stop testing
- device offline or in standby

Fix:

- block appliance commands when key entities are unavailable
- verify the device in the vendor app
- reload the integration if needed
- avoid repeated rapid control tests

## Security Notes

Never commit:

- real public endpoints
- private hostnames or IP addresses
- Home Assistant tokens
- Alexa debug payloads
- Alexa user IDs
- Alexa device IDs
- Alexa access tokens
- skill IDs
- Home Assistant device IDs
- internal appliance identifiers
