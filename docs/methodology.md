# Methodology and limitations

This project is a public factual research compilation maintained by [Airbotix](https://airbotix.ai/). It covers domestic day-school fee research for 2026. Private means non-government, including Catholic and Independent schools. School fees are not a school-quality ranking.

## What the first release contains

The release imports ten primary/secondary city research groups. A record is a school/campus **and stage**, so a P–12 school may appear twice. Shared campus schedules may represent multiple campuses. The count of records must not be described as a count of unique Australian schools.

The sources were checked in July 2026. Publication on 19 October 2026 is **not** a fresh verification of the fees or URLs. A source might since have changed, been removed or switched to 2027. Always check its year and domestic/international applicability.

Imported observations are factual research records, not fictional demo prices. Some records remain pending and some published guides contain more information than the underlying imported CSV. In particular, Sydney secondary has readable sources with no year-specific extracted amounts, and Adelaide primary imports only priced rows. See coverage.json for every known limitation. No national average or cheapest-school ranking is computed from this incomplete, uneven sample.

## Amounts

- `annual_amounts_aud` contains explicitly numeric year-level amounts from the research table, only when its source was marked 2026-domestic-readable. Empty object means unknown/unextracted, never free.
- Values can include tuition plus compulsory levies, and some guides allocate a family levy to a single child. The source-specific basis is retained. They are not harmonised tuition-only prices.
- `fee_detail` preserves narrative year ranges or a published entry-year fee where a safe numeric mapping is unavailable. Do not extract a number without reading the year, conditions and levies.
- `entry_nonrefundable_as_reported` and `deposit_or_credit_as_reported` are historical source text, not computed amounts. A blank means unknown. Refundability, eligibility, payment dates and per-family/per-student rules need confirmation.
- `compulsory_items`, `family_levy_note` and `notes` may include costs not already in the amount. Do not automatically add them: this can double-count a levy.
- Boarding, international fees, discounts, scholarships, transport, uniforms, devices, excursions, optional subjects and taxes/charges are not consistently included. The original school schedule controls.
- No first-year total is calculated. A refundable bond or tuition credit is a cash timing item, not automatically a permanent expense.

## Two separate status fields

| Field | Meaning |
|---|---|
| source_status = 2026-domestic-readable | Researcher found an applicable readable source at its recorded check date; extraction may still be missing |
| pending-source-research | No completed review in the imported record |
| not-publicly-listed | Research did not find a full applicable public price at that date; not proof none exists today |
| old-year-only | Imported research found an older schedule only; older prices are not used as 2026 annual values |
| login-restricted | Applicable source could not be read openly during the review |
| extraction_status = amounts-extracted | Some annual amount/year-range text exists; not proof of a complete schedule |
| extraction_status = no-annual-amount-extracted | No annual amount in this record, regardless of source availability |

## Coverage and the national target

The target is all registered, open Australian non-government schools providing mainstream primary or secondary education. A completed national edition requires an explicit, dated register for each state and territory, stable school/campus identifiers, cross-stage deduplication and a source status for every entity. Special and alternative schools need a separately stated inclusion policy. Kindergarten-only providers are outside the school-age target.

**This release has not met that national target.** ACT, NT, Tasmania and WA have no imported records. Regional coverage in the other states is incomplete. Even inside the covered cities, directory-only and priced-only imports cannot establish complete coverage.

The [Australian Schools List](https://asl.acara.edu.au/home) and [ACARA Data Access Program](https://acara.edu.au/contact-us/acara-data-access) are discovery references. ACARA download availability does not mean its datasets may be re-licensed under this project's licence; review the applicable source terms before any future import. No ACARA bulk dataset is redistributed here.

## Corrections and updates

Submit a source URL, school/campus, fee year, student type, relevant year levels, amount basis, check date and a short explanation. Prefer the school's own fee page/PDF or the school's designated hosting service. Third-party directories are leads, not authoritative fee evidence. Never bypass a login. Recheck pending and older-year records before changing their status. Keep 2026 history separate from future years. Do not attach private documents or student/family information.
