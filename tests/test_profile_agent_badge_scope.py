"""Keep the autonomous-agent badge descriptive rather than scored."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AgentBadgeScopeTests(unittest.TestCase):
    def test_agent_badge_scope(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("Autonomous%20Agents-runtime", text)
            self.assertNotIn("Autonomous%20Agents-expert", text)
            self.assertNotIn("Autonomy-100", text)


if __name__ == "__main__":
    unittest.main()
