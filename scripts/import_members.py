import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / 'members-v1.1.csv'
OUT_PATH = ROOT / 'members.json'

if not CSV_PATH.exists():
    print('members-v1.1.csv not found')
    raise SystemExit(1)

out = {}
with open(CSV_PATH, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        country = row.get('Country') or row.get('Country ')
        if not country:
            continue
        region = (row.get('Region') or '').strip().upper()
        web = (row.get('Web Presence') or row.get('Web Presence ') or row.get('Web') or '').strip()
        out[country.strip()] = { 'region': region, 'web': web }

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f'Wrote {len(out)} entries to {OUT_PATH}')
