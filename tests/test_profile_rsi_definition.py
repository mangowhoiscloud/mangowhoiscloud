from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RsiDefinitionTests(unittest.TestCase):
    def test_definition(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("이전 실행에서 얻은 결과를 이후 변경과 실험의 입력으로 되돌리는", ko)
        self.assertIn("feeding evidence from earlier executions back into later changes and experiments", en)

if __name__ == "__main__":
    unittest.main()
