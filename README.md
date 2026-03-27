<h1 align="center">류지환 (Jihwan Ryu)</h1>

<p align="center">
  <strong>모델 능력이 상수일 때, 변수는 오케스트레이션의 구조입니다.</strong><br/>
  확률적 시스템은 제어 없이 발산합니다. 저는 그 발산을 구조로 수렴시키는 하네스를 만듭니다.
</p>

<p align="center">
  <a href="https://www.youtube.com/@mango_fr">
    <img src="https://img.shields.io/badge/YouTube-@mango__fr-FF0000?style=flat-square&logo=youtube&logoColor=white" />
  </a>
  <a href="https://rooftopsnow.tistory.com">
    <img src="https://img.shields.io/badge/Blog-rooftopsnow-FF5722?style=flat-square&logo=tistory&logoColor=white" />
  </a>
  <a href="https://linkedin.com/in/jihwan-ryu-b6b04a202">
    <img src="https://img.shields.io/badge/LinkedIn-Jihwan_Ryu-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/mng990">
    <img src="https://img.shields.io/badge/prev-mng990-181717?style=flat-square&logo=github&logoColor=white" />
  </a>
</p>

---

### Harness Engineering

LLM은 확률적 시스템입니다. 제어 평면(control plane) 없이 장시간 자율 실행하면 발산합니다.
하네스는 이 발산을 구조로 수렴시키는 다섯 가지 축입니다.

| 축 | 역할 | 실천 사례 |
|---|---|---|
| **컨텍스트 제어** | 입력의 정밀도가 출력의 상한을 결정 | GEODE/REODE 5-Layer Context Hub(C0-C4, 글로벌과 로컬 .geode/.reode), Runtime PromptAssembler 6-Phase, Model Switching Context Compression, SHA-256 pinning |
| **Plan and Execute** | LLM 출력을 받아 다음 행동을 결정하는 오케스트레이션 | AgenticLoop `while(tool_use)`, Hook System(Event Bus), LaneQueue, TaskGraph, bash->tool->skill->MCP Registry, Sub-Agent(MAX_CONCURRENT=5, DAG) |
| **Verify** | 비결정론적 출력을 신뢰 가능한 수준으로 수렴 | Eco² Swiss Cheese 3-Layer(69.4 → 99.8%), GEODE 5-Layer Verification + Cross-LLM |
| **Observe** | 위 네 가지가 실제로 작동하는지 계측 | 36-Event Hook Observer, LangSmith or 자체 Token, Transcript Tracing, CUSUM Drift Detection |
| **Scaffold** | Assistance/Autonomous 에이전트 하네스를 설계·제작하고 도메인 간 이식하는 메타 레이어 | Claude Code(.claude/ Skills·Hooks·CLAUDE.md)와 스캐폴딩으로 GEODE를 생산, harness-for-real, GEODE→REODE 2-Protocol 재설계로 클라이언트 확보 |

다섯 축을 관통하는 원칙: 프론티어 모델(Claude, GPT)뿐 아니라 GLM 등 다양한 모델을 직접 운영하며 각 모델의 강점과 한계를 파악하고, 어떤 프로바이더에 장애가 발생하더라도 서비스가 지속되는 Resilience를 설계합니다.

#### Three-Layer Harness Architecture

LLM은 매번 다른 답을 합니다. 같은 프롬프트에도 품질이 들쭉날쭉하고, 할루시네이션을 스스로 검증하지 못합니다.
이 확률적 시스템을 제어 가능한 실행 엔진으로 바꾸려면, 모델 위에 구조를 쌓아야 합니다.

```
Layer ③  Scaffold: CLAUDE.md + 25 Skills + 36 Hook ← 제약과 지식, workflow
Layer ②  Coding Agent (Platform Harness)           ← Anthropic이 제공한 실행 환경
Layer ①  Foundation LLM        ← 확률적 컴퓨팅 인프라
```

같은 LLM이라도 Layer ③의 설계에 따라 SWE-bench 점수가 11.6%p 갈립니다.
GEODE는 이 구조를 실증하는 과정에서 **Producer-Product Inversion**을 만들었습니다 — Coding Agent Harness가 GEODE(Autonomous 하네스)를 생산하는 역전 구조.
도구 선택부터 실행, 검증, 자기 개선까지 자율적으로 수행하며, 4단계 Guardrails와 Cross-LLM 교차 검증으로 출력을 수렴시킵니다.

