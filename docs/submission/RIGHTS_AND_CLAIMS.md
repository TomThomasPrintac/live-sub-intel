# Data rights, source use and consistent project claims

Reviewed 26 October 2026 against the retained files, builder, web/API and primary source terms. This is a factual source/terms review, not legal advice, provider permission or an organizer's acceptance decision. Current technical release: [FINAL_STATUS.md](FINAL_STATUS.md).

## 1. Approved product description

> Live Substitution Intelligence transforms synthetic football events into explainable substitution recommendations. The demo uses an authored match simulation and player profiles derived from historical attributes, supplemented by generated physical estimates. StatsBomb Open Data supported our research and analytical methodology, while SkillCorner positional references informed the physical estimates. The recommendations are experimental model outputs, not observations or predictions of an actual match. Detailed sources and transformations are documented separately in the repository.

Use this description in the project page and README. The short spoken equivalent is: **“The match is synthetic, with historical player profiles and generated physical estimates.”** Detailed provenance belongs in the linked source documentation; the short description does not replace it or assert that every input is independently generated.

## 2. Source-by-source assessment

The levels below compare the clarity of the documented permission basis, not numerical litigation probabilities or findings that a use is lawful/unlawful.

| Component | Actual use | Permission basis and remaining limit | Accurate description |
|---|---|---|---|
| Original code, formulas, optimizer and interface | Authored implementation and generic pitch/shirt graphics | Original project work; external dependencies and source inputs retain separate rights. No new MIT grant for the team's code has been approved/applied. | Original software and an experimental decision model. Public source is available; do not call the entire repository MIT-licensed. |
| Original simulated match actions | Own seeded possession/event generator, authored goals/cards and manager substitutions | Strongest originality basis among the data layers. The scenario still uses historical roster metadata and derived profiles; generating actions does not independently clear those inputs. | Synthetic match events, not a replay, prediction, actual match footage or current licensed live Premier League feed. |
| StatsBomb research and computed analysis | 203 pre-cutoff matches; 1,131 retained player-match evidence rows; calibration distributions, baselines, positions and historical metadata | Research and public analysis/conclusions are expressly contemplated. The README requires source attribution and logo for published research/analysis. Those are retained. | StatsBomb Open Data supported research, historical evidence and methodology; calculated outputs are our analysis. |
| StatsBomb-related retained/distributed inputs | Evidence JSON, historical-derived profiles, generated research HTML and historical benchmark outputs | The agreement also restricts providing/reproducing/distributing data and commercial exploitation. Whether these particular retained exports/derived profiles fit the permitted analytical-publication scope has not been established. Credit is necessary for the analysis but does not resolve that scope question. | Do not claim that no historical data is published. Distinguish analysis from the retained data supporting it. |
| Historical FIFA16/SoFIFA attribute snapshot | Republished scraped CSV supplies 70 matched player records. Two missing-player fallbacks use source-derived cohort medians and explicit assumptions. Attributes feed capability priors, suitability and generated physical estimates. | Least established permission basis: the pinned publisher README says the dataset was scraped from SoFIFA. No redistribution grant covering this particular source and retained/derived use was established by the review. A third-party public repository is not itself a license from the relevant rights holder. | Historical player-attribute inputs in detailed provenance; derived player profiles in the short product description. Do not assert independent model generation of all attributes. |
| SkillCorner positional reference | A-League 2024/25 position-group physical aggregates; formulas scale references to create estimates | Pinned source includes MIT; full notice is retained in LICENSES/SkillCorner-MIT.txt. This is a clearer permission basis for that reference. It does not clear the other inputs used in scaling. | SkillCorner-referenced generated physical estimates, not observed tracking or medical measurements for the displayed players. |
| Player/team names, numbers and lineup metadata | Descriptive historical identities, roster and schematic starting positions | No blanket fictional-name requirement was found in the reviewed hackathon rules. That is not individual clearance of trademarks, database, privacy or publicity rights. Avoid implying player/club endorsement. | Historical squad identifiers used in a simulated scenario. No claim of official club partnership or measured current fitness. |
| StatsBomb logo | Official portal rendition linked by the provider media pack | Portal asset was marked External Use Approved; its provenance/hash is recorded. Retain it as attribution, without implying endorsement. Logo availability is not a blanket data license. | Source acknowledgement; see STATSBOMB_LOGO.md. |
| Own screenshots and architecture | Screenshots of this app; current code-native SVG architecture; older raster retained as historical | Original layout/diagram work. Screenshots can contain provider marks and source-derived values, whose conditions still matter. No player photos, club crests, match footage or music were added. | Actual app screenshot or schematic architecture, identified as such. |
| Runtime libraries | NumPy, pandas, pydantic and OpenAI Python SDK, installed as dependencies | NumPy/pandas BSD-3-Clause; pydantic MIT; SDK Apache-2.0. Exact installed distributions/transitive components have their own notices, which must accompany redistribution as required. No SDK implementation is vendored here. | Open-source software dependencies, separately licensed from data and original code. |
| Microsoft Foundry / Azure | Hosted explanation fact selection and template translation | Service/account use is governed by the team's provider agreement. An SDK license does not license source football data or certify generated output. This review does not certify the Azure subscription's contract or output rights. | Foundry-assisted explanation and translation; the deterministic engine chooses the decision. |

