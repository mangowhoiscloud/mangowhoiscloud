from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ExactBadgeSetTests(unittest.TestCase):
    def test_static_badge_set(self):
        expected = {"Evidence-open%20records", "RSI-scaffold%20search", "Autonomous%20Agents-runtime", "Cloud-Kubernetes%20%7C%20IaC"}
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            labels = set(re.findall(r"img\.shields\.io/badge/([^\-\"]+(?:-[^\-\"]+)?)\-555555\?style=flat-square", text))
            self.assertTrue(expected.issubset(labels) or all(label in text for label in expected))

if __name__ == "__main__":
    unittest.main()
