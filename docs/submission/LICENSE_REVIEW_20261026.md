# License review — 26 October 2026

## Scope and constraints

This review covers the retained numerical profiles, recommendations and descriptive real names. No independent replacement dataset is included in the audited release; historical-derived inputs remain identified as such. This is a documented source review, not a legal opinion or an organizer's acceptance decision.

The repository is public. No MIT code-license grant is applied by this review.

## Findings

| Component | Finding | What is complete / what remains |
|---|---|---|
| Original project code | No root code license was present at the reviewed baseline. MIT is recommended for the team's original code/docs. | A concrete MIT text is prepared for team approval; it permits reuse, including commercial reuse, with its notice retained. It does not relicense data. |
| SkillCorner reference | The pinned source carries MIT. | Full notice already retained in LICENSES/SkillCorner-MIT.txt. Reference values are identified as inputs to synthetic estimates. |
| StatsBomb research/analysis | The agreement permits research/analysis and public sharing of conclusions, with brand attribution. | Official logo and source credit are already in the app/repository. This supports presenting the work as noncommercial analysis. |
| StatsBomb data redistribution | The same agreement separately restricts providing/editing/distributing the data and commercial exploitation. | Committed evidence rows, embedded exports and public bootstrap profiles require a scope/permission assessment. Noncommercial purpose and attribution alone do not prove that every retained file is covered. |
| FIFA16/SoFIFA inputs | The pinned CSV source README explicitly describes scraped SoFIFA data. No license file was found at that revision's root. | No grant authorizing this project's CSV/derived-data redistribution has been established. A transformed rating is still derived from an input. |
| EA policy | EA permits certain personal fan projects under conditions, including an affiliation disclaimer; it excludes other uses and does not grant third-party rights. | Add the requested non-endorsement wording as a precaution. Do not interpret that notice as approval of this particular dataset, scraping, integration or submission. |
| SoFIFA API | Its published API requirements describe a noncommercial partner API with a source logo/link and an existing database requirement. | This is not a retroactive license for an unrelated scraped historical CSV. No new API connection is being added. |
| Team/player names | The hackathon rules reviewed do not impose a blanket fictional-name requirement. | Keep descriptive names as requested. No club crests, player photos, game art or asserted official endorsement are introduced. This is not a blanket clearance of identity/trademark rights. |

## What other projects actually do

- [Parma's event-data-chatbot attribution](https://github.com/parmacalcio1913/event-data-chatbot/blob/main/ATTRIBUTION.md) separates its MIT code from StatsBomb terms. It states that the data is downloaded locally rather than vendored, with a limited documented test-fixture exception.
- [Football-Analytics](https://github.com/AlexandreMorel/Football-Analytics) describes fetching StatsBomb data and placing the provider logo on published visualizations and PDF output; it also acknowledges the commercial-use restriction.

These are implementation examples, not permission for this project. Their existence does not establish that our different bundled files are covered. No example code, data or assets were copied into this project during this comparison.

## Source exposure in this repository

- `demo_data/fifa16_anchors.json`: retained input attributes, not merely final ratings.
- `demo_data/source_evidence.json`: historical player-match evidence and baselines.
- `demo_data/demo_player_profiles.json` and CSV: derived cards; JSON includes source attributes.
- `docs/player-cards/index.html`, `docs/match-replay/index.html` and research exports: embedded/derived data displays.
- `/api/bootstrap`: publicly returns the player-profile payload.

GitHub and Azure are publicly accessible. They are public distribution surfaces even if the team does not sell the project. Removing a current export would not erase prior Git history or independently clear the remaining derived values. No history rewrite or data deletion is authorized by this review.

## Practical conclusion with the numbers fixed

The original synthetic match, software, visualization and noncommercial analysis can be described accurately. Preserve StatsBomb attribution and SkillCorner's MIT notice. Keep exact provenance and distinguish code licensing from data licensing.

The outstanding FIFA/SoFIFA permission and the scope of StatsBomb-derived distribution cannot be declared resolved merely by calling all cards generated. With the team's fixed-data constraint, finishing that clearance requires an applicable permission or qualified assessment covering the retained use. An independently authored replacement remains an alternative only if the team later authorizes changing the data.

The film can be prepared as a functional demonstration; this review does not certify that only filming remains for compliant submission.

## Primary sources

- [Official hackathon rules](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md): third-party permissions, submission ownership, video and repository requirements, and rights granted to organizers.
- [StatsBomb Open Data](https://github.com/hudl/open-data) and [Public Data User Agreement](https://github.com/hudl/open-data/blob/master/LICENSE.pdf): research/public analysis, clauses 1.2.1, 1.2.2 and 1.4. The project's collected evidence pins revision 4b73468fc5b0f1950f9f66fada70ad3a4f9327cb; the retained agreement text was also inspected.
- [SkillCorner MIT](https://github.com/SkillCorner/opendata/blob/4340d274572876239c154c90bc507a9b3250a656/LICENSE).
- [Pinned FIFA CSV source README](https://github.com/kushal-gopal/EA-Sports-Fifa/blob/658e9f96cafcfdb636d6ca96fcc9bfdb1c064868/README.md) and that revision's root file listing.
- [EA content policy](https://help.ea.com/en/articles/security-and-rules/ea-content-policy/).
- [SoFIFA API requirements](https://sofifa.com/document) and [terms](https://sofifa.com/help/tos).
- [MIT license explanation](https://choosealicense.com/licenses/mit/): recommended for original code, subject to team authorization.

## Unchanged-data check

SHA-256 values recorded before this license-only work. The first column was computed on a Windows checkout (CRLF line endings); the second is the content stored in Git (LF), which is what a Linux checkout, GitHub and Azure see. Both describe the same unchanged files, last modified in commit 84b7926 (18 October).

| File | SHA-256, Windows checkout (CRLF) | SHA-256, stored in Git (LF) |
|---|---|---|
| demo_player_profiles.json | 8456e8e73109002faae436382dc46ef42cb5391e6473a74772b90267e17d278c | 88675d732f44faa02d1319932316de150b79b2d5c841ebaac687ffd71028ec77 |
| source_evidence.json | e371eb5114a7508e52d93c926ca2288a74c417a4d62f8e07168520073eae2290 | d3ba7ba27b3335fd3d544ed1d62c2c840d9e2d2d369e525f7bb03534074f1d4b |
| fifa16_anchors.json | 6497567b4c453c46c184aac648a472f327706169b60f18e372b1b5b548130a45 | d1845a1ab248004ec19bc0ca91fa86eec19014af8af95594a274dc0b2dbec4ba |

These hashes establish that those inputs were not changed by the review; they are not permission evidence.
