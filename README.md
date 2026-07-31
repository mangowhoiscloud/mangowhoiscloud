<p align="right">
  <strong>🇰🇷 한국어</strong> · <a href="README_EN.md">🇺🇸 English</a>
</p>

<h1 align="center">류지환</h1>

<p align="center">
  <strong>행동도, 검증도, 개선도 루프로 만듭니다.</strong><br/>
  통제 없는 LLM은 발산합니다. 하네스가 루프를 닫아 수렴시킵니다.
</p>

<p align="center">
  <a href="https://github.com/mangowhoiscloud?tab=followers"><img src="https://img.shields.io/github/followers/mangowhoiscloud?label=Follow&style=social" alt="Follow"></a>&nbsp;
  <a href="https://www.youtube.com/@mango_fr"><img src="https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube"></a>
  <a href="https://rooftopsnow.tistory.com"><img src="https://img.shields.io/badge/Blog-FF5722?style=flat-square&logo=tistory&logoColor=white" alt="Blog"></a>
  <a href="https://linkedin.com/in/jihwan-ryu-b6b04a202"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/Self--Improving_Hub-6B4FBB?style=flat-square&logo=githubpages&logoColor=white" alt="Self-Improving Hub"></a>
</p>

<p align="center">
  이전 GitHub 계정: <a href="https://github.com/mng990"><strong>@mng990</strong></a>
</p>

---

### 모든 층위의 루프

에이전트의 한 턴부터 배포, 자기개선까지 모든 층위를 같은 루프 구조로 다룹니다.
바깥 루프는 안쪽 루프의 결과를 측정하고, 측정값이 다음 루프의 입력이 됩니다.

```
┌─ ⑤ 피드백 루프       시장·사용자·채용 과제 → 다음 빌드의 입력
│  ┌─ ④ 자기개선 루프   행동 정량화 → 변이 제안 → 측정 게이트 → 채택/기각
│  │  ┌─ ③ 제품화 루프  계획 → 구현 → CI 래칫 → 배포 → 공유
│  │  │  ┌─ ② 검증 루프 생성 → 검증 → 반성 → 재계획
│  │  │  │  ┌─ ① 에이전트 루프   while(tool_use): 추론 → 행동 → 관찰
```

### 작업 방식

- **에이전트를 컴퓨팅 위의 탐색 프로세스로 두고, 시스템으로 감쌉니다**: 도구를 부르는 손, 호출을 스케줄링하는 큐, 컨텍스트를 계층화하는 메모리, 위험한 호출 앞에 서는 권한 게이트
- **검증은 에이전트 바깥의 결정론 코드에 둡니다**: 자기 보고는 불신, 생성·평가는 다른 모델 제공자로 분리, 개선 곡선보다 노이즈 밴드·대조군이 먼저
- **평가 층을 먼저 깔고 자율성을 엽니다**: 도구 호출 하나에 평가 층 하나, 코드 마이그레이션은 결정론 70%를 먼저 긋고 LLM을 모호한 30%에만

### 하네스 엔지니어링

| 축 | 역할 | 실천 |
|---|---|---|
| **오케스트레이션** | LLM 출력을 받아 다음 행동을 결정 | AgenticLoop `while(tool_use)`, 하위 목표 그래프, 하위 에이전트 병렬 위임, 레인 큐 |
| **컨텍스트와 메모리** | 장기 세션의 컨텍스트를 계층·압축·복구 | 5계층 메모리, 2단계 압축, 200K 절대 한계: 장기 세션 오버플로우 0회, 프롬프트 캐시 정렬로 멀티턴 입력 토큰 약 80% 절감 |
| **게이트웨이** | 여러 모델 제공자를 단일 통제점으로 | Anthropic·OpenAI·Zhipu 단일 인터페이스, 4단계 장애 전환, 회로 차단기, 모델 제공자 간 분기, 토큰 단위 비용 추적 |
| **검증** | 비결정론적 출력을 신뢰 수준으로 수렴 | 결정론 게이트 + LLM 심판 + 드리프트 감지의 직교 다층, 여러 LLM 합의도 기준 |
| **관측과 개선** | 작동을 계측하고 개선을 측정으로 채택 | 훅 이벤트 버스, 실행별 기록, Petri 행동 감사 + 측정 게이트 |

#### 하네스 지형도 · 4분면 배치

