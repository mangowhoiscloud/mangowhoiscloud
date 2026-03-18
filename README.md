<h1 align="center">류지환 (Jihwan Ryu)</h1>

<p align="center">
  Harness Engineering<br/>
  LLM이 올바른 방향으로 작동하도록 구조를 설계하는 엔지니어링.
</p>

<p align="center">
  <a href="https://www.youtube.com/@mango_fr">
    <img src="https://img.shields.io/badge/YouTube-@mango__fr-FF0000?style=flat-square&logo=youtube&logoColor=white" />
  </a>
  <a href="https://rooftopsnow.tistory.com">
    <img src="https://img.shields.io/badge/Blog-mango__fr_개발기-FF5722?style=flat-square&logo=tistory&logoColor=white" />
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

전통적인 소프트웨어 개발에서 엔지니어는 코드를 직접 작성해 왔습니다.
에이전틱 시스템에서 엔지니어의 역할은 LLM이 올바른 방향으로 작동하도록 구조를 설계하는 쪽으로 이동합니다. 
LLM에게 하네스(harness)는 "대상을 제어 가능한 환경에 묶어두고 관측하는 틀"이며, LLM 맥락에서는 네 가지 축으로 구성됩니다.

| 축 | 역할 | 실천 사례 |
|---|---|---|
| **컨텍스트 제어** | 어떤 정보를 언제 얼마나 LLM에 주입할지 설계 | GEODE PromptAssembler 6-Phase, SHA-256 고정으로 prompt caching 활성화(비용 90% 절감) |
| **실행 루프** | LLM 출력을 받아 다음 행동을 결정하는 오케스트레이션 | GEODE AgenticLoop `while(tool_use)`, 38 tools × 15 rounds 자율 실행 |
| **검증 파이프라인** | 비결정론적 출력을 신뢰할 수 있는 수준으로 수렴 | Eco² Swiss Cheese 3-Layer(69.4 → 99.8/100), GEODE 5-Layer Verification |
| **관측** | 위 세 가지가 실제로 작동하는지 측정하는 계측 | Eco² 4-Pillar Observability, GEODE 27-Event Hook Observer |

Karpathy는 nanochat을 "the simplest experimental harness for training LLMs"라 부릅니다.
Claude Code는 `.claude/` 디렉토리 하나로 에이전트 컨텍스트를 제어합니다.
아래는 같은 접근을 Multi-Agent 하네스와 분산 백엔드, 자율 실행 에이전트에 걸쳐 직접 실천한 기록입니다.

**Eco²** 
MVP: 5인 팀 Solo Backend/Infra, E2E Product Engineering
LangGraph Multi-Agent 하네스를 구축하고, 계측 근거로 아키텍처를 네 차례 전환해 LLMx2 DAG **VU 1,000 / 97.8%** 도달.
Auth Offloading **48 → 1,477 RPS**. Swiss Cheese 3-Layer 평가에서 **69.4 → 99.8/100**. 
2025 AI 새싹톤 우수상 수상 (**4th/181**)

**GEODE** 
Claude Code `while(tool_use)` 패턴을 참고한 AgenticLoop 설계. 
38 tools × 15 rounds 자율 실행. Domain-specific한 탐색/가치추론을 지원하는 DAG형 PLUG-IN.

**REODE** 
GEODE v0.12.0 fork. 
DomainPort → PipelineTemplate Protocol 교체, `register_domain()`으로 마이그레이션, 코드 리뷰 파이프라인 DAG 개발.

---

### Loop

시스템을 구축하고, 관측하고, 병목을 부수고, 더 나은 구조로 개선합니다.
프로젝트와 도메인이 바뀌어도 개발(DAG)은 일관되게 반복됩니다.

```
Plan → Build → Observe → Break → Rebuild → Share → (repeat)
```

#### Implementation Loop

Ratchet 패턴 — 빌드+테스트를 통과한 변경만 커밋, 실패 시 롤백 후 재시도.

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
| Post-Merge | docs-sync validation | CLAUDE.md, CHANGELOG.md, README.md 수치 일치 |

#### Multi-Agent Loop

병렬 서브에이전트가 독립 컨텍스트에서 평가/검수/수정을 수행하고, 결과를 부모 세션으로 수렴.

```
Parent AgenticLoop
  ├─ spawn Agent ×N  (MAX_CONCURRENT=5, DAG scheduling)
  │     ├─ Scoring Agent    — 품질 차원별 평가
  │     ├─ Inspection Agent — lint, coverage, SOT 정합성
  │     └─ Review Agent     — 6-lens code review
  ├─ collect results  (4096-token guard, summary 필수)
  └─ threshold check
       ├─ Pass → commit
       └─ Below → fix batch → re-score (loop)
```

