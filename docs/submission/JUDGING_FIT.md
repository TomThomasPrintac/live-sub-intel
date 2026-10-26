# Hackathon fit and evidence

**Recommended category: Best Use of Microsoft Foundry Project.** The working submission connects football decision analysis to audience-specific, multilingual explanations through a deployed Foundry integration. Azure App Service and GitHub Actions provide its hosting and delivery path.

This mapping uses the [official challenge, categories and five equally weighted judging criteria](https://github.com/microsoft/insidethegamehackathon/blob/main/OFFICIAL%20RULES.md). It describes implemented evidence, not an expected score or a promise of category selection.

## Follow the challenge through one decision

| Stage | What the project demonstrates | Where to inspect it |
|---|---|---|
| Events | Seeded football-like actions and authored manager changes update the replay XI, bench and score. | Advance the timeline; inspect the event feed and player markers. |
| Interpretation | Past-event statistics, live player performance, estimated load and coach context become current team needs. | Match statistics, needs and [event pipeline](../EVENT_PIPELINE.md). |
| Explanation | A selected substitution or tactical plan has a purpose, relevant facts, role movements and costs. | Explain the Campbell → Oxlade-Chamberlain plan at Arsenal 65. |
| Screen presentation | Current/proposed pitches, player comparisons and alternative plans make the decision visible. | Inspect the proposed XI and comparison panel. |
| Personalization | Broadcaster, Analyst and Coach outputs share the selected plan; ten output locales are independent of interface language. | Keep the plan selected, switch to Spanish, then compare audiences. |

## Match the judging criteria to evidence

| Criterion area | Weight | Contribution to emphasize | Evidence |
|---|---:|---|---|
| Engineering | 20% | A reproducible synthetic scenario, bounded formation/position search, server/browser statistics parity and a deployed Microsoft integration. | [Methodology](../METHODOLOGY.md), regression tests, [46-case live report](../research/live_acceptance_6056cb4_20261026.json). |
| AI workflow and innovation | 20% | A purposeful handoff from computed plans to model-selected facts and protected translation. Server validation, status preservation and recoverable fallback connect the stages. | [Architecture](architecture.svg), plan narrative/translation modules and explanation acceptance checks. |
| Practical applicability | 20% | One decision view supports coaching discussion, statistical analysis and broadcast explanation. Event and profile schemas separate the scenario from the planner. | [Judge route](JUDGE_GUIDE.md), API and [event pipeline](../EVENT_PIPELINE.md). |
| Experience and presentation | 20% | Visual XI comparison, explicit trade-offs, accessible commentary, relevant analyst statistics and separate output-language selection. | Live Arsenal 65; same plan in Spanish; [recording table](RECORDING_ROUTE_HE.md). |
| Category alignment | 20% | Foundry performs verified-fact selection and translation in the actual deployed experience; Azure serves the app and CI/CD maintains the delivery path. | [Accepted Azure run](https://github.com/TomThomasPrintac/live-sub-intel/actions/runs/40352309569), build SHA and provider source labels. |

## Three concrete design contributions

1. **The comparison baseline is the current eleven's best tactical alternative.** A substitute has to contribute beyond what repositioning can already achieve, with a separate tactical-quality guard.
2. **The plan and its explanation share a verified identity.** Selecting another alternative updates the proposed XI and the facts being explained. Audience and language personalize the presentation of that inspected plan.
3. **Translation protects decision meaning as well as structure.** The system validates placeholders and recommendation status, with language-specific regression cases and bounded retry. The engineering evidence records successful checks and their scope.

## Position the submission precisely

Use the deployed Foundry integration as the primary category case. App Service hosting, OIDC deployment, protected server-side credentials, build reporting and live acceptance are supporting operational evidence. The implemented AI workflow is a deterministic planner connected to fact selection, translation and validation; the three audience modes are presentation experiences within it.

The prototype's current demonstration is checkpoint-based decision support and explanation over a synthetic replay. A production event-feed connection, expert calibration and operational scaling are follow-on work. Technical acceptance establishes request/identity behavior; it does not establish causal coaching outcomes or native-speaker fluency. The retained source conditions are documented in [DATA_SOURCES.md](DATA_SOURCES.md).
