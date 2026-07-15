# Roadmap

Keriol Home evolves as a local-first smart-home platform with Alfred providing one coherent interface to its services.

The roadmap is organized by delivery horizon rather than by implementation history.

## Current Foundation

- Home Assistant, MQTT and Node-RED orchestration
- FastAPI and Alfred Core
- Tool Registry with READ, ACTION and DANGEROUS permissions
- Deterministic-first routing with AI fallback
- Alexa custom-skill and free-text backend paths
- Shared Giorgio speech rendering
- Osvaldo proactive notification policy
- Snoozable notification queue
- Plex and Tautulli integration
- Charon media-domain foundation
- Laundry, RSVP and server READ tools
- Confirmed Plex scan actions
- Tailscale private access
- Cloudflare Tunnel public integration layer
- Public-safe documentation and model export
- Umberto Development Ledger with SQLite-backed tasks and commit evidence
- Strict private-to-public project-model export and validation

## Near Term

### Voice and Agent

- Complete the Alexa Developer Console free-text model
- Validate free-text behavior on supported Alexa devices
- Keep legacy deterministic intents available during migration
- Add a general Home Assistant notification tool
- Review AI latency, logging and model-cost behavior

### Appliances

- Register laundry start and stop as Alfred ACTION/DANGEROUS tools
- Require explicit confirmation before physical control
- Verify hOn and Home Assistant state after commands
- Add PV-aware laundry suggestions when presence and energy inputs are reliable

### Media and Charon

- Add dedicated tests for Plex notification cooldown and `mark_notified`
- Expand playback-offer handling
- Build missing-title and catalog-quality analysis
- Add recommendation workflows
- Explore coordinated home-theater scenes

### Maintenance

- Remove pre-Git backup files in a dedicated cleanup commit
- Continue reducing duplicated integration logic
- Keep private and public project models synchronized through the export pipeline
- Automate health checks, tests, evidence and documentation through Umberto checkout workflows

## Platform Development

### Presence and House Modes

- Build reliable person and home-presence states
- Stabilize network and Bluetooth inputs
- Add guest, empty-house and vacation modes
- Expose presence through Alfred READ tools
- Avoid critical automation until confidence is measurable

### Operations and Observability

- Add a dashboard for registered tools, health and logs
- Track AI requests, latency and cost
- Move persistent Alfred memory from JSON to SQLite
- Add an AI Budget Manager with cache and usage controls

### Network, NAS and Backup

- Add NAS health and capacity tools
- Expose backup status without revealing private paths
- Monitor core network and tunnel availability
- Keep runtime and database backups separate from Git history

### Energy and UPS

- Add READ tools for production, consumption and grid exchange
- Add battery and UPS health visibility
- Detect abnormal consumption and outage risk
- Suggest useful actions during solar surplus
- Integrate energy context into appliance recommendations

### Calendar and Weather

- Add live READ tools
- Use current data rather than cached model knowledge
- Support future planning and proactive workflows

## Domain Expansion

### Security and Cameras

- Review and normalize the Home Assistant camera inventory
- Validate ONVIF capabilities
- Define a common camera-event model
- Add a security dashboard
- Pilot presence-aware alerts
- Evaluate Frigate only where object detection adds clear value

### Climate

- Combine temperature, humidity, weather, presence and room usage
- Start with advisory workflows
- Introduce automation gradually and with conservative safeguards

### Bambu and Maker

- Add READ tools for printer state, job progress, temperatures and errors
- Add confirmed pause and cancel actions
- Route proactive print notifications through Osvaldo

### Cross-Domain Automation

- Use presence to improve notification timing
- Combine energy surplus with appliance suggestions
- Combine house modes with security and camera events
- Coordinate media, lighting and room scenes
- Keep proactive behavior quiet, useful and explainable

## Documentation

- Keep architecture, ADRs, diagrams and worklogs aligned with implementation
- Document significant decisions rather than command-by-command noise
- Use the private model for active project state and roadmap
- Generate the public model through the sanitizing export script
- Reserve milestone releases for major completed phases or architectural improvements
