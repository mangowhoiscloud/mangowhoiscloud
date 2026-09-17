"""Ensure the RSI signal routes to the public experiment surface."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RsiBadgeDestinationTests(unittest.TestCase):
    def test_rsi_badge_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            expected = '<a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/RSI-scaffold%20search-555555?style=flat-square"'
            self.assertIn(expected, text)


if __name__ == "__main__":
    unittest.main()
