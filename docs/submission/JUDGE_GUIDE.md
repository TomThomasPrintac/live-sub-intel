# Judge guide — one decision, several experiences

Open the [live Arsenal demo at 65 minutes](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=65&stance=attack&objective=win&inspect=1). No login required. [Judging fit and evidence](JUDGING_FIT.md).

## 1. See the proposed change

The audited build recommends **Campbell → Oxlade-Chamberlain**, with benefit about **0.192** against **0.150**. Compare the current and proposed pitches, then open the player comparison. The incoming player takes the right-wing role; the plan also records its other positional movements.

The substitute is compared with the best action available without using a bench player. The score breakdown separates freshness and tactical contributions, and a separate quality check governs eligibility.

## 2. Hear the same plan differently

Choose Broadcaster and press Explain. Switch explanation language to Español, then choose Analyst and explain again. The interface remains in English while the explanation changes language and audience emphasis. Select another alternative: its pitch and explanation follow that plan's identity.

The source label identifies model-assisted fact selection, translation and any fallback. The server owns the plan and inserts protected literal values after template translation.

## 3. Change the match objective

Open [Arsenal 85, attack / win](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=85&stance=attack&objective=win&inspect=1). Arsenal trails with one substitution available. The tactical adjustment scores about **0.217**; the best swap adds about **0.115** beyond the best no-swap action. Change the objective to Avoid defeat and inspect the recalculated recommendation.

## Optional: a shape-changing plan

Explore [Liverpool 85, balanced / win](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=24&minute=85&stance=balanced&objective=win&inspect=1). The reviewed scenario recommends **Ibe → Lucas Leiva** in **4-1-4-1**, trading attacking contribution for defending/retention and freshness. This is outside the Arsenal recording route and illustrates another use of the formation search.

## Evidence and method

- [Current build and live acceptance](FINAL_STATUS.md): 6056cb4 and its preserved 46-case provider report.
- [Methodology](../METHODOLOGY.md): event cutoffs, estimated values, player metrics and scoring.
- [Decision review](DECISION_REVIEW_20261024.md) and [228-case checkpoint review](RECORDING_CHECKPOINT_REVIEW.md).
- [Architecture and product description](SUBMISSION.md) and [source inventory](DATA_SOURCES.md).

Match actions are synthetic; profiles use historical inputs and generated physical estimates. The pitch is schematic. These are inspectable model proposals; scores are model units and the authored replay continues independently of the inspected alternative.
