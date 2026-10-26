# Release and delivery status

26 October 2026. [Live Arsenal demo](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=65&stance=attack&objective=win&inspect=1).

## Verified release

- Main and live health: **6056cb414d5b669543e494863ed0c792a7f210c9**, merged PR #36. Health reports synthetic mode and CONFIG_VALID.
- [Live acceptance run 40352309569](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40352309569): successful. The original artifact was independently retrieved; **46/46 model-assisted explanations**, all eight translated locales, no English fallback, no recorded identity failures or broadcaster digits, and the same build SHA before and after. [Preserved report](../research/live_acceptance_6056cb4_20261026.json).
- Regression baseline: **292 Python passed, one optional historical-cache check skipped; 16 Node passed**.
- Local scenario coverage: **228 cases**, two teams × nineteen checkpoints × six coach contexts. [Computed review](RECORDING_CHECKPOINT_REVIEW.md).

The package includes the current narration revision and concise submission entry points. Runtime code, data, weights, thresholds and scenario events are unchanged by this documentation cleanup. Technical checks establish software consistency; coaching accuracy and native-speaker fluency have separate limits documented in the methodology and research.

## Ready materials

| Material | Purpose |
|---|---|
| [Submission copy](SUBMISSION.md) | English pitch, Azure implementation and testing instructions |
| [Judge guide](JUDGE_GUIDE.md) | Short inspection route |
| [Video table](RECORDING_ROUTE_HE.md) and [voiceover](VIDEO_NARRATION_EN.txt) | Opening match playback, Chamberlain substitution, Spanish/audience examples and late objective comparison |
| [Architecture](architecture.svg) | Decision engine, Foundry fact selection, translation and validation |
| [Sources](DATA_SOURCES.md) | Input provenance, generated layers, attribution and applicable source conditions |
| [Checklist](SUBMISSION_CHECKLIST.md) | Remaining delivery and entry-form actions |

## Delivery

The team has recorded footage; final editing/upload is pending. Finish the video and captions, check the export is less than two minutes, upload it and verify playback without login. Add the actual URL to the README and entry form. Confirm team membership, complete the required entry declarations and submit before **28 October 2026 at 08:59 Israel**; save confirmation. Keep Azure available through the end of judging, 11 November 2026 at 09:59 Israel, with a safety buffer. [Official rules](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md).

The existing workflow deploys documentation-only merges as well. Avoid merging during recording/edit capture; after a merge, verify the new health SHA and run Live acceptance on Azure. An earlier report remains evidence for its own build, not a later deployment.
