"""Ensure the autonomous-agent signal routes to the runtime repository."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AgentBadgeDestinationTests(unittest.TestCase):
    def test_agent_badge_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            expected = '<a href="https://github.com/mangowhoiscloud/geode"><img src="https://img.shields.io/badge/Autonomous%20Agents-runtime-555555?style=flat-square"'
            self.assertIn(expected, text)


if __name__ == "__main__":
    unittest.main()
