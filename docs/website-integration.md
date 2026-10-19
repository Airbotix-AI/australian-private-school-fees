# Website association and SEO handoff

## Already configured in the public repository

- Organisation: Airbotix-AI.
- Repository homepage: https://airbotix.ai/.
- README identifies Airbotix as maintainer, links to its website and links each imported group to the corresponding parent guide.
- Full data, readable city tables, source links, coverage limitations and reuse licences are public. The useful reusable research is the reason to cite the project.

## Website-side source plan (not deployed)

The existing city guides already provide complete parent-facing content. Add one contextual source/download paragraph to each relevant guide and an open-data link on its resource detail page when that website change is separately implemented and visually checked:

> Download the underlying 2026 school-fee research as CSV or JSON from [Australian Private School Fees](https://github.com/Airbotix-AI/australian-private-school-fees), maintained by Airbotix. The first release covers selected city research, with explicit missing prices and coverage gaps; it is not yet a national census. Check the source dates and each school's current fee schedule before budgeting.

A future English landing page at `/resources/australian-private-school-fees-2026/` should contain a useful comparison method, actual fee examples, clear city boundaries, coverage counts and direct downloads. This is a proposed route, not an existing public URL. Only add it to sitemap and navigation after the content and canonical URL are implemented. Preserve the existing city guide URLs and their individual value.

If adding Dataset structured data, use the actual dataset name, observed source dates, explicit partial spatial coverage, correct licence scope, public CSV/JSON distributions and Airbotix as creator. Do not label all Australia as fully covered or use the repository release date as the source-check date. Validate structured data after the real page exists.

## How to measure

Record the publish date and inspect the actual canonical page in Search Console. Monitor indexing, queries, impressions and clicks for school-fee topics; separately measure GitHub referral visits to the relevant parent guides. No GSC or GA4 performance was measured for this release.

A repository link does not establish ranking gains. Google identifies link spam and scaled low-value content as spam: https://developers.google.com/search/docs/essentials/spam-policies. Keep the repository useful as a standalone data resource, with natural attribution and no repetitive keyword links, artificial stars, bulk doorway pages or paid link arrangements.

No Airbotix website source was changed or deployed for this repository release. The existing website is linked from GitHub; a website-to-GitHub link remains outstanding. No CI/CD was triggered.
