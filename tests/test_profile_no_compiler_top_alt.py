from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoCompilerTopAltTests(unittest.TestCase):
    def test_no_compiler_alt_in_top(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            nav = text.index("[작업 방식]" if filename == "README.md" else "[How I work]")
            self.assertNotIn("Compiler AX", text[:nav])

if __name__ == "__main__":
    unittest.main()
