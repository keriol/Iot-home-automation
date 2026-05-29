# Presence Flow Diagram

```mermaid
flowchart LR

    Phone[BLE Phone Beacon]
    Adapter[Bluetooth Adapter]
    Bermuda[Bermuda BLE]
    HA[Home Assistant]
    Presence[Presence Entities]
    Automations[Occupancy Automations]

    Phone --> Adapter
    Adapter --> Bermuda
    Bermuda --> HA
    HA --> Presence
    Presence --> Automations
```
