"""Keep top badges as domain navigation, while project detail remains in prose."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectBadgeSeparationTests(unittest.TestCase):
    def test_compiler_ax_only_below_selected_work(self):
        for filename, marker in (("README.md", "## 대표 작업"), ("README_EN.md", "## Selected work")):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("Compiler AX", text[:text.index(marker)])
            self.assertIn("Compiler AX", text[text.index(marker):])


if __name__ == "__main__":
    unittest.main()
