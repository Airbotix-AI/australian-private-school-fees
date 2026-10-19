# Release import notes — 19 October 2026

The public files were built by whitelisting factual fields from nine historical CSV research tables and the Gold Coast primary published guide. Internal research notes, contact information, marketing assets, account data and full school PDFs are excluded. The original artifact fingerprints are in data/2026/coverage.json. No private source checkout is needed to use this dataset or reproduce its rendered reports.

Two Adelaide secondary rows had an extra CSV field: the fee-source URL, explanation and date had shifted columns. For Inventorium Academy and Premed Senior College, the import restores the source URL and 21 July 2026 check date, moves contextual text into notes, and leaves annual amounts and non-refundable entry fees unknown. The after-hours accelerated-program prices are explicitly not treated as Premed's full-time school fees. The private source files were not modified.

Gold Coast primary imports the published 31-row entry-year summary. It preserves the annual fee text and entry-cash explanation rather than inventing year-level values. The linked guide contains the extended year-level discussion. It does not claim that every year of primary schooling has been extracted into JSON.

Missing annual amounts in other groups are retained even when the research found a readable source. No price is inferred from a different stage, campus, year or family arrangement. Melbourne values retain a generic source-specific annual basis because internal annotation fields were excluded; check the original school schedule before using them as tuition or total costs.

Validation is offline and structural. It checks CSV/JSON parity, provenance fields, status/amount consistency, unique record IDs, coverage counts and deterministic reports. It does not verify that every July fee is still correct in October, establish nationwide completeness, or measure SEO performance.
