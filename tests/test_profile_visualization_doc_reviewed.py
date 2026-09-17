from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualizationReviewDateTests(unittest.TestCase):
    def test_review_date(self):
        self.assertIn("Reviewed: 2026-09-17", (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
