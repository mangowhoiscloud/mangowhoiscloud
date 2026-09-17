"""Keep autonomous agent work explicit and connected to GEODE."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AutonomousAgentSignalTests(unittest.TestCase):
    def test_geode_runtime(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("자율 에이전트 런타임", ko)
        self.assertIn("autonomous agent runtime", en.lower())
        for text in (ko, en):
            self.assertIn("https://github.com/mangowhoiscloud/geode", text)


if __name__ == "__main__":
    unittest.main()
