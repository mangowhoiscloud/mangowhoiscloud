"""Reject common vanity metric services from the profile README."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MetricPolicyTests(unittest.TestCase):
    def test_no_vanity_widgets(self):
        forbidden = (
            "github-readme-stats",
            "github-readme-streak-stats",
            "komarev.com/ghpvc",
            "profile-counter.glitch.me",
            "github-profile-trophy",
            "github-readme-activity-graph",
        )
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for service in forbidden:
                self.assertNotIn(service, text, f"{filename}: {service}")


if __name__ == "__main__":
    unittest.main()
