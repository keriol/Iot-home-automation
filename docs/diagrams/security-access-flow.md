# Security and Access Flow Diagram

```mermaid
flowchart TD

    User[Remote User]
    Internet[Internet]
    Tailscale[Tailscale VPN]
    Cloudflare[Cloudflare Tunnel]
    HA[Home Assistant]
    Server[Linux Server]
    NAS[NAS / Private Storage]
    PublicAPI[Selected Public HTTPS Integrations]

    User --> Tailscale
    Tailscale --> HA
    Tailscale --> Server
    Tailscale --> NAS

    Internet --> Cloudflare
    Cloudflare --> PublicAPI
    PublicAPI --> HA
```