## 3. Where source-related material is actually exposed

| Surface | What is present | Required description/boundary |
|---|---|---|
| Standard coach-room UI | Synthetic score/events/statistics; historical-derived player names, capabilities and lineup; computed load/fit | Keep synthetic-match/estimated-value wording. The main screen need not recite the full source inventory. Footer retains StatsBomb logo/credit and a link to sources. |
| About/data section | Scenario, historical-prior and inspection-only explanations | Do not say that the profiles are entirely independent synthetic inputs. The precautionary non-affiliation sentence has been removed; this does not establish rights or assert reliance on the relevant provider fan-content policy. |
| `/api/bootstrap` | Full profile payload, including historical attributes and provenance; current synthetic fixtures/events | This is publicly accessible, not private computation. The current builder exposes 72 player profiles even though the live fixture has two teams. No statement that all historical inputs stay server-private is justified. |
| `/api/evaluate`, `/api/explain`, integration JSON | Derived plans, player comparisons, metrics/facts and explanation outputs | Scores are model units and estimates, not calibrated win probabilities, measured medical fitness or evidence that a proposed substitution improves results. These are not substitutes for input permission. |
| Model requests | Verified explanation facts/metadata and protected translation templates under the implemented request contract | Do not claim that no information derived from historical inputs is processed externally. Translation inserts protected literal names/numbers server-side; that is a factual-control mechanism, not a data license. |
| `demo_data/fifa16_anchors.json` | Retained attribute records, including more fields than final capability scores | Actual retained source-derived input; not merely inspiration or a newly generated set of numbers. |
| `demo_data/source_evidence.json` | Historical summaries, baselines, roles, match IDs and raw-file hashes | Contains research evidence, not the full 203 raw event files. Avoid both extremes: do not call it a full raw event dump or claim it contains no retained historical data. |
| `demo_player_profiles.json` / CSV, position suitability, roster | Derived cards plus source/identity fields, generated estimates and historical metadata | Distinguish the layers and preserve original provenance/status fields. Renaming keys would not change their origin. |
| Research HTML, CSV, JSON/gzip and historical mode | Historical research snapshots, derived analysis, benchmark decisions and computed scenario audits | Label dated snapshots as research/history. They remain publicly present even when not used as the main submission demo. |
| README, submission text and architecture | Concise product story; direct source/methodology links | Use the approved description. Detailed historical source names do not have to appear in the pitch, but stay in DATA_SOURCES.md, THIRD_PARTY_NOTICES.md and the technical source records. |
| Video and project form | Screen capture, narration, team declarations and linked repository | Use the actual Azure app, synthetic-match wording and permitted/original media. A short narration does not need to read all sources aloud. Keep required attribution visible in the app and accessible in submission/source materials. Do not imply that hiding the footer clears marks or data. |
| Git history, forks and prior public versions | Earlier files and wording remain reachable | This work does not rewrite history, delete public forks or recall copies. No claim that all source references or prior data exposure have disappeared is made. |

## 4. Phrases to use and avoid consistently

| Use | Avoid |
|---|---|
| Synthetic match events with historical-derived player profiles | Everything, including all player inputs, was independently generated by an LLM |
| Research based on StatsBomb Open Data, with attributed analysis | We used only the schema/inspiration, when retained evidence was also used |
| Generated physical estimates informed by positional references | Measured Premier League tracking or clinically measured fatigue |
| Descriptive historical squad identities | Officially endorsed club/player data or partnerships |
| Experimental substitution scores and transparent trade-offs | Validated win probabilities or proof that the substitute causes later goals |
| Historical period selected for a fixed reproducible benchmark | Old dates make the source public domain or automatically free to redistribute |
| Publicly accessible source dataset, with its terms assessed separately | Public GitHub/Kaggle availability automatically means an open-source data license |

