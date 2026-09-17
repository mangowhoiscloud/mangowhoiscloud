from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoBestMethodTests(unittest.TestCase):
    def test_no_best_method_claim(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for phrase in ("최고의 방법", "완성된 방법론", "the best method", "final methodology"):
                self.assertNotIn(phrase.lower(), text)

if __name__ == "__main__":
    unittest.main()
