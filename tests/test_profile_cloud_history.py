"""Keep cloud experience represented by both Eco2 and Rakuten history."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CloudHistoryTests(unittest.TestCase):
    def test_cloud_history(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("Eco²", text)
            self.assertIn("Rakuten Symphony Korea", text)
            self.assertIn("Kubernetes", text)


if __name__ == "__main__":
    unittest.main()
