from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeTextTests(unittest.TestCase):
    def test_concise_labels(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for label in ("Evidence-open%20records", "RSI-scaffold%20search", "Autonomous%20Agents-runtime", "Cloud-Kubernetes%20%7C%20IaC"):
                self.assertIn(label, text)

if __name__ == "__main__":
    unittest.main()
