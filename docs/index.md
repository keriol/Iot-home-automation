---
title: Butler Documentation
kind: landing
scope: public
status: current
---

# Butler Documentation

Public-safe architecture, API and engineering documentation for the Butler ecosystem.

## Start here

- [Architecture Overview](architecture/overview.md)
- [Bifröst Client API](api/bifrost.md)
- [Midgard](architecture/midgard.md)
- [Asgard](architecture/asgard.md)
- [IGNITION-001](milestones/ignition-001.md)
- [Agent Guide](agent/index.md)

## Documentation model

The Markdown in this repository is canonical.

MkDocs and GitHub Pages provide navigation, search and presentation. They do not
create a second documentation source of truth.

Development state belongs in GitHub Issues, release evidence belongs in
tags/releases/workflows, and live systems remain authoritative for runtime state.


## Site version

Current documentation-site development line: **0.1.0.dev0**.

The documentation site has its own release lifecycle. A site version becomes
`0.1.0` only after GitHub Pages deployment succeeds and the live site is
verified. Documentation-site releases use the `docs-vX.Y.Z` tag namespace.
