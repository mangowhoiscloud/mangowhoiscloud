<h1 align="center">류지환 (Jihwan Ryu)</h1>

<p align="center">
  <strong>모델 능력이 상수일 때, 변수는 오케스트레이션의 구조입니다.</strong><br/>
  Harness Engineering — 제어 없는 확률적 시스템은 발산합니다. 구조로 수렴시킵니다.
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
| **컨텍스트 제어** | 입력의 정밀도가 출력의 상한을 결정 | GEODE 5-Layer Context Hub(C0-C4), PromptAssembler 6-Phase, SHA-256 pinning(비용 40-60% 절감) |
| **실행 루프** | LLM 출력을 받아 다음 행동을 결정하는 오케스트레이션 | AgenticLoop `while(tool_use)`, 46 tools, Sub-Agent(MAX_CONCURRENT=5, DAG, Token Guard) |
| **검증 파이프라인** | 비결정론적 출력을 신뢰 가능한 수준으로 수렴 | Eco² Swiss Cheese 3-Layer(69.4 → 99.8%), GEODE 5-Layer Verification + Cross-LLM |
| **관측** | 위 네 가지가 실제로 작동하는지 계측 | 36-Event Hook Observer, LangSmith Tracing, CUSUM Drift Detection |
| **외부 하네스 구축** | 하네스 자체를 설계·납품하고 도메인 간 이식하는 메타 역량 | Claude Code(.claude/ Skills·Hooks·CLAUDE.md)로 GEODE를 생산, harness-for-real(해커톤 4-Phase FSM), GEODE→REODE 2-Protocol 재설계로 클라이언트 납품 |

다섯 축을 관통하는 원칙: 프론티어 모델(Claude, GPT)뿐 아니라 GLM 등 다양한 모델을 직접 운영하며 각 모델의 강점과 한계를 파악하고, 어떤 프로바이더에 장애가 발생하더라도 서비스가 지속되는 Resilience를 설계합니다.

---

### Projects

**Eco²** — Multi-Agent AI Service
MVP(1개월): 5인 팀에서 백엔드·인프라 단독 담당 → E2E(3개월): FE/BE/Infra/LLM/Harness 전체 단독 설계·개발·운영.
EDA 기반 Event Bus로 동시접속 0→1,000VU 확보. 서비스 간 부하 독립 — Agent MS가 느려도 SSE MS는 즉시 응답.

- **VU 1,000 / 97.8%** · 373 RPM · 400+ TPM | ext-authz **48 → 1,477 RPS** (31x)
- Swiss Cheese 3-Layer 평가: **69.4 → 99.8%** | 2025 AI 새싹톤 우수상 **4th/181**
- EDA-MSA 8-Domain Clean Architecture, KEDA 오토스케일링, ArgoCD GitOps

**GEODE** — 범용 자율 실행 에이전트 하네스 (CLI + Slack Daemon)
Claude Code `while(tool_use)` 패턴을 참고한 AgenticLoop. DomainPort Protocol로 도메인 로직을 플러그인 레벨로 분리.

- **184 modules · 3,055 tests · 46 tools · 42 MCP · 36 hooks · 25 skills · 364+ PR**
- 3사 LLM Failover(Anthropic/OpenAI/GLM), 노드별 모델 라우팅(.geode/routing.toml)
- `geode serve` Slack 데몬 — ChannelBinding, LaneQueue, Echo Prevention 3중
- Sub-Agent 병렬 위임(CoalescingQueue + TaskGraph DAG + IsolatedRunner)
- 5-Layer Context Hub(C0-C4), Context Compaction(WARNING 80% → Haiku 압축)
- 5-Layer Verification + Cross-LLM(Krippendorff α ≥ 0.67) + Confidence Gate
- Security: Secret Redaction 8패턴, Bash 3-Layer Sandbox, PolicyChain 6-layer

**REODE** — Autonomous Code Migration Agent @ Pinkx Lab (Freelance)
GEODE를 코드 마이그레이션 도메인에 이식하면서, DomainPort를 단순 교체하지 않고 **삭제 후 2-Protocol 직교 분리로 재설계**.

- L1 **PipelineTemplate**(워크플로우 토폴로지) + L2 **LanguageAdapter**(언어별 빌드/테스트/스킬) — DI 3점 분리
- MigrationPipeline 6노드(ASSESS→PLAN→TRANSFORM→VALIDATE⟲FIX→MEASURE) + PortingPipeline 4노드
- OpenRewrite(결정적 70%) + LLM(확률적 30%) 하이브리드 — 확률적 시스템 개입 범위 최소화
- Migration Scorecard 3-Tier: 5 Gate(Reward Hacking 방지) + 4등급 + Insight
- AgentRole 4종(ARCHITECT/ENGINEER/REVIEWER/SCOUT) 노드별 비용 라우팅
- L0 인프라(AgenticLoop, HookSystem, Memory, PromptAssembler) 수정 없이 재사용

**harness-for-real** — AI 에이전트 해커톤용 자율 수행 하네스
랄프톤(한국 최초 AI 코딩 해커톤) 우승팀 전략을 분석하고, 재현 가능한 하네스로 구조화.

- 4-Phase FSM: Socratic(모호성 제거) → Plan(의존 그래프) → Build(Opus/Sonnet 적응 라우팅) → Verify(3-Agent 검증)
- Backpressure hooks(매 write마다 typecheck+lint), Pre-commit gate(테스트+@Disabled 차단)
- Runtime LEARNINGS.md 축적 → 다음 이터레이션 자동 주입, Token budget 80%/100% 자동 정지

