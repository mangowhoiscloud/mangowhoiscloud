from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TaskLoopTests(unittest.TestCase):
    def test_task_loop(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("작업 루프: 목표 → 도구 실행 → 결과 확인 → 다음 행동", ko)
        self.assertIn("task loop:    goal → tool execution → inspect result → next action", en)

if __name__ == "__main__":
    unittest.main()