#### Harness Landscape — 4-Quadrant Positioning

제작한 하네스들이 이 지형도 위에 어떻게 분포하는지를 나타냅니다.

```
                          Autonomous
                              ▲
                              │
           Q2                 │                Q1
      Minimal+Autonomous      │       Comprehensive+Autonomous
                              │
      · SWE-agent             │         ★ GEODE (L4 Meta)
      · Codex CLI             │         · Devin
      · AutoGen               │         · Manus
                              │         · OpenHands
                              │
  ◄───────────────────────────┼───────────────────────────────►
      Minimal                 │              Comprehensive
                              │
           Q3                 │                Q4
      Minimal+Assisted        │        Comprehensive+Assisted
                              │
      · Aider                 │         · Claude Code ← 생산 도구
      · Gemini CLI            │         · Cursor
      · CrewAI                │         · Copilot
                              │         · Kiro
                              │
                              ▼
                           Assisted
```

#### Scaffolding — 생산 하네스의 제어 지점

스캐폴딩은 에이전트를 생산하는 하네스의 구성 레이어입니다. 코드가 아니라 **제약의 설계**가 품질을 결정합니다.

| 구성 요소 | 비중 | 역할 | GEODE 실측 |
|----------|------|------|-----------|
| **Instruction (CLAUDE.md)** | Soft 78% | 행동 규칙, CANNOT/CAN 프레임워크 | 428줄, 20 CANNOT 규칙 |
| **Skills** | 지식 인코딩 | 도메인별 재사용 가능한 프롬프트 | 25개, 3,468 LoC |
| **Hooks** | Hard 16% | 이벤트 기반 자동 제어 | 36 이벤트 중 1개 활성 (확장 여지) |
| **CI/CD Gates** | Ratchet 3% | 자동 롤백 게이트 | 5 CI jobs, test ≥ 3181 |
| **Memory** | 세션 간 학습 | 패턴 축적 → 다음 세션 자동 주입 | 19 메모리 파일 |

핵심 발견: 제약의 78%가 LLM 자기 규율(soft)에 의존합니다. 이 비율이 하네스 성숙도를 결정합니다.

