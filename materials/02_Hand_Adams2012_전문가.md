# [Hand 원고 2] Adams 2012로 읽는 ACL 재건술 후 기준 기반 재활

C.C 작성 · 2026-11-18 · 전문가용 · 에이온 원고 3개를 한 편으로 합쳐 다시 씀

- 원문(에이온): `library/adams-2012-acl-criterion-based.html`(논문 리뷰), `adams-2012-acl-protocol.html`(실무 가이드), `adams-acl-rehabilitation.html`(짧은 안내). 세 원문은 를르슈가 `source-originals/`에 보존합니다.
- 이 글은 원문에 몇 줄 고치는 방식이 아니라 **새로 쓴 본문**입니다. 아래 「본문」을 그대로 Hand 리더 형식(HTML)으로 옮겨 주세요.
- **표지 이미지 없음.** Hand 규칙상 주제에 맞는 표지가 필요합니다. 만들기 전에 재필님께 참고 이미지를 먼저 받습니다(원고 1의 `acl-cover.webp`를 같이 써도 되는지도 함께 여쭙니다).

---

## 1. editorial-spec 항목

```json
{
  "slug": "adams-2012-acl-criterion-based",
  "title": "Adams 2012로 읽는 ACL 재건술 후 기준 기반 재활",
  "subtitle": "주차는 안내선, 진행은 기준 — 원 논문에 있는 것과 없는 것",
  "description": "Delaware 그룹의 ACL 재건술 후 재활 지침(Adams 2012)을 단계별 기준, LSI 계산, 동반 수술 수정 사항으로 정리했습니다. 원 논문에 없는 후기 복귀 기준은 후속 근거로 구분했습니다.",
  "audience": "pro",
  "primary": "return",
  "topics": ["return", "knee", "assessment"],
  "image": "(재필님 참고 이미지 받은 뒤 결정)",
  "imageAlt": "(표지 확정 후)",
  "imageCredit": "(표지 확정 후)",
  "sourceType": "전문가용 논문 리뷰 · Current Concepts 해설",
  "review": "에이온 원고 3편을 합쳐 다시 썼습니다. 단계별 기준 숫자는 PMC 공개 원문(PMC3576892) 본문과 대조했고, 본문에서 확인하지 못한 기준(12주 hop >85%, KOS-Sports >70%)은 넣지 않았습니다. 2012년 이후 근거는 따로 표시했습니다.",
  "summary": [
    "Adams 2012의 주차는 안내선이고, 다음 단계는 기준을 모두 통과했을 때만 넘어갑니다.",
    "1주 0–90°, 2주 굴곡 110° 초과·KOS-ADL 65% 초과, 대퇴사두근 지수 60%·80%·90%가 단계마다 쓰입니다.",
    "반월상연골 봉합·이식건·재수술은 별도 수정 사항이 있고, 후기 복귀 판단은 후속 근거로 보완해야 합니다."
  ],
  "changes": [
    "에이온 논문 리뷰·실무 가이드·짧은 안내 3편을 한 편으로 통합",
    "원 논문 본문에서 확인한 기준만 남기고, 확인하지 못한 숫자 2개 제외",
    "원 논문에 없는 3–9개월 이후 단계를 ‘후속 근거’ 절로 분리",
    "센터 기록 틀·상담 문구를 일반 임상 기록 예시로 바꿈"
  ],
  "relatedIds": [
    "aon-adams-acl-rehabilitation",
    "ami-clinical-reasoning-20261011",
    "hamstring-return-20261012"
  ]
}
```

> relatedIds 마지막 항목은 Hand의 햄스트링 복귀 글 id로 짐작해서 적었습니다. 실제 id로 맞춰 주세요.

---

## 2. 본문

### 먼저 정확히 읽기

Adams 등(2012)은 Delaware 대학 그룹이 1996년에 낸 ACL 재건술 후 기준 기반 재활 지침을 당시 근거에 맞춰 다시 정리한 **Current Concepts 논문**입니다. 새로 환자를 모은 임상시험이 아니므로 치료군·대조군의 효과크기를 제시하지 않습니다. 이 글의 숫자는 「이 기준이 더 낫다」는 효과 추정치가 아니라, 한 임상 체계가 쓰는 **진행 관문**입니다.[1]

