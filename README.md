<p align="right">
  <strong>🇰🇷 한국어</strong> · <a href="README_EN.md">🇺🇸 English</a>
</p>

<h1 align="center">류지환 (Jihwan Ryu)</h1>

<p align="center">
  <strong>모든 것을 루프로 만듭니다. 행동도, 검증도, 개선도.</strong><br/>
  확률적 시스템(LLM)은 제어 없이 발산합니다. 발산을 루프로 수렴시키는 하네스를 만듭니다.
</p>

<p align="center">
  <a href="https://github.com/mangowhoiscloud?tab=followers"><img src="https://img.shields.io/github/followers/mangowhoiscloud?label=Follow&style=social" alt="Follow"></a>&nbsp;
  <a href="https://www.youtube.com/@mango_fr"><img src="https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube"></a>
  <a href="https://rooftopsnow.tistory.com"><img src="https://img.shields.io/badge/Blog-FF5722?style=flat-square&logo=tistory&logoColor=white" alt="Blog"></a>
  <a href="https://linkedin.com/in/jihwan-ryu-b6b04a202"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/Self--Improving_Hub-6B4FBB?style=flat-square&logo=githubpages&logoColor=white" alt="Self-Improving Hub"></a>
</p>

---

### 🔁 Loops All the Way Down

루프가 제 개발의 아이덴티티입니다. 에이전트의 한 턴부터 저 자신의 성장까지, 모든 층위가 같은 모양으로 돕니다.
바깥 루프는 안쪽 루프가 만든 결과를 측정하고, 측정이 다음 안쪽 루프의 전제가 됩니다.

```
┌─ ⑤ Feedback Loop          시장·사용자·채용 과제 → 다음 빌드의 입력
│  ┌─ ④ Self-Improving Loop  행동 정량화 → 변이 제안 → 측정 게이트 → 채택/기각
│  │  ┌─ ③ Production Loop   plan → build → CI Ratchet → ship → share
│  │  │  ┌─ ② Verify Loop    generate → verify → reflect → replan
│  │  │  │  ┌─ ① Agentic Loop   while(tool_use): reason → act → observe
```

- **① Agentic Loop**: `while(tool_use)` 한 줄에서 시작해 ReAct, Plan-and-Execute, Reflexion을 품은 Cognitive Loop로 발전. 수렴 감지와 컨텍스트 복구가 장기 세션을 지탱
- **② Verify Loop**: 매 턴 경계에서 rule-based 점검이 결정론으로 돌고, 실패 시 verbal RL 힌트가 다음 라운드에 주입
- **③ Production Loop**: 빌드·테스트·보안을 통과한 변경만 전진(Ratchet). 통과 못 한 변경은 롤백 후 재시도. 반복 패턴은 스킬·훅으로 승격되어 다음 세션의 기본값이 됨
- **④ Self-Improving Loop**: 적대 시나리오 생성 → Anthropic Petri 행동 감사 → 무변이 대조군의 노이즈 밴드를 넘는 변이만 채택. 개선이 주장이 아니라 측정이 되도록
- **⑤ Feedback Loop**: 매 단계를 YouTube·블로그·공개 감사 번들로 공유하고(build-prove-share), 시장의 응답을 다음 루프의 입력으로 환류

### 🧠 Philosophy

**LLM은 현시대의 컴퓨팅입니다.** 연산의 단위가 명령어에서 토큰으로 옮겨 왔고, 추론 호출은 새로운 프로세스입니다.
프로세스가 늘어나며, 에이전트를 OS로 다루는 접근을 이어오고 있습니다.
도구를 부르는 손, 프로세스를 관리하는 스케줄러, 컨텍스트를 계층화하는 메모리, 위험한 호출 앞에 서는 권한 게이트.

**신뢰는 감정이 아니라 아키텍처입니다.** 
에이전트의 자기 보고를 믿지 않아 검증을 에이전트 바깥의 결정론 코드에 둡니다.
평가자도 믿지 않아 생성과 평가의 모델 패밀리를 가르고(cross-family judge), 단일 평가 층도 믿지 않아 직교 다층(Swiss Cheese)으로 겹칩니다.
GEODE의 경우, 안전/감사 시뮬레이터(Petri)로 검증 절차가 확장되었으며, 측정 품질을 높이고자 개선 곡선보다 노이즈 밴드와 대조군을 먼저 세웁니다.

