"""Keep current research focus explicit in the opening paragraphs."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CurrentFocusTests(unittest.TestCase):
    def test_focus(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")[:1200]
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")[:1200]
        self.assertIn("자율 에이전트 런타임", ko)
        self.assertIn("RSI (Recursive Self-Improvement)", ko)
        self.assertIn("autonomous agent runtimes", en)
        self.assertIn("RSI (Recursive Self-Improvement)", en)


if __name__ == "__main__":
    unittest.main()