```
                          자율형
                              ▲
                              │
           Q2                 │                Q1
      경량+자율형             │          종합+자율형
                              │
      · SWE-agent             │         ★ GEODE (+ 자기개선)
      · Codex CLI       · Claude Code   · REODE (납품 완료)
      · AutoGen          (← 생산 도구)   · Devin · Manus
                              │         · OpenHands
                              │
  ◄───────────────────────────┼───────────────────────────────►
      경량형                  │             종합형
                              │
           Q3                 │                Q4
      경량+보조형             │          종합+보조형
                              │
      · Aider                 │         · Cursor · Copilot
      · Gemini CLI            │         · Eco² (채팅 하네스)
      · CrewAI                │         · Kiki (Slack 거버넌스)
                              │
                              ▼
                            보조형
```

---

### 주요 프로젝트

**GEODE** · 에이전트 루프 기반 자율 에이전트 하네스 · [저장소](https://github.com/mangowhoiscloud/geode) · [문서](https://mangowhoiscloud.github.io/geode/docs) · [포트폴리오](https://mangowhoiscloud.github.io/geode/)
탐색·리서치·시그널 수집에 특화한 장기 실행 시스템. 멀티 프로바이더 게이트웨이, 5-Tier 메모리,
4계층 도구 디스패치, HITL 권한 게이트를 SDK 런타임부터 단독 구축. 일상 업무를 자율 수행 중.

**GEODE 자기개선 루프** · 측정 게이트 기반 자기개선 폐회로 · [허브](https://mangowhoiscloud.github.io/geode/self-improving/) · [감사 로그 원본](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [영상](https://www.youtube.com/watch?v=TuEOGQrO9Us)
적대 시나리오 생성(co-scientist 토폴로지) → Petri 다차원 행동 감사 → 무변이 대조군의 노이즈 밴드를 넘는 변이만 채택.
첫 측정이 조용한 결함(미발생 변이·운 좋은 기준선)을 드러냈고 결함은 공개·정정. Petri 감사 로그 408건 전량을 원본으로 공개.

**Crucible** · τ²-bench 기반 능력 축 게이트 루프 · [설계](https://github.com/mangowhoiscloud/geode/blob/main/plugins/crucible/program.md) · [실측 로그](https://github.com/mangowhoiscloud/geode-eval-artifacts)
Petri 안전성 루프의 승격 규율(챔피언 체인·짝지은 판정·고정 판정자)을 능력 평가로 옮기고, 싼 대리 게이트로 후보를 압축해 비싼 tau2 실행은 최종 판정에만 사용.
변이 시도 35건 중 core 승격 0건, 기각 사유는 전건 기계 기록. 거짓 승격을 막는 게이트 검증이 첫 사이클의 산출물.

**REODE** · 코드 마이그레이션 자율 에이전트 @ pinxlab (프리랜스 납품)
GEODE 하네스를 코딩 에이전트 제품으로 재설계해 라이브 서비스의 Java 8→22, Spring Boot 2→3 마이그레이션을 납품.
OpenRewrite 결정론 70% + LLM 30% 분리, 검증을 우회하는 기망 행위를 5-Gate Scorecard로 차단,
동일 에러 40회 고착 장애를 explore_before_fix 의무화로 해소.

| 실서비스 납품 결과 (2026.03) | |
|------|------|
| 대상 | 5,523개 파일 (Java 241개 + JSP 355개 + XML 47개), Java 1.8→22 · Spring 4→6 |
| 결과 | 83/83 테스트 + 프론트엔드/백엔드 종단 검증 통과 |
| 실행 | 33 자율 세션 · 1,133 에이전트 라운드 · 5h 48m (사람 개입 0) |

**Eco²** · AI 멀티에이전트 재활용 서비스 · [포트폴리오](https://mangowhoiscloud.github.io/portfolio/eco2) · 2025 AI 새싹톤 우수상 (4th/181)
EC2 14노드에서 시작해 Terraform·Ansible IaC와 ArgoCD 선언형으로 24-Node K8s를 단독 운영.
temperature 0.1 strict 챗봇을 툴콜링·LangGraph 병렬·SSE·Agent SDK로 상용 멀티에이전트로 고도화.
동시접속 0→1,000 VU 97.8%, 평가 품질 69.4→99.8/100(Swiss Cheese 3-Layer), 인증 핸들러 48→1,500 RPS.

**Kiki** · Slack 행동 관측 기반 멀티 에이전트 거버넌스 @ pinxlab
CTO·PO·Lead·Dev·QA 계층 self-team이 실 운영 레거시를 자율 분석·구현·리뷰. 관리자는 Slack 대화만으로 지시·승인.
"보수적 PASS"를 2-stage gate가 시스템 차원에서 차단.

**Cotton** · RPG 게임 스크립트 번역 단일 입주형 SaaS @ pinxlab
기존 번역 도구(Crowdin·Lokalise)는 게임 대화를 키-값 문자열로 취급. 분기·조건·캐릭터 voice·자막 길이 예산을 지닌 대화 그래프를 데이터 모델 1급 시민으로 모델링.
LLM CLI 어댑터(Codex·Claude Code)와 모델 제공자 간 심판으로 번역 품질 수렴.

**Crumb & Crumb Studio** · 멀티 호스트 에이전트 게임 제작 스튜디오 · [저장소](https://github.com/mangowhoiscloud/crumb)
Claude Code·Codex·Gemini CLI를 공통 인터페이스로 추상화한 3일 실험. transcript.jsonl 단일 진실원 + 순수 리듀서로
재생 결정성 확보, 동일 모델 제공자 평가 인플레이션을 교차 제공자 배치로 차단.

---

### 연표

```
mangowhoiscloud/
├── 2017.03-2023.08/  부산대학교 정보컴퓨터공학부 · 학사
├── 2024.07-2024.11/  카카오테크 부트캠프 · 백엔드 · 데브옵스 · LLM
├── 2024.09/          DREAM · 카카오테크 해커톤 · 생성형 AI 꿈 서사·이미지 · 백엔드·AI
├── 2024.12-2025.08/  Rakuten Symphony Korea · 클라우드 엔지니어 (페타바이트 분산 스토리지, 글로벌 팀)
├── 2025.10-2026.02/  Eco² · 5인 MVP 백엔드/인프라 → 전 과정 단독 (24노드 K8s, 2025 AI 새싹톤 우수상)
├── 2026.02-present/  GEODE · 자율 에이전트 하네스 (단독)
├── 2026.03-2026.05/  REODE · Kiki · Cotton @ pinxlab · 프리랜스 납품
├── 2026.05-2026.06/  GEODE 자기개선 루프 · 측정 게이트 자기개선
└── 2026.07-present/  Crucible · tau2-bench 능력 축 게이트 루프
```

---

### 프로젝트 링크

| 기간 | 프로젝트 | 역할 | 링크 |
|------|---------|------|------|
| 2026.07 | **GEODE - Crucible:** τ²-bench 능력 축 게이트 루프 | 단독 | [설계/제작/운용](https://github.com/mangowhoiscloud/geode/blob/main/plugins/crucible/program.md) · [실측 로그](https://github.com/mangowhoiscloud/geode-eval-artifacts) |
| 2026.05-2026.06 | **GEODE - SIL:** Petri 감사 × 측정 게이트 | 단독 | [허브](https://mangowhoiscloud.github.io/geode/self-improving/) · [감사 로그](https://github.com/mangowhoiscloud/geode-eval-artifacts) |
| 2026.04-2026.05 | **Kiki**: Slack 행동 관측 기반 에이전트 조직 오케스트레이션 | 프리랜스 | pinxlab |
| 2026.03-2026.04 | **REODE**: GEODE에서 파생한 마이그레이션·코딩 에이전트 | 프리랜스 | pinxlab |
| 2026.02-present | **GEODE**: 자율 에이전트 하네스 | 단독 | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) · [문서](https://mangowhoiscloud.github.io/geode/docs) |
| 2025.10-2026.02 | **Eco²**: AI 멀티에이전트, 24노드 K8s, 2025 AI 새싹톤 우수상 | 백엔드/인프라 → 전 과정 | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2024.12-2025.08 | **Rakuten Cloud Native Platform - Storage Server v5.5.0 · Rakuten Storage v1.0.0**: 분산 스토리지 서버 개발 | Jr. Cloud Engineer [C, K8s] | Rakuten Symphony(정규직, 퇴사) |
| 2024.09 | **DREAM**: 노년층의 못 이룬 꿈을 생성형 AI(LLM·RAG·Diffusion)로 서사·이미지화하는 해커톤 서비스 | 인프라 | [KakaoTech-Hackathon-Dream](https://github.com/KakaoTech-Hackathon-Dream) |
| 2024 | **Aimo**: LLM 갈등 중재 앱 | 백엔드 | [KTB16Team](https://github.com/KTB16Team) |
