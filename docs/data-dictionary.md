# Data dictionary

`data/2026/fees.json` and `fees.csv` contain the same ordered records. UTF-8; currency AUD; fee year 2026. CSV `annual_amounts_aud` is a JSON-encoded object. Dates are YYYY-MM-DD or empty if not researched.

| Field | Meaning |
|---|---|
| record_id | Stable within this release; preserve on correction; not a government school identifier |
| dataset_id | Imported city-stage group; a primary group has no primary suffix |
| school_name | Public school/entity or campus name as researched |
| state / city / stage | Research grouping; not a claim of complete geographic coverage |
| suburb_or_campus | Public locality/campus; may describe more than one campus |
| fee_year / student_type / currency | 2026 / domestic / AUD |
| annual_amounts_aud | Object mapping k, prep, reception, foundation or y1–y12 to historical annual amounts |
| fee_detail | Narrative annual fees when a precise year mapping was not imported |
| amount_basis | Scope warning: amounts are not consistently tuition-only |
| compulsory_items / family_levy_note / notes | Conditions, levies, exclusions and explanation; consult before comparison |
| entry_nonrefundable_as_reported | Research field for entry cash marked non-refundable; text or blank |
| deposit_or_credit_as_reported | Research field for potentially refundable/credited cash; text or blank |
| source_status | Historical source accessibility/applicability; see methodology |
| extraction_status | Whether any annual amount has been extracted, separate from source status |
| source_url | School-owned or school-designated fee source; may change after review |
| source_checked_at | Historical research date, not repository publication date |
| freshness | historical-research-not-rechecked-at-release |
| guide_url | Corresponding Airbotix parent guide |

`coverage.json` contains counts by dataset, known gaps, the explicitly false national completeness flag, and original research-artifact SHA-256 fingerprints. These fingerprints record import provenance; the private source archive is not a public dependency. Reproduce public reports from the committed JSON using scripts/render.py.
