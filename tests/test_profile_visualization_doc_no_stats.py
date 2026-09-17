from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualizationNoStatsTests(unittest.TestCase):
    def test_omissions_documented(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        for term in ("Contribution streaks", "total commits", "language percentages", "visitor counters", "star totals"):
            self.assertIn(term, text)

if __name__ == "__main__":
    unittest.main()
