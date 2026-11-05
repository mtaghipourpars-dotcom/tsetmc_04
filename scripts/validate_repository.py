from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = 60

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)

files = sorted(SKILLS.glob("SKILL-[0-9][0-9].md"))
if len(files) != EXPECTED:
    fail(f"expected {EXPECTED} skill files, found {len(files)}")

for number, path in enumerate(files, start=1):
    text = path.read_text(encoding="utf-8")
    expected_id = f"SKILL-{number:02d}"
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML front matter")
    front = text.split("---", 2)[1]
    if not re.search(rf"(?m)^id: {expected_id}$", front):
        fail(f"{path}: id mismatch")
    if not re.search(r"(?m)^status: SPECIFICATION$", front):
        fail(f"{path}: expected SPECIFICATION status")
    if f'"skill_id": "{expected_id}"' not in text:
        fail(f"{path}: output contract skill_id mismatch")
    if "## آزمون پذیرش" not in text:
        fail(f"{path}: acceptance criteria section missing")

required = [
    ROOT / "README.md",
    ROOT / "MASTER_CATALOG.md",
    ROOT / "docs" / "ARCHITECTURE.md",
    ROOT / "docs" / "DATA_CONTRACTS.md",
    ROOT / "docs" / "SECURITY_AND_GOVERNANCE.md",
    ROOT / "docs" / "IMPLEMENTATION_STATUS.md",
]
for path in required:
    if not path.is_file():
        fail(f"required file missing: {path.relative_to(ROOT)}")

print(f"OK: validated {len(files)} skill specifications and repository baseline files.")
