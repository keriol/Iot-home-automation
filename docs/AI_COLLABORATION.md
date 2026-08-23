# AI-Assisted Development

## Overview

This project follows a hybrid engineering workflow that combines human decision-making with AI-assisted development.

The platform began as a personal home-automation experiment and gradually evolved into a structured smart-home and IoT platform with reusable Butler components.

AI tools are used as technical copilots for research, architecture review, troubleshooting, documentation, planning and knowledge organization.

Architecture decisions, implementation choices, safety decisions and production validation remain under human control.

## AI Usage Areas

AI is actively used for:

- architecture reviews;
- design discussions;
- troubleshooting assistance;
- documentation generation and review;
- GitHub issue/task planning;
- knowledge management;
- automation design review;
- code review support;
- refactoring suggestions;
- technology evaluation;
- research and feasibility analysis.

## Development Context and Sources of Truth

The project originally relied on a continuously updated project model, and later on a separate private development ledger, to preserve development context.

As the Butler ecosystem became multi-repository and increasingly public, development ownership moved to GitHub.

Current authority is split deliberately:

- **GitHub Issues** own tasks, priorities, dependencies, planning and active development status.
- **Git `main`** owns merged implementation and versioned documentation.
- **Commits, tags, workflows and releases** provide implementation and release evidence.
- **Live systems** own deployed operational truth.
- **Project models and portfolio analysis** provide compact derived architectural context.

The project model is therefore neither a task ledger nor the primary development-state authority.

See [ADR-011 - GitHub as Development Source of Truth](adr/ADR-011-github-development-source-of-truth.md).

Older ADRs and historical snapshots retain the governance model that was current when they were written.

## Development Workflow

Human responsibilities include:

- requirements and priorities;
- architecture and ownership decisions;
- security and privacy decisions;
- implementation acceptance;
- validation strategy;
- production/runtime verification.

AI-assisted responsibilities include:

- knowledge retrieval;
- documentation support;
- troubleshooting support;
- design review;
- alternative-solution exploration;
- repository/state analysis;
- structured knowledge organization.

## Evidence Discipline

AI-generated analysis does not promote a feature to released or available status.

Portfolio and release claims remain grounded in the authoritative evidence for the owning layer:

- issue state for planned/active work;
- Git for merged implementation;
- tags/releases/workflows for release evidence;
- live systems for runtime behavior.

## Benefits

Observed benefits include:

- faster experimentation;
- stronger documentation continuity;
- reduced knowledge loss;
- faster troubleshooting;
- more explicit architectural trade-offs;
- improved multi-repository continuity;
- retained intermediate analysis for later review.

## Important Note

AI assists the engineering process but does not replace engineering judgment or observable verification.
