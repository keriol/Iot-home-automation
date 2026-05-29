# Energy Flow Diagram

```mermaid
flowchart LR

    PV[PV Inverter]
    Battery[Battery Storage]
    Poller[Python Energy Poller]
    MQTT[MQTT Broker]
    HA[Home Assistant]
    Dashboard[Energy Dashboard]

    PV --> Poller
    Battery --> Poller
    Poller --> MQTT
    MQTT --> HA
    HA --> Dashboard
```
