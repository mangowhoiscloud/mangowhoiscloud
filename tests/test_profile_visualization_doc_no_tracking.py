from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoTrackingPolicyTests(unittest.TestCase):
    def test_no_tracking(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("tracking pixels", text)
        self.assertIn("visitor counters", text)

if __name__ == "__main__":
    unittest.main()
