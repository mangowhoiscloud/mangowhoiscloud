"""Keep static badge labels oriented around work domains and evidence."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeSemanticTests(unittest.TestCase):
    def test_expected_static_badges(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            expected = (
                "Evidence-open%20records",
                "RSI-scaffold%20search",
                "Autonomous%20Agents-runtime",
                "Cloud-Kubernetes%20%7C%20IaC",
            )
            for label in expected:
                self.assertIn(f"badge/{label}", text)


if __name__ == "__main__":
    unittest.main()
