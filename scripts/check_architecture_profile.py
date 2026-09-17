#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = (ROOT / "README.md", ROOT / "README_EN.md")

COMMON = (
    "```mermaid",
    "sequenceDiagram",
    "Eco²",
    "GEODE",
    "Experimental Loop",
    "Context Control",
    "Plan and Execute",
    "Verify",
    "Observe",
    "Scaffold",
    "Trajectory",
    "Ratchet",
    "Baseline",
    "Scaffold Search",
    "Evaluation",
    "Ledger",
    "83/83",
    "97.8%",
    "1,477",
)

KO = (
    "## 발전 과정",
    "## 검증, 재현, 기록",
    "trajectory는 연구 데이터",
    "래칫은 기억을 자동화",
    "탐색 공간은 닫지 않습니다",
)

EN = (
    "## Evolution",
    "## Verification, reproduction, and records",
    "A trajectory is research data",
    "A ratchet automates memory",
    "search space stays open",
)

FORBIDDEN = (
    "Compiler AX",
    "compiler-ax-lab",
    "46,080",
    "doctest",
    "FuriosaAI",
)


def main() -> int:
    errors = []
    for path in PAGES:
        text = path.read_text(encoding="utf-8")
        if text.count("```mermaid") < 4:
            errors.append(f"{path.name}: expected at least four Mermaid sequence diagrams")
        if "—" in text:
            errors.append(f"{path.name}: em dash is not allowed")
        for term in FORBIDDEN:
            if term in text:
                errors.append(f"{path.name}: removed Compiler AX reference returned: {term!r}")
        for term in COMMON:
            if term not in text:
                errors.append(f"{path.name}: missing architecture term {term!r}")
    for term in KO:
        if term not in PAGES[0].read_text(encoding="utf-8"):
            errors.append(f"README.md: missing Korean ratchet {term!r}")
    for term in EN:
        if term not in PAGES[1].read_text(encoding="utf-8"):
            errors.append(f"README_EN.md: missing English ratchet {term!r}")
    if errors:
        print("Architecture profile checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Architecture profile checks passed: evolution, runtime, evidence, sequence diagrams, and ratchets are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
