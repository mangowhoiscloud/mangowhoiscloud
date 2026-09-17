from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualizationToolDocTests(unittest.TestCase):
    def test_tools_documented(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("Shields.io", text)
        self.assertIn("GitHub Actions", text)
        self.assertIn("No third party contribution analytics", text)

if __name__ == "__main__":
    unittest.main()
