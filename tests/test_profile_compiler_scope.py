from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CompilerScopeTests(unittest.TestCase):
    def test_compiler_scope(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("FuriosaAI 소속 또는 승인 프로젝트는 아닙니다", ko)
        self.assertIn("unaffiliated with and not approved by FuriosaAI", en)
        self.assertIn("동률", ko)
        self.assertIn("tied", en)

if __name__ == "__main__":
    unittest.main()
