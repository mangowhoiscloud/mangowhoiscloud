from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class OldProjectTitleTests(unittest.TestCase):
    def test_old_titles_absent(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for term in ("도구를 쓰고, 결과를 남기는 에이전트", "AI의 수정안을 리뷰 가능한 변경으로", "챗봇에서 서비스 운영까지"):
            self.assertNotIn(term, ko)
        for term in ("An agent that uses tools and leaves a record", "From an AI draft to a reviewable change", "From a chatbot to an operated service"):
            self.assertNotIn(term, en)

if __name__ == "__main__":
    unittest.main()
