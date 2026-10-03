from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

errors = []

rufy_html = SITE / "rufy" / "index.html"
if not rufy_html.exists():
    errors.append("secret page was not built")
else:
    html = rufy_html.read_text(encoding="utf-8")
    if 'name="robots"' not in html or "noindex,nofollow" not in html:
        errors.append("secret page is missing noindex,nofollow")

search_file = SITE / "search" / "search_index.json"
if not search_file.exists():
    errors.append("search index was not generated")
else:
    raw = search_file.read_text(encoding="utf-8").lower()
    for forbidden in ("there is no king of the pirates", "rufy was here"):
        if forbidden in raw:
            errors.append(f"secret page leaked into search index: {forbidden}")

for required in (
    SITE / "index.html",
    SITE / "api" / "bifrost" / "index.html",
    SITE / "architecture" / "midgard" / "index.html",
    SITE / "architecture" / "asgard" / "index.html",
    SITE / "milestones" / "ignition-001" / "index.html",
):
    if not required.exists():
        errors.append(f"expected page missing from site: {required.relative_to(SITE)}")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors), file=sys.stderr)
    raise SystemExit(1)

print("docs build checks: PASS")
