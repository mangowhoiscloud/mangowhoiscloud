from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoCommitCountTests(unittest.TestCase):
    def test_no_commit_count(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            self.assertNotIn("total commits", text)
            self.assertNotIn("commit count", text)

if __name__ == "__main__":
    unittest.main()
