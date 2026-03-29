<p align="right">
  <a href="README.md">🇰🇷 한국어</a> · <strong>🇺🇸 English</strong>
</p>

<h1 align="center">류지환 (Jihwan Ryu)</h1>

<p align="center">
  <strong>Act with language. Verify with structure. Build with loops.</strong><br/>
  Probabilistic systems (LLMs) diverge without control. I build harnesses that converge divergence through loops and values.
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

LLMs are probabilistic systems. Without a control plane, long-running autonomous execution diverges.
A harness converges this divergence through five axes.

| Axis | Role | Implementation |
|---|---|---|
| **Context Control** | Loops and guardrails determine the upper bound of output quality | CANNOT/CAN, Ratchet, GEODE/REODE 5-Layer Context Hub(C0-C4, global and local .geode/.reode), Runtime PromptAssembler, Model Switching Context Compression |
| **Plan and Execute** | Orchestration that receives LLM output and decides the next action | AgenticLoop `while(tool_use)`, Hook System(Event Bus), LaneQueue, TaskGraph, bash/tool/skill/MCP Registry, Sub-Agent(MAX_CONCURRENT=5, inherits parent Agent loop) |
| **Verify** | Converges non-deterministic output to a trustworthy level | Eco² Swiss Cheese 3-Layer(69.4 → 99.8%), GEODE 5-Layer Verification + Cross-LLM |
| **Observe** | Instruments whether the above four axes actually work | 36-Event Hook Observer, LangSmith or custom Token + Transcript Tracing, CUSUM Drift Detection |
| **Scaffold** | Meta layer that produces agents via platform harness (Claude Code) and scaffolding | Claude Code(.claude/ Skills·Hooks·CLAUDE.md) producing GEODE, harness-for-real, GEODE→REODE 2-Protocol redesign. Currently hardening and validating before productionization |

Beyond frontier models (Claude, GPT), I directly operate various models including GLM, understanding each model's strengths and limitations. I build systems so the service loop continues even when any provider experiences an outage.

#### Three-Layer Harness Architecture

LLMs give different answers every time. Quality fluctuates even with the same prompt, and they cannot self-verify hallucinations.
To turn this probabilistic system into a controllable execution engine, structure must be layered on top of the model.

```
Layer ③  Scaffold: CLAUDE.md + 25 Skills + 36 Hook ← 제약과 지식, workflow
Layer ②  Coding Agent (Platform Harness)           ← Anthropic이 제공한 실행 환경
Layer ①  Foundation LLM        ← 확률적 컴퓨팅 인프라
```

Even with the same LLM, the design of Layer ③ can produce an 11.6%p difference in SWE-bench scores.
GEODE created **Producer-Product Inversion** while demonstrating this architecture: a reversed structure where the Coding Agent Harness produces GEODE (an Autonomous harness).
It autonomously performs tool selection, execution, verification, and self-improvement, converging output through 4-stage Guardrails and Cross-LLM cross-verification.

#### Harness Landscape. 4-Quadrant Positioning

This landscape shows how the harnesses I built are distributed.

```
                          Autonomous
                              ▲
                              │
           Q2                 │                Q1
      Minimal+Autonomous      │       Comprehensive+Autonomous
                              │
      · SWE-agent             │         ★ GEODE (L4 Meta)
      · Codex CLI       · Claude Code   · Devin
      · AutoGen          (← 생산 도구)   · Manus
                              │         · OpenHands
                              │         · OpenClaw
                              │
  ◄───────────────────────────┼───────────────────────────────►
      Minimal                 │              Comprehensive
                              │
           Q3                 │                Q4
      Minimal+Assisted        │        Comprehensive+Assisted
                              │
      · Aider                 │         · Cursor
      · Gemini CLI            │         · Copilot
      · CrewAI                │         · Kiro
                              │
                              ▼
                           Assisted
```

#### Scaffolding: Control Points of the Production Harness

