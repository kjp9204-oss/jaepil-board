# jaepil-board — 김재필 업무 전광판

주소: https://kjp9204-oss.github.io/jaepil-board/ (2026-11-18부터 업무보드)

## 같이 쓰는 사이트 (11-19 기준)
- PNP 팀 뉴스레터: https://kjp9204-oss.github.io/PNPHealthcare/ (FearX 창간호는 `/PNPHealthcare/fearx/`)
- **에이온 업무는 11-19부터 에이온 컴퓨터가 맡는다.** 이 전광판에는 올리지 않는다.
- AON 오늘의 센터 (에이온 업무 입력, 로그인): https://aon-work-dashboard.jaepilkim.chatgpt.site/ · 소스 https://github.com/kjp9204-oss/aon-work-dashboard
- 그대로 쓰는 곳: kjp9204-oss.github.io 첫 화면(에이온 대문) · handphysio · grand-library · ControlmyLife

## 통합 업무보드 시트와의 관계 (11-18 재필님: 같이 씀)
- **시트 「김재필 통합 업무보드」 = 상세 정본.** 의견(N·O열), 반영 기록, 내부 메모는 시트에만 둡니다.
- **전광판 = 공개해도 되는 한 줄 요약 화면.** C.C가 시트를 고칠 때 같은 업무 ID 줄을 `tasks.json`에도 맞춥니다. 상태·차례는 두 곳이 같아야 합니다.
- 둘이 다르면 시트가 맞습니다. C.C가 전광판을 시트에 맞춰 고칩니다.

## 이 저장소에 쓰는 사람
- **C.C(노트북·집컴)**: 업무·일정·공지·자료를 고칩니다.
- **를르슈(ChatGPT)·Codex**: 화면 수정이나 C.C가 맡긴 반영만 합니다. 업무 내용은 C.C에게 넘깁니다.
- **완료는 재필님만** 정합니다. 재필님이 「끝났어」라고 해야 `done`으로 바꿉니다.

## 고치는 파일
| 파일 | 내용 |
|---|---|
| `data/tasks.json` | 업무 |
| `data/schedule.json` | 오늘 일정 `[{ "t": "14:00", "w": "내용" }]` |
| `data/notices.json` | 맨 위 공지 띠 `["문장", …]` |
| `data/materials.json` + `materials/` | 자료 탭 |

업무 한 건의 모양:
```json
{ "id": "CC-20261118-01", "area": "PNP", "status": "todo", "today": true,
  "title": "한 줄 제목", "who": "C.C", "turn": "재필님", "due": "11-20", "note": "다음 행동 한두 줄" }
```
- `area`: `PNP` · `에이온` · `CML` · `개인`
- `status`: `todo`(할 일) · `check`(확인 필요) · `hold`(보류) · `done`(완료)
- `turn`(차례): `재필님` · `C.C` · `를르슈` · `Codex` — 이 네 이름만 씁니다.
- 업무 ID는 지금처럼 `CC-YYYYMMDD-NN`. 같은 ID를 새로 만들지 말고 기존 줄을 고칩니다.

## 지킬 것
- **공개 페이지입니다.** 선수·환자·회원 이름과 건강정보, 구단·고객 내부 숫자, 계정·결제 정보, 민감한 개인 일정, 원고 본문은 올리지 않습니다. 대신 「무엇을 해야 하는지」 한 줄만 씁니다.
- 고치기 전에 `git pull`로 최신을 받고, 한 번에 한 사람만 고칩니다. 끝나면 바로 올립니다(같은 파일을 두 PC가 동시에 고치면 충돌).
- 커밋 메시지 첫머리에 누가 어디서 고쳤는지 적습니다. 예: `[C.C@노트북] 업무 2건 갱신`
- 긴 지시문·인계 전문은 지금처럼 `AI_협업허브\HANDOFF_BOARD.md`에 둡니다. 이 전광판에는 한 줄 요약만.
- 화면의 완료·완료 취소 버튼은 재필님이 해당 저장소 쓰기 권한의 GitHub 키를 설정한 기기에서 `tasks.json`에 저장합니다. 다른 기기에도 반영되며 시트는 C.C가 맞춥니다. 키는 해당 브라우저에만 보관하고 공개 파일에는 넣지 않습니다.
