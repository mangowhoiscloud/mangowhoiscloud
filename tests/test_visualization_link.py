"""Ensure visualization policy exists alongside the profile."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualizationPolicyTests(unittest.TestCase):
    def test_policy_exists(self):
        self.assertTrue((ROOT / "docs/VISUALIZATION.md").is_file())


if __name__ == "__main__":
    unittest.main()
