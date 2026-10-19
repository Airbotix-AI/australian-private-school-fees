# Australian Private School Fees 2026

**Open fee research for Australian families and developers, maintained by [Airbotix](https://airbotix.ai/).**

**First release: 1,431 school/campus-stage research records across five cities; 404 contain extracted annual amounts. This is not yet all Australian private schools.**

Historical source checks: July 2026. Repository release: 19 October 2026. Prices and links have not been rechecked at release. A record is not a unique school, and a readable source is not necessarily an extracted fee.

## Get the data

- [Download CSV](data/2026/fees.csv) · [JSON](data/2026/fees.json) · [Coverage and gaps](data/2026/coverage.json)
- [Methodology](docs/methodology.md) · [Data dictionary](docs/data-dictionary.md) · [Contribute a correction or missing school](CONTRIBUTING.md)

Browse the complete imported records below. Every row retains its school source, research date and available fee detail; no account or setup is needed.

| City / stage | Research records | With annual amounts | Browse | Parent guide |
|---|---:|---:|---|---|
| Adelaide | 72 | 72 | [Full table](docs/cities/adelaide.md) | [Airbotix guide](https://airbotix.ai/resources/adelaide-private-school-fees-2026/) |
| Adelaide Secondary | 12 | 10 | [Full table](docs/cities/adelaide-secondary.md) | [Airbotix guide](https://airbotix.ai/resources/adelaide-secondary-private-school-fees-2026/) |
| Brisbane | 50 | 23 | [Full table](docs/cities/brisbane.md) | [Airbotix guide](https://airbotix.ai/resources/brisbane-private-school-fees-2026/) |
| Brisbane Secondary | 59 | 49 | [Full table](docs/cities/brisbane-secondary.md) | [Airbotix guide](https://airbotix.ai/resources/brisbane-secondary-private-school-fees-2026/) |
| Gold Coast | 31 | 28 | [Full table](docs/cities/gold-coast.md) | [Airbotix guide](https://airbotix.ai/resources/gold-coast-private-school-fees-2026/) |
| Gold Coast Secondary | 24 | 19 | [Full table](docs/cities/gold-coast-secondary.md) | [Airbotix guide](https://airbotix.ai/resources/gold-coast-secondary-private-school-fees-2026/) |
| Melbourne | 385 | 27 | [Full table](docs/cities/melbourne.md) | [Airbotix guide](https://airbotix.ai/resources/melbourne-private-school-fees-2026/) |
| Melbourne Secondary | 188 | 79 | [Full table](docs/cities/melbourne-secondary.md) | [Airbotix guide](https://airbotix.ai/resources/melbourne-secondary-private-school-fees-2026/) |
| Sydney | 472 | 91 | [Full table](docs/cities/sydney.md) | [Airbotix guide](https://airbotix.ai/resources/sydney-private-school-fees-2026/) |
| Sydney Secondary | 138 | 6 | [Full table](docs/cities/sydney-secondary.md) | [Airbotix guide](https://airbotix.ai/resources/sydney-secondary-private-school-fees-2026/) |

## Read an actual result

The historical Sydney primary record for Al Zahra College reports Kindergarten A$4,240 and Year 6 A$4,350, including compulsory curriculum fees, with books and uniforms excluded. Its A$600 non-refundable entry amount and A$500 deposit/credit field are separate cash categories. Checked 15 July 2026; [school source](https://www.azc.nsw.edu.au/enrolment/tuition-fees/). Confirm the deposit conditions and current fee year with the school.

For comparison, the Melbourne secondary record for Ivanhoe Girls’ Grammar School contains Year 7 A$32,500, Year 9 A$35,000 and Year 12 A$36,400 as published annual amounts, checked 24 July 2026. These are source-specific amounts rather than a harmonised tuition-only benchmark. [See the full record and source](docs/cities/melbourne-secondary.md).

Missing amounts remain unknown; they are never zero. Compulsory levies, per-family charges, deposits, boarding, optional items and discounts differ. Do not rank schools or calculate a national average from this uneven sample.

## Nationwide coverage target

The intended scope is open non-government primary and secondary schools, including Catholic and Independent schools, across all eight states and territories. This initial release imports existing Airbotix city research. **ACT, NT, Tasmania and WA have no records yet; regional areas elsewhere and some city directories are incomplete.** Adelaide primary includes priced rows only. Some July pending records lag the later parent guides. A reconciled national register and school/campus deduplication are outstanding; no national coverage percentage is claimed.

Priority work: establish dated state registers; reconcile city research with published guides; extract missing year-level fees; expand to unrepresented states and regional areas; recheck 2026 sources without mixing in 2027 fees. [Coverage detail](data/2026/coverage.json).

## Use with Python

```python
import json
from pathlib import Path

records = json.loads(Path("data/2026/fees.json").read_text())
for row in records:
    if row["state"] == "NSW" and "y6" in row["annual_amounts_aud"]:
        print(row["school_name"], row["annual_amounts_aud"]["y6"],
              row["source_checked_at"], row["source_url"])
```

Offline maintenance, no dependencies: `python3 scripts/render.py` then `python3 scripts/validate.py`. No CI workflows, deployment, paid API or model calls are included.

## About Airbotix

[Airbotix](https://airbotix.ai/) provides AI and creative technology education for Australian children. Its parent guides explain fee inclusions and school budgeting; this project opens the underlying factual research for reuse and correction. Schools are not affiliated with or endorsed by this project. School fees are not a measure of education quality.

## 中文说明

这是一份由 Airbotix 维护的 2026 澳洲私校费用开源资料，包含 Catholic 与 Independent 学校。现在公开 1,431 条「学校／校区 × 学段」研究记录，其中 404 条已提取年度金额；不是 1,431 所独立学校，也尚未覆盖全澳。包含悉尼、墨尔本、布里斯班、黄金海岸、阿德莱德，具体边界见各城市指南。

资料来源核验于 2026 年 7 月，没有在 10 月发布时全部重新核验。未知价格不补零，不把押金当成本，不把年度固定费统一写成纯学费。可以直接打开上方完整表格、下载 CSV/JSON，并沿每条记录的学校来源复核。全国全量采集与逐校更新仍未完成。

## Licence and citation

Code: [MIT](LICENSE). Original compilation, annotations and documentation: [CC BY 4.0](LICENSE-DATA.md). Third-party source documents retain their own rights. Suggested citation: “Airbotix contributors (2026), Australian Private School Fees 2026, release 2026-10-19”, with this repository URL and the specific school sources.