| 항목 | 내용 |
|---|---|
| 원 논문 | Current Concepts for Anterior Cruciate Ligament Reconstruction: A Criterion-Based Rehabilitation Progression |
| 저자 | Douglas Adams, David Logerstedt, Airelle Hunter-Giordano, Michael J. Axe, Lynn Snyder-Mackler |
| 학술지 | J Orthop Sports Phys Ther. 2012;42(7):601–614 |
| 식별자 | DOI 10.2519/jospt.2012.3871 · PMID 22402434 · PMC3576892 |

핵심 문장은 하나입니다. 주차는 치료사를 돕는 안내로 붙어 있지만, **기간과 상관없이 모든 임상 기준을 통과해야 다음 단계로 넘어갑니다.**[1]

### 기본 전제: 단독 ACL 재건술

아래 단계표는 동반 수술이 없는 단독 재건술을 기준으로 합니다. 반월상연골 봉합, 연골 수술, 인대 동반 손상, 재수술이 있으면 뒤의 「수정 사항」을 먼저 확인합니다. 수술기록과 집도의의 제한이 항상 우선입니다.[1]

### 단계별 통과 기준 (원 논문 본문 기준)

| 단계 | 통과 기준 | 이 단계에서 주로 하는 일 |
|---|---|---|
| 수술 전 | 완전 신전, 부종 없음 또는 최소, SLR 신전 지연(lag) 없음. 대퇴사두근 지수 90% 초과를 목표로 함 | 신전 회복, 부종 관리, 섭동 훈련과 대퇴사두근 강화 |
| 1주 (직후) | 능동·수동 ROM 0–90°, 슬개골 상방 활주를 동반한 능동 대퇴사두근 수축 | 신전 회복, NMES, 대퇴사두근 활성화. 2주까지 완전 신전이 안 되면 prone hang 같은 저부하 장시간 신장 |
| 2주 (초기) | 굴곡 110° 초과, 목발 없이 보행, 자전거·계단 기구 사용, 완전 신전 보행, 교대 계단, SLR lag 없음, KOS-ADL 65% 초과 | 통증 없는 범위(보통 0–60°)의 체중지지 운동(wall slide, step-up) |
| 중간 | 굴곡이 반대쪽과 10° 이내, 대퇴사두근 지수 60% 초과 | 균형·신경근 재교육 시작 |
| 후기 | 대퇴사두근 지수 80% 초과, 정상 보행, 완전 ROM, 부종 trace 이하 | 근력 운동 강도·시간 증가 |
| 전환 | 수술 후 8주 이상 + 대퇴사두근 지수 80% + 부종 trace 이하 + soreness rule 이해 → 달리기 진행 시작 | 3.2km(2마일) 걷기·조깅 교대로 시작해 비율·거리·속도를 단계적으로 늘림 |
| 기능검사 | 빠르면 12주부터. 대퇴사두근 지수 80% 이상, 부종 trace 이하, 완전 ROM, 한발 뛰기 통증 없음 | single·crossover·triple hop, 6m timed hop |
| 복귀 기준 | 대퇴사두근 지수와 기능검사 LSI 90%, 자기보고 척도 2개도 90% 기준 | 연습 참여부터 시작해 경기로 단계적으로 진행 |

KOS-ADL 65%는 이 그룹 환자의 2주차 중앙값(64%)을 근거로 정한 값이라고 원 논문이 밝힙니다. 연구로 검증된 절단점이 아니라 임상 자료에서 정한 기준입니다.[1]

열린사슬 운동은 피하지 않습니다. 원 논문은 체중지지·비체중지지 운동을 함께 쓰되, 비체중지지 무릎 펴기는 90°→45° 범위로 시작해 12주까지 90°→10°로 넓히도록 안내합니다.[1]

### LSI 계산과 해석

| 검사 종류 | 공식 | 예시 |
|---|---|---|
| 값이 클수록 좋은 검사(근력, hop 거리) | LSI(%) = 수술측 ÷ 반대측 × 100 | 수술측 32kg, 반대측 40kg → 80% |
| 시간이 짧을수록 좋은 검사(6m timed hop) | LSI(%) = 반대측 시간 ÷ 수술측 시간 × 100 | 반대측 2.4초, 수술측 3.0초 → 80% |

LSI 90%라도 양쪽이 모두 약하면 「대칭이지만 약한 상태」일 수 있습니다. Wellsandt 등(2017)은 70명에서 수술 후 6개월 LSI가 수술 전 반대측 기준(EPIC)보다 무릎 기능을 과대평가했다고 보고했습니다.[2] 가능하면 수술 전 값, 체중 대비 근력, 종목 기준치를 함께 봅니다.

