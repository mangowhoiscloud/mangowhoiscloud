from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualNotClaimTests(unittest.TestCase):
    def test_policy(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("badges as navigation", text)
        self.assertIn("without inventing an autonomy score", text)
        self.assertIn("distinguish the work from model weight training", text)

if __name__ == "__main__":
    unittest.main()