Scaffolding is the configuration layer of the harness that produces agents. It is the **design of constraints**, not code, that determines quality.

| Component | Weight | Role | GEODE Measured |
|----------|------|------|-----------|
| **Instruction (CLAUDE.md)** | Soft 78% | Behavioral rules, CANNOT/CAN framework | 428 lines, 20 CANNOT rules |
| **Skills** | Knowledge encoding | Domain-specific reusable prompts | 25 skills, 3,468 LoC |
| **Hooks** | Hard 16% | Event-driven automated control | 1 of 36 events active (room for expansion) |
| **CI/CD Gates** | Ratchet 3% | Automated rollback gates | 5 CI jobs, test ≥ 3181 |
| **Memory** | Cross-session learning | Pattern accumulation → auto-injected in next session | 19 memory files |

78% of constraints rely on LLM self-discipline (soft). This ratio determines harness maturity.

---

### Projects

4-quadrant positioning of my projects:

| Project | Quadrant | Position | Core Role |
|---------|----------|--------|----------|
| **GEODE** | Q1 (Comprehensive + Autonomous + Domain-specific Plug-in) | L4 Meta-Harness | General-purpose autonomous execution. Domain-swappable |
| **REODE** | Q1 (Autonomous + Domain-specific Plug-in) | L4 Meta-Harness | Autonomous agent specialized in code migration |
| **Eco²** | Q4 (Comprehensive + Assisted) | Multi-Agent Service | User-driven, Chat-based agent harness, AI parallel evaluation and tool calling, intent classification via natural language |
| **harness-for-real** | Q2 (Minimal + Autonomous) | Hackathon Harness | 4-Phase FSM, minimal-config autonomous execution |
| Claude Code (production tool) | Q4 | Platform Harness | The tool that produces GEODE/REODE |

**Eco²**, Multi-Agent AI Service
MVP 1mon: Solo Backend/Infra in a 5-person team → E2E 3mon: Solo design, development, and operations across FE/BE/INFRA/HARNESS/LLM.

- **Concurrent connection problem solved**: SSE connections exploded at 1:21 ratio, 0% completion rate at 100VU → Decoupled production/consumption via EDA-based Event Bus, achieving **0→1,000VU, 97.8% SLA**
- **LLM evaluation quality**: Single evaluator bias limitation → Swiss Cheese 3-Layer defense, Expert Review **69.4→99.8%**
- **Auth bottleneck eliminated**: All requests routed through Auth MS, capped at 48 RPS → Istio ext-authz Offloading achieved **1,477 RPS (31x)**
- 2025 AI Saessak-thon Excellence Award **4th/181** (Seoul Metropolitan Government, DAYCON)

**GEODE**, General-Purpose Autonomous Execution Agent Harness (CLI + Slack Daemon)
`v0.28.1` · 221 modules · 3,181 tests · 47 tools + 44 MCP · 36 hooks · 25 skills

"Can we build a harness that works even when the domain changes?" Started as a game-IP-specific pipeline, then pivoted to a general-purpose harness. 32 releases in 32 days, 0 regressions.

- **Domain independence**: DomainPort Protocol makes analysis DAGs pluggable → Ported to code migration domain via REODE, with 0 lines modified in AgenticLoop. This portability led to a freelance contract
- **Autonomous execution**: `while(tool_use)` loop where the LLM autonomously selects from 54 tools + 44 MCP. Covers bash execution, sub-agent delegation, schedule registration, and MCP external integration. Sub-Agent parallel delegation (MAX 5, DAG, Token Guard) for complex task decomposition
- **3-Provider Resilience**: Anthropic/OpenAI/GLM 3-provider failover chain + per-provider circuit breaker. Per-pipeline-node model pinning (Opus 4.6) separates from the REPL model
- **Context control**: 5-Layer Context Hub(C0-C4) + per-turn status line (per-turn metrics, not session-cumulative). Auto-compression via Haiku at 80% threshold
- **Verification convergence**: 5-Layer Verification + Cross-LLM(Krippendorff α ≥ 0.67). Converges non-deterministic output to a trustworthy level
- **Slack daemon**: `geode serve` headless. Per-channel session isolation, Echo Prevention triple defense. Operate the agent from Slack without CLI

