"""Keep categorical visual signals on a transparent, common badge service."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class StaticBadgeSourceTests(unittest.TestCase):
    def test_static_badges_use_shields(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for label in ("Evidence-open%20records", "RSI-scaffold%20search", "Autonomous%20Agents-runtime", "Cloud-Kubernetes%20%7C%20IaC"):
                self.assertIn(f"https://img.shields.io/badge/{label}", text)


if __name__ == "__main__":
    unittest.main()
