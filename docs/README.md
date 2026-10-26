# Documentation

Start with the [live Azure app](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=65&stance=attack&objective=win&inspect=1), [judge guide](submission/JUDGE_GUIDE.md) or [current release status](submission/FINAL_STATUS.md).

## Product and submission

- [Submission text](submission/SUBMISSION.md), [video script](submission/VIDEO_SCRIPT.md) and [final checklist](submission/SUBMISSION_CHECKLIST.md).
- [Methodology](METHODOLOGY.md), [event-to-decision pipeline](EVENT_PIPELINE.md), [automatic tactical plans](AUTO_TACTICAL_PLANS.md) and [estimated match load](MATCH_LOAD.md).
- [Calculation walkthrough in Hebrew](research/CALCULATIONS_SANITY_HE_20261024.md) and [five football decision sanity checks](submission/DECISION_REVIEW_20261024.md).
- [Exact data sources](submission/DATA_SOURCES.md), [source/license review](submission/LICENSE_REVIEW_20261026.md), [logo provenance](submission/STATSBOMB_LOGO.md) and [third-party notices](../THIRD_PARTY_NOTICES.md).
- [Repository audit](submission/REPOSITORY_AUDIT_20261026.md) and [final owner steps](submission/OWNER_FINAL_STEPS_HE.md).

## Research and development history

The following preserve experiments and implementation checkpoints. Their old build IDs, test counts, local ports, feature requests and connection failures are not the current deployment status.

- [Research reports and HTML snapshot](research/README.md), [player-card snapshot](player-cards/README.md), [historical match replay](match-replay/README.md) and [early synthetic demo](synthetic-demo/README.md).
- Dated validation, design, integration, diagnostics and handoff files in this directory record how the project evolved. Some use the earlier manual-formation UI or fan audience. The current room searches tactical plans automatically and has Broadcaster, Analyst and Coach audiences.
- Dated `FINAL_RELEASE`, `FINAL_CLOSEOUT`, `CLAUDE_*`, `THOMAS_FINAL_HANDOFF` and release-review files under `submission/` are historical checkpoints. Do not follow their completed merge requests again.
- [Original data contract](CONTRACT.md) records the v0 design; current runtime code, methodology and the automatic planner describe the implementation now deployed.
- [Earlier architecture raster](research/architecture_legacy.png) is retained as a development asset; the [current architecture](submission/architecture.svg) includes the later translation layer.

Original evidence reports keep their original timestamps and results. A later passing test does not rewrite an earlier failure, and an earlier failure does not imply the current release is broken.
