from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
LLMS = (ROOT / "docs" / "llms.txt").read_text(encoding="utf-8")
RUFY = (ROOT / "docs" / "rufy" / "index.md").read_text(encoding="utf-8")
SITE_VERSION = (ROOT / "docs" / "site-version.txt").read_text(encoding="utf-8").strip()

CURRENT_SURFACES = {
    "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
    "ROADMAP.md": (ROOT / "ROADMAP.md").read_text(encoding="utf-8"),
    "docs/PROJECT_STATUS.md": (ROOT / "docs" / "PROJECT_STATUS.md").read_text(encoding="utf-8"),
    "docs/SHOWCASE.md": (ROOT / "docs" / "SHOWCASE.md").read_text(encoding="utf-8"),
    "docs/project-model/project-model-public.md": (
        ROOT / "docs" / "project-model" / "project-model-public.md"
    ).read_text(encoding="utf-8"),
}

errors = []

required_current = {
    "README.md": ("Butler Core `0.3.0`", "Bifröst `0.1.0`", "Midgard `0.1.0`"),
    "ROADMAP.md": ("Butler Core `0.3.0`", "Alfred `0.5.0`", "IGNITION-001"),
    "docs/PROJECT_STATUS.md": ("Butler Core | Available | `0.3.0`", "Alfred | Private operational | `0.5.0`"),
    "docs/SHOWCASE.md": ("Butler Core `0.3.0`", "Ignition Butler-to-Android Network"),
    "docs/project-model/project-model-public.md": ("Butler Core 0.3.0", "Bifröst 0.1.0", "Midgard 0.1.0"),
}

for path, needles in required_current.items():
    body = CURRENT_SURFACES[path]
    for needle in needles:
        if needle not in body:
            errors.append(f"current documentation drift in {path}: missing {needle}")

forbidden_current = (
    "Butler Core `0.2.0` is the current released",
    "Core `main` is on the `0.2.1.dev0`",
    "currently on its `0.2.0.dev0` development line",
    "Alfred `0.4.0` is the released private baseline",
)

for path, body in CURRENT_SURFACES.items():
    for forbidden in forbidden_current:
        if forbidden in body:
            errors.append(f"stale current baseline in {path}: {forbidden}")

if not SITE_VERSION:
    errors.append("documentation site version is empty")

if f"site_version: {SITE_VERSION}" not in MKDOCS:
    errors.append("mkdocs.yml site_version does not match docs/site-version.txt")

for forbidden in ("rufy/index.md", "There is no king of the pirates"):
    if forbidden.lower() in MKDOCS.lower():
        errors.append(f"secret page leaked into mkdocs nav/config: {forbidden}")
    if forbidden.lower() in LLMS.lower():
        errors.append(f"secret page leaked into llms.txt: {forbidden}")

for required in (
    "robots: noindex,nofollow",
    "exclude: true",
    "# There is no king of the pirates",
):
    if required not in RUFY:
        errors.append(f"secret page missing guard: {required}")

for required in (
    "api/bifrost.md",
    "architecture/midgard.md",
    "architecture/asgard.md",
    "milestones/ignition-001.md",
    "agent/index.md",
    "PROJECT_MODEL.md",
    "history/index.md",
):
    if required not in MKDOCS:
        errors.append(f"mkdocs nav missing canonical page: {required}")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors), file=sys.stderr)
    raise SystemExit(1)

print("docs source checks: PASS")
