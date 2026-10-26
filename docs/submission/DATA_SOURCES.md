# Data sources and attribution

The demo uses an original synthetic match, player profiles computed from historical base attributes and match evidence, and generated physical estimates. Detailed computation remains in [the methodology](../METHODOLOGY.md) and [dataset documentation](../../demo_data/README.md).

| Layer | Input and transformation |
|---|---|
| Match events | Own seeded possession generator; authored actions, cards, goals and manager substitutions. The displayed fixture is a simulation. |
| Player base attributes | [Pinned historical player-attribute snapshot](https://github.com/kushal-gopal/EA-Sports-Fifa/tree/658e9f96cafcfdb636d6ca96fcc9bfdb1c064868). Seventy matched records and two cohort-median fallbacks with explicit assumptions. The precise source update date is unverified. |
| Historical evidence | [StatsBomb Open Data](https://github.com/hudl/open-data/tree/4b73468fc5b0f1950f9f66fada70ad3a4f9327cb): 203 matches before 13 January 2016; retained player-match summaries, baselines and positions inform capped profile adjustments. |
| Physical estimates | [SkillCorner A-League 2024/25 positional aggregates](https://github.com/SkillCorner/opendata/blob/4340d274572876239c154c90bc507a9b3250a656/data/aggregates/aus1league_physicalaggregates_20242025.csv), scaled by authored formulas and player attributes. These are generated estimates, not tracking measurements of the displayed players. |
| Live decisions | Synthetic events, computed profiles, coach context and the original scoring/search implementation. Scores are model units; inspecting a plan does not change subsequent match events. |

## Attribution and terms

Historical research uses StatsBomb Open Data. Its [README](https://github.com/hudl/open-data) requests source credit and logo for published analysis; the official logo is retained in the website and repository. [Logo provenance](STATSBOMB_LOGO.md).

![Hudl Statsbomb](../../web/coach-room/statsbomb-logo.png)

The [StatsBomb agreement](https://github.com/hudl/open-data/blob/master/LICENSE.pdf) permits research/public analysis and separately limits data redistribution and commercial exploitation. The retained evidence/derived exports require an assessment against those terms. No redistribution grant covering the retained historical attribute snapshot has been established by this source review. These source conditions are separate from the originality of the generated match and code.

The [SkillCorner source license](https://github.com/SkillCorner/opendata/blob/4340d274572876239c154c90bc507a9b3250a656/LICENSE) is MIT; its complete notice is retained in [LICENSES/SkillCorner-MIT.txt](../../LICENSES/SkillCorner-MIT.txt). It does not relicense other source inputs.

## Public data boundary

Input records and derived profiles remain in demo_data, historical research snapshots and the public profile API. The public package therefore does not claim that all player inputs were generated independently or that no historical data is distributed. The source records retain their actual provenance. Old public commits and forks are not removed by current-tree cleanup.

## Code and assets

The pitch, shirts and diagrams are project-authored. No player photos, club crests, match footage or music are bundled. External names identify sources or descriptive squad members; no endorsement is asserted. [Third-party notices](../../THIRD_PARTY_NOTICES.md) cover dependencies and source boundaries. No new MIT license is granted for the team's code by this document. The representative completes the entry's required rights declarations under the [official rules](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md).
