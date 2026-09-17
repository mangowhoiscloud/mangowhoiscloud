from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SearchSpaceDefinitionTests(unittest.TestCase):
    def test_definition(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("변경 후보가 될 수 있는 모든 선택의 집합", ko)
        self.assertIn("set of choices that may become change candidates", en)

if __name__ == "__main__":
    unittest.main()
