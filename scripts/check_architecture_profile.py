#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = (ROOT / "README.md", ROOT / "README_EN.md")

COMMON = (
    "Eco²",
    "GEODE",
    "Experimental Loop",
    "Context Control",
    "AgenticLoop",
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
    "KEEP",
    "REJECT",
    "INVALID",
    "RSI",
    "Event Router",
    "ArgoCD",
)

KO = (
    "## 발전 과정",
    "## 검증, 재현, 기록",
    "개선 루프 · 관측한 실패가 다음 구조를 바꾸는 방식",
    "guardrail 자체도 검증 대상",
    "same workload",
)

EN = (
    "## Evolution",
    "## Verification, reproduction, and records",
    "Improvement loop · How observed failures changed the next architecture",
    "guardrail itself became an object of verification",
    "same workload",
)

FORBIDDEN = (
    "Compiler AX",
    "compiler-ax-lab",
    "46,080",
    "doctest",
    "FuriosaAI",
)


def validate_architecture(text: str) -> list[str]:
    """Preserve subjects and decision outcomes, not a diagram type or slogan."""
    errors = []
    if "—" in text:
        errors.append("em dash is not allowed")
    for term in FORBIDDEN:
        if term in text:
            errors.append(f"removed Compiler AX reference returned: {term!r}")
    for term in COMMON:
        if term not in text:
            errors.append(f"missing architecture term {term!r}")
    return errors


def main() -> int:
    errors = []
    for path, headings in zip(PAGES, (KO, EN)):
        text = path.read_text(encoding="utf-8")
        errors.extend(f"{path.name}: {error}" for error in validate_architecture(text))
        for heading in headings:
            if heading not in text:
                errors.append(f"{path.name}: missing section {heading!r}")
    if errors:
        print("Architecture profile checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Architecture profile checks passed: evolution, runtime, evidence, and decision outcomes are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