**REODE**, Autonomous Code Migration Agent @ pinxlab (Freelance)
"When a probabilistic system modifies code, how do you guarantee quality?" Redesigned the GEODE harness and deployed it for legacy Java migration at an actual production site. Currently in operation.

- **Deterministic/probabilistic separation**: Mechanical transformations (javax→jakarta, etc.) use OpenRewrite recipes (70%), only business-logic-dependent transformations use LLM (30%). Minimizes probabilistic system involvement
- **Failure path design**: On VALIDATE failure, Fix Node analyzes the error and auto-retries (max 3). Upon detecting 3 identical errors converging → model escalation. Code that fails build/test cannot merge (Ratchet)
- **Reward Hacking prevention**: Migration Scorecard 5 Gate. Structurally blocks test deletion, skipTests flags, JDK downgrade, and @SuppressWarnings insertion
- **Harness redesign**: Removed GEODE's DomainPort (1 DI) and introduced PipelineTemplate(L1) + LanguageAdapter(L2) 2-Protocol orthogonal separation. Reuses L0 infrastructure without modification
- **Sandbox isolation**: macOS Seatbelt + 34-pattern deny-list + 3-Level Permission (deny→ask→allow) for agent system access control
- **Measured migration**: Java 8→22 + Spring 4→6 legacy project (241 sources, 103K LoC). 33 sessions / 1,133 LLM rounds / 5 hours 48 minutes. `mvn compile` + `mvn test` 83/83 passed, javax→jakarta transition + Security reconfiguration complete

  **Real-World Result (Completed 2026.03.28)**

  | Metric | Value |
  |--------|-------|
  | Codebase | 5,523 files (241 Java + 355 JSP + 47 XML) |
  | Migration | Java 1.8 → 22, Spring 4 → 6 |
  | Result | 83/83 tests + FE/BE E2E verified |
  | Cost | ~$388 (33 sessions, 1,133 LLM rounds) |
  | Time | 5h 48m (autonomous, zero human intervention) |

  > Client feedback: *"Exceeded expectations."*

**harness-for-real**, Autonomous Execution Harness for AI Agent Hackathons
"The moment your hands touch the keyboard, the harness has failed." Analyzed the winning team's strategy from Ralph-thon (Korea's first AI coding hackathon) and structured it into a reproducible harness.

- **Ambiguity elimination first**: Socratic Phase refines requirements before coding (winning team: 133 rounds). Input precision determines the upper bound of output
- **Self-verification**: typecheck+lint Backpressure hooks on every write, 70% test ratio. Structurally blocks @Disabled/@pytest.mark.skip
- **Long-running stability**: Error patterns accumulated in LEARNINGS.md → auto-injected in next iteration. Auto-halt at Token budget 80%/100%

---

### Loop

Minimizing feedback intervals drastically reduces defect repair cost (Beck, XP).
This loop repeats identically regardless of project or domain. GEODE's 32 releases are the product of this loop.

```
Plan → Build → Observe → Break → Rebuild → Share → (repeat)
```

#### Implementation Loop

Ratchet pattern: only changes that pass build+test get committed. On failure, rollback and retry.<br>
Beck: "Code without tests is legacy code."

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
| PR | GitHub Actions CI | `gh pr checks --watch` all green |
| Post-Merge | docs-sync validation | Version sync across 4 locations (CHANGELOG, CLAUDE.md, README, pyproject.toml) |

#### Multi-Agent Loop

Parallel sub-agents perform evaluation, review, and fixes in independent contexts, then converge results into the parent session.

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

25 custom skills encode domain knowledge into reusable prompts, ensuring consistent quality across sessions.

#### Cross-Project Loop

