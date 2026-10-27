# Release and delivery status

27 October 2026. [Watch the 1:45 demo video](https://www.youtube.com/watch?v=pkH76wz9Qq4) · [Live Arsenal demo](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=65&stance=attack&objective=win&inspect=1).

## Verified release

- Last checked main and live health, before this video-link documentation change: **83d23a13cb36f14c6027bcb354b3ab5ad684127e**, merged PR #38. Health reports synthetic mode and CONFIG_VALID. [Live acceptance run 40384751556](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40384751556) completed successfully on that build; [build and deployment](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40384287953) also succeeded. The run artifact contains its detailed results.
- [Live acceptance run 40352309569](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40352309569): successful. The original artifact was independently retrieved; **46/46 model-assisted explanations**, all eight translated locales, no English fallback, no recorded identity failures or broadcaster digits, and the same build SHA before and after. [Preserved report](../research/live_acceptance_6056cb4_20261026.json).
- Regression baseline: **292 Python passed, one optional historical-cache check skipped; 16 Node passed**.
- Local scenario coverage: **228 cases**, two teams × nineteen checkpoints × six coach contexts. [Computed review](RECORDING_CHECKPOINT_REVIEW.md).

The package includes the current narration revision and concise submission entry points. Runtime code, data, weights, thresholds and scenario events are unchanged by this documentation cleanup. Technical checks establish software consistency; coaching accuracy and native-speaker fluency have separate limits documented in the methodology and research.

## Ready materials

| Material | Purpose |
|---|---|
| [Submission copy](SUBMISSION.md) | English pitch, Azure implementation and testing instructions |
| [Hackathon fit](JUDGING_FIT.md) | Implemented strengths and evidence mapped to the five judging areas |
| [Judge guide](JUDGE_GUIDE.md) | Short inspection route |
| [Video table](RECORDING_ROUTE_HE.md) and [voiceover](VIDEO_NARRATION_EN.txt) | Opening match playback, Chamberlain substitution, Spanish/audience examples and late objective comparison |
| [Architecture](architecture.svg) | Decision engine, Foundry fact selection, translation and validation |
| [Sources](DATA_SOURCES.md) | Input provenance, generated layers, attribution and applicable source conditions |
| [Checklist](SUBMISSION_CHECKLIST.md) | Remaining delivery and entry-form actions |

## Delivery

The team has uploaded the [final demo video](https://www.youtube.com/watch?v=pkH76wz9Qq4); the YouTube player shows 1:45, within the two-minute limit. The README links to it. The team reports that the project page has been populated; its saved fields, team membership and final submission status require confirmation by a signed-in team member. Verify video playback without login, complete the required entry declarations and submit before **28 October 2026 at 08:59 Israel**; save confirmation. Keep the repository public and Azure available through the end of judging, 11 November 2026 at 09:59 Israel, with a safety buffer. [Official rules](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md).

The existing workflow deploys documentation-only merges as well. Avoid merging during recording/edit capture; after a merge, verify the new health SHA and run Live acceptance on Azure. An earlier report remains evidence for its own build, not a later deployment.
