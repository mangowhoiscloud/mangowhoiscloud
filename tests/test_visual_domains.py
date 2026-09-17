"""Keep requested RSI, autonomous-agent, and cloud signals represented visually."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualDomainTests(unittest.TestCase):
    def test_requested_domains(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            badge_block = text[text.index("<p>\n  <a href=\"https://github.com/mangowhoiscloud/geode/releases/latest\""):]
            badge_block = badge_block[:badge_block.index("</p>")]
            for signal in ("RSI", "Autonomous%20Agents", "Cloud"):
                self.assertIn(signal, badge_block)


if __name__ == "__main__":
    unittest.main()
