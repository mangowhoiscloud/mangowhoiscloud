from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ResearchDomainBadgeTests(unittest.TestCase):
    def test_domain_order(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertLess(text.index("RSI-scaffold%20search"), text.index("Autonomous%20Agents-runtime"))
            self.assertLess(text.index("Autonomous%20Agents-runtime"), text.index("Cloud-Kubernetes%20%7C%20IaC"))

if __name__ == "__main__":
    unittest.main()
