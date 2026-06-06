# Voice Flow

~~mermaid
flowchart LR
    User[User voice command]

    User --> Alexa[Alexa]
    User --> Assist[Home Assistant Assist]

    Alexa --> AlexaDevices[Alexa Devices integration]
    Alexa --> EmulatedHue[Emulated Hue triggers]
    Alexa --> CustomSkill[Alexa Custom Skill]

    AlexaDevices --> TTS[Echo TTS / text / sound]
    EmulatedHue --> HARoutines[Home Assistant routines]

    CustomSkill --> CF[Cloudflare Tunnel HTTPS]
    CF --> FastAPI[FastAPI Alexa bridge]

    FastAPI --> Alfred[Alfred session UX]
    Alfred --> IntentRouter[Intent routing]
    IntentRouter --> LaundryStatus[Laundry status intent]
    IntentRouter --> LaundryCatalog[Laundry catalog intents]
    IntentRouter --> LaundryControl[Laundry start / stop intents]
    IntentRouter --> PlexFuture[Future Plex HTTPS intents]

    LaundryStatus --> HA[Home Assistant REST API]
    LaundryCatalog --> ProgramCatalog[Validated local program catalog]
    LaundryControl --> ProgramCatalog
    LaundryControl --> SafetyChecks[Connection / remote / running-state checks]
    SafetyChecks --> HAScript[Home Assistant script wrapper]

    HA --> Laundry[hOn washing machine entities]
    HAScript --> LaundryAction[hOn start / stop services]
    LaundryAction --> Laundry

    Assist --> HA

    HA --> Plex[Plex helpers]
    HA --> Theater[Home theater automations]
    HA --> Energy[Energy / PV validation track]
    HA --> Presence[Presence validation track]

    Plex --> PlexPlayback[Plex search / playback]
    Theater --> SafePower[Safe-power logic]
    Energy --> FutureEnergyNotifications[Future proactive energy notifications]
    Presence --> FutureOccupancy[Future reliable occupancy logic]

    Alfred --> ExitIntent[Explicit exit intent]
    ExitIntent --> SessionClose[Close Alexa session]
~~

## Notes

- Alexa Custom Skill traffic enters through a public HTTPS bridge, not directly through Home Assistant.
- Alfred keeps the Alexa session open after functional responses.
- Alfred closes the session only on explicit exit phrases or Alexa timeout.
- Laundry start/stop uses quick command dispatch for Alexa UX.
- Laundry status remains the verification source of truth after command dispatch.
- Laundry control uses a validated local catalog and deterministic aliases, not fuzzy matching.
- Home Assistant owns the physical hOn command wrapper.
- Energy/PV and presence flows are shown as validation tracks, not completed automation foundations.
