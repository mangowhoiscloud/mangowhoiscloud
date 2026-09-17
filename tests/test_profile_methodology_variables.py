"""Keep multiple methodology variables visible rather than prompt-only framing."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MethodologyVariableTests(unittest.TestCase):
    def test_variable_count(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for term in ("문제 분해", "컨텍스트", "도구 선택", "검증 순서", "Skill", "에이전트 역할", "사람의 개입"):
            self.assertIn(term, ko)
        for term in ("Task decomposition", "context", "tool selection", "verification order", "Skills", "agent roles", "human intervention"):
            self.assertIn(term.lower(), en.lower())


if __name__ == "__main__":
    unittest.main()
