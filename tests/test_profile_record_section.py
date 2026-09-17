"""Keep the closing notes aligned with reusable execution records."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RecordSectionTests(unittest.TestCase):
    def test_records(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("이후 작업에서 다시 사용할 수 있는 형태", ko)
        self.assertIn("reused in later work", en)


if __name__ == "__main__":
    unittest.main()
