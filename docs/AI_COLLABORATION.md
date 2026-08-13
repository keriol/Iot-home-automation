# AI-Assisted Development

## Overview

This project follows a hybrid engineering workflow that combines human decision-making with AI-assisted development.

The platform was originally started as a personal home automation experiment and gradually evolved into a structured smart-home and IoT platform.

Throughout the project lifecycle, AI tools have been used as technical copilots to support research, architecture reviews, troubleshooting, documentation and knowledge management.

All architecture decisions, implementation choices and production validations remain under human control.

## AI Usage Areas

AI is actively used for:

- Architecture reviews
- Design discussions
- Troubleshooting assistance
- Documentation generation
- Roadmap management
- Knowledge management
- Automation design reviews
- Code review support
- Refactoring suggestions
- Technology evaluation
- Research and feasibility analysis

## Development Context and Sources of Truth

The project originally relied on a continuously updated project model to preserve development context.

As the platform became multi-repository and Umberto matured, that responsibility was separated into explicit sources of truth:

- **Git** owns versioned implementation and documentation.
- **Umberto** owns tasks, milestones, priorities, dependencies and development evidence.
- **Live runtime state** owns operational truth.
- **Project models** provide compact derived architectural context.

The project model is therefore no longer a manually synchronized task ledger or the primary development-state authority.

It is refreshed when architectural changes or release milestones make a new compact snapshot useful.

See [ADR-009 - Development State Sources of Truth](adr/ADR-009-development-state-sources-of-truth.md).

## Development Workflow

Human responsibilities:

- Requirements
- Architecture decisions
- Security decisions
- Implementation
- Validation
- Production testing

AI responsibilities:

- Knowledge retrieval
- Documentation support
- Troubleshooting support
- Design review
- Alternative solution exploration
- Knowledge organization

## Benefits

Observed benefits include:

- Faster experimentation
- Better documentation quality
- Reduced knowledge loss
- Faster troubleshooting
- Consistent architectural decisions
- Improved project continuity

## Important Note

AI assists the development process but does not replace engineering judgment.

All final technical decisions and production deployments remain the responsibility of the project maintainer.
