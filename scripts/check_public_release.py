from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

# Public release hygiene: detect accidental private markers without storing
# workflow-specific names in source code.
DENY_FILES = {
    ".private",
    "private_notes.md",
}

TEXT_SUFFIXES = {
    ".py", ".pyfrag", ".md", ".txt", ".json", ".yml", ".yaml", ".cff",
    ".csv", ".toml", ".ini", ".cfg", ".sh", ""
}

violations = []

for path in ROOT.rglob("*"):
    rel = path.relative_to(ROOT)

    if path.name in DENY_FILES:
        violations.append(f"path: {rel}")

    if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
        try:
            text = path.read_text(encoding="utf-8").lower()
        except (UnicodeDecodeError, OSError):
            continue

        if "private repository marker" in text:
            violations.append(f"content: {rel}")

if violations:
    print("Public repository hygiene scan failed:")
    for item in sorted(set(violations)):
        print(" -", item)
    sys.exit(1)

print("Public repository hygiene scan passed.")
