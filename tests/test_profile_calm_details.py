from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CalmDetailsTests(unittest.TestCase):
    def test_no_question_details(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for line in text.splitlines():
                if "<summary>" in line:
                    self.assertNotIn("?", line)

if __name__ == "__main__":
    unittest.main()
