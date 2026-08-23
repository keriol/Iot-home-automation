# Hardware Inventory

## Overview

This project integrates multiple consumer and prosumer devices into a unified smart-home platform.

The inventory is intentionally sanitized and does not expose serial numbers, device identifiers, private host paths or private network information.

## Compute

### Home Automation Server

Role:

- Home Assistant host
- MQTT broker host
- Node-RED host
- energy telemetry collection
- private remote-access endpoint
- selected HTTPS integration endpoint

Technologies:

- Linux
- Docker
- Python

## Voice Assistants

### Smart Speakers

Role:

- voice interaction
- text-to-speech notifications
- announcements
- smart-home control

Voice rendering remains a frontend concern and does not define Butler architecture ownership.

## Media

### Android TV

Role:

- Plex playback
- voice-driven media experience
- home-theater integration

### Home Theater System

Role:

- enhanced audio
- automated power management
- eARC integration

## Networking

### Router and Local Network

Role:

- local connectivity
- Internet access
- device communication

### Private Remote Access

Role:

- secure administration
- private access to internal services

## Energy

### Solar Inverter

Role:

- photovoltaic production monitoring
- local telemetry acquisition

### Battery Storage System

Role:

- energy storage
- battery-state monitoring

Energy telemetry is currently **In testing**: stable and usable privately, but still subject to long-window validation before stronger claims are made.

## Sensors

### BLE Adapter

Role:

- experimental presence-signal collection
- evaluation of privacy-conscious occupancy approaches

BLE presence is **Designed to enable**, not an authoritative occupancy source. Critical home/away automations must not depend on the current experimental signal alone.

### Temperature Sensors

Role:

- environmental monitoring
- incremental climate-automation validation

## Cameras

### RTSP Cameras

Role:

- video monitoring
- future smart-event evaluation

## Smart Devices

### Smart Plugs

Role:

- power automation
- device protection
- media workflows

### Smart Lighting

Role:

- lighting automation
- scene management

### Smart Appliances

Role:

- laundry monitoring
- controlled appliance workflows
- future energy-aware recommendations

## Candidate Hardware Directions

Potential additions are evaluated only when they solve a validated need. Examples include dedicated low-power presence beacons, expanded environmental sensing and additional local event-processing hardware.

Candidate hardware does not imply an active implementation or purchase commitment.
