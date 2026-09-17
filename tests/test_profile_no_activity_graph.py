from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoActivityGraphTests(unittest.TestCase):
    def test_no_activity_graph(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertNotIn("activity-graph", (ROOT / filename).read_text(encoding="utf-8").lower())

if __name__ == "__main__":
    unittest.main()
