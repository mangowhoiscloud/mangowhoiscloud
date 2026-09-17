"""Ensure the cloud signal routes to the current technical portfolio."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CloudBadgeDestinationTests(unittest.TestCase):
    def test_cloud_badge_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            expected = '<a href="https://mangowhoiscloud.github.io/eco2/"><img src="https://img.shields.io/badge/Cloud-Kubernetes%20%7C%20IaC-555555?style=flat-square"'
            self.assertIn(expected, text)


if __name__ == "__main__":
    unittest.main()
