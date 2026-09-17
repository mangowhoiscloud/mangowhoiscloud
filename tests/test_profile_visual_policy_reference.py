"""Keep the visualization policy committed as documentation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualPolicyReferenceTests(unittest.TestCase):
    def test_policy_heading(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Profile visualization choices\n"))


if __name__ == "__main__":
    unittest.main()
