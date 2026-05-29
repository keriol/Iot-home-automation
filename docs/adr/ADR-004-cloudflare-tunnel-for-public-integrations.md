# ADR-004 - Cloudflare Tunnel for Public Integrations

## Status

Accepted

## Context

Some services require public HTTPS access:

- Future voice assistant integrations
- Webhooks
- Public APIs
- External callbacks
- Future portfolio demonstrations

The project requires public HTTPS connectivity without exposing the home network through traditional port forwarding.

## Decision

Cloudflare Tunnel is used as the preferred solution for exposing selected services over HTTPS.

The tunnel provides secure inbound access without opening firewall ports directly to the Internet.

## Responsibilities

Cloudflare Tunnel is used for:

- HTTPS endpoint publication
- Webhook reception
- Future voice assistant integrations
- Public API exposure
- Controlled external access

## Alternatives Considered

### Port Forwarding

Rejected due to security concerns and increased attack surface.

### Dynamic DNS + Reverse Proxy

Rejected because it still requires inbound exposure and additional maintenance.

### VPN-only Access

Rejected because some integrations require publicly reachable HTTPS endpoints.

## Consequences

### Positive

- No inbound ports required
- HTTPS available by default
- Reduced attack surface
- Easier certificate management
- Simpler firewall configuration
- Suitable for webhook-driven integrations

### Negative

- Additional dependency on Cloudflare services
- Tunnel service must remain operational
- Public endpoints require access control policies

## Security Model

Public integrations and private administration are intentionally separated.

### Private Layer

Used for:

- Home Assistant administration
- SSH access
- NAS administration
- Internal dashboards

Technology:

- Tailscale

### Public Layer

Used for:

- Webhooks
- External integrations
- Public APIs
- Future voice assistant services

Technology:

- Cloudflare Tunnel

## Follow-up Rules

- Never expose management interfaces publicly.
- Keep public endpoints limited to required services.
- Prefer Cloudflare Access policies when possible.
- Maintain separation between public and private traffic.
