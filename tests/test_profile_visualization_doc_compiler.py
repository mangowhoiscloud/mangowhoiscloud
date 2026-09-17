"""Record the explicit choice to keep Compiler AX out of the badge row."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CompilerBadgeDecisionTests(unittest.TestCase):
    def test_decision_recorded(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("Compiler AX Lab remains a selected project", text)
        self.assertIn("deliberately has no top badge", text)


if __name__ == "__main__":
    unittest.main()
