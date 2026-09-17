from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CalmNavTests(unittest.TestCase):
    def test_nav_no_emoji(self):
        for filename, marker in (("README.md", "[작업 방식]"), ("README_EN.md", "[How I work]")):
            text = (ROOT / filename).read_text(encoding="utf-8")
            line = next(line for line in text.splitlines() if line.startswith(marker))
            self.assertNotRegex(line, r"[👋🪨🔬🛠️🌱]")

if __name__ == "__main__":
    unittest.main()
