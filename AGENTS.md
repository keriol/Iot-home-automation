# Butler Documentation Agent Entry

This repository is the public-safe documentation hub for the Butler ecosystem and
Keriol Home portfolio.

Start with `docs/agent/index.md` and choose the correct workflow.

For feature/architecture work:

1. `docs/agent/source-of-truth.md`
2. `docs/agent/feature-design.md`
3. relevant component/API/architecture pages

For first installation/onboarding assistance:

1. `docs/agent/source-of-truth.md`
2. `docs/agent/first-installation.md`
3. released installation documentation from the owning repository

Do not treat this repository as the source of active task status, runtime state or
private Alfred implementation.

Authoritative sources:

- GitHub Issues: active work, priorities, dependencies and planning;
- repository `main`: merged implementation and versioned documentation;
- tags/releases/workflows: release evidence;
- live systems: deployed/runtime truth;
- this repository: public-safe derived architecture and engineering documentation.

Public/private boundary:

- never add credentials, private endpoints, household-specific identifiers,
  sensitive runtime state or readable private Alfred implementation;
- private Alfred knowledge belongs in the Alfred repository;
- reusable architecture belongs here or in the owning public component repository.

For feature work, identify the owning component before proposing code.