> 상세 분석: [Scaffolding 실측](https://rooftopsnow.tistory.com/354) · [Landscape 리포트](https://rooftopsnow.tistory.com/353)

---

### Projects

제 프로젝트들의 4사분면 포지셔닝:

| Project | Quadrant | 포지션 | 핵심 역할 |
|---------|----------|--------|----------|
| **GEODE** | Q1 (Comprehensive + Autonomous + Domain-specific Plug-in) | L4 Meta-Harness | 범용 자율 실행 — 도메인 교체 가능 |
| **REODE** | Q1(Autonomous + Domain-specific Plug-in) | L4 Meta-Harness | 코드 마이그레이션 특화 자율 에이전트 |
| **Eco²** | Q4 (Comprehensive + Assisted) | Multi-Agent Service | 사용자 주도, Chat-based 에이전트 하네스, AI 병렬 평가 및 툴콜링, 자연어 기반 의도 분류 |
| **harness-for-real** | Q2 (Minimal + Autonomous) | Hackathon Harness | 4-Phase FSM, 최소 구성 자율 실행 |
| Claude Code (생산 도구) | Q4 | Platform Harness | GEODE/REODE를 생산하는 도구 |

**Eco²** — Multi-Agent AI Service
MVP 1mon: 5인 팀에서 백엔드·인프라 단독 담당 → E2E 3mon: FE/BE/INFRA/HARNESS/LLM 전체 단독 설계·개발·운영.

- **동시접속 문제 해결**: SSE 연결 1:21 비율 폭발로 100VU 완료율 0% → EDA 기반 Event Bus로 생산/소비 분리, 동시접속 **0→1,000VU, 97.8% SLA** 달성
- **LLM 평가 품질**: 단일 평가자의 편향 한계 → Swiss Cheese 3-Layer 방어, Expert Review **69.4→99.8%**
- **Auth 병목 제거**: 모든 요청이 Auth MS를 경유하여 48 RPS 한계 → Istio ext-authz Offloading으로 **1,477 RPS (31x)**
- 2025 AI 새싹톤 우수상 **4th/181** (서울특별시, DAYCON)

**GEODE** — 범용 자율 실행 에이전트 하네스 (CLI + Slack Daemon)
`v0.28.1` · 221 modules · 3,181 tests · 47 tools + 44 MCP · 36 hooks · 25 skills

"도메인이 바뀌어도 동작하는 하네스를 만들 수 있는가?" — 게임 IP 전용 파이프라인에서 출발, 범용 하네스로 피봇. 32일간 32번 릴리스, regression 0건.

- **도메인 독립성**: DomainPort Protocol로 분석 DAG를 플러그인화 → REODE로 코드 마이그레이션 도메인에 이식, AgenticLoop 수정 0줄. 이 이식이 프리랜스 계약으로 발전
- **자율 실행**: `while(tool_use)` 루프로 47 tools + 44 MCP 중 LLM이 자율 선택. Sub-Agent 병렬 위임(MAX 5, DAG, Token Guard)으로 복합 태스크 분해
- **3사 Resilience**: Anthropic/OpenAI/GLM 3-provider failover chain + per-provider circuit breaker. 파이프라인 노드별 모델 고정(Opus 4.6)으로 REPL 모델과 분리
- **컨텍스트 제어**: 5-Layer Context Hub(C0-C4) + per-turn status line(세션 누적이 아닌 턴 단위 메트릭). 80% 임계 시 Haiku 자동 압축
- **검증 수렴**: 5-Layer Verification + Cross-LLM(Krippendorff α ≥ 0.67). 비결정론적 출력을 신뢰 가능 수준으로 수렴
- **Slack 데몬**: `geode serve` 헤드리스 — 채널별 세션 격리, Echo Prevention 3중 방어, CLI 없이 Slack에서 에이전트 운용

**REODE** — Autonomous Code Migration Agent @ pinxlab (Freelance)
"확률적 시스템이 코드를 수정할 때, 어떻게 품질을 보장하는가?" — GEODE 하네스를 재설계하여 실제 산업 현장의 레거시 Java 마이그레이션에 도입 운영 중.

- **결정적/확률적 분리**: 기계적 변환(javax→jakarta 등)은 OpenRewrite recipe(70%), 비즈니스 로직 의존 변환만 LLM(30%) — 확률적 시스템 개입 범위를 최소화
- **장애 경로 설계**: VALIDATE 실패 시 Fix Node가 에러를 분석하고 자동 재시도(max 3), 동일 에러 3회 수렴 감지 → 모델 에스컬레이션. 빌드/테스트 미통과 코드는 머지 불가(Ratchet)
- **Reward Hacking 방지**: Migration Scorecard 5 Gate — 테스트 삭제, skipTests 플래그, JDK 다운그레이드, @SuppressWarnings 삽입을 구조적으로 차단
- **하네스 재설계**: GEODE의 DomainPort(1 DI)를 삭제하고 PipelineTemplate(L1) + LanguageAdapter(L2) 2-Protocol 직교 분리. L0 인프라 수정 없이 재사용
- **Sandbox 격리**: macOS Seatbelt + 34패턴 deny-list + 3-Level Permission(deny→ask→allow)으로 에이전트의 시스템 접근 제어

**harness-for-real** — AI 에이전트 해커톤용 자율 수행 하네스
"키보드에 손이 닿는 순간 하네스의 실패다" — 랄프톤(한국 최초 AI 코딩 해커톤) 우승팀 전략을 분석하고, 재현 가능한 하네스로 구조화.

- **모호성 제거 우선**: Socratic Phase에서 코딩 전 요구사항 정제 (우승팀 133라운드). 입력의 정밀도가 출력의 상한을 결정
- **자기 검증**: 매 write마다 typecheck+lint Backpressure hooks, 테스트 비율 70%. @Disabled/@pytest.mark.skip 구조적 차단
- **장시간 안정성**: LEARNINGS.md에 에러 패턴 축적 → 다음 이터레이션 자동 주입. Token budget 80%/100% 자동 정지

---

### Loop

피드백 간격을 최소화하면 결함 수정 비용이 급감합니다 (Beck, XP).
프로젝트와 도메인이 바뀌어도 이 루프는 동일하게 반복됩니다. GEODE 32릴리스가 이 루프의 산물입니다.

```
Plan → Build → Observe → Break → Rebuild → Share → (repeat)
```

#### Implementation Loop

Ratchet 패턴 — 빌드+테스트를 통과한 변경만 커밋, 실패 시 롤백 후 재시도.<br>
Beck: "테스트 없는 코드는 레거시 코드다."

```
Code ─→ Ratchet Gate ─→ Commit ─→ PR ─→ CI Gate ─→ Merge ─→ Docs-Sync
            │                            │
      lint (ruff)                  gh pr checks --watch
      type (mypy)                        │
      test (pytest)                Fail → fix → re-push
      security (bandit)
            │
      Fail → rollback → retry
```

| Phase | Gate | Threshold |
|-------|------|-----------|
| Pre-Commit | ruff + mypy + pytest + bandit | All pass, zero tolerance |
| PR | GitHub Actions CI | `gh pr checks --watch` 전체 green |
| Post-Merge | docs-sync validation | 4곳 버전 동기화(CHANGELOG, CLAUDE.md, README, pyproject.toml) |

#### Multi-Agent Loop

병렬 서브에이전트가 독립 컨텍스트에서 평가/검수/수정을 수행하고, 결과를 부모 세션으로 수렴.

```
Parent AgenticLoop
  ├─ spawn Agent ×N  (MAX_CONCURRENT=5, DAG scheduling)
  │     ├─ ARCHITECT Agent  — 설계/평가 (Opus)
  │     ├─ ENGINEER Agent   — 구현/수정 (Sonnet)
  │     ├─ REVIEWER Agent   — 검증/린트 (Haiku)
  │     └─ SCOUT Agent      — 탐색/검색 (Haiku)
  ├─ collect results  (Token Guard, summary 필수)
  └─ threshold check
       ├─ Pass → commit
       └─ Below → fix batch → re-score (loop)
```

25개 커스텀 스킬이 도메인 지식을 재사용 가능한 프롬프트로 인코딩하여 세션마다 동일 품질을 보장합니다.

#### Cross-Project Loop

이전 프로젝트에서 검증된 패턴이 다음 프로젝트의 인프라로 전이됩니다.

| 패턴 | Eco² (origin) | GEODE (진화) | REODE (재설계) |
|------|---------------|--------------|----------------|
| **메모리** | ReadThroughCheckpointer | 3-Tier Memory + HybridSessionStore | 수정 없이 재사용 |
| **평가** | Swiss Cheese 3-Layer (69.4→99.8%) | 5-Layer Verification + Cross-LLM | Migration Scorecard 3-Tier |
| **컨텍스트** | Intent Confidence Scoring | PromptAssembler 6-Phase + Token Budget | 수정 없이 재사용 |
| **Resilience** | Provider Registry (OpenAI/Gemini) | Port/Adapter DI (20+ Ports) + 3사 Failover | Cross-Provider 에스컬레이션 |
| **루프 제어** | Celery→KEDA→Event Bus 4회 전환 | Worktree→Socratic Gate→CI Ratchet | Ratchet + Anti-Deception 7 Guard |

#### Loop in Action

| Project | Loop | Result (루프가 만든 변화) |
|---------|------|------------------------|
| **Eco²** | 완료율 0% Sync → EDA Event Bus, 계측 근거 아키텍처 4회 전환 | 동시접속 0→**1,000VU 97.8%**, 평가 품질 69.4→**99.8%**, 새싹톤 **4th/181** |
| **GEODE** | Worktree→GAP Audit→Socratic Gate→CI Ratchet→PR | 게임 IP 전용 → **범용 하네스 피봇**, REODE로 코드 마이그레이션 도메인에 피봇 → **프리랜스 계약으로 발전** |
| **REODE** | DomainPort 삭제 → 2-Protocol 재설계, Ratchet + Anti-Deception | OpenRewrite 70%로 **확률적 시스템 개입 최소화**, 5-Gate Scorecard로 **Reward Hacking 구조적 차단** |
| **harness-for-real** | 랄프톤 우승팀 전략 분석 → 4-Phase FSM 하네스화 | Backpressure hooks + LEARNINGS.md로 **장시간 자율 실행 안정성 확보** |

---

### Timeline

```
mangowhoiscloud/
├── 2017.03-2023.08/  부산대학교 정보컴퓨터공학부
│   └── Bachelor of Computer Science & Engineering
│
├── 2024.07-2024.11/  카카오테크 부트캠프
│   └── Backend · DevOps · LLM
│
├── 2024.12-2025.08/  Rakuten Symphony Korea, Cloud Engineer, Full-time
│   └── PB급 분산 스토리지 개발, 글로벌 팀 22-40명, 영어 기반
│
├── 2025.10-2026.02/  Eco² (MVP 1mon: Solo Backend/Infra, E2E 3mon: FE/BE/INFRA/HARNESS/LLM)
│   └── AI Multi-Agent, 24-Node K8s, 2025 AI 새싹톤 우수상 4th/181
│
├── 2026.01.31-present/  GEODE (Solo)
│   └── 범용 자율 실행 에이전트 하네스(CLI+Slack), 221 modules, 3,181 tests, 32 releases
│
└── 2026.03-2026.05/  REODE @ pinxlab (Freelance)
    └── DomainPort 삭제 → 2-Protocol 재설계, Migration/Porting/Coding Agent
```

---

### Project Links

| Date | Project | Role | Link |
|------|---------|------|------|
| 2026.03 | **harness-for-real**: 랄프톤 & AI 해커톤용 자율 하네스, 4-Phase FSM | Solo | [mangowhoiscloud/harness-for-real](https://github.com/mangowhoiscloud/harness-for-real) |
| 2026.03-2026.05 | **REODE**: Migration & Coding Agent @ pinxlab | Freelance | pinxlab |
| 2026.01.31-Present | **GEODE**: 범용 자율 실행 에이전트 하네스, 221 modules, 3,181 tests, v0.28.1 | Solo | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) |
| 2026.02 | **LLMART**: CLI-based LLM-as-Judge Evaluation System | Solo | [mangowhoiscloud/llmart](https://github.com/mangowhoiscloud/llmart) |
| 2025.10.31-2026.02 | **Eco²**: AI Multi-Agent, 24-Node K8s, 새싹톤 4th/181 | MVP: BE/Infra → E2E | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2025 | **Rakuten OStore v1.0.0**: PB급 오브젝트 스토리지 | Cloud Engineer | Rakuten Symphony |
| 2024.12-2025.08 | **Rakuten Robin Storage v5.5.0**: 분산 스토리지, 2천만 유저 통신망 | Cloud Engineer | Rakuten Symphony |
| 2024 | **Aimo**: LLM 기반 갈등 중재 앱 | Backend | [KTB16Team](https://github.com/KTB16Team) |
| 2024 | **Dream**: LLM + RAG 기반 이미지/스토리 생성 앱 | DevOps | [KakaoTech-Hackathon-Dream](https://github.com/KakaoTech-Hackathon-Dream) |

---

### Writing

하네스를 만드는 과정에서 발견한 것들을 기록합니다.

| Title | Topic | Key Insight |
|-------|-------|-------------|
| [GEODE 회고: 32일, 32릴리스, 47K LoC](https://rooftopsnow.tistory.com/355) | DAG → 자율 하네스 진화 과정 | 래칫이 32번의 릴리스에서 regression 0건을 지켜낸 방법 |
| [Scaffolding: 하네스 구성 레이어 실측](https://rooftopsnow.tistory.com/354) | Claude Code 제약 분포 분석 | 78% soft / 16% hard / 3% ratchet — 제약의 종류가 품질을 결정 |
| [GEODE 랜드스케이프: 3중 하네스 발견](https://rooftopsnow.tistory.com/353) | L4 Meta-Harness 포지셔닝 | 동일 모델, 다른 scaffold → SWE-bench 11.6%p 차이 |

---

### Stack

**Lang** &nbsp;
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)

**LLM Models** &nbsp;
![Claude Opus 4.6](https://img.shields.io/badge/Claude_Opus_4.6-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![Claude Sonnet 4.6](https://img.shields.io/badge/Sonnet_4.6-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![GPT-5.4](https://img.shields.io/badge/GPT--5.4-412991?style=flat-square&logo=openai&logoColor=white)
![GPT-4.1](https://img.shields.io/badge/GPT--4.1-412991?style=flat-square&logo=openai&logoColor=white)
![GLM-5](https://img.shields.io/badge/GLM--5-3F51B5?style=flat-square&logo=chatbot&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)

**Harness(Develop)** &nbsp;
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangSmith](https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![Anthropic SDK](https://img.shields.io/badge/Anthropic_SDK-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![OpenAI SDK](https://img.shields.io/badge/OpenAI_SDK-412991?style=flat-square&logo=openai&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)

**Harness(Gate)** &nbsp;
![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black)
![mypy](https://img.shields.io/badge/mypy-2A6DB2?style=flat-square&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Bandit](https://img.shields.io/badge/Bandit-FFC107?style=flat-square&logo=python&logoColor=black)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

**Harness(Use)** &nbsp;
![Claude Code Max](https://img.shields.io/badge/Claude_Code_Max_×20-D4A574?style=flat-square&logo=anthropic&logoColor=white)

**Backend** &nbsp;
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![gRPC](https://img.shields.io/badge/gRPC-244C5A?style=flat-square&logo=google&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white)

**Infra** &nbsp;
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Istio](https://img.shields.io/badge/Istio-466BB0?style=flat-square&logo=istio&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat-square&logo=argo&logoColor=white)

**Observability** &nbsp;
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![Jaeger](https://img.shields.io/badge/Jaeger-66CFE3?style=flat-square&logo=jaeger&logoColor=black)
![OpenTelemetry](https://img.shields.io/badge/OTel-7B5EA7?style=flat-square&logo=opentelemetry&logoColor=white)
![EFK](https://img.shields.io/badge/EFK-005571?style=flat-square&logo=elastic&logoColor=white)

---

### Professional Experience

**Rakuten Symphony Korea** · Cloud BU · Cloud Engineer (Full-time) `2024.12 — 2025.08`

| Product | Stack | Description |
|---------|-------|-------------|
| **CNP Storage** | C / RPC | 2,000만 유저 통신망 PB급 분산 스토리지. SEGMENT_LOCK down_write→down_read 전환으로 읽기 병렬성 확보 |
| **Object Storage** | C | Eventual Consistency 기반 분산 게이트웨이 캐시 정합성 설계, CM→Gateway 브로드캐스트 동기화 |

글로벌 팀(인도·일본·한국 22-40명) 영어 기반 코드 리뷰·아키텍처 논의·장애 분석

**pinxlab** · AI R&D · 하네스 개발 (Freelance) `2026.03 — 2026.05`

| Product | Stack | Description |
|---------|-------|-------------|
| **REODE** | Python / LangGraph | 자율 코드 마이그레이션 에이전트(185 modules, 2,979 tests). GEODE 3-Layer Hybrid 재설계 |

Java 8→22, Spring Boot 2→3 마이그레이션<br/>
· OpenRewrite(결정적 70%) + LLM(확률적 30%) 하이브리드<br/>
· Ratchet Loop(빌드/테스트 실패 = 자동 롤백)<br/>
· Migration Scorecard 3-Tier(5 Gate + S/A/B/C 등급)<br/>
· macOS Seatbelt Sandbox + 34패턴 deny-list<br/>
· 7 Anti-Deception 가드레일

---

### Education & Certifications

| 구분 | 내용 | 기간 |
|------|------|------|
| **학사** | 부산대학교 정보컴퓨터공학부 | 2017.03 — 2023.08 |
| **부트캠프** | 카카오테크 부트캠프 Backend | 2024.06 — 2024.11 |
| **자격** | 정보처리기사 (HRD Korea) · OPIc IH (ACTFL) | 2024 - Present |
| **수상** | 2025 AI 새싹톤 우수상 4th/181 (서울특별시) | 2025.12 |

---
