from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
LLMS = (ROOT / "docs" / "llms.txt").read_text(encoding="utf-8")
RUFY = (ROOT / "docs" / "rufy" / "index.md").read_text(encoding="utf-8")
SITE_VERSION = (ROOT / "docs" / "site-version.txt").read_text(encoding="utf-8").strip()

errors = []

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
):
    if required not in MKDOCS:
        errors.append(f"mkdocs nav missing canonical page: {required}")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors), file=sys.stderr)
    raise SystemExit(1)

print("docs source checks: PASS")
