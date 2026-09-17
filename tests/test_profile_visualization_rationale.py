from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualizationRationaleTests(unittest.TestCase):
    def test_rationale(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("navigation rather than a decorative developer dashboard", text)
        self.assertIn("weak proxies", text)

if __name__ == "__main__":
    unittest.main()