Validated patterns from previous projects transfer as infrastructure for the next.

| Pattern | Eco² (origin) | GEODE (evolution) | REODE (pivot) |
|------|---------------|--------------|-------------|
| **Scaffold** | Closed loop with observation (recursive improvement + Retry/Fallback) | CLAUDE.md(428 lines) + 25 Skills + CI Hooks | REODE.md + 23 Skills + Seatbelt Sandbox |
| **Autonomous** | User-driven Chat-based | 37 Hook Events + TaskGraph + LaneQueue | 36 Hook Events + fix_node Architect/Editor separation |
| **Memory** | ReadThroughCheckpointer | .geode/ 4-Tier context persistence (SOUL→User→Org→Project→Session) + ~/.geode/ global | .reode/ local + ~/.reode/ global persistence (reused without modification) |
| **Evaluation** | Swiss Cheese 3-Layer (69.4→99.8%) | 5-Layer Verification + Cross-LLM | Scorecard 3-Tier + Anti-Deception 7 Guard |
| **Context** | Intent Confidence Scoring | PromptAssembler 6-Phase + Journal/Vault deterministic persistence | Reused without modification |
| **Loop Control** | In-app closed feedback loop (observe→recursive improvement) | `while(tool_use)` AgenticLoop enhancement. LLM autonomously selects tool/bash/MCP/DAG. Sub-Agent inherits parent loop | AgenticLoop inherited + Ratchet + FixEventLog auto-learning |

#### Loop in Action

| Project | Loop | Result (changes produced by the loop) |
|---------|------|------------------------|
| **Eco²** | 0% completion rate Sync → EDA Event Bus, architecture pivoted 4 times based on instrumentation | Concurrent connections 0→**1,000VU 97.8%**, evaluation quality 69.4→**99.8%**, AI Saessak-thon **4th/181** |
| **GEODE** | Worktree→GAP Audit→Socratic Gate→CI Ratchet→PR | Game IP value-inference DAG → **developed into general-purpose autonomous execution harness**, Domain DAG plugin → **pivoted to migration domain** (freelance contract) |
| **REODE** | GEODE harness pivot → 2-Protocol separation, Ratchet + Anti-Deception | OpenRewrite 70% to **minimize probabilistic system involvement**, 5-Gate Scorecard to **structurally block Reward Hacking** |
| **harness-for-real** | Ralph-thon winning team strategy analysis → 4-Phase FSM harness | Backpressure hooks + LEARNINGS.md for **long-running autonomous execution stability** |

---

### Timeline

```
mangowhoiscloud/
├── 2017.03-2023.08/  Pusan National University, CSE
│   └── Bachelor of Computer Science & Engineering
│
├── 2024.07-2024.11/  Kakao Tech Bootcamp
│   └── Backend · DevOps · LLM
│
├── 2024.12-2025.08/  Rakuten Symphony Korea, Cloud Engineer, Full-time
│   └── PB-scale distributed storage development, global team of 22-40, English-based
│
├── 2025.10-2026.02/  Eco² (MVP 1mon: Solo Backend/Infra, E2E 3mon: FE/BE/INFRA/HARNESS/LLM)
│   └── AI Multi-Agent, 24-Node K8s, 2025 AI Saessak-thon Excellence Award 4th/181
│
├── 2026.01.31-present/  GEODE (Solo)
│   └── General-purpose autonomous execution agent harness (CLI+Slack), 221 modules, 3,181 tests, 32 releases
│
└── 2026.03-2026.05/  REODE @ pinxlab (Freelance)
    └── DomainPort removed → 2-Protocol redesign, Migration/Porting/Coding Agent
```

---

### Project Links

