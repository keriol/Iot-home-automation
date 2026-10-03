# Project Model

The active project model is now the **versioned documentation corpus**, not one
standalone context file.

Use the documentation according to the kind of knowledge you need:

- [Architecture Overview](architecture/overview.md) for current ownership and layering;
- [Bifröst API](api/bifrost.md) for the Butler client/API boundary;
- [Communication Model](architecture/communication-model.md) for Bifröst/Midgard/Asgard;
- [Project Status](PROJECT_STATUS.md) for the current public-safe baseline;
- [ADRs](adr/) for architectural decisions;
- [IGNITION-001](milestones/ignition-001.md) for the released communication compatibility baseline;
- [Project History](history/index.md) for evolution and superseded stages;
- [Agent Guide](agent/index.md) for automated contributor reading order.

The compact file
[project-model-public.md](project-model/project-model-public.md) remains a
public-safe compatibility/reference summary. Dated files in that directory are
historical snapshots.

GitHub Issues own active development state. Repository `main` owns merged
implementation and documentation. Tags/releases/workflows provide release
evidence. Live systems provide runtime truth.

The raw private local project model is retired and is not published as a public
source. Its final era is preserved through a
[sanitized historical record](history/local-project-model-retirement-2026-10-03.md).
