from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class AgentBadgePublicTests(unittest.TestCase):
    def test_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn('<a href="https://github.com/mangowhoiscloud/geode"><img src="https://img.shields.io/badge/Autonomous%20Agents-', text)

if __name__ == "__main__":
    unittest.main()
