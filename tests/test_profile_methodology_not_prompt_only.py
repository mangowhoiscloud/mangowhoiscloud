from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NotPromptOnlyTests(unittest.TestCase):
    def test_prompt_not_only_variable(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("프롬프트만 조정하는 대신", ko)
        self.assertIn("Rather than treating the prompt as the only variable", en)

if __name__ == "__main__":
    unittest.main()
