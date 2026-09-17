"""Keep meaningful alt text for each top domain badge."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeAccessibilityTests(unittest.TestCase):
    def test_korean_alt(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for alt in ("GEODE 최신 릴리스", "공개 평가 기록", "RSI 실행 구성 탐색", "자율 에이전트 런타임", "Kubernetes와 IaC 클라우드 엔지니어링"):
            self.assertIn(f'alt="{alt}"', text)

    def test_english_alt(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for alt in ("Latest GEODE release", "Public evaluation records", "RSI scaffold search", "Autonomous agent runtime", "Kubernetes and IaC cloud engineering"):
            self.assertIn(f'alt="{alt}"', text)


if __name__ == "__main__":
    unittest.main()
