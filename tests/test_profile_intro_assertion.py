from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class IntroAssertionTests(unittest.TestCase):
    def test_intro_assertion(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("실행을 검증 가능한 시스템으로 만들고, 그 결과를 다음 탐색의 입력으로 돌립니다", ko)
        self.assertIn("I build verifiable systems, then feed their results back into the next search", en)

if __name__ == "__main__":
    unittest.main()
