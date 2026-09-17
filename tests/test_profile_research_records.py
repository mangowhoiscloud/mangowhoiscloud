"""Keep both experiment and evidence surfaces reachable from GEODE."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResearchRecordTests(unittest.TestCase):
    def test_records(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("https://mangowhoiscloud.github.io/geode/self-improving/", text)
            self.assertIn("https://github.com/mangowhoiscloud/geode-eval-artifacts", text)


if __name__ == "__main__":
    unittest.main()