hop 거리만으로 통과를 정하지 않습니다. 착지 후 균형, 동적 외반, 몸통 기울기, 뻣뻣한 착지와 두려움을 같이 기록하고, 반대발 짚기·손 짚기·균형 상실은 무효 시도로 처리합니다. 이 부분은 원 논문의 숫자가 아니라 임상 기록 원칙입니다.

### 동반 수술·이식건별 수정 사항 (원 논문)

| 상황 | 원 논문의 수정 |
|---|---|
| 반월상연골 봉합 동반 | 4주간 무릎 45° 넘는 굴곡에서 체중지지 금지(완전 신전 체중지지는 제한 없음). 이후 체중지지 굴곡은 90° 미만. 8주 뒤 일반 ACL 지침으로 복귀 |
| 부분 반월상연골 절제 동반 | 집도의 지시가 없으면 별도 수정 없음 |
| 햄스트링 자가건 | 12주까지 저항 햄스트링 운동을 하지 않음 |
| 슬개건(BPTB) 자가건 | 대퇴사두근 강화 중 슬개건 통증 관찰 |
| 동종건 | 초기 회복이 빨라 조기 복귀 위험. 단계 기준을 똑같이 모두 통과해야 진행 |
| 수술 전 ACL+MCL 동반 손상 | 4–6주간 시상면 운동으로 제한 |
| 재수술(revision) | 목발·보조기 2주 추가, 달리기 12주·기능검사 16주로 늦춤 |
| 연골 수술·반월상연골 이식 | 수술마다 다름. 가장 보수적인 지침을 따르거나 이 지침 적용 범위 밖 |

반월상연골 봉합 후 재활은 2025년 EU-US 합의문이 수술 형태에 따라 시간 기준과 기준 기반을 함께 쓰도록 권고합니다. 2012년 수정 사항을 그대로 쓰기 전에 최신 합의문과 집도의 지침을 확인합니다.[3]

### 막혔을 때 먼저 볼 것

| 문제 | 먼저 확인 | 우선 대응 |
|---|---|---|
| 완전 신전이 안 나옴 | 통증·부종, 햄스트링 방어 수축, 슬개골 가동성 | prone hang, heel prop, 슬개골 가동술, 보행 큐 |
| SLR lag가 남음 | 대퇴사두근 수축의 질, 부종 | NMES, quad set, 부종 관리 |
| 운동 뒤 붓기 증가 | 운동량·강도·보행량 | 24–48시간 부하 감량, ROM·활성화 단계로 후퇴 |
| 대퇴사두근 지수 60%·80%에 정체 | 관절성 근억제(AMI), 강도 부족 또는 과다 | NMES, 등척성 운동, 점진 저항, 회복 반응 확인 |
| hop 수치는 좋은데 착지가 나쁨 | 전두면 외반, 몸통 기울기, 고관절 전략 | step-down, 착지·감속 과제를 낮은 난도부터 |

관절성 근억제는 수술 후 신경계 억제로 대퇴사두근을 충분히 수축하지 못하는 현상입니다. 원 논문은 NMES가 운동 단위를 직접 동원해 수의적 운동만 할 때보다 근력 향상이 크다고 설명합니다.[1][4]

### 원 논문에 없는 것: 후기 복귀 판단은 후속 근거로

에이온 원문에는 「3–6개월」「6–9개월+」 단계가 함께 정리돼 있었지만, 이 부분은 Adams 2012 본문에 있는 단계가 아닙니다. 2012년 이후 근거로 다음을 보완합니다.

- **복귀는 연속 과정입니다.** Panther 합의문은 참여 → 종목 복귀 → 수행 회복으로 이어지는 과정으로 정의하고, 시간만으로 정하는 복귀를 버려야 한다고 합니다.[5]
- **9개월 전 복귀와 재손상.** Beischer 등(2020)은 15–30세 159명에서 9개월 전 고부하 스포츠 복귀가 두 번째 ACL 손상 위험비 6.7(95% CI 2.6–16.7)과 관련됐다고 보고했습니다. 관찰연구이며 9개월이 지나면 안전하다는 뜻은 아닙니다.[6]
- **LSI 단독의 한계.** Simonsson 등(2025)은 233명에서 근력·hop LSI만으로 복귀 후 2년 내 재손상 여부를 구분하지 못했다고 보고했습니다.[7]
- **최신 지침.** Aspetar 지침(2023)은 근력·움직임 조절 훈련과 달리기·복귀 기준을 정리하면서, 다수 기준이 전문가 의견으로 보완된 것임을 밝힙니다.[8]

