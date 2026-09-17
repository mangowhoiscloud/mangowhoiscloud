"""Keep the domain labels readable and stable."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualSignalLabelTests(unittest.TestCase):
    def test_labels(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for label in ("RSI-scaffold%20search", "Autonomous%20Agents-runtime", "Cloud-Kubernetes%20%7C%20IaC"):
                self.assertIn(label, text)


if __name__ == "__main__":
    unittest.main()