**자율성은 평가가 따라잡는 속도만큼만 늘립니다.** temperature 0.1의 strict 챗봇에서 출발해 도구 호출 하나를 열 때마다
평가 층 하나를 얹었고, 코드 마이그레이션에서는 결정론의 영토(70%)를 먼저 긋고 LLM을 모호 지대(30%)에만 세웠습니다.

### 🛠️ Harness Engineering

| 축 | 역할 | 실천 |
|---|---|---|
| **Orchestration** | LLM 출력을 받아 다음 행동을 결정 | AgenticLoop `while(tool_use)`, SubGoal DAG, Sub-Agent 병렬 위임, Lane Queue |
| **Context & Memory** | 장기 세션의 컨텍스트를 계층·압축·복구 | 5-Tier Memory, 2-Phase Compaction, 200K Absolute Guard: 장기 세션 오버플로우 0회, Prompt Cache 정렬로 멀티턴 입력 토큰 ~80% 절감 |
| **Gateway** | 멀티 프로바이더를 단일 통제점으로 | Anthropic·OpenAI·Zhipu 단일 인터페이스, 4-Stage Failover, Circuit Breaker, Cross-Provider Dispatch, 토큰 단위 비용 추적 |
| **Verify** | 비결정론적 출력을 신뢰 수준으로 수렴 | 결정론 게이트 + LLM Judge + 드리프트 감지의 직교 다층, Cross-LLM 합의(Krippendorff α 기준) |
| **Observe & Improve** | 작동을 계측하고 개선을 측정으로 채택 | Hook 이벤트 버스, per-run transcript, Petri 행동 감사 + 측정 게이트(Self-Improving Loop) |

#### 🗺️ Harness Landscape · 4-Quadrant Positioning

```
                          Autonomous
                              ▲
                              │
           Q2                 │                Q1
      Minimal+Autonomous      │       Comprehensive+Autonomous
                              │
      · SWE-agent             │         ★ GEODE (+ Self-Improving)
      · Codex CLI       · Claude Code   · REODE (delivered)
      · AutoGen          (← 생산 도구)   · Devin · Manus
                              │         · OpenHands
                              │
  ◄───────────────────────────┼───────────────────────────────►
      Minimal                 │              Comprehensive
                              │
           Q3                 │                Q4
      Minimal+Assisted        │        Comprehensive+Assisted
                              │
      · Aider                 │         · Cursor · Copilot
      · Gemini CLI            │         · Eco² (Chat Harness)
      · CrewAI                │         · Kiki (Slack Governance)
                              │
                              ▼
                           Assisted
```

---

### 🚀 Projects

