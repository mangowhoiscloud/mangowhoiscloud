from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CompilerBadgeAbsenceTests(unittest.TestCase):
    def test_compiler_badge_absent(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("badge/Compiler", text)
            self.assertNotIn("CPU%20tests", text)

if __name__ == "__main__":
    unittest.main()
