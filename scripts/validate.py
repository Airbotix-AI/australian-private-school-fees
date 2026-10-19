"""Focused offline data validation. No network, dependencies or CI."""
import collections
import csv
import json
import math
import re
from pathlib import Path
from render import render
ROOT = Path(__file__).resolve().parents[1]
records = json.loads((ROOT / 'data/2026/fees.json').read_text())
coverage = json.loads((ROOT / 'data/2026/coverage.json').read_text())
assert len({r['record_id'] for r in records}) == len(records)
assert len(records) == coverage['records']
assert coverage['national_coverage_complete'] is False
assert coverage['national_school_denominator'] is None
assert set(coverage['covered_states']) == {r['state'] for r in records}
assert len(records) == sum(g['records'] for g in coverage['datasets'])
known = {'2026-domestic-readable', 'pending-source-research', 'old-year-only', 'not-publicly-listed', 'login-restricted'}
for r in records:
    assert r['school_name'] and r['fee_year'] == 2026 and r['currency'] == 'AUD'
    assert r['student_type'] == 'domestic' and r['source_status'] in known
    assert r['freshness'] == 'historical-research-not-rechecked-at-release'
    assert not r['source_checked_at'] or re.fullmatch(r'2026-\d{2}-\d{2}', r['source_checked_at'])
    has_amount = bool(r['annual_amounts_aud'] or r['fee_detail'])
    assert (r['extraction_status'] == 'amounts-extracted') == has_amount
    if has_amount:
        assert r['source_status'] == '2026-domestic-readable'
        assert r['source_url'].startswith(('https://', 'http://')) and r['source_checked_at']
    for year, amount in r['annual_amounts_aud'].items():
        assert year in {'k', 'prep', 'foundation', 'reception'} | {f'y{i}' for i in range(1, 13)}
        assert isinstance(amount, (int, float)) and math.isfinite(amount) and amount >= 0
    assert not any(k in r for k in ['notes_internal', 'research_note', 'phone', 'address'])
for g in coverage['datasets']:
    rows = [r for r in records if r['dataset_id'] == g['dataset_id']]
    assert len(rows) == g['records']
    assert sum(r['extraction_status'] == 'amounts-extracted' for r in rows) == g['with_extracted_amounts']
    assert dict(collections.Counter(r['source_status'] for r in rows)) == g['source_status_counts']
assert sum(r['extraction_status'] == 'amounts-extracted' for r in records) == coverage['with_extracted_amounts']
with (ROOT / 'data/2026/fees.csv').open(newline='') as f:
    csv_rows = list(csv.DictReader(f))
assert len(csv_rows) == len(records)
for row, record in zip(csv_rows, records):
    assert set(row) == set(record)
    for key, value in record.items():
        assert (json.loads(row[key]) if isinstance(value, dict) else row[key]) == (value if isinstance(value, dict) else str(value))
before = {p: p.read_bytes() for p in (ROOT / 'docs/cities').glob('*.md')}
render()
assert before == {p: p.read_bytes() for p in (ROOT / 'docs/cities').glob('*.md')}, 'Run scripts/render.py and commit updated reports'
assert not (ROOT / '.github/workflows').exists(), 'This repository intentionally has no CI workflows'
print(f"PASS: {len(records)} records, CSV/JSON parity, provenance, amounts, coverage and 10 rendered reports")
