"""통합 업무보드 시트(협업보드 A:K) → data/tasks.json 맞추기.

쓰는 법: python3 tools/sync_from_sheet.py <시트값.json> [오늘 YYYY-MM-DD]
  <시트값.json> = Google Sheets get_values 결과({"values": [[...], ...]}), 1행은 제목줄.
규칙(README 「통합 업무보드 시트와의 관계」):
  - 상태·차례·오늘 표시는 시트를 따른다. 제목·분야·메모는 전광판에 이미 있는 값을 지킨다(공개용으로 다듬은 문장).
  - 시트에서 끝난 일(완료)은 최근 3일 안에 바뀐 것만 남긴다.
  - 에이온 이관 행([이관]) · 에이온 컴퓨터 행은 올리지 않는다.
  - 재필님이 전광판 「완료」 버튼으로 끝낸 일(doneBy)은 시트가 아직 열려 있어도 되돌리지 않고, 시트에 「완료」로 쓸 목록으로 알린다.
  - 전광판에 없는 새 업무는 시트 제목을 그대로 쓰지 않고 「new」 목록으로만 알린다(이름·건강정보가 섞일 수 있어 C.C가 다듬어 넣는다).
  - data/task-decisions.json의 미요청 결정은 재배정하지 않고 보류/C.C/오늘 해제로 보존한다. 이미 재필님이 완료한 기록은 완료를 보호한다.
  - 알 수 없는 차례는 재필님으로 배정하지 않고 기존 유효값 또는 C.C로 보존하며 검토 목록으로 알린다.
"""
import json, sys, datetime
SM = {'할 일':'todo','접수':'todo','진행중':'todo','진행 중':'todo','확인 필요':'check','검수대기':'check','승인대기':'check','보류':'hold','보관':'hold','완료':'done'}
TM = {'재필님':'재필님','김재필':'재필님','C.C':'C.C','를르슈':'를르슈','를르슈(검수)':'를르슈','Codex':'Codex'}
src, today = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else datetime.date.today().isoformat())
rows = json.load(open(src, encoding='utf-8'))['values'][1:]
old = {t['id']: t for t in json.load(open('data/tasks.json', encoding='utf-8'))}
with open('data/task-decisions.json', encoding='utf-8') as decision_file:
    decisions = json.load(decision_file)
if not isinstance(decisions, dict):
    raise ValueError('task-decisions.json must map task IDs to decision objects')
for decision_id, decision in decisions.items():
    if not isinstance(decision_id, str) or not decision_id.strip() or not isinstance(decision, dict):
        raise ValueError('task-decisions.json contains an invalid decision entry')
    if decision.get('kind') != 'not_requested':
        raise ValueError('task-decisions.json contains an unsupported decision kind')
    if any(key in decision and not isinstance(decision[key], str) for key in ('scope', 'decidedBy', 'date', 'note')):
        raise ValueError('task-decisions.json decision fields must be strings')
cut = (datetime.date.fromisoformat(today) - datetime.timedelta(days=3)).isoformat()
out, new, dropped, board_done = [], [], [], []
user_decisions, unmapped_turn = [], []
for r in rows:
    r = (r + [''] * 11)[:11]
    tid, D, E, F, H, I, J, K = r[0], r[3], r[4], r[5], r[7], r[8], r[9], r[10]
    if not tid: continue
    if '[이관]' in H or E.startswith('에이온'): dropped.append(tid); continue
    decision = decisions.get(tid, {})
    if decision.get('kind') == 'not_requested':
        notice = {'id': tid, 'kind': 'not_requested', 'scope': decision.get('scope', '')}
        if tid in old:
            t = dict(old[tid])
            if t.get('doneBy') and t.get('status') == 'done':
                notice['action'] = 'done_preserved'
                if SM.get(F) != 'done': board_done.append((tid, t.get('doneAt', '')))
            else:
                t.update(status='hold', turn='C.C', today=False)
                if isinstance(decision.get('note'), str):
                    t['note'] = decision['note']
                notice['action'] = 'held'
            out.append(t)
        else:
            notice['action'] = 'not_added'
        user_decisions.append(notice)
        continue
    st = SM.get(F)
    if st is None: dropped.append(tid); continue
    if st == 'done' and I[:10] < cut: continue
    if tid not in old:
        if st != 'done': new.append((tid, F, K, D[:60]))
        continue
    t = dict(old[tid])
    if t.get('doneBy') and t.get('status') == 'done' and st != 'done':
        board_done.append((tid, t.get('doneAt', '')))   # 재필님이 전광판에서 완료 → 시트에 「완료」로 써야 함
        out.append(t); continue
    t['status'] = st
    turn = TM.get(str(K).strip())
    if turn is None:
        turn = t.get('turn') if t.get('turn') in TM.values() else 'C.C'
        unmapped_turn.append({'id': tid, 'reason': 'empty' if not str(K).strip() else 'unrecognized', 'kept_turn': turn})
    t['turn'] = turn
    t['today'] = (J.strip() == '✓' and st != 'done')
    out.append(t)
order = {'check': 0, 'todo': 1, 'hold': 2, 'done': 3}
out.sort(key=lambda x: (not x['today'], order[x['status']], x['id']))
json.dump(out, open('data/tasks.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open('data/tasks.json', 'a').write('\n')
gone = sorted(set(old) - {t['id'] for t in out})
print(json.dumps({'tasks': len(out), 'board_done_write_to_sheet': board_done, 'new_needs_title': new, 'removed_from_board': gone, 'user_decisions': user_decisions, 'unmapped_turn': unmapped_turn}, ensure_ascii=False, indent=1))
