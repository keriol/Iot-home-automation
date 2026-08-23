# 01 — Baseline and Documentation Drift Audit

## Question

What did the public portfolio claim before DOC-003, and which claims had drifted from authoritative repository evidence?

## Repository baseline

The portfolio repository was already structurally sound: README, roadmap, architecture docs, ADRs, analysis notes, worklogs and historical material were separated rather than collapsed into one document.

The main problem was not repository organization. It was **current-state drift** after rapid Butler development.

## Evidence-backed baselines established during the audit

- Butler Core `0.1.4` is the released Core baseline consumed by Wilfred `0.2.1`.
- Butler Core `main` has moved to the `0.1.5.dev0` development line.
- Wilfred `0.2.1` is the current Public Alpha.
- `wilfred-home-assistant` remains on its `0.1.0.dev0` development line.
- Alfred `0.4.0` is the current private released baseline; later Alfred work is private development evidence, not a public release claim.

The important distinction is between **released baseline** and **current development line**. Development versions must not silently replace released versions in public prose.

## Drift found in the README

The pre-refresh README still described Wilfred as moving *toward* the `0.2.0` Public Alpha even though `0.2.1` was already the current Public Alpha.

It also still reflected an older development-governance model in which the former private ledger owned active development state.

The architecture story itself remained useful, especially the split between Home Assistant physical orchestration and Butler reasoning/execution.

## Drift found in the roadmap

The roadmap contained several obsolete checkpoints:

- Butler Core `0.1.3` as current state;
- Wilfred `0.2.0.dev0` as the active public-alpha line;
- tasks to complete the `0.2.0` release that had already happened;
- a crowdfunding gate tied to the `0.2.0` release;
- the former private development ledger as active coordination authority.

These were not historical documents. They were current-state claims, so leaving them unchanged would misrepresent the project.

## Drift found in the architecture/model documents

The architecture overview was directionally correct but predated the stronger capability-first/domain-ownership language.

The public project model was the most visibly stale document:

- dated 2026-08-13;
- still assigned active development ownership to the retired private ledger;
- still said the current direction was to finish Wilfred `0.2.0` Public Alpha readiness;
- used the earlier `Public / Private validated / Candidate` maturity vocabulary.

## What was deliberately not treated as drift

Historical ADRs, dated project-model snapshots and old worklogs may contain superseded architecture or governance. Those documents are evidence of what was true or believed at that time.

They are not corrected retroactively merely because the current model changed.

## Outcome

DOC-003 therefore became a **current-state refresh**, not a history rewrite.

The refresh updates only documents that present themselves as current, while preserving historical snapshots and superseded ADRs as historical evidence.
