# Voice Flow

```mermaid
flowchart LR
    User[User voice command]

    subgraph Frontends
        Alexa[Alexa]
        Assist[Home Assistant Assist]
    end

    subgraph AlexaPath["Alexa Custom Skill"]
        Skill[Alfred the Butler]
        Tunnel[Cloudflare Tunnel HTTPS]
        API[FastAPI /alexa]
        IntentType{Intent type}
        FreeText[AlfredFreeTextIntent]
        Legacy[Legacy deterministic intent]
    end

    subgraph AlfredLayer["Alfred Agent Layer"]
        Alfred[Alfred Core]
        Registry[Tool Registry]
        Domain[Registered Domain Tool]
        Giorgio[Giorgio Speech / SSML]
    end

    subgraph LegacyPath["Legacy Compatibility Path"]
        LegacyHandler[Legacy Handler]
        Safety[Validation and Safety Checks]
        HAWrapper[Home Assistant Physical Wrapper]
    end

    subgraph ProactivePath["Separate Proactive Path"]
        Event[Domain Event]
        Queue[Queue / Dispatcher]
        Osvaldo[Osvaldo Policy]
        Delivery[Shared HA Delivery]
    end

    HA[Home Assistant]
    AlexaResponse[Alexa Response]
    Session{Session control}
    Open[Keep Session Open]
    Close[Close Session]

    User --> Alexa
    User --> Assist

    Alexa --> Skill
    Skill --> Tunnel
    Tunnel --> API
    API --> IntentType

    IntentType -->|Free text| FreeText
    IntentType -->|Known legacy intent| Legacy

    FreeText --> Alfred
    Alfred --> Registry
    Registry --> Domain
    Domain --> Alfred
    Alfred --> Giorgio

    Legacy --> LegacyHandler
    LegacyHandler --> Safety
    Safety --> HAWrapper
    HAWrapper --> HA
    LegacyHandler --> Giorgio

    Giorgio --> AlexaResponse
    AlexaResponse --> Session
    Session -->|Normal response| Open
    Session -->|Exit, thanks or timeout| Close

    Assist --> HA
    Registry --> HA

    Event --> Queue
    Queue --> Osvaldo
    Osvaldo -->|Allow| Giorgio
    Osvaldo -->|Defer| Queue
    Osvaldo -->|Deny| NoDelivery[No Delivery]
    Giorgio --> Delivery
    Delivery --> HA
```

## Interactive Voice Flow

Alexa is a frontend. Free-text requests are forwarded to Alfred Core, which selects a registered tool through the Tool Registry.

Known legacy intents remain available for compatibility and deterministic physical-control workflows.

Giorgio renders the spoken response for both Alfred and supported legacy handlers.

## Proactive Voice Flow

Unsolicited domain events do not use the interactive request path.

They pass through the queue or dispatcher and Osvaldo, which may allow, defer or deny delivery before Giorgio renders the message.

## Rules

- `AlfredFreeTextIntent` forwards the free-text query to Alfred Core.
- Known requests use deterministic routing before AI fallback.
- Home Assistant owns physical device wrappers.
- Physical command dispatch is not considered success.
- Device state must be verified whenever supported.
- Interactive responses do not require Osvaldo approval.
- Proactive notifications must pass through Osvaldo.
- Normal responses keep the Alexa session open.
- Exit, thanks and timeout close the session.
