"""Check that visualization policy stays aligned with profile signals."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualizationDocTests(unittest.TestCase):
    def test_visualization_doc_records_selected_domains(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        for term in ("RSI", "Autonomous Agents", "Cloud", "Shields.io"):
            self.assertIn(term, text)

    def test_visualization_doc_excludes_compiler_ax_badge(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        self.assertIn("no top badge", text)


if __name__ == "__main__":
    unittest.main()
