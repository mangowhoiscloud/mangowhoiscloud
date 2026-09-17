"""Keep deployment as part of the verification chain."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WorkflowTermTests(unittest.TestCase):
    def test_korean_chain(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for term in ("코드 수정", "CI", "병합", "설치", "배포"):
            self.assertIn(term, text)

    def test_english_chain(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for term in ("Code changes", "CI", "merge", "installation", "deployment"):
            self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