### 매 세션 기록 예시

| 항목 | 기록 예시 |
|---|---|
| 오늘 상태 | 통증, 열감, 부종 등급, 지난 세션 뒤 24시간 반응 |
| ROM | 신전 0° / 굴곡 125°, 끝 느낌 |
| 대퇴사두근 활성 | SLR lag 유무, quad set의 질, NMES 필요 여부 |
| 근력 | 무릎 신전 kg, 햄스트링 kg, LSI |
| 기능 | step-down, 한발 스쿼트, pogo·hop, 보행·달리기 반응 |
| 진행 판단 | 통과 / 유지 / 후퇴와 그 기준 |
| 다음 목표 | 예: 대퇴사두근 지수 70%, 부종 trace 유지 |

### 이 글의 한계

- Adams 2012는 한 임상 그룹의 진행 체계를 정리한 Current Concepts 논문입니다. 기준 숫자 대부분은 효과를 비교한 연구에서 나온 값이 아닙니다.
- 원 논문 부록 표의 일부 기준(예: 단계별 hop·자기보고 절단점)은 이번에 대조하지 못해 넣지 않았습니다.
- 개인의 진단·수술 후 처방·복귀 허가를 대신하지 않습니다.

### 참고문헌

1. Adams D, Logerstedt DS, Hunter-Giordano A, Axe MJ, Snyder-Mackler L. Current concepts for anterior cruciate ligament reconstruction: a criterion-based rehabilitation progression. J Orthop Sports Phys Ther. 2012;42(7):601–614. DOI: 10.2519/jospt.2012.3871 · PMID 22402434 · PMC3576892
2. Wellsandt E, Failla MJ, Snyder-Mackler L. Limb symmetry indexes can overestimate knee function after anterior cruciate ligament injury. J Orthop Sports Phys Ther. 2017;47(5):334–338. DOI: 10.2519/jospt.2017.7285
3. Pujol N, et al. The Formal EU-US Meniscus Rehabilitation 2024 Consensus: An ESSKA-AOSSM-AASPT Initiative: Part I—Rehabilitation management after meniscus surgery. Orthop J Sports Med. 2025;13(5):23259671251343088. DOI: 10.1177/23259671251343088
4. Sonnery-Cottet B, et al. Arthrogenic muscle inhibition after ACL reconstruction: a scoping review of the efficacy of interventions. Br J Sports Med. 2019;53(5):289–298. DOI: 10.1136/bjsports-2017-098401
5. Meredith SJ, et al. Return to sport after anterior cruciate ligament injury: Panther Symposium ACL Injury Return to Sport Consensus Group. J ISAKOS. 2021;6(3):138–146. DOI: 10.1136/jisakos-2020-000495
6. Beischer S, et al. Young athletes who return to sport before 9 months after anterior cruciate ligament reconstruction have a rate of new injury 7 times that of those who delay return. J Orthop Sports Phys Ther. 2020;50(2):83–90. DOI: 10.2519/jospt.2020.9071
7. Simonsson R, et al. Questioning the rules of engagement: a critical analysis of the use of limb symmetry index for safe return to sport after anterior cruciate ligament reconstruction. Br J Sports Med. 2025;59(6):376–384. DOI: 10.1136/bjsports-2024-108079
8. Kotsifaki R, et al. Aspetar clinical practice guideline on rehabilitation after anterior cruciate ligament reconstruction. Br J Sports Med. 2023;57(9):500–514.

서지는 PubMed에서 확인했습니다(2026-11-18).

---

## 3. 원문에서 뺀 것과 이유 (를르슈·재필님 확인용)

| 원문 내용 | 처리 | 이유 |
|---|---|---|
| 「9–12주: hop test >85% LSI, KOS-Sports >70%」 | 뺌 | PMC 원문 본문에서 확인 못 함(부록 표에 있을 수 있음). 한 곳뿐이라 원칙대로 제외 |
| 「3–6개월」「6–9개월+」 단계 행 | 후속 근거 절로 옮김 | Adams 2012 본문에 없는 단계 |
| 「1주 LAQ 90–45°」 | 표현 바꿈 | 원 논문은 비체중지지 운동 90°→45°에서 12주 90°→10°로 설명 |
| van Melick 2016, Logerstedt 2010 참고문헌 | 뺌 | 이번 본문에서 인용하는 주장이 없음 |
| 「에이온 기록 항목」「센터 내부 파일」「센터 문의 전화」 | 일반 기록 예시로 바꾸거나 뺌 | 센터 전용 내용 |
