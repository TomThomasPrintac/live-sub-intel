# Current release and submission status

Verified 26 October 2026. This is the current status entry point; dated handoffs and audits retain their original results.

## Working release

- Public app: [Arsenal, 65 minutes, attack / win](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=65&stance=attack&objective=win&inspect=1).
- Deployed build: **ca18fb480a5e78ce9205dfc7aa31669f427a0750**, merged PR #34. Live `/healthz` independently returned this SHA, synthetic mode and `CONFIG_VALID` on 26 October.
- [Strict live acceptance run 40299465098](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40299465098): successful; **46/46** model-assisted explanations, all eight translated locales, no English fallback, no recorded identity failures and no digits in broadcaster output. The artifact's build SHA matches before and after the run. [Original report retrieved from that run](../research/live_acceptance_ca18fb4_20261026.json).
- Regression baseline: **292 Python passed, one optional historical-cache check skipped; 16 Node passed**. These are technical consistency checks, not proof of improved football outcomes or perfect translations.
- The teammate reported an Italian plural agreement issue in one live output. Automatic structural checks do not establish native-speaker fluency. The recording route uses English.

The current documentation audit changes no runtime code, web UI, player values, source inputs, decision weights, thresholds or scenario events. No new feature work is needed for the English recording route. The latest screenshot represents the deployed interface; an inspected plan does not execute a counterfactual match.

## Prepared materials

| Material | Use |
|---|---|
| [Submission copy](SUBMISSION.md) | English pitch, product description, Azure usage, source summary and testing instructions |
| [Judge guide](JUDGE_GUIDE.md) | Short Arsenal-only inspection route |
| [Video script](VIDEO_SCRIPT.md) | Screen actions and English narration, target 1:45–1:50 |
| [Architecture](architecture.svg) | Decision engine, fact selection, translation and validation |
| [Methodology](../METHODOLOGY.md) and [event pipeline](../EVENT_PIPELINE.md) | How events become player metrics, needs and recommendations |
| [Data sources](DATA_SOURCES.md) and [third-party notices](../../THIRD_PARTY_NOTICES.md) | Exact source provenance, attribution and remaining permission limits |
| [Submission checklist](SUBMISSION_CHECKLIST.md) | Team, recording, links and final form tasks |

## Remaining actions

1. Record the actual Azure app with Arsenal, English narration and corrected English captions. Export less than two minutes; upload to a supported public video service and test without login.
2. Add the actual video URL to the README and project form. There is no fabricated or placeholder video link in these materials.
3. Confirm team membership and the authorized representative. Paste the prepared English text, include the live app, repository and video URLs, complete the required declarations, submit and save confirmation. The preparation of these files does not complete the Studio form.
4. The representative has chosen to retain the current inputs after the source review. That decision is distinct from proof of permission: the questions documented in [the source review](LICENSE_REVIEW_20261026.md) remain unresolved. Do not claim independent generation of all profile inputs or blanket legal clearance.
5. Keep the Azure app available through judging, ending 10 November 2026 at 23:59 Pacific, which is 11 November at 09:59 Israel; retain a safety buffer.

Submission deadline: **28 October 2026, 08:59 Israel**. Aim to complete submission on 27 October evening. [Official rules](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md).

## Change control before recording

The current deployed build can be recorded now. Do not merge unrelated work before recording. The deployment workflow also runs on documentation-only merges, so any later merge requires checking the new `/healthz` SHA and running **Live acceptance on Azure** again. Do not reuse an old report as evidence of a new deployment.

The team's original code has no newly applied MIT grant; source visibility and code licensing are separate. This status does not claim that the video is uploaded, the form is submitted, all translations are fluent or all third-party publication permissions are established.
