from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RsiResultFeedbackTests(unittest.TestCase):
    def test_rsi_and_feedback_nearby(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            first_rsi = text.index("RSI (Recursive Self-Improvement)")
            next_experiment = text.index("다음 실험" if filename == "README.md" else "next experiment")
            self.assertLess(abs(first_rsi - next_experiment), 1200)

if __name__ == "__main__":
    unittest.main()