19개 커스텀 스킬(`/ratchet-loop`, `/code-review-workflow` 등)이 도메인 지식을 재사용 가능한 프롬프트로 인코딩하여 세션마다 동일 품질을 보장합니다.

#### Loop in Action

| Project | Loop | Result |
|---------|------|--------|
| **Eco²** | 완료율 0% Sync 구조 → Grafana/ELK 계측 근거 아키텍처 4회 전환 | **VU 1,000 / 97.8%**, 69.4→99.8/100 |
| **GEODE** | Research→Implement→Verify→Merge ×5/day, 래칫 기반 22일 스프린트 | **119 PR, 35K LOC, 2,366+ tests** |
| **REODE** | DomainPort→PipelineTemplate Protocol 교체, 래칫+멀티에이전트 파이프라인 | **도메인 무관성 실증, 1,805 tests** |

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
├── 2024.12-2025.08/  Rakuten Symphony Korea, Jr. Cloud Engineer, Full-time
│   └── PB급 분산 스토리지 개발, 글로벌 팀 22-40명, 영어 기반
│
├── 2025.10-2026.02/  Eco² (MVP: 5인 팀 Solo Backend & Infra, E2E: Product Engineer)
│   └── AI Multi-Agent, 24-Node K8s, MVP: 2025 AI 새싹톤 우수상 수상 4th/181, 3개월간 E2E로 FE/BE/Harness(LLM) 개발 및 운용
│
├── 2026.02-present/  GEODE (Solo)
│   └── 게임 IP 도메인 탐색 에이전트(DAG) -> 자율 실행 에이전트로 디벨롭, 도메인 기능은 Plug-in 레벨로 격하.
│
└── 2026.03-present/  REODE @ Pinkx Lab (Freelance)
    └── Migration & Coding Core Agent, 자율 실행 + 마이그레이션/리뷰/코딩 파이프라인(DAG)
```

---

### Projects

| Date | Project | Role | Link |
|------|---------|------|------|
| 2026.03 - 2026.05 | **REODE**:Migration & Coding Agent @ Pinx Lab | AI R&D Freelance | Pinx Lab |
| 2026.02 - 2026.03 | **GEODE**:게임 도메인 IP 탐색 에이전트 -> 범용 자율 리서치 에이전트, IP 탐색 에이전트(DAG)는 Plug-In 레이어로 활용 | Solo | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) |
| 2026.02 - 2026.02 | **LLMART(AD ONLY)**:CLI-based LLM-as-Judge Evaluation System | Solo | [mangowhoiscloud/llmart](https://github.com/mangowhoiscloud/llmart) |
| 2025.10.31 - 2026.02 | **Eco²**:AI 재활용 Multi-Agent, 24-Node K8s, 새싹톤 4th/181 | MVP: Backend & Infra, E2E: Product Engineer | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2025.03 - 2025.06 | **Rakuten OStore v1.0.0**:PB급 오브젝트 스토리지 | Jr. Cloud Storage Dev | Rakuten Symphony |
| 2024.12.09 - 2025.08.31 | **Rakuten Robin Storage v5.5.0**:분산 스토리지, 2천만 유저 통신망 | Jr. Cloud Storage Dev | Rakuten Symphony |
| 2024 | **Aimo**:LLM 기반 갈등 중재 앱 | Backend | [KTB16Team](https://github.com/KTB16Team) |
| 2024 | **Dream**:LLM + RAG 기반 이미지/스토리 생성 앱 | DevOps | [KakaoTech-Hackathon-Dream](https://github.com/KakaoTech-Hackathon-Dream) |
| 2022 | **Fisher Market**:ERC-1155 기반 수산물 거래 DApp | Backend | [mng990/ethereum_FisheriesMarket](https://github.com/mng990/ethereum_FisheriesMarket) |

---

### Stack

**Lang** &nbsp;
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)

**Harness(Develop)** &nbsp;
![Claude Agent SDK](https://img.shields.io/badge/Claude-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![OpenAI Agent SDK](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Gemini SDK](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangSmith](https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

**Harness(Use)** &nbsp;
![Claude Code Max](https://img.shields.io/badge/Claude_Code_Max_×20-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![Opus 4.6](https://img.shields.io/badge/Opus_4.6-D4A574?style=flat-square&logo=anthropic&logoColor=white)

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
![ELK](https://img.shields.io/badge/ELK-005571?style=flat-square&logo=elastic&logoColor=white)

---