⚙️ **GEODE** · 에이전틱 루프 기반 자율 에이전트 하네스 · [repo](https://github.com/mangowhoiscloud/geode) · [portfolio](https://mangowhoiscloud.github.io/portfolio/geode)
탐색·리서치·시그널 수집에 특화한 장기 실행 시스템. 멀티 프로바이더 게이트웨이, 5-Tier 메모리,
4계층 도구 디스패치, HITL 권한 게이트를 SDK 런타임부터 단독 구축. 일상 업무를 자율 수행 중.

📈 **GEODE Self-Improving Loop** · 측정 게이트 기반 자기개선 폐회로 · [hub](https://mangowhoiscloud.github.io/geode/self-improving/) · [petri bundle](https://mangowhoiscloud.github.io/geode/petri-bundle/) · [video](https://www.youtube.com/watch?v=TuEOGQrO9Us)
적대 시나리오 생성(co-scientist 토폴로지) → Petri 다차원 행동 감사 → 무변이 대조군의 노이즈 밴드를 넘는 변이만 채택.
측정을 처음 돌리자 드러난 조용한 결함들(미발생 변이, 운 좋은 기준선)을 공개·정정하며, 개선 곡선보다 측정의 바닥을 먼저 세움.
감사 결과 전체를 외부 열람 가능한 정적 번들로 공개.

🔧 **REODE** · 코드 마이그레이션 자율 에이전트 @ pinxlab (프리랜스 납품)
GEODE 하네스를 코딩 에이전트 제품으로 재설계해 라이브 서비스의 Java 8→22, Spring Boot 2→3 마이그레이션을 납품.
OpenRewrite 결정론 70% + LLM 30% 분리, 검증을 우회하는 기망 행위를 5-Gate Scorecard로 차단,
동일 에러 40회 고착 장애를 explore_before_fix 의무화로 해소.

| Real-World Result (2026.03 납품) | |
|------|------|
| 대상 | 5,523 files (241 Java + 355 JSP + 47 XML), Java 1.8→22 · Spring 4→6 |
| 결과 | 83/83 tests + FE/BE E2E 검증 통과 |
| 실행 | 33 자율 세션 · 1,133 agentic rounds · 5h 48m (사람 개입 0) |

♻️ **Eco²** · AI 멀티에이전트 재활용 서비스 · [portfolio](https://mangowhoiscloud.github.io/portfolio/eco2) · 새싹톤 우수상 4th/181
EC2 14노드에서 시작해 Terraform·Ansible IaC와 ArgoCD 선언형으로 24-Node K8s를 단독 운영.
temperature 0.1 strict 챗봇을 툴콜링·LangGraph 병렬·SSE·Agent SDK로 상용 레벨 멀티에이전트로 디벨롭.
동시접속 0→1,000 VU 97.8%, 평가 품질 69.4→99.8/100(Swiss Cheese 3-Layer), 인증 핸들러 48→1,500 RPS.

💬 **Kiki** · Slack 행동 관측 기반 멀티 에이전트 거버넌스 @ pinxlab
CTO·PO·Lead·Dev·QA 계층 self-team이 실 운영 레거시를 자율 분석·구현·리뷰. 관리자는 Slack 대화만으로 지시·승인.
"보수적 PASS"를 2-stage gate가 시스템 레벨에서 차단.

🎮 **Crumb & Crumb Studio** · 멀티 호스트 에이전트 게임 제작 스튜디오 · [repo](https://github.com/mangowhoiscloud/crumb)
Claude Code·Codex·Gemini CLI를 공통 인터페이스로 추상화한 3-day spike. transcript.jsonl 단일 진실원 + pure reducer로
replay-deterministic 확보, 동일 프로바이더 평가 인플레이션을 cross-provider 배치로 차단.

---

### 🗓️ Timeline

```
mangowhoiscloud/
├── 2017.03-2023.08/  부산대학교 정보컴퓨터공학부 · B.S.
├── 2024.07-2024.11/  카카오테크 부트캠프 · Backend · DevOps · LLM
├── 2024.12-2025.08/  Rakuten Symphony Korea · Cloud Engineer (페타바이트 분산 스토리지, 글로벌 팀)
├── 2025.10-2026.02/  Eco² · MVP 5인 BE/Infra → E2E 단독 (24-Node K8s, 새싹톤 4th/181)
├── 2026.02-present/  GEODE · 자율 에이전트 하네스 (Solo)
├── 2026.03-2026.05/  REODE · Kiki @ pinxlab · 프리랜스 납품
├── 2026.05-present/  GEODE Self-Improving Loop · 측정 게이트 자기개선
└── 2026.05-present/  Crumb (3-day spike) · Cotton (설계)
```

---

### 🔗 Project Links

| Date | Project | Role | Link |
|------|---------|------|------|
| 2026.05-present | **Self-Improving Loop**: Petri 감사 × 측정 게이트 | Solo | [hub](https://mangowhoiscloud.github.io/geode/self-improving/) |
| 2026.05 | **Crumb**: 멀티 호스트 에이전트 스튜디오 | Solo | [mangowhoiscloud/crumb](https://github.com/mangowhoiscloud/crumb) |
| 2026.04-2026.05 | **Kiki**: Slack 행동 관측 기반 에이전트 조직 오케스트레이션 | Freelance | pinxlab |
| 2026.03-2026.04 | **REODE**: Migration & Coding Agent, forked from GEODE | Freelance | pinxlab |
| 2026.02-present | **GEODE**: 자율 에이전트 하네스 | Solo | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) |
| 2026.02 | **LLMART**: CLI 기반 LLM-as-Judge 평가 | Solo | [mangowhoiscloud/llmart](https://github.com/mangowhoiscloud/llmart) |
| 2025.10-2026.02 | **Eco²**: AI Multi-Agent, 24-Node K8s | BE/Infra → E2E | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2024.12-2025.08 | **Rakuten Robin Storage · Object Storage**: 분산 스토리지 | Cloud Engineer | Rakuten Symphony |
| 2024 | **Aimo**: LLM 갈등 중재 앱 | Backend | [KTB16Team](https://github.com/KTB16Team) |
