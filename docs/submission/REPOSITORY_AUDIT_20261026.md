# Repository consistency audit — 26 October 2026

Baseline: `ca18fb480a5e78ce9205dfc7aa31669f427a0750`, merged PR #34. The audit covers the tracked submission package and distinguishes current documentation from development history. It does not rewrite history, delete source evidence or establish third-party legal permission.

## Checks and findings

| Area | Result / action |
|---|---|
| Tracked-file inventory | Baseline: 173 files, including code, tests, data, reports, HTML, graphics and workflows. All tracked text was included in selected-pattern scans; JSON and compressed reports receive structural checks. |
| Product description | The approved description distinguishes synthetic match events, historical-derived player profiles and generated physical estimates. README and submission copy now use that description consistently; the video script uses its shorter equivalent. Exact source provenance remains in the source documents. |
| Current vs historical documents | Added a documentation index and current status entry point. Dated handoffs, diagnostics and audits are marked historical so old failures, test counts and completed integration requests are not presented as current tasks. PR_LINK.txt no longer calls merged PR #21 an active draft. |
| Release evidence | Independently retrieved the original Actions artifact from run 40299465098. It records ca18fb4 before and after 46 successful model-assisted explanations, all eight translated locales, no English fallback, no identity failures and no broadcaster digits. It is not relabelled as a new run. |
| Azure | Public health independently returned ca18fb4, synthetic mode and CONFIG_VALID. The Arsenal 65 attack/win route loaded the expected Campbell → Oxlade-Chamberlain plan and 0.192 benefit. Footer logo, attribution, license link and English non-affiliation text were visible in English and Hebrew, including the narrow browser viewport. |
| Architecture and assets | Added a current code-native SVG diagram including both Foundry fact selection and protected-template translation. Retained the original generated raster diagram as a labelled research asset. No club crests, player photos, match footage or music were added. |
| Relative Markdown links | Checked for missing file targets; the final package audit reports the outcome. This is not a remote-link or heading-anchor validator. |
| File structure | JSON, gzip JSON and SVG XML are checked by the reproducible package audit. Historical generated HTML and reports remain research snapshots, not the current Azure UI. |
| Selected secret patterns | No matches in baseline tracked text for the selected token/private-key/credential-assignment patterns. Also scanned 563 reachable Git blobs across locally fetched refs for selected GitHub/OpenAI token and private-key patterns: no matches. These limited scans are not an exhaustive security audit or a guarantee that no secret ever existed. Matched values would not be printed. |
| Repository presentation | GitHub About has a malformed character in the description and no Website URL. Exact replacement text and owner steps are provided in OWNER_FINAL_STEPS_HE.md. The connected account has Write without Admin on the upstream; no repository visibility change or new license grant is applied. |
| Runtime/data preservation | Runtime code, web UI, source data, dependency files, workflows and tests match the audited main baseline. Engine weights, thresholds and scenario events are unchanged. New executable content is only a local read-only package-audit script. |

## Validation

- Full Python suite: **292 passed, 1 optional historical-cache check skipped**.
- All three Node UI test files: **16 passed**.
- `git diff --check` and a zero-diff check of runtime/data/web/tests/dependencies/workflows against the baseline.
- Reproducible package check: `python scripts/audit_submission_package.py`. It checks tracked relative Markdown file targets, JSON/gzip JSON, SVG XML and selected secret patterns without network calls. Stage intended new files before invoking it to include them in the tracked inventory.
- Final staged package: **180 tracked files, 51 Markdown documents, 32 JSON/gzip JSON documents and one SVG; zero reported packaging issues**.

## Limits and remaining work

The live acceptance is a structural and identity check, not proof of perfect translation fluency or improved football decisions. The teammate reported an Italian grammar issue; English is the recording language. No new runtime deployment was performed for this documentation audit.

The representative chose to retain the current profiles after review. This does not establish missing third-party permissions; [DATA_SOURCES.md](DATA_SOURCES.md) and [LICENSE_REVIEW_20261026.md](LICENSE_REVIEW_20261026.md) remain the source-specific record. No claim that all player inputs were independently generated, that historical evidence is absent, or that publication rights are universally cleared has been introduced.

The remaining delivery actions are the actual video recording/upload/link, owner About edits, any documentation merge and resulting deployment verification, team/form completion, the representative's required rights declarations, and submission confirmation. [Current status](FINAL_STATUS.md) and [owner steps](OWNER_FINAL_STEPS_HE.md).
