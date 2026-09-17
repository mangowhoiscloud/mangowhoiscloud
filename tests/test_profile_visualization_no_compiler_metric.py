from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoCompilerMetricVisualTests(unittest.TestCase):
    def test_compiler_metrics_below_visuals(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            badge_end = text.index("</p>", text.index("img.shields.io/"))
            for metric in ("46,080", "720", "55"):
                self.assertNotIn(metric, text[:badge_end])
                self.assertIn(metric, text[badge_end:])

if __name__ == "__main__":
    unittest.main()