## 5. The non-affiliation sentence

It was added as a precaution after reviewing EA's fan-content policy, then removed from the UI at the team's request. The review did not establish that our particular dataset/use is authorized under that policy or that the sentence is a mandatory notice under an applicable license we hold. We do not use its removal as evidence that no historical attributes were used, nor claim that the policy grants us permission. If qualified review later establishes reliance on a policy/license that requires a particular notice, that condition must be followed.

This optional sentence is distinct from StatsBomb's explicit publication attribution/logo request and SkillCorner's retained MIT notice. Those are preserved.

## 6. Hackathon implications

The [official rules](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md), especially 4.3, 4.4, 4.6–4.7 and 7, require appropriate third-party permissions, a public repository, a functioning accessible project, synthetic football-realistic data and an English/translated video under two minutes. They also grant organizers broad rights to use submissions, including commercial purposes. Noncommercial team intent is not by itself proof that every submission right has been obtained.

The live demo's event stream is synthetic. The rules' synthetic-event requirement is not a blanket license for historical priors. Accepting responsibility or adding citations is not permission from a third-party right holder. This review does not conclude that each numerical value is copyrighted or that the project is definitely infringing; the unresolved issue is the legal/contractual basis for the particular retained and distributed use.

The representative has chosen to retain the existing inputs. That choice is recorded as a team decision, not as established permission. To close the unresolved source gate, establish an applicable permission or a qualified assessment covering the actual files/uses; otherwise independently authored or appropriately licensed replacement inputs remain the technical alternative. No such replacement has been made under the fixed-data constraint.

## 7. What is complete, and what cannot be certified here

Complete: accurate short product wording; source-level technical provenance; retained StatsBomb attribution/logo and SkillCorner notice; separation of current release from research history; recording route and narration; regression/package checks recorded in the PR. No code license has been newly granted, and no source inputs or recommendation rules were changed to alter the rights story.

Not certified: blanket clearance for retained historical attributes/exports, the scope of StatsBomb-derived distribution, individual identity/trademark rights, exact provider-account terms, native-speaker fluency, football coaching accuracy, final video media rights or completion of the Studio submission. These are distinct questions. A passing test or deployment cannot resolve a permission question.

## 8. Primary sources and evidence

- [StatsBomb Open Data README](https://github.com/hudl/open-data) and [Public Data User Agreement](https://github.com/hudl/open-data/blob/master/LICENSE.pdf). Research/public conclusions, redistribution/commercial limits and logo attribution are distinct provisions. The agreement text associated with the project's pinned evidence was inspected; a fresh webpage load does not imply that the PDF text was re-rendered by the web tool.
- [Pinned attribute-source README](https://github.com/kushal-gopal/EA-Sports-Fifa/blob/658e9f96cafcfdb636d6ca96fcc9bfdb1c064868/README.md), re-read through GitHub at that revision on 26 October; it explicitly describes a SoFIFA-scraped dataset. Source SHA and attributes remain in the repository records.
- [EA content policy](https://help.ea.com/en/articles/security-and-rules/ea-content-policy/): conditional fan-content permissions and exceptions, not a demonstrated grant for this retained snapshot.
- [SoFIFA API documentation](https://sofifa.com/document): previously reviewed API conditions are not a retroactive license for a republished CSV. A fresh fetch returned 403 on 26 October; no new current API authorization is claimed.
- [Pinned SkillCorner MIT license](https://github.com/SkillCorner/opendata/blob/4340d274572876239c154c90bc507a9b3250a656/LICENSE), [retained notice](../../LICENSES/SkillCorner-MIT.txt) and [logo evidence](STATSBOMB_LOGO.md).
- Official library licenses: [NumPy](https://github.com/numpy/numpy/blob/main/LICENSE.txt), [pandas](https://github.com/pandas-dev/pandas/blob/main/LICENSE), [pydantic](https://github.com/pydantic/pydantic/blob/main/LICENSE), [OpenAI Python SDK](https://github.com/openai/openai-python/blob/main/LICENSE). Exact installed distributions can include further notices.
- [Detailed source review and unchanged-data hashes](LICENSE_REVIEW_20261026.md), [data inventory](DATA_SOURCES.md), [package audit](REPOSITORY_AUDIT_20261026.md) and [current status](FINAL_STATUS.md).
