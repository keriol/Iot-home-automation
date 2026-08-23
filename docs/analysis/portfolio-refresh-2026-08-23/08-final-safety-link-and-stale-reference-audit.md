# 08 — Final Safety, Navigation and Stale-Reference Audit

## Scope

This final DOC-003 audit checked the public portfolio for residual current-state drift, privacy/sanitization violations and navigation problems before integration.

The goal was not to rewrite historical evidence. The goal was to ensure that anything presented as **current guidance or current state** matches the present architecture and governance model.

## Findings corrected during the final pass

### 1. Machine-specific deployment paths

`docs/architecture/server-paths.md` still exposed a section labelled as a real local layout with concrete host paths.

That contradicted the DOC-003 public-safety rule that public-facing documentation must not publish machine-specific private server paths.

The document now contains only sanitized example paths and explicitly states that they are documentation placeholders rather than the real Keriol Home layout.

### 2. Volatile runtime metrics presented as durable portfolio state

`docs/METRICS.md` contained exact container, automation, script and YAML-file counts collected from an older live environment snapshot.

It also described BLE presence more strongly than current evidence supports.

Those values were removed from current-state documentation. The file now records durable evidence indicators and capability maturity rather than attempting to mirror live operational counts.

### 3. Former development-ledger governance still presented as current

`docs/project-model/README.md` and `docs/AI_COLLABORATION.md` still assigned active development-state ownership to the retired private ledger and linked ADR-009 as current governance.

They now point to ADR-011 and the current authority split:

- GitHub Issues for planning and active development state;
- Git `main` for merged implementation/documentation;
- commits/tags/workflows/releases for implementation and release evidence;
- live systems for runtime truth;
- project models and portfolio analysis as derived context only.

`docs/PROJECT_MODEL.md` was also clarified so that the public model is described as curated architectural context, not a mechanical export of private implementation.

### 4. Old maturity vocabulary in current narrative

`docs/PROJECT_ORIGIN.md` still used the earlier `Public / Private validated / Candidate` vocabulary as if it were current.

The document now uses:

- Available;
- In testing;
- Designed to enable.

Historical snapshots retain their original vocabulary.

### 5. Presence diagram implied production-ready automation

`docs/diagrams/presence-flow.md` previously showed a direct path from BLE-derived presence entities to occupancy automations.

Current evidence does not support that level of confidence. The presence effort is deliberately conservative and parked pending a more reliable, privacy-conscious signal.

The diagram now shows candidate occupancy signal -> confidence/safety evaluation -> future automations, with the final edge explicitly conditional on validation.

### 6. Historical Umberto documents lacked superseded status

The old analysis and checkout-flow diagram remain useful as engineering history, but direct readers could still mistake them for current workflow guidance.

Both now contain explicit **superseded historical evidence** labels and point to ADR-011 for current governance.

### 7. Hardware narrative overclaimed presence maturity

`docs/HARDWARE.md` previously described the BLE adapter as supporting presence detection and occupancy tracking without qualification.

It now describes BLE as experimental presence-signal collection and marks the direction as Designed to enable. Energy telemetry is likewise labelled In testing rather than implicitly production-final.

## Public-safety verification

The final public boundary requires that the repository exclude:

- readable private Alfred implementation;
- credentials, tokens and secrets;
- private endpoints, hostnames or private network topology;
- machine-specific private server paths;
- unnecessary real entity/device/account identifiers;
- runtime databases, logs or private configuration snapshots;
- private media-acquisition implementation, naming or recognizable implementation details.

During DOC-003, private mechanisms were represented only through architectural boundary terms such as `private media-acquisition implementation` when the boundary itself needed explanation.

No public documentation change intentionally exposes the private implementation behind that boundary.

## Navigation verification

The main reader path is now coherent:

`README -> docs/README -> PROJECT_STATUS / SHOWCASE / architecture -> case studies / ADRs / analysis trail`

The documentation index links to the current project model and ADR-011-based governance. Historical Umberto material is no longer presented as current planning guidance.

Existing referenced diagrams for architecture, energy, presence, laundry verification, home theater, security access and AI-assisted development are present on the DOC-003 branch.

## Release/state verification

The current portfolio baseline remains:

- Butler Core `0.1.4` released baseline;
- Butler Core `main` on `0.1.5.dev0` development line;
- Wilfred `0.2.1` current Public Alpha;
- `wilfred-home-assistant` on `0.1.0.dev0` development line;
- Alfred `0.4.0` private released baseline with later private development.

Development versions and open issues are not presented as releases.

## Historical-preservation rule

Dated project-model snapshots, old worklogs and superseded ADRs remain untouched unless a current wrapper/index must clarify their historical status.

The portfolio therefore preserves evolution without allowing historical state to masquerade as current state.

## Final assessment before integration

DOC-003 is ready for integration once:

1. the branch is confirmed to remain ahead of and not behind `main`;
2. the DOC-003 checklist is reconciled with completed evidence;
3. integration into `main` is verified;
4. final integration evidence is recorded on the issue;
5. the issue is closed only after those checks succeed.
