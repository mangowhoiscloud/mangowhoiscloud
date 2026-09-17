"""Keep measured project results in scoped prose instead of top badges."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SelectedWorkMetricPlacementTests(unittest.TestCase):
    def test_metrics_not_in_badge_block(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            start = text.index("<p>\n  <a href=\"https://github.com/mangowhoiscloud/geode/releases/latest\"")
            end = text.index("</p>", start)
            block = text[start:end]
            for metric in ("46,080", "83/83", "97.8%", "1,477"):
                self.assertNotIn(metric, block)
                self.assertIn(metric, text[end:])


if __name__ == "__main__":
    unittest.main()
