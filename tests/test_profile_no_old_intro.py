from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class OldIntroTests(unittest.TestCase):
    def test_old_intro_absent(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertNotIn("안녕하세요, 류지환입니다", ko)
        self.assertNotIn("Hi, I'm Jihwan Ryu", en)

if __name__ == "__main__":
    unittest.main()
