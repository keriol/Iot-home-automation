# ADR-003 - Tailscale for Private Access

## Status

Accepted

## Context

The platform requires secure remote access to:

- Home Assistant
- Linux server
- NAS resources
- Internal dashboards
- Administrative services

Traditional approaches such as port forwarding expose services directly to the Internet and increase operational risk.

A secure private-access solution was required.

## Decision

Tailscale is used as the primary remote administration solution.

The platform exposes private services through a VPN-based model instead of opening management interfaces directly to the Internet.

## Responsibilities

Tailscale is used for:

- Home Assistant administration
- Server administration
- SSH access
- NAS access
- Internal dashboard access
- Private troubleshooting

## Alternatives Considered

### Port Forwarding

Rejected due to increased attack surface and operational complexity.

### Dynamic DNS + Open Ports

Rejected because it still exposes management services publicly.

### Full Self-Hosted VPN

Rejected because Tailscale provided faster deployment and lower maintenance overhead.

## Consequences

### Positive

- Minimal public attack surface
- Simple deployment
- Easy device onboarding
- Secure remote access
- Reduced firewall complexity
- Works well with mobile devices

### Negative

- Requires Tailscale client installation
- Dependency on Tailnet authentication
- Additional troubleshooting layer when diagnosing connectivity issues

## Security Model

Private administration remains private.

Administrative interfaces should not be exposed through public HTTPS endpoints unless explicitly required.

## Follow-up Rules

- Prefer Tailscale for administration.
- Avoid exposing management interfaces publicly.
- Keep VPN and public integration layers separated.
- Use HTTPS tunnels only for services that genuinely require public access.
