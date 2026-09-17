"""Keep the concrete, scoped engineering results in both profile languages."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectMetricTests(unittest.TestCase):
    def test_metrics_preserved(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for value in ("46,080", "720", "55", "5,523", "83/83", "1,000", "97.8%", "2,500", "1,477"):
                self.assertIn(value, text, f"{filename}: {value}")


if __name__ == "__main__":
    unittest.main()
