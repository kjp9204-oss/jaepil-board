# [Hand 원고 1] ACL 재건술 후 재활, 날짜와 회복을 함께 봅니다

C.C 작성 · 2026-11-18 · 일반 독자용 · 에이온 원고를 Hand 형식으로 재구성

- 원문: 에이온 재활운동센터 `posts/adams-acl-rehabilitation.html` (원게시 2026-10-15, 근거 확인 2026.10.15)
- 원문 보존: 를르슈가 `drafts/aon-native-YYYYMMDD/source-originals/`에 그대로 복사합니다. 본문은 지난 6편처럼 원문 HTML에 아래 「바꿀 곳」만 적용합니다.
- 표지: 원문 AI 교육용 이미지 `assets/posts/acl-20261015/acl-cover.webp`, 본문 그림 `acl-readiness.webp`를 그대로 씁니다. 원문 캡션이 이미 「AI 생성 이미지」로 표시돼 있어 새 이미지를 만들지 않습니다.

---

## 1. editorial-spec 항목 (지난 6편과 같은 형식)

```json
{
  "slug": "adams-acl-rehabilitation",
  "title": "ACL 재건술 후 재활, 날짜와 회복을 함께 봅니다",
  "subtitle": "몇 개월째인지보다, 다음 단계에서 무엇을 확인하는지",
  "description": "ACL 재건술 후 수술 날짜와 무릎의 실제 회복을 함께 보는 기준 기반 재활을 설명합니다. 상담 때 물어볼 질문과 바로 진료가 필요한 신호까지 담은 일반 독자용 글입니다.",
  "audience": "public",
  "primary": "return",
  "topics": ["return", "knee", "sport"],
  "image": "aon-import/posts/acl-20261015/acl-cover.webp",
  "imageAlt": "ACL 재건술 후 단계별 회복을 표현한 AI 교육용 표지",
  "imageCredit": "원문 제공: 에이온 재활운동센터 · AI 생성 교육용 이미지. 실제 환자·센터 공간 사진이나 따라 하기용 운동 처방이 아닙니다.",
  "sourceType": "일반 독자용 건강정보 · 지침·합의문·관찰연구 소개",
  "review": "원문 편집·재구성. 참고문헌 10건의 저자·학술지·권호를 PubMed와 공식 기관 안내로 대조했고, 1건(Panther 합의문)은 PubMed 색인판으로 서지를 바꿨습니다. 모든 임상 주장을 새로 검증한 글은 아닙니다.",
  "summary": [
    "수술 후 날짜는 꼭 필요하지만, 그 날짜만으로 다음 단계로 넘어가지 않습니다.",
    "붓기, 무릎 펴기, 허벅지 힘, 실제 동작과 자신감을 함께 확인합니다.",
    "‘반대쪽의 90%’나 ‘9개월’ 같은 숫자 하나로 안전을 확정할 수 없습니다."
  ],
  "changes": [
    "센터 이름·상담 안내 문구를 빼고 HandPhysio 읽기 흐름으로 재편",
    "Panther 합의문 서지를 PubMed에 색인된 J ISAKOS 판으로 교체",
    "AI 이미지 캡션의 표현을 일반화(‘실제 회원·직원’ → ‘실제 환자·센터 공간’)"
  ],
  "relatedIds": [
    "aon-adams-2012-acl-criterion-based",
    "aon-walking-to-running-physiology",
    "ami-clinical-reasoning-20261011"
  ]
}
```

> relatedIds의 `aon-adams-2012-acl-criterion-based`는 원고 2(전문가용)가 들어갈 때의 id입니다. 같이 배포하지 않으면 빼 주세요.

---

## 2. 본문에서 바꿀 곳 (원문 문장 → 바꿀 문장)

| # | 원문 그대로 | 바꿀 문장 | 이유 |
|---|---|---|---|
| 1 | 「이해를 돕기 위한 AI 생성 이미지입니다. 실제 회원·직원·센터 공간을 촬영한 사진이나 따라 하기용 운동 처방이 아닙니다.」 | 「이해를 돕기 위한 AI 생성 이미지입니다. 실제 환자나 센터 공간을 촬영한 사진, 따라 하기용 운동 처방이 아닙니다.」 | 센터 회원·직원 표현 일반화 |
| 2 | 「에이온 재활운동센터의 일반 건강정보입니다. 개인의 진단·수술 후 처방·스포츠 복귀 허가를 대신하지 않습니다.」 | 「일반 건강정보입니다. 개인의 진단·수술 후 처방·스포츠 복귀 허가를 대신하지 않습니다.」 | 센터 문구 제외(원저자는 표시 영역에 남음) |
| 3 | 참고문헌 「Meredith SJ, et al. Return to Sport After Anterior Cruciate Ligament Injury: Panther Symposium ACL Injury Return to Sport Consensus Group. Orthop J Sports Med. 2020;8(6).」 | 「Meredith SJ, et al. Return to sport after anterior cruciate ligament injury: Panther Symposium ACL Injury Return to Sport Consensus Group. J ISAKOS. 2021;6(3):138–146. DOI: 10.1136/jisakos-2020-000495.」 | 원문 서지(OJSM 2020)는 PubMed에서 찾지 못함. 같은 합의문의 PubMed 색인판(PMID 34006577)으로 교체 |
| 4 | 「← 에이온 게시글 전체 보기」 | (삭제) | 에이온 사이트 목록 링크 |

그 밖의 본문·숫자·참고문헌 문장은 원문 그대로 둡니다.

---

## 3. 숫자·서지 대조 결과 (두 곳 이상 확인)

| 본문 숫자·서지 | 원문 | 대조한 곳 | 결과 |
|---|---|---|---|
| Beischer 2020: 15–30세 159명, HR 6.7 (95% CI 2.6–16.7) | 원문 6절 | PubMed 32005095 초록 | 일치 |
| Simonsson 2025: 233명, LSI 단독 구분 능력 낮음 | 원문 6절 | PubMed 39797641 초록 | 일치 |
| Wellsandt 2017: 70명 코호트 | 참고문헌 | PubMed 28355978 초록 | 일치 |
| Adams 2012 JOSPT 42(7):601–614 | 참고문헌 | PubMed 22402434 | 일치 |
| Aspetar 2023 BJSM 57:500–514 | 참고문헌 | PubMed 36731908 | 일치 |
| Brinlee 2022 Sports Health 14(5):770–779 | 참고문헌 | PubMed 34903114 | 일치 |
| Sonnery-Cottet 2019 BJSM 53(5):289–298 | 참고문헌 | PubMed 30194224 | 일치 |
| Pujol 2025 반월상연골 합의문 Part I | 참고문헌 | PubMed 40416991 (OJSM 2025;13(5)) | 일치 |
| NHS 합병증 안내, 2025-07-17 검토 | 9절·참고문헌 | NHS 페이지 직접 확인 | 일치. 원문 9절 응급 신호(숨참·가슴 통증 → 응급)와 같은 내용 |
| Panther 합의문 OJSM 2020;8(6) | 참고문헌 | PubMed에서 못 찾음 | **J ISAKOS 2021판으로 교체(위 표 3번)** |
