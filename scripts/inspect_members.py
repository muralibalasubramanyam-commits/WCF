import json
from pathlib import Path
p = Path('members.json')
if not p.exists():
    print('members.json missing')
    raise SystemExit(1)
data = json.loads(p.read_text(encoding='utf-8'))
counts = {}
for k,v in data.items():
    r = (v.get('region') or '').upper()
    counts[r] = counts.get(r,0) + 1
print('total', sum(counts.values()))
for k in sorted(counts.keys()):
    print(k or 'UNSET', counts[k])
print('\nSample entries:')
for i,(k,v) in enumerate(data.items()):
    print(i+1, k, v.get('web'))
    if i>=4: break
