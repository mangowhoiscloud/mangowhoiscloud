#!/bin/bash
# Hook: Stop — progress.md 갱신 리마인드
# 오늘 커밋이 있는데 docs/progress.md에 오늘 날짜가 없으면 리마인드.

set -euo pipefail

TODAY=$(date +%Y-%m-%d)
PROGRESS_FILE="docs/progress.md"

COMMITS_TODAY=$(git log --since="$TODAY 00:00:00" --oneline 2>/dev/null | wc -l | tr -d ' ')

if [ "$COMMITS_TODAY" -eq 0 ]; then
  echo '{"continue": true}'
  exit 0
fi

if [ -f "$PROGRESS_FILE" ] && grep -q "## $TODAY" "$PROGRESS_FILE"; then
  echo '{"continue": true}'
  exit 0
fi

cat <<EOF
{
  "continue": true,
  "message": "[progress] 오늘 ${COMMITS_TODAY}건 커밋이 있지만 docs/progress.md에 ${TODAY} 섹션이 없습니다. 세션 종료 전 갱신해주세요."
}
EOF
