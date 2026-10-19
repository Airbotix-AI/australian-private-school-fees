# Contributing

Help build a nationwide, source-traceable dataset. Read [methodology](docs/methodology.md) first. No fees are accepted without an applicable source, date, domestic/international distinction and year-level basis. A link alone is not an extracted fee.

Use GitHub issues for corrections, missing schools and sources. Include the affected record_id if one exists. For a proposed new school, include state, locality, campus, registration evidence and the school's fee URL. Missing amounts stay unknown. Do not copy entire fee PDFs or contact lists into this repository.

For data changes, update both fees.json and fees.csv, recompute coverage counts, run `python3 scripts/render.py`, then `python3 scripts/validate.py`. Keep stable identifiers. The validator runs offline without dependencies. No GitHub Actions workflows are configured.

Contributions to original data/compilation and documentation use CC BY 4.0; code contributions use MIT. Confirm you may contribute the material. Third-party source documents remain under their own terms. No student or family personal data, credentials or private school records.
