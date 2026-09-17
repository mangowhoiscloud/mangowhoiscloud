from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualizationPolicyScopeTests(unittest.TestCase):
    def test_domains_and_evidence(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        for term in ("release state", "public evaluation records", "RSI scaffold search", "autonomous agent runtime", "cloud infrastructure"):
            self.assertIn(term, text)

if __name__ == "__main__":
    unittest.main()