| Date | Project | Role | Link |
|------|---------|------|------|
| 2026.03 | **harness-for-real**: Autonomous harness for Ralph-thon & AI hackathons, 4-Phase FSM | Solo | [mangowhoiscloud/harness-for-real](https://github.com/mangowhoiscloud/harness-for-real) |
| 2026.03-2026.05 | **REODE**: Migration & Coding Agent @ pinxlab | Freelance | pinxlab |
| 2026.01.31-Present | **GEODE**: General-purpose autonomous execution agent harness, 221 modules, 3,181 tests, v0.28.1 | Solo | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) |
| 2026.02 | **LLMART**: CLI-based LLM-as-Judge Evaluation System | Solo | [mangowhoiscloud/llmart](https://github.com/mangowhoiscloud/llmart) |
| 2025.10.31-2026.02 | **Eco²**: AI Multi-Agent, 24-Node K8s, AI Saessak-thon 4th/181 | MVP: BE/Infra → E2E | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2025 | **Rakuten OStore v1.0.0**: PB-scale object storage | Cloud Engineer | Rakuten Symphony |
| 2024.12-2025.08 | **Rakuten Robin Storage v5.5.0**: Distributed storage, 20M-user telecom network | Cloud Engineer | Rakuten Symphony |
| 2024 | **Aimo**: LLM-based conflict mediation app | Backend | [KTB16Team](https://github.com/KTB16Team) |
| 2024 | **Dream**: LLM + RAG-based image/story generation app | DevOps | [KakaoTech-Hackathon-Dream](https://github.com/KakaoTech-Hackathon-Dream) |

---

### Writing

Recording discoveries made while building harnesses.

| Title | Topic | Key Insight |
|-------|-------|-------------|
| [Scaffolding: Measured Harness Configuration Layers](https://rooftopsnow.tistory.com/354) | Claude Code constraint distribution analysis | 78% soft / 16% hard / 3% ratchet. The type of constraint determines quality |
| [GEODE Landscape: Discovering the Three-Layer Harness](https://rooftopsnow.tistory.com/353) | L4 Meta-Harness positioning | Same model, different scaffold → 11.6%p SWE-bench difference |

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

**Rakuten Symphony Korea** · Cloud BU · Cloud Engineer (Full-time) `2024.12 - 2025.08`

| Product | Stack | Description |
|---------|-------|-------------|
| **CNP Storage** | C / RPC | PB-scale distributed storage for 20M-user telecom network. SEGMENT_LOCK down_write→down_read transition to secure read parallelism |
| **Object Storage** | C | Distributed gateway cache consistency design based on Eventual Consistency, CM→Gateway broadcast synchronization |

Global team (India, Japan, Korea, 22-40 members), English-based code review, architecture discussion, and incident analysis

**pinxlab** · AI R&D · Harness Development (Freelance) `2026.03 - 2026.05`

| Product | Stack | Description |
|---------|-------|-------------|
| **REODE** | Python / LangGraph | Autonomous code migration agent (185 modules, 2,979 tests). GEODE 3-Layer Hybrid pivot |

Scaffold: CLAUDE.md(109 lines) + REODE.md(55 lines) + 23 Skills(java-migration, spring-expert, mybatis-expert, scorecard, ratchet-loop, etc.)<br/>
Java 8→22, Spring Boot 2→3 migration<br/>
· OpenRewrite (deterministic 70%) + LLM (probabilistic 30%) hybrid<br/>
· Ratchet Loop (build/test failure = auto-rollback)<br/>
· Migration Scorecard 3-Tier (5 Gate + S/A/B/C grading)<br/>
· macOS Seatbelt Sandbox + 34-pattern deny-list<br/>
· 7 Anti-Deception guardrails

---

### Education & Certifications

| Category | Details | Period |
|------|------|------|
| **Bachelor's** | Pusan National University, CSE | 2017.03 - 2023.08 |
| **Bootcamp** | Kakao Tech Bootcamp Backend | 2024.06 - 2024.11 |
| **Certification** | Engineer Information Processing (HRD Korea) · OPIc IH (ACTFL) | 2024 - Present |
| **Award** | 2025 AI Saessak-thon Excellence Award 4th/181 (Seoul Metropolitan Government) | 2025.12 |

---
