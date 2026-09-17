<p align="right"><strong>한국어</strong> · <a href="README_EN.md">English</a></p>

# 안녕하세요, 류지환입니다 👋

**아이디어를 작동하는 시스템으로, 한 번의 해결을 다음에도 쓸 수 있는 방법으로.**

분산 스토리지와 백엔드·인프라를 거쳐, 지금은 **AI 에이전트 런타임과 개발 워크플로우**를 만듭니다.
모델이 도구를 쓰게 하는 것에서 멈추지 않고, 실패를 복구하고 결과를 확인해 실제로 배포하는 과정까지 연결합니다.

“일단 돌아가네요”도 반갑지만, 제가 더 좋아하는 질문은 <strong>“왜 됐고, 다음에도 될까요?”</strong>입니다.
로그로 원인을 찾고, 작은 수정으로 고치고, 같은 문제는 다음에 테스트가 잡게 만드는 쪽을 좋아합니다.

[GEODE 둘러보기](https://mangowhoiscloud.github.io/geode/) · [기술 블로그](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

<p>
  <a href="https://github.com/mangowhoiscloud/geode/releases/latest"><img src="https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&amp;label=GEODE" alt="GEODE 최신 릴리스"></a>
  <a href="https://github.com/mangowhoiscloud/geode-eval-artifacts"><img src="https://img.shields.io/badge/Evidence-open%20records-5865F2?style=flat-square" alt="공개 평가 기록 보기"></a>
  <a href="https://github.com/mangowhoiscloud/compiler-ax-lab"><img src="https://img.shields.io/badge/Compiler%20AX-CPU%20tests-327A52?style=flat-square" alt="Compiler AX Lab의 범위가 명시된 CPU 검증 기록"></a>
</p>

[작업 방식](#how-i-work) · [대표 작업](#selected-work) · [개념 안내](#concepts) · [이력](#experience) · [더 둘러보기](#more)

<a id="how-i-work"></a>
## 저는 이렇게 일합니다

**먼저 좁힙니다.** 큰 코드를 바로 고치기보다, 실패한 입력과 실제 호출 경로부터 찾습니다. 무엇을 바꿀 수 있고 무엇은 그대로여야 하는지 정한 뒤, 문제를 재현할 가장 작은 확인 방법을 만듭니다.

**탐색은 모델과, 판정은 근거로 합니다.** 가설을 세우고 낯선 코드를 읽는 데 AI를 적극적으로 씁니다. 하지만 “고쳤다”는 말 대신 실행한 명령, 테스트 결과, 원본 로그를 봅니다. 테스트를 지워서 얻은 초록불은 해결이 아닙니다.

**한 번의 삽질을 다음 작업의 자산으로 남깁니다.** 알아낸 원인은 회귀 테스트로, 반복할 조사 순서는 짧은 지침과 Skill로 정리합니다. 긴 프롬프트 하나에 모든 경험을 넣기보다 필요한 순간에 찾아 쓰는 편을 택합니다.

**배포까지 닫되, 결과를 부풀리지는 않습니다.** 코드 수정, CI 통과, 병합, 설치·배포 확인은 각각 확인합니다. 실험이 동률이면 동률이라고 쓰고, CPU에서 확인한 결과를 장치 성능으로 포장하지 않습니다.

> 제가 만들고 싶은 자동화는 사람이 안 보는 자동화보다, **사람이 어디를 봐야 할지 분명한 자동화**에 가깝습니다.

<a id="selected-work"></a>
## 작업으로 소개할게요

### 🪨 GEODE — 도구를 쓰고, 결과를 남기는 에이전트

자연어로 맡긴 일을 계획하고 도구를 호출하는 **자율 에이전트 런타임**입니다. 장기 실행에 필요한 메모리, 여러 모델 제공자 연결, 도구 실행과 권한 확인을 단독으로 구축해 왔습니다.

**요즘 집중하는 것:** 실행하는 `core`, 확인하는 `evals`, 개선 후보를 실험하는 `evolve`의 경계를 분리하는 일입니다. 원본 실행 결과와 요약을 구분하고, 실패·미완료 호출도 기록에 남겨 “무엇이 실제로 일어났는지” 따라갈 수 있게 합니다.

**실험도 공개합니다:** SIL은 안전성, Crucible은 과제 수행 능력을 기준으로 변경 후보를 검사합니다. 여기서 바꾸는 것은 모델 가중치가 아니라 지침·도구 정책·Skill 같은 **모델 주변의 실행 구성**입니다. 지속적인 자기개선이 입증됐다는 뜻은 아닙니다.

[코드](https://github.com/mangowhoiscloud/geode) · [문서](https://mangowhoiscloud.github.io/geode/docs) · [실행·평가 기록](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [자기개선 실험실](https://mangowhoiscloud.github.io/geode/self-improving/)

### 🔬 Compiler AX Lab — AI의 수정안을 리뷰 가능한 변경으로

AI가 만든 코드를 “그럴듯한 답”이 아니라 **원인·변경·실행 증거를 연결한 작은 수정안**으로 넘기는 방법을 연구합니다. 공개 `furiosa-opt` SDK의 Rust 테스트와 Python 실행기를 다루는 독립 프로젝트이며, FuriosaAI 소속·승인 프로젝트는 아닙니다.

**확인한 것:** 2026-09-16 공개 CPU 기록에는 double-buffering 예제의 **46,080개 출력값 일치**, 워크스페이스의 **720개 일반 테스트·55개 doctest 통과**가 남아 있습니다. 서로 다른 실행의 수치를 하나의 점수로 더하지 않습니다.

**중요했던 배움:** A/B 파일럿의 대조 검사 결과는 동률이었습니다. B 수정안을 선택한 판단과 “B 절차가 더 효과적이다”라는 주장은 별개로 남겼습니다. CPU 값 검증은 NPU 정확성·실행 중첩·성능 검증을 대신하지 않습니다.

[코드와 검증 범위](https://github.com/mangowhoiscloud/compiler-ax-lab) · [회고 보고서](https://mangowhoiscloud.github.io/compiler-ax-lab/report.pdf)

### 🛠️ REODE @ pinxlab — 레거시 마이그레이션을 납품까지

GEODE에서 출발한 하네스를 코드 마이그레이션 제품으로 재설계했습니다. 규칙으로 바꿀 수 있는 부분은 OpenRewrite에 맡기고, 문맥 해석이 필요한 부분에 LLM을 사용했습니다. 같은 오류를 반복해서 고치려는 상황에는 **수정 전에 조사하는 절차**를 넣었습니다.

**2026.03 납품 기록:** Java 1.8→22·Spring 4→6 대상, **5,523개 파일** 규모의 서비스에서 **83/83 테스트와 프론트엔드·백엔드 종단 검증**을 통과했습니다. 기록된 실행은 33개 자율 세션·1,133라운드·5시간 48분이며, 해당 실행 중 사람 개입은 0회였습니다. 준비·설계·최종 검토까지 없었다는 뜻은 아닙니다.

클라이언트 코드는 비공개입니다. [공개해 온 납품 요약과 수치의 범위](docs/PROFILE_NOTES.md#reode)를 연결해 두었습니다.

### 🌱 Eco² — 챗봇에서 서비스 운영까지

재활용을 돕는 AI 서비스입니다. 5인 팀의 백엔드·인프라 담당으로 시작해 이후 고도화와 운영을 단독으로 이어갔습니다. 단순 챗봇을 도구 호출·LangGraph 병렬 처리·SSE 스트리밍을 갖춘 멀티에이전트 워크플로우로 발전시켰습니다.

**남긴 성과:** **2025 AI 새싹톤 우수상(4th/181)**, Terraform·Ansible·ArgoCD 기반 **24노드 Kubernetes 운영**. 공개 부하 기록은 Scan API **1,000 VU에서 97.8%**, 별도의 ext-authz 인증 경로 **2,500 VU에서 1,477 RPS**입니다. VU는 부하 시험의 가상 사용자이며 실제 이용자 수가 아닙니다.

서비스 운영은 종료됐고, 구조와 시행착오는 기술 포트폴리오로 남겼습니다.

[최신 기술 포트폴리오](https://mangowhoiscloud.github.io/eco2/) · [프로젝트 저장소](https://github.com/SeSACTHON/backend)

<details>
<summary><strong>그 밖에 만든 것들 — 협업, 번역, 게임 제작</strong></summary>

**Kiki @ pinxlab · 2026.04–05:** Slack에서 지시·승인하고, 여러 에이전트가 분석·구현·리뷰를 나눠 맡는 워크플로우입니다. 역할을 많이 만드는 것보다, 근거 없이 통과시키지 못하는 2단계 게이트에 집중했습니다.

**Cotton @ pinxlab · 2026.05:** RPG 스크립트 번역을 위한 single-tenant SaaS입니다. 대사를 낱개 문자열이 아니라 분기·조건·캐릭터 말투·자막 길이가 있는 대화 그래프로 모델링했습니다. LLM CLI 어댑터와 생성·평가 제공자 분리를 적용했습니다.

**[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb) · 2026.05:** 여러 CLI 에이전트를 하나의 인터페이스로 묶은 3일간의 게임 제작 스튜디오 실험입니다. `transcript.jsonl`과 순수 리듀서로 실행 기록을 재생하고, 생성과 평가의 제공자를 분리했습니다.

**[DREAM](https://github.com/KakaoTech-Hackathon-Dream) · 2024.09:** 노년층의 못 이룬 꿈을 생성형 AI 서사·이미지로 풀어낸 카카오테크 해커톤 서비스입니다. 백엔드·AI·인프라 작업에 참여했습니다.

**[Aimo](https://github.com/KTB16Team) · 2024:** LLM 기반 갈등 중재 앱의 백엔드를 개발했습니다.

</details>

<a id="concepts"></a>
## 낯선 단어는 여기서 잠깐

제가 자주 쓰는 말들이지만, 처음부터 알고 오실 필요는 없습니다.

**에이전트**는 답변만 하는 대신 도구를 써서 일을 진행하는 프로그램입니다. **하네스**는 그 주변에서 도구·메모리·권한·실패 처리를 관리하는 실행 장치입니다. 모델이 무엇을 할지 제안한다면, 하네스는 무엇을 실행하고 어떻게 확인할지 맡습니다.

```text
일을 하는 루프: 목표 → 도구 실행 → 결과 확인 → 다음 행동
개선하는 루프: 변경 후보 → 같은 조건의 검사 → 채택 / 기각
```

<details>
<summary><strong>Skill, 회귀 테스트, 래칫, 자기개선도 궁금하다면</strong></summary>

**Skill:** 특정 일을 할 때 꺼내 읽는 작업 안내서입니다. 예를 들어 “호출 경로를 찾고, 실패를 재현한 뒤 수정하자”는 조사 순서를 담습니다. 파일이 있다는 것만으로 효과가 입증되지는 않아, 실제로 읽고 쓴 다음 작업에서 확인해야 합니다.

**회귀 테스트:** 고친 문제가 다시 생겼을 때 알려주는 검사입니다. 해결한 버그를 다음에도 기억해 주는 장치라고 생각하면 쉽습니다.

**래칫(ratchet):** 좋아진 기준이 뒤로 밀리지 않게 하는 장치입니다. 검사가 느려졌을 때 통과 기준부터 느슨하게 바꾸지 않고, 느려진 원인을 먼저 찾는 식입니다.

**평가 게이트:** 결과를 채택하기 전에 통과해야 하는 조건입니다. 생성한 에이전트의 자신감보다 독립된 검사 결과를 우선합니다. LLM 심판도 보조 수단이지, 언제나 맞는 정답지는 아닙니다.

**자기개선:** 같은 답을 여러 번 고치는 것과, 변경을 보존해 다음 작업에서 재사용하는 것은 다릅니다. GEODE에서는 모델 주변 구성을 바꾸는 실험을 합니다. 변경이 채택됐는지와 반복해서 더 좋아졌는지도 따로 확인합니다.

[GEODE의 두 루프 설명](https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops) · [실험 결과를 읽는 기준](https://github.com/mangowhoiscloud/geode-eval-artifacts)

</details>

<a id="experience"></a>
## 지나온 길

| 기간 | 경험 |
| --- | --- |
| 2026.09 | **Compiler AX Lab** · 공개 CPU 테스트·개발 워크플로우 연구 기록 |
| 2026.02–현재 | **GEODE** · 단독 개발. SIL 실험 2026.05–06, Crucible 2026.07–현재 |
| 2026.03–05 | **pinxlab** · 프리랜스 · REODE, Kiki, Cotton 납품 |
| 2025.10–2026.02 | **Eco²** · 5인 MVP의 백엔드·인프라 → 단독 고도화·운영 · 2025 AI 새싹톤 우수상 |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer - Storage Developer · 정규직 · 글로벌 팀에서 PB 규모 분산 스토리지 개발 |
| 2024.07–11 | **카카오테크 부트캠프** · 백엔드·DevOps·LLM · DREAM 해커톤 프로젝트 |
| 2017.03–2023.08 | **부산대학교 정보컴퓨터공학부** · 학사 |

Rakuten에서는 C·Kubernetes 기반 스토리지 개발에 참여했습니다. 기존 이력의 **Rakuten Cloud Native Platform - Storage Server v5.5.0 · Rakuten Storage v1.0.0** 경험도 이 시기에 해당합니다.

<a id="more"></a>
## 코드 밖의 기록도 남깁니다

구현하며 배운 것은 [블로그](https://rooftopsnow.tistory.com)에, 실행 과정과 설명은 [YouTube](https://www.youtube.com/@mango_fr)에 남깁니다.
에이전트가 이상하게 행동한 순간, 오래된 시스템을 고친 경험, 결과를 검증하는 방법에 관한 이야기를 환영합니다.

[LinkedIn에서 이야기하기](https://linkedin.com/in/jihwan-ryu-b6b04a202) · 이전 GitHub 계정: [@mng990](https://github.com/mng990)

---

<sub>내용 검토: 2026-09-17 · <a href="docs/PROFILE_NOTES.md">수치의 출처·범위와 업데이트 원칙</a> · 릴리스 배지는 최신 버전 링크이며, 프로필 검사는 프로젝트 성능 인증이 아닙니다.</sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
