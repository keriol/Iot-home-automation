# 06 — Decisions and Rejected Alternatives

This note records decisions made during DOC-003 that are easy to lose once the final documentation looks clean.

## 1. Do not infer release state from recent development

### Rejected

Treat the newest commit, branch or open issue as the current release state.

### Why rejected

Development and release evidence answer different questions. Butler Core, for example, can have a development version on `main` while the released baseline remains an earlier tagged version.

### Decision

Document released baseline and development line separately.

---

## 2. Do not rewrite historical ADRs

### Rejected

Edit the earlier development-governance ADR so it appears to have always used GitHub as the source of truth.

### Why rejected

That would destroy the chronology of the architecture and make historical reasoning unreliable.

### Decision

Preserve the earlier ADR and supersede it with a new current ADR.

---

## 3. Do not turn the portfolio into a new development ledger

### Rejected

Mirror every issue, branch, milestone and task state into portfolio documents.

### Why rejected

That recreates the exact synchronization problem the governance change was intended to remove.

### Decision

Keep a reference ledger only for documentation evidence and refresh triggers. GitHub Issues remain authoritative for development state.

---

## 4. Do not equate a branch with a feature

### Rejected

Use branch existence as proof that a capability is implemented or available.

### Why rejected

Branches may contain incomplete work, abandoned experiments, historical code or development scaffolding.

### Decision

Use branches as development references only. Availability requires merged/released evidence.

---

## 5. Do not collapse maturity into public/private location

### Rejected

Use only `Public / Private validated / Candidate` as current maturity language.

### Why rejected

A private behavior may be strongly validated but still not be public, while an architecture may support a future capability without implementing it.

### Decision

Use `Available / In testing / Designed to enable` for current evidence maturity, while separately describing where the behavior lives.

---

## 6. Do not move frontend presentation into Butler Core

### Rejected

Treat speech, SSML, named voices or Alexa behavior as part of the reusable Core architecture.

### Why rejected

Core must remain provider-neutral and frontend-replaceable.

### Decision

Keep presentation at the provider/frontend boundary. Hermes handles delivery framework concerns; Osvaldo handles communication policy.

---

## 7. Do not model a configured voice as an architectural actor

### Rejected

Represent the configured Alexa voice as a service, domain, persona owner or diagram node.

### Why rejected

It is a speech-rendering parameter. Giving it architectural ownership would confuse presentation with behavior.

### Decision

Document it narrowly as frontend/provider configuration where relevant to voice delivery.

---

## 8. Do not patch a runtime discrepancy from architecture assumptions

### Rejected

Apply a source change immediately after one real notification used an unexpected voice.

### Why rejected

Rapid triage showed the expected rendering and speech-delivery path was still present in source. A blind patch could hide the real fallback/routing problem.

### Decision

Track the regression privately and require concrete runtime tracing before implementation.

---

## 9. Do not publish private implementation merely to make a case study convincing

### Rejected

Include readable private code, operational mappings or private acquisition details as proof that a workflow is real.

### Why rejected

The engineering lesson can be demonstrated through architecture, observable behavior and public-safe evidence without exposing the private system.

### Decision

Publish derived patterns and sanitized outcomes only.

---

## 10. Do not reuse historical documentation IDs

### Observation

The initial refresh was briefly named `DOC-001` before repository history showed that `DOC-001` and `DOC-002` had already been used.

### Risk

Reusing an old identifier would make commits and historical references ambiguous.

### Decision

The active refresh was corrected to `DOC-003`, with branch `docs/doc-003-portfolio-sync`, before new history was allowed to depend on the conflicting identifier.

---

## 11. Do not hide intermediate reasoning once the final docs are clean

### Rejected

Keep only the polished README, roadmap and architecture files.

### Why rejected

Future maintainers would see what the current model says but not why older claims were removed, why evidence thresholds changed or why certain public directions were deliberately not promoted.

### Decision

Preserve a public-safe intermediate analysis trail under `docs/analysis/portfolio-refresh-2026-08-23/`.

New DOC-003 analysis should be added there as further case-study, narrative and final-safety reviews are completed.
