from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class OldBadgeAltTests(unittest.TestCase):
    def test_old_alt_absent(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertNotIn("Compiler AX Lab의 범위가 명시된 CPU 검증 기록", ko)
        self.assertNotIn("Compiler AX Lab CPU verification records with explicit scope", en)

if __name__ == "__main__":
    unittest.main()
