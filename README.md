<p align="right"><strong>한국어</strong> · <a href="README_EN.md">English</a></p>

# 류지환

**실행을 검증 가능한 시스템으로 만들고, 그 결과를 다음 탐색의 입력으로 돌립니다.**

분산 스토리지와 백엔드, 클라우드 인프라를 거쳐 현재는 **자율 에이전트 런타임과 RSI(Recursive Self-Improvement) 방법론**을 다룹니다. 모델의 한 번의 성공보다 실행 과정이 관찰 가능하고 재현 가능한지, 그리고 그 결과가 다음 실험의 재료로 남는지를 중요하게 봅니다.

개별 실행은 명확한 범위와 검증 조건 안에서 닫습니다. 반면 탐색 공간은 닫지 않습니다. 프롬프트만 조정하는 대신 문제 분해, 컨텍스트 구성, 도구 정책, Skill, 평가 방식, 에이전트 역할, 사람의 개입 지점까지 방법론 자체를 탐색 대상으로 둡니다.

[GEODE](https://mangowhoiscloud.github.io/geode/) · [기술 블로그](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

<p>
  <a href="https://github.com/mangowhoiscloud/geode/releases/latest"><img src="https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&amp;label=GEODE" alt="GEODE 최신 릴리스"></a>
  <a href="https://github.com/mangowhoiscloud/geode-eval-artifacts"><img src="https://img.shields.io/badge/Evidence-open%20records-555555?style=flat-square" alt="공개 평가 기록"></a>
  <a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/RSI-scaffold%20search-555555?style=flat-square" alt="RSI 실행 구성 탐색"></a>
  <a href="https://github.com/mangowhoiscloud/geode"><img src="https://img.shields.io/badge/Autonomous%20Agents-runtime-555555?style=flat-square" alt="자율 에이전트 런타임"></a>
  <a href="https://mangowhoiscloud.github.io/eco2/"><img src="https://img.shields.io/badge/Cloud-Kubernetes%20%7C%20IaC-555555?style=flat-square" alt="Kubernetes와 IaC 클라우드 엔지니어링"></a>
</p>

[작업 방식](#how-i-work) · [대표 작업](#selected-work) · [개념](#concepts) · [이력](#experience) · [기록](#more)

<a id="how-i-work"></a>
## 작업 방식

**먼저 문제와 검증 범위를 좁힙니다.** 큰 코드를 바로 고치기보다 실패한 입력과 실제 호출 경로를 찾습니다. 무엇을 바꿀 수 있고 무엇을 보존해야 하는지 정한 뒤, 문제를 재현할 가장 작은 검사를 만듭니다.

**탐색에는 모델을 사용하고 판정에는 근거를 사용합니다.** 가설을 세우고 낯선 코드를 읽는 데 AI를 적극적으로 활용하지만, 수정의 성립 여부는 실행한 명령, 테스트 결과, 원본 로그로 판단합니다. 테스트를 약화해 얻은 통과는 해결로 보지 않습니다.

**결과를 다음 탐색의 데이터로 남깁니다.** 성공한 변경뿐 아니라 실패한 시도, 기각된 가설, 실행 궤적과 평가 결과를 보존합니다. 알아낸 원인은 회귀 테스트로, 반복할 조사 과정은 짧은 지침과 Skill로 정리합니다. 이 기록은 다음 후보를 만들고 탐색 공간을 조정하는 입력이 됩니다.

**방법론 자체를 탐색 공간으로 둡니다.** 문제 분해, 컨텍스트, 도구 선택, 검증 순서, Skill, 에이전트 역할, 평가자 구성과 사람의 개입 지점까지 변경 후보가 될 수 있습니다. 하나의 방법을 정답으로 고정하기보다 같은 조건에서 다시 측정하고, 결과에 따라 다음 탐색 방향을 정합니다.

**개별 실행은 유한하게 닫고 탐색 공간은 닫지 않습니다.** 코드 수정, CI, 병합, 설치와 배포는 각각 확인합니다. 실험이 동률이면 동률로 남기고, CPU에서 확인한 결과를 장치 성능으로 확대하지 않습니다.

```text
가설 → 실행 → 관찰 → 검증 → 기록
 ↑                         │
 └──── 다음 후보와 방법론 ←┘
```

<a id="selected-work"></a>
## 대표 작업

### GEODE

자연어로 맡긴 일을 계획하고 도구를 호출하는 **자율 에이전트 런타임**입니다. 장기 실행에 필요한 메모리, 여러 모델 제공자 연결, 도구 실행과 권한 경계를 단독으로 구축해 왔습니다.

현재는 실행을 담당하는 `core`, 평가와 증거 생산을 담당하는 `evals`, 변경 후보를 탐색하는 `evolve`를 분리합니다. 원본 실행 결과와 요약을 구분하고 실패와 미완료 호출도 기록에 남깁니다. 평가 결과와 trajectory는 단순 보관물이 아니라 이후 분석, 학습 뷰, 다음 실험 설계의 입력으로 사용합니다.

SIL은 안전성 관련 행동을, Crucible은 과제 수행 능력을 기준으로 변경 후보를 검사합니다. 여기서 바꾸는 것은 모델 가중치가 아니라 시스템 지침, 도구 정책, Skill, 작업 분해와 같은 **모델 주변의 실행 구성**입니다. 이 작업을 RSI의 한 형태인 비파라메트릭 scaffold 탐색으로 다루되, 지속적인 자기개선이 입증됐다고 전제하지 않습니다.

[코드](https://github.com/mangowhoiscloud/geode) · [문서](https://mangowhoiscloud.github.io/geode/docs) · [실행과 평가 기록](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [RSI 실험](https://mangowhoiscloud.github.io/geode/self-improving/)

### Compiler AX Lab

AI가 만든 코드를 그럴듯한 답이 아니라 **원인, 변경, 실행 증거를 연결한 검토 가능한 수정안**으로 넘기는 방법을 연구합니다. 공개 `furiosa-opt` SDK의 Rust 테스트와 Python 실행기를 다루는 독립 프로젝트이며 FuriosaAI 소속 또는 승인 프로젝트는 아닙니다.

2026-09-16 공개 CPU 기록에는 double-buffering 예제의 **46,080개 출력값 일치**, 워크스페이스의 **720개 일반 테스트와 55개 doctest 통과**가 남아 있습니다. 서로 다른 실행의 수치를 하나의 점수로 합치지 않습니다.

A/B 파일럿의 대조 검사 결과는 동률이었습니다. B 수정안을 선택한 판단과 B의 절차가 더 효과적이라는 주장은 별개로 남겼습니다. CPU 값 검증은 NPU 정확성, 실행 중첩, 성능 검증을 대신하지 않습니다.

[코드와 검증 범위](https://github.com/mangowhoiscloud/compiler-ax-lab) · [회고 보고서](https://mangowhoiscloud.github.io/compiler-ax-lab/report.pdf)

### REODE @ pinxlab

GEODE에서 출발한 하네스를 코드 마이그레이션 제품으로 재설계했습니다. 규칙으로 처리할 수 있는 부분은 OpenRewrite에 맡기고 문맥 해석이 필요한 부분에 LLM을 사용했습니다. 같은 오류를 반복해서 수정하려는 상황에는 수정 전에 조사하는 절차를 넣었습니다.

**2026.03 납품 기록:** Java 1.8→22, Spring 4→6 대상의 **5,523개 파일** 규모 서비스에서 **83/83 테스트와 프론트엔드, 백엔드 종단 검증**을 통과했습니다. 기록된 실행은 33개 자율 세션, 1,133라운드, 5시간 48분이며 해당 실행 중 사람 개입은 0회였습니다. 준비, 설계, 최종 검토까지 없었다는 의미는 아닙니다.

클라이언트 코드는 비공개입니다. [공개해 온 납품 요약과 수치의 범위](docs/PROFILE_NOTES.md#reode)를 별도로 기록했습니다.

### Eco²

재활용을 돕는 AI 서비스입니다. 5인 팀의 백엔드와 인프라 담당으로 시작해 이후 고도화와 운영을 단독으로 이어갔습니다. 단순 챗봇을 도구 호출, LangGraph 병렬 처리, SSE 스트리밍을 갖춘 멀티에이전트 워크플로우로 발전시켰습니다.

**주요 기록:** **2025 AI 새싹톤 우수상(4th/181)**, Terraform, Ansible, ArgoCD 기반 **24노드 Kubernetes 운영**. 공개 부하 기록은 Scan API **1,000 VU에서 97.8%**, 별도의 ext-authz 인증 경로 **2,500 VU에서 1,477 RPS**입니다. VU는 부하 시험의 가상 사용자이며 실제 이용자 수가 아닙니다.

서비스 운영은 종료됐고 구조와 시행착오는 기술 포트폴리오로 남겼습니다.

[기술 포트폴리오](https://mangowhoiscloud.github.io/eco2/) · [프로젝트 저장소](https://github.com/SeSACTHON/backend)

<details>
<summary><strong>그 밖의 작업</strong></summary>

**Kiki @ pinxlab · 2026.04–05:** Slack에서 지시와 승인을 받고 여러 에이전트가 분석, 구현, 리뷰를 나눠 맡는 워크플로우입니다. 역할의 수보다 근거 없는 승인을 차단하는 2단계 게이트에 집중했습니다.

**Cotton @ pinxlab · 2026.05:** RPG 스크립트 번역을 위한 single-tenant SaaS입니다. 대사를 낱개 문자열이 아니라 분기, 조건, 캐릭터 말투, 자막 길이가 있는 대화 그래프로 모델링했습니다. LLM CLI 어댑터와 생성, 평가 제공자 분리를 적용했습니다.

**[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb) · 2026.05:** 여러 CLI 에이전트를 하나의 인터페이스로 묶은 게임 제작 스튜디오 실험입니다. `transcript.jsonl`과 순수 리듀서로 실행 기록을 재생하고 생성과 평가의 제공자를 분리했습니다.

**[DREAM](https://github.com/KakaoTech-Hackathon-Dream) · 2024.09:** 노년층의 못 이룬 꿈을 생성형 AI 서사와 이미지로 풀어낸 카카오테크 해커톤 서비스입니다. 백엔드, AI, 인프라 작업에 참여했습니다.

**[Aimo](https://github.com/KTB16Team) · 2024:** LLM 기반 갈등 중재 앱의 백엔드를 개발했습니다.

</details>

<a id="concepts"></a>
## 개념

**에이전트**는 답변만 생성하는 대신 도구를 사용해 작업을 진행하는 프로그램입니다. **하네스**는 그 주변에서 도구, 메모리, 권한, 실패 처리를 관리하는 실행 계층입니다. 모델이 행동을 제안한다면 하네스는 무엇을 실행하고 어떻게 검증할지 담당합니다.

**RSI(Recursive Self-Improvement)**는 이전 실행에서 얻은 결과를 이후 변경과 실험의 입력으로 되돌리는 재귀적 개선 문제를 가리킵니다. GEODE에서는 모델 가중치를 직접 학습시키는 대신 실행 구성을 탐색합니다. 변경의 채택과 반복적인 개선은 별개의 증거를 요구합니다.

```text
작업 루프: 목표 → 도구 실행 → 결과 확인 → 다음 행동
탐색 루프: 후보 → 평가 → 기록 → 다음 후보와 탐색 전략
```

<details>
<summary><strong>검증과 탐색에 사용하는 개념</strong></summary>

**Skill:** 특정 작업에서 필요할 때 불러오는 작업 지침입니다. 파일이 존재한다는 사실만으로 효과가 입증되지는 않으며 실제 작업에서 사용한 뒤 다시 평가해야 합니다.

**회귀 테스트:** 해결한 문제가 다시 발생하는지를 확인하는 검사입니다.

**래칫(ratchet):** 이미 확보한 검증 기준이 조용히 낮아지지 않도록 하는 장치입니다.

**평가 게이트:** 결과를 채택하기 전에 통과해야 하는 조건입니다. 생성한 에이전트의 자기 평가보다 독립된 검사를 우선하며 LLM 심판도 보조 수단으로 취급합니다.

**탐색 공간:** 변경 후보가 될 수 있는 모든 선택의 집합입니다. 프롬프트뿐 아니라 문제 분해, 컨텍스트, 도구 정책, Skill, 역할 구성, 평가 방법과 사람의 개입 지점까지 포함합니다.

[GEODE의 두 루프](https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops) · [평가 기록](https://github.com/mangowhoiscloud/geode-eval-artifacts)

</details>

<a id="experience"></a>
## 이력

| 기간 | 경험 |
| --- | --- |
| 2026.09 | **Compiler AX Lab** · 공개 CPU 테스트와 개발 워크플로우 연구 기록 |
| 2026.02–현재 | **GEODE** · 단독 개발. SIL 실험 2026.05–06, Crucible 2026.07–현재 |
| 2026.03–05 | **pinxlab** · 프리랜스 · REODE, Kiki, Cotton 납품 |
| 2025.10–2026.02 | **Eco²** · 5인 MVP의 백엔드와 인프라에서 단독 고도화와 운영으로 확장 · 2025 AI 새싹톤 우수상 |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer, Storage Developer · 정규직 · 글로벌 팀에서 PB 규모 분산 스토리지 개발 |
| 2024.07–11 | **카카오테크 부트캠프** · 백엔드, DevOps, LLM · DREAM 해커톤 프로젝트 |
| 2017.03–2023.08 | **부산대학교 정보컴퓨터공학부** · 학사 |

Rakuten에서는 C와 Kubernetes 기반 스토리지 개발에 참여했습니다. 기존 이력의 **Rakuten Cloud Native Platform, Storage Server v5.5.0 · Rakuten Storage v1.0.0** 경험도 이 시기에 해당합니다.

<a id="more"></a>
## 기록

구현과 실험에서 얻은 내용은 [블로그](https://rooftopsnow.tistory.com)와 [YouTube](https://www.youtube.com/@mango_fr)에 정리합니다. 실행 기록과 실패 사례를 포함해 이후 작업에서 다시 사용할 수 있는 형태로 남기는 것을 선호합니다.

[LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202) · 이전 GitHub 계정: [@mng990](https://github.com/mng990)

---

<sub>내용 검토: 2026-09-17 · <a href="docs/PROFILE_NOTES.md">수치의 출처, 범위와 업데이트 원칙</a> · 릴리스 배지는 최신 버전 링크이며 프로필 검사는 프로젝트 성능 인증이 아닙니다.</sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
