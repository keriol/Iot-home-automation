# Alexa Custom Skill Troubleshooting Checklist

## Setup Order

Before opening the Test tab:

1. Set invocation name.
2. Set HTTPS endpoint.
3. Select the correct SSL certificate type.
4. Save.
5. Build model.
6. Test.

## Endpoint

Use the Alexa-compatible bridge route:

```text
https://<public-alexa-bridge-host>/alexa
```

Do not point Alexa directly to Home Assistant.

Do not use a generic health/status route as the skill endpoint.

## SSL Certificate

If the public hostname uses a wildcard certificate such as:

```text
*.example.com
```

select the Alexa Developer Console option for a sub-domain of a domain with a wildcard certificate.

## Debugging

### Check local FastAPI

```bash
curl -i http://localhost:5055/
curl -i http://localhost:5055/health
curl -i http://localhost:5055/laundry/status
```

### Check Alexa route locally

```bash
curl -i -X POST http://localhost:5055/alexa \
  -H "Content-Type: application/json" \
  -d '{"request":{"type":"LaunchRequest"}}'
```

### Check public HTTPS route

```bash
curl -i -X POST https://<public-alexa-bridge-host>/alexa \
  -H "Content-Type: application/json" \
  -d '{"request":{"type":"LaunchRequest"}}'
```

### Check bridge logs

```bash
sudo journalctl -u alexa-ha-bridge.service -f
```

Expected log when Alexa reaches the bridge:

```text
POST /alexa HTTP/1.1" 200 OK
```

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

### Alexa says the command is not supported

Likely cause:

- the utterance matched a different intent than expected

Check:

- Skill I/O JSON input
- `request.intent.name`
- bridge logs
