<h1 align="center">류지환 (Jihwan Ryu)</h1>

<p align="center">
  Harness Engineering <br/>
  동작하는 코드를 부수고 더 나은 구조로 재조립하는 과정 자체가 설계 방법론.
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

Karpathy는 nanochat을 "the simplest experimental harness for training LLMs"라 부른다. Claude Code는 `.claude/` 디렉토리 하나로 에이전트의 컨텍스트 전체를 제어한다. 같은 접근을 직접 실천한 사례들.

**Eco²** — LangGraph Multi-Agent 하네스를 밑바닥부터 구축. Sync Thread Pool에서 시작해 Event Bus 3-Tier까지, Grafana/ELK 계측 결과가 아키텍처 전환의 유일한 근거였다. Auth 병목 48 RPS → Go gRPC 사이드카로 오프로드 → **1,477 RPS**. Swiss Cheese 3-Layer 평가 파이프라인에서 LLM 응답 품질 **69.4 → 99.8/100**.

**GEODE** — 고정 DAG 파이프라인의 한계를 확인하고, Claude Code의 `while(tool_use)` 패턴을 참고해 AgenticLoop를 설계했다. 38 tools, 15 rounds 자율 실행. 도메인 파이프라인은 도구 중 하나로 재배치. PromptAssembler 6-Phase가 시스템 프롬프트를 SHA-256으로 고정해 Anthropic prompt caching 자동 활성화, 반복 호출 **90% 비용 절감**. `.claude/` 디렉토리에 CLAUDE.md(SOT) + skills/(12+) + rules/ + worktrees/를 배치하고, 이 구조 위에서 22일간 **119 PR**을 실행했다.

**REODE** — GEODE를 포크한 뒤 GameIP 도메인을 전부 제거하고, DomainPort를 PipelineTemplate Protocol로 교체했다. `register_domain()`으로 코드 마이그레이션 파이프라인을 플러그인 등록. 동일한 AgenticLoop · Hook · Memory · Verification 인프라가 도메인 교체 후에도 그대로 작동한다.

---

### Loop

완성된 시스템을 측정하고, 병목이 보이면 부수고, 더 나은 구조로 다시 쌓는 루프.
프로젝트와 도메인은 바뀌어도 개발의 사이클은 동일하게 반복됩니다.

```
Plan → Build → Measure → Break → Rebuild → Share → (repeat)
```

| Project | Loop in Action |
|---------|---------------|
| **Eco²** | 완료율 0%의 Sync 구조에서 출발, Grafana/ELK 계측 결과를 근거로 아키텍처를 네 번 전환해 **VU 1,000 / 97.8%** 도달 |
| **GEODE** | 22일간 119 PR. 하루 5회 이상 Research→Implement→Verify→Merge 사이클을 실행하며 35K LOC의 에이전트를 단독 구축 |
| **REODE** | GEODE에서 도메인 레이어를 분리하고 PipelineTemplate Protocol로 재조립. 같은 인프라가 코드 마이그레이션 도메인에서 작동함을 실증 |

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
├── 2024.12-2025.08/  Rakuten Symphony Korea
│   └── PB급 분산 스토리지, 글로벌 팀 22-40명, 영어 기반
│
├── 2025.10-2026.02/  Eco² (5인 팀 Solo Backend & Infra)
│   └── AI Multi-Agent, 24-Node K8s, 새싹톤 4th/181
│
├── 2026.02-present/  GEODE (Solo)
│   └── 자율 실행 에이전트, 35K LOC, 2,366+ tests
│
└── 2026.03-present/  REODE @ Pinkx Lab (Freelance)
    └── Migration & Coding Core Agent
```

---

### Projects

| Year | Project | Role | Link |
|------|---------|------|------|
| 2026 | **REODE** — Migration & Coding Core Agent @ Pinkx Lab | AI R&D Freelance | `private` |
| 2026 | **GEODE** — 범용 자율 실행 에이전트, 35K LOC, 2,366+ tests | Solo Full-Stack | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) |
| 2026 | **LLMART** — CLI-based LLM-as-Judge Evaluation System | Solo | [mangowhoiscloud/llmart](https://github.com/mangowhoiscloud/llmart) |
| 2025 | **Eco²** — AI 재활용 Multi-Agent, 24-Node K8s, 새싹톤 4th/181 | 5인 팀 Solo Backend & Infra | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2025 | **Rakuten OStore v1.0.0** — PB급 오브젝트 스토리지 | Jr. Cloud Storage Dev | Rakuten Symphony |
| 2024 | **Rakuten Robin Storage v5.5.0** — 분산 스토리지, 2천만 유저 통신망 | Jr. Cloud Storage Dev | Rakuten Symphony |
| 2024 | **Aimo** — LLM 기반 법률 상담 앱 | Backend | [KTB16Team](https://github.com/KTB16Team) |
| 2024 | **Dream** — LLM + RAG 기반 꿈 해석 앱 | DevOps | [KakaoTech-Hackathon-Dream](https://github.com/KakaoTech-Hackathon-Dream) |
| 2024 | **Musinsa Product API** — 상품 API 개발 과제 | Backend | [mng990/musinsa-test](https://github.com/mng990/musinsa-test) |
| 2022 | **Fisher Market** — ERC-1155 기반 수산물 거래 DApp | Backend | [mng990/ethereum_FisheriesMarket](https://github.com/mng990/ethereum_FisheriesMarket) |

---

### Stack

**Lang** &nbsp;
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)

**AI** &nbsp;
![Claude](https://img.shields.io/badge/Claude-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangSmith](https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

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

**Harness** &nbsp;
![Claude Code Max](https://img.shields.io/badge/Claude_Code_Max_×20-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![Opus 4.6](https://img.shields.io/badge/Opus_4.6-D4A574?style=flat-square&logo=anthropic&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

---

<p align="center">
  <sub>매 바퀴마다 구조가 단단해지고, 그 과정 전체를 공개합니다.</sub>
</p>
