# Home Theater Safe Power Flow

```mermaid
flowchart TD

    TV[Bravia TV Powered On]
    Guard[Safe Power Guard]
    Plug[Tapo Smart Plug]
    Dolby[Home Theater System]
    Reboot[Controlled TV Restart]
    EARC[eARC Handshake]

    TV --> Guard
    Guard --> Plug
    Plug --> Dolby
    Dolby --> Reboot
    Reboot --> TV
    TV --> EARC
```
