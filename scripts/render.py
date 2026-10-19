"""Render browseable reports from the committed public JSON. Python 3, no packages."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def cell(value):
    return str(value or '—').replace('|', '&#124;').replace('\n', '<br>')

def render():
    records = json.loads((ROOT / 'data/2026/fees.json').read_text())
    coverage = json.loads((ROOT / 'data/2026/coverage.json').read_text())
    directory = ROOT / 'docs/cities'
    directory.mkdir(parents=True, exist_ok=True)
    for group in coverage['datasets']:
        dataset = group['dataset_id']
        lines = [f'# {dataset.replace("-", " ").title()}: 2026 fee research', '',
                 f"{group['records']} stage/campus records; {group['with_extracted_amounts']} with extracted annual amounts.", '',
                 '**Historical July 2026 research. Not rechecked at the October release. Not a complete city or national price census.**', '',
                 f"[Airbotix parent guide]({group['guide_url']}) · [Methodology](../methodology.md) · [CSV](../../data/2026/fees.csv)", '',
                 'Annual amounts may include different compulsory items. Read the basis and notes before comparing. Entry fees and deposits below are source text, not a calculated first-year total.', '',
                 '| School / campus | Annual amounts (AUD) | Basis and fee notes | Compulsory / family items | Entry fee / deposit or credit | Source status / extraction | Source checked |',
                 '|---|---|---|---|---|---|---|']
        for r in records:
            if r['dataset_id'] != dataset:
                continue
            amounts = '; '.join(f'{k.upper()}: ${v:,.2f}' for k, v in r['annual_amounts_aud'].items()) or r['fee_detail']
            name = cell(r['school_name']) + ' · ' + cell(r['suburb_or_campus'])
            if r['source_url']:
                name = f"[{name}]({r['source_url']})"
            values = [name, amounts, r['amount_basis'] + ' ' + r['notes'],
                      r['compulsory_items'] + ' ' + r['family_levy_note'],
                      'Non-refundable: ' + (r['entry_nonrefundable_as_reported'] or 'unknown') + '; Deposit/credit: ' + (r['deposit_or_credit_as_reported'] or 'unknown'),
                      r['source_status'] + ' / ' + r['extraction_status'], r['source_checked_at']]
            lines.append('| ' + ' | '.join(cell(x) for x in values) + ' |')
        (directory / f'{dataset}.md').write_text('\n'.join(lines) + '\n')

if __name__ == '__main__':
    render()
