# Third-party notices and source boundaries

This inventory distinguishes original project code and generated match events from historical inputs and external software.

The [source inventory](docs/submission/DATA_SOURCES.md) records input versions, transformations and applicable conditions.

## SkillCorner Open Data

Physical-generation references use position-group aggregates from SkillCorner's Australian A-League 2024/25 Open Data, revision `4340d274572876239c154c90bc507a9b3250a656`. These are not observed tracking measurements for the displayed players. The original MIT notice is retained in [LICENSES/SkillCorner-MIT.txt](LICENSES/SkillCorner-MIT.txt). Source: https://github.com/SkillCorner/opendata.

## StatsBomb Open Data

Historical evidence and derived analysis use https://github.com/hudl/open-data, pinned in the collector and subject to its Public Data User Agreement. The official Hudl Statsbomb logo and attribution are retained in the website and repository; [asset provenance](docs/submission/STATSBOMB_LOGO.md). The applicable source conditions are summarized in [DATA_SOURCES.md](docs/submission/DATA_SOURCES.md).

![Hudl Statsbomb](web/coach-room/statsbomb-logo.png)

## Historical player-attribute inputs

Source versions and conditions for historical-derived profiles are recorded in [DATA_SOURCES.md](docs/submission/DATA_SOURCES.md). Code and input-data licensing remain separate.

The project describes computed profiles as historical-derived estimates, alongside original synthetic match events and generated physical estimates.

## Runtime packages

NumPy and pandas: BSD-3-Clause; pydantic: MIT; OpenAI Python SDK: Apache-2.0. Install via the declared package dependencies and retain notices distributed with the exact installed versions, including bundled binaries and transitive packages when redistributed. This short inventory is not a complete software bill of materials. No copied SDK implementation is vendored in this repository.

External provider names describe sources and integrations; they do not imply endorsement of the project's recommendations. The generic pitch/shirts are code-rendered. No player photos, club crests, match footage or music are included in the reviewed app assets.
