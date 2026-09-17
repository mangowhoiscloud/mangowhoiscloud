"""Keep live project metadata first, followed by evidence and current domains."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualSignalOrderTests(unittest.TestCase):
    def test_order(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            positions = [
                text.index("github/v/release/mangowhoiscloud/geode"),
                text.index("badge/Evidence-open%20records"),
                text.index("badge/RSI-scaffold%20search"),
                text.index("badge/Autonomous%20Agents-runtime"),
                text.index("badge/Cloud-Kubernetes%20%7C%20IaC"),
            ]
            self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
