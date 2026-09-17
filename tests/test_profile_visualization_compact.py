from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualizationCompactTests(unittest.TestCase):
    def test_badges_on_five_lines(self):
        for filename in ("README.md", "README_EN.md"):
            lines = (ROOT / filename).read_text(encoding="utf-8").splitlines()
            self.assertEqual(sum("img.shields.io/" in line for line in lines), 5)

if __name__ == "__main__":
    unittest.main()
