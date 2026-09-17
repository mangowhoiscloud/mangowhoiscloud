from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class GeodeCurrentTests(unittest.TestCase):
    def test_geode_present(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("2026.02", text)
            self.assertIn("GEODE", text)
            self.assertIn("Crucible", text)
            self.assertIn("SIL", text)

if __name__ == "__main__":
    unittest.main()
