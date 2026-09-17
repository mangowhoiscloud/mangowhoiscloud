"""Keep Skills framed as reusable instructions that still require evaluation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillReuseTests(unittest.TestCase):
    def test_skill_boundary(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("실제 작업에서 사용한 뒤 다시 평가", ko)
        self.assertIn("used and evaluated on subsequent work", en)


if __name__ == "__main__":
    unittest.main()
