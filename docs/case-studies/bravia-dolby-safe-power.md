# Case Study - Bravia and Dolby Safe Power

## Problem

The TV could boot before the Dolby/home theater system was ready, causing eARC fallback to internal speakers.

## Solution

A native Home Assistant controlled smart plug powers the Dolby/home theater system. A guard helper prevents automation loops.

## Flow

1. TV turns on.
2. Home Assistant checks whether the Dolby plug is off.
3. If needed, the plug is turned on first.
4. The system waits for readiness.
5. TV restart or recovery is performed only when needed.
6. Guard is cleared.

## Result

The automation became local-first, easier to debug and independent from Alexa text commands.

## Skills Demonstrated

- State-based automation
- Failure mitigation
- Local-first design
- Debuggable smart-home orchestration
