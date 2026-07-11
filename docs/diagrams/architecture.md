# Architecture

```mermaid
flowchart TD
    User[User]

    subgraph Frontends
        Alexa[Alexa]
        Assist[Home Assistant Assist]
        Web[Web / App / Messaging]
    end

    subgraph Access
        Tunnel[Cloudflare Tunnel]
        VPN[Tailscale]
    end

    subgraph Agent
        API[FastAPI]
        Alfred[Alfred Core]
        Registry[Tool Registry]
        Giorgio[Giorgio]
    end

    subgraph Proactive
        Events[Domain Events]
        Queue[Queue / Dispatcher]
        Osvaldo[Osvaldo]
        Snoozable[Snoozable Queue]
        Delivery[Shared HA Delivery]
    end

    subgraph Core
        HA[Home Assistant]
        MQTT[Mosquitto MQTT]
        NodeRED[Node-RED]
    end

    subgraph Domains
        Laundry[Laundry]
        RSVP[RSVP]
        Operations[Server Operations]
        Charon[Charon]
    end

    subgraph Services
        Plex[Plex]
        Tautulli[Tautulli]
        NAS[QNAP NAS]
        Python[Python Services]
    end

    subgraph Devices
        Theater[Home Theater]
        Lights[Lighting]
        Climate[Climate]
        Energy[Energy / UPS]
        Cameras[Cameras / Security]
        Presence[Presence]
        Maker[Bambu / Maker]
    end

    User --> Alexa
    User --> Assist
    User --> Web

    Alexa --> Tunnel
    Web --> Tunnel
    User --> VPN

    Tunnel --> API
    API --> Alfred
    Alfred --> Registry

    Registry --> Laundry
    Registry --> RSVP
    Registry --> Operations
    Registry --> Charon
    Registry --> HA

    Laundry --> Alfred
    RSVP --> Alfred
    Operations --> Alfred
    Charon --> Alfred
    HA --> Alfred

    Alfred --> Giorgio
    Giorgio --> Alexa
    Giorgio --> Web

    Laundry --> Events
    RSVP --> Events
    Charon --> Events
    HA --> Events

    Events --> Queue
    Queue --> Osvaldo
    Osvaldo -->|Allow| Giorgio
    Osvaldo -->|Defer| Snoozable
    Osvaldo -->|Deny| NoDelivery[No Delivery]
    Snoozable --> Osvaldo
    Giorgio --> Delivery
    Delivery --> HA

    Assist --> HA
    VPN --> HA
    VPN --> NAS
    VPN --> NodeRED

    HA <--> MQTT
    HA <--> NodeRED
    HA <--> Python

    Charon --> Plex
    Charon --> Tautulli
    Plex --> NAS

    HA --> Theater
    HA --> Lights
    HA --> Climate
    HA --> Energy
    HA --> Cameras
    HA --> Presence
    HA --> Maker
```

## Reading the Diagram

The interactive path starts from a frontend and reaches Alfred through FastAPI. Alfred selects a registered domain tool and Giorgio renders the response.

The proactive path starts from a domain event. Osvaldo decides whether the event may be delivered, deferred or denied before Giorgio and the shared Home Assistant delivery service are involved.

Home Assistant remains responsible for physical orchestration and device wrappers. Alfred coordinates capabilities but does not replace the home-automation core.
