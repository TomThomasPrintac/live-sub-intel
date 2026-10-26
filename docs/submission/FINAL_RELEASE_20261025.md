> **Historical record.** Build IDs, test counts and action requests below describe that document's original checkpoint. For the current release and remaining tasks, use [FINAL_STATUS.md](FINAL_STATUS.md); do not repeat completed integrations.

# Release and submission status — 25 October 2026

## Deployed integration

`main` and Azure were independently observed at **980bde2ee0ac07173334b09ccc55bd2a48e31c6f**. PR #28 is merged. Follow-ups #29–#32 improve broadcaster joining, grammatical translation context, per-item validation and bounded retry. Engine weights, thresholds, player priors and scripted substitutions were unchanged by those follow-ups.

The [latest accepted Azure run](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40109792305) produced the [preserved report](../research/live_acceptance_980bde2_20261024.json). It records:

- 46/46 HTTP-successful model-assisted explanations.
- Model translation in all eight translated locales, without an English fallback.
- No recorded plan-identity failures or digits in broadcaster explanations.
- The same build SHA before and after the run.

The artifact was retrieved from GitHub Actions artifact `12566665919` on 25 October. Original report timestamp: 24 October, 16:09:42 UTC. The report is preserved rather than relabelled as a new 25 October acceptance run. The team's report of other successful runs is not substituted for this particular artifact.

These automated checks do not certify native-speaker fluency, opponent-specific tactical insight or a causal improvement in results. A source label of `llm` means model fact selection; literal names and numbers are rendered by the server. Translation templates use their own validation and fallback.

## Submission-readiness branch

`release/submission-ready-20261025` updates the judge-facing entry point, source presentation, recording/checklist documents and event-to-decision explanation. It preserves the actual Azure lineup screenshot and the accepted report above. A small English-template edit avoids "1 shots on target" through count-neutral labels and bumps the template version. The previously accepted 980bde2 report does not establish live success for that later template change.

Local validation on this branch: **292 Python passed / 1 optional historical raw-cache check skipped; all 16 Node tests passed.** The event trace was reproduced with the committed audit script. A narrow tracked-file scan found no matches for the selected common token/private-key patterns; it is not an exhaustive secret audit.

PR #33 was merged and deployed as **0f3e19d24963c41ca12e857a65fc942381426bf7**. [Build and deployment](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40195478083) succeeded. The subsequent [strict extended live acceptance](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40195568545) passed **46/46** with model-assisted explanations, translation in all eight additional locales, no translation fallback, no plan-identity failures and no broadcaster digits. The earlier 980bde2 artifact above remains a separate historical baseline. Any later deployment requires its own SHA and live check.

## Remaining submission tasks

1. Resolve the applicable publication permissions described in [DATA_SOURCES.md](DATA_SOURCES.md). Attribution/logo and data redistribution are distinct. No provenance is being concealed or rewritten.
2. Record/upload the English video, less than two minutes, with Arsenal throughout. [Script and capture route](VIDEO_SCRIPT.md).
3. Add the actual public video URL to the project page and repository; no placeholder is proof of an uploaded video.
4. Confirm the team's Studio membership and final fields, submit and retain confirmation. Deadline: 28 October 2026, 08:59 Israel, according to the [official rules](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md).
5. Keep the deployed demo available through judging, with a buffer beyond 11 November morning in Israel.

Optional reviews: one native-speaker example and a short football review of late repositioning/waiting. Do not add new engine features just to increase claim breadth before recording.

The repository package can be reviewed now. This document does not claim legal clearance, video upload or completed submission. [Final checklist](SUBMISSION_CHECKLIST.md).