---

### Loop

피드백 간격을 최소화하면 결함 수정 비용이 급감합니다 (Beck, XP).
프로젝트와 도메인이 바뀌어도 이 루프는 동일하게 반복됩니다.

```
Plan → Build → Observe → Break → Rebuild → Share → (repeat)
```

#### Implementation Loop

Ratchet 패턴 — 빌드+테스트를 통과한 변경만 커밋, 실패 시 롤백 후 재시도.
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

| Project | Loop | Result |
|---------|------|--------|
| **Eco²** | 완료율 0% Sync → EDA Event Bus, 계측 근거 아키텍처 4회 전환 | **VU 1,000 / 97.8%**, 69.4→99.8% |
| **GEODE** | Worktree→GAP Audit→Socratic Gate→CI Ratchet→PR | **184 modules, 3,055 tests, 364+ PR** |
| **REODE** | DomainPort 삭제 → 2-Protocol 재설계, Scorecard 3-Tier | **5-Gate quality, 4-Role Agent Team, Freelance 계약** |
| **harness-for-real** | 랄프톤 우승 전략 분석 → 4-Phase FSM 하네스화 | **Socratic→Plan→Build→3-Agent Verify** |

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
├── 2025.10-2026.02/  Eco² (MVP 1mo: Solo Backend/Infra, E2E 3mo: Full-stack)
│   └── AI Multi-Agent, 24-Node K8s, 2025 AI 새싹톤 우수상 4th/181
│
├── 2026.01.31-present/  GEODE (Solo)
│   └── 범용 자율 실행 에이전트 하네스(CLI+Slack), 184 modules, 3,055 tests
│
└── 2026.03-2026.05/  REODE @ Pinkx Lab (Freelance)
    └── DomainPort 삭제 → 2-Protocol 재설계, Migration/Porting/Coding Agent
```

---

### Project Links

| Date | Project | Role | Link |
|------|---------|------|------|
| 2026.03 | **harness-for-real**: 랄프톤 & AI 해커톤용 자율 하네스, 4-Phase FSM | Solo | [mangowhoiscloud/harness-for-real](https://github.com/mangowhoiscloud/harness-for-real) |
| 2026.03-2026.05 | **REODE**: Migration & Coding Agent @ Pinkx Lab | Freelance | pinxlab |
| 2026.01.31-Present | **GEODE**: 범용 자율 실행 에이전트 하네스, 184 modules, 3,055 tests | Solo | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) |
| 2026.02 | **LLMART**: CLI-based LLM-as-Judge Evaluation System | Solo | [mangowhoiscloud/llmart](https://github.com/mangowhoiscloud/llmart) |
| 2025.10.31-2026.02 | **Eco²**: AI Multi-Agent, 24-Node K8s, 새싹톤 4th/181 | MVP: BE/Infra → E2E | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2025 | **Rakuten OStore v1.0.0**: PB급 오브젝트 스토리지 | Cloud Engineer | Rakuten Symphony |
| 2024.12-2025.08 | **Rakuten Robin Storage v5.5.0**: 분산 스토리지, 2천만 유저 통신망 | Cloud Engineer | Rakuten Symphony |
| 2024 | **Aimo**: LLM 기반 갈등 중재 앱 | Backend | [KTB16Team](https://github.com/KTB16Team) |
| 2024 | **Dream**: LLM + RAG 기반 이미지/스토리 생성 앱 | DevOps | [KakaoTech-Hackathon-Dream](https://github.com/KakaoTech-Hackathon-Dream) |

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

### Experience

**Rakuten Symphony Korea** · Cloud BU · Cloud Engineer (Full-time) `2024.12 — 2025.08`

| Product | Stack | Description |
|---------|-------|-------------|
| **CNP Storage** | C / RPC | 2,000만 유저 통신망 PB급 분산 스토리지. SEGMENT_LOCK down_write→down_read 전환으로 읽기 병렬성 확보 |
| **Object Storage** | C | Eventual Consistency 기반 분산 게이트웨이 캐시 정합성 설계, CM→Gateway 브로드캐스트 동기화 |

글로벌 팀(인도·일본·한국 22-40명) 영어 기반 코드 리뷰·아키텍처 논의·장애 분석, Jira·GitOps 기반 개발

**Pinkx Lab** · AI R&D · Harness Engineer (Freelance) `2026.03 — 2026.05`

| Product | Stack | Description |
|---------|-------|-------------|
| **REODE** | Python / LangGraph | 자율 코드 마이그레이션 에이전트. GEODE에서 DomainPort 삭제 → PipelineTemplate + LanguageAdapter 2-Protocol 직교 재설계 |

Java 8→22, Spring Boot 2→3 마이그레이션 파이프라인. OpenRewrite(결정적 70%) + LLM(확률적 30%) 하이브리드, Migration Scorecard 3-Tier 품질 프레임워크

---

### Education & Certifications

| 구분 | 내용 | 기간 |
|------|------|------|
| **학사** | 부산대학교 정보컴퓨터공학부 | 2017.03 — 2023.08 |
| **부트캠프** | 카카오테크 부트캠프 Backend | 2024.06 — 2024.11 |
| **자격** | 정보처리기사 (HRD Korea) · OPIc IH (ACTFL) | 2024 |
| **수상** | 2025 AI 새싹톤 우수상 4th/181 (서울특별시) | 2025.12 |

---
