from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class MetricPolicyDocTests(unittest.TestCase):
    def test_metric_policy(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("If a new metric is added later", text)
        self.assertIn("stable and inspectable source", text)
        self.assertIn("unit and scope", text)

if __name__ == "__main__":
    unittest.main()
