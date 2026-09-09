from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

# Construct private-workflow markers without embedding them verbatim in the repository.
DENY = (
    "co" + "dex",
    "ко" + "декс",
    "chat" + "gpt",
    "open" + "ai",
    "_" + "prompt",
    "agent_" + "prompt",
)

TEXT_SUFFIXES = {
    ".py", ".md", ".txt", ".json", ".yml", ".yaml", ".cff",
    ".csv", ".toml", ".ini", ".cfg", ".sh", ""
}

violations = []
for path in ROOT.rglob("*"):
    rel = str(path.relative_to(ROOT))
    rel_low = rel.lower()
    for marker in DENY:
        if marker in rel_low:
            violations.append(f"path: {rel}")

    if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
        try:
            text = path.read_text(encoding="utf-8").lower()
        except (UnicodeDecodeError, OSError):
            continue
        for marker in DENY:
            if marker in text:
                violations.append(f"content: {rel}")
                break

if violations:
    print("Public repository hygiene scan failed:")
    for item in sorted(set(violations)):
        print(" -", item)
    sys.exit(1)

print("Public repository hygiene scan passed.")
