from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RecordsNotArchiveOnlyTests(unittest.TestCase):
    def test_records_feed_design(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("단순 보관물이 아니라", ko)
        self.assertIn("not only archives", en)

if __name__ == "__main__":
    unittest.main()
