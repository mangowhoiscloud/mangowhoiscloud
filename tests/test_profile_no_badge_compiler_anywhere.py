from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoCompilerShieldsTests(unittest.TestCase):
    def test_no_compiler_shields(self):
        for filename in ("README.md", "README_EN.md"):
            for line in (ROOT / filename).read_text(encoding="utf-8").splitlines():
                if "img.shields.io" in line:
                    self.assertNotIn("compiler", line.lower())
                    self.assertNotIn("cpu%20tests", line.lower())

if __name__ == "__main__":
    unittest.main()
