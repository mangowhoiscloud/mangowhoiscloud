from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualizationAdmissionTests(unittest.TestCase):
    def test_three_conditions(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("1. It has a stable and inspectable source.", text)
        self.assertIn("2. Its unit and scope are understandable", text)
        self.assertIn("3. It helps a reader understand RSI", text)

if __name__ == "__main__":
    unittest.main()
