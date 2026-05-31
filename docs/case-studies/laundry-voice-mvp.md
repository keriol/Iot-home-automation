# Case Study - Local-first laundry voice assistant MVP

## Problem

The washing machine was integrated in Home Assistant through hOn, but the vendor voice experience was unreliable for program catalog questions.

In particular, catalog queries for white laundry programs could be mapped to generic cotton programs instead of the expected white-specific programs.

The target was to create a reliable local-first voice flow:

- ask for the current washing machine status;
- ask which programs are available for white laundry;
- receive spoken answers on an Echo device;
- avoid fragile cloud-only program naming.

## Architecture

Voice command
-> Alexa Routine
-> Emulated Hue virtual switch
-> Home Assistant automation
-> Python helper
-> hOn catalog / Home Assistant runtime states
-> Echo TTS notification

## Implementation summary

### Runtime status

A Python helper reads Home Assistant states for the washing machine:

- remote control status;
- current program name;
- remaining time;
- start and end time;
- temperature;
- spin speed.

If no wash cycle is active, the helper avoids exposing stale values such as old temperature, spin speed, duration, or steam state.

### Program catalog

The hOn integration can generate program detail notifications. These were used as a source to build a local JSON catalog of available washing programs.

The catalog was enhanced with Italian names from local hOn translation files, so spoken responses are understandable and not tied to raw internal codes.

### Alexa bridge

A local Emulated Hue bridge exposes virtual Home Assistant inputs to Alexa as simple on/off devices.

Alexa routines turn on those virtual inputs. Home Assistant automations react to them, run the correct local script, announce the answer on Echo, then reset the input.

## Why Emulated Hue

For the MVP, Emulated Hue provided a fast local bridge from Alexa to Home Assistant without requiring a custom Alexa Skill or public HTTPS endpoint.

This approach is useful for simple trigger-style commands, while a future custom Alexa Skill remains the better solution for rich natural language intents with parameters.

## Trade-offs

### Pros

- Local-first trigger path.
- No public endpoint required for the MVP.
- Reliable Home Assistant controlled responses.
- Sanitizable and portfolio-friendly architecture.
- Avoids incorrect vendor voice mappings.

### Cons

- Alexa sees virtual triggers as on/off devices.
- Natural phrases require Alexa routines.
- Dynamic parameters still need a custom Alexa Skill or another intent bridge.

## Result

Validated MVP flows:

- washing machine status voice command;
- white laundry programs voice command;
- spoken Echo response using Home Assistant generated text;
- local virtual trigger reset after execution.

## Future work

- Add safe remote start validation.
- Add safe stop/pause command validation.
- Add custom Alexa Skill through HTTPS tunnel for dynamic commands.
- Add PV-aware laundry recommendation.
- Add richer program categories and synonyms.
