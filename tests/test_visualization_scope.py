"""Keep visualization choices tied to inspectable signals."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualizationScopeTests(unittest.TestCase):
    def test_policy_mentions_inspectable_source(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("stable and inspectable source", text)
        self.assertIn("unit and scope", text)
        self.assertIn("Contribution streaks", text)


if __name__ == "__main__":
    unittest.main()
