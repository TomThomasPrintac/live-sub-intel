# Full checkpoint and intent review — 26 October 2026

Coverage: **228 evaluations = two teams × 19 checkpoints × three approaches × two result objectives**. Fixed lively scenario, seed 20261021, baseline ca18fb4. The decision engine and data match that deployed baseline. This is a local coverage audit, not 228 live model requests, professional coaching validation or a counterfactual simulation.

[Full JSON](../research/recording_route_audit_20261026.json.gz) · [Excel-friendly CSV](../research/recording_route_audit_20261026.csv) · [Recording route in Hebrew](RECORDING_ROUTE_HE.md)

An optional live comparison was attempted separately, but the network connection to the evaluate endpoint was refused. No live parity result is claimed. The committed report is the successful local audit.

All available swap plans were checked for eleven distinct players, removal of the outgoing player and inclusion of the incoming player. Every combination completed without those assertions failing. The report preserves the selected plan, top three alternatives, game state, position movements, match facts and scoring gates.

## Arsenal: every five minutes

Each cell is the selected action and its benefit. **Move** means repositioning without a substitute. **Wait** means no recommended action. All selected Arsenal plans retain 4-2-3-1. Tactical-plan benefit is measured against the observed XI; substitution benefit is incremental against the best no-substitution action, so those two score types must not be ranked against each other directly.

| Minute | Balanced / win | Balanced / draw | Attack / win | Attack / draw | Defend / win | Defend / draw |
|---|---|---|---|---|---|---|
| 0 | Wait | Wait | Wait | Wait | Wait | Wait |
| 5 | Wait | Wait | Wait | Wait | Wait | Wait |
| 10 | Wait | Wait | Wait | Wait | Wait | Wait |
| 15 | Wait | Wait | Wait | Wait | Wait | Wait |
| 20 | Move · 0.324 | Move · 0.244 | Move · 0.530 | Move · 0.447 | Move · 0.399 | Move · 0.419 |
| 25 | Move · 0.353 | Move · 0.261 | Move · 0.545 | Move · 0.449 | Move · 0.390 | Move · 0.407 |
| 30 | Move · 0.267 | Move · 0.267 | Move · 0.445 | Move · 0.445 | Move · 0.400 | Move · 0.400 |
| 35 | Move · 0.279 | Move · 0.279 | Move · 0.430 | Move · 0.430 | Move · 0.358 | Move · 0.358 |
| 40 | Move · 0.213 | Move · 0.213 | Move · 0.355 | Move · 0.355 | Move · 0.329 | Move · 0.329 |
| 45 | Wait | Wait | Move · 0.248 | Move · 0.248 | Move · 0.249 | Move · 0.249 |
| 50 | Wait | Wait | Move · 0.182 | Move · 0.182 | Move · 0.181 | Move · 0.181 |
| 55 | Bellerín → Chambers · 0.150 | Bellerín → Chambers · 0.150 | Wait | Wait | Wait | Wait |
| 60 | Bellerín → Chambers · 0.194 | Bellerín → Chambers · 0.194 | Wait | Wait | Bellerín → Chambers · 0.192 | Bellerín → Chambers · 0.192 |
| 65 | Campbell → Oxlade-Chamberlain · 0.201 | Campbell → Oxlade-Chamberlain · 0.201 | Campbell → Oxlade-Chamberlain · 0.192 | Campbell → Oxlade-Chamberlain · 0.192 | Campbell → Oxlade-Chamberlain · 0.191 | Campbell → Oxlade-Chamberlain · 0.191 |
| 70 | Mertesacker → Paulista · 0.246 | Mertesacker → Paulista · 0.246 | Mertesacker → Paulista · 0.259 | Mertesacker → Paulista · 0.259 | Campbell → Oxlade-Chamberlain · 0.219 | Campbell → Oxlade-Chamberlain · 0.219 |
| 75 | Mertesacker → Paulista · 0.243 | Mertesacker → Paulista · 0.243 | Mertesacker → Paulista · 0.254 | Mertesacker → Paulista · 0.254 | Koscielny → Paulista · 0.160 | Koscielny → Paulista · 0.160 |
| 80 | Koscielny → Paulista · 0.219 | Koscielny → Paulista · 0.225 | Koscielny → Paulista · 0.204 | Koscielny → Paulista · 0.229 | Koscielny → Paulista · 0.170 | Koscielny → Paulista · 0.202 |
| 85 | Move · 0.169 | Wait | Move · 0.217 | Wait | Move · 0.185 | Wait |
| 90 | Wait | Wait | Wait | Wait | Wait | Wait |

## Visible story and events

Score below is Liverpool–Arsenal. Events must occur strictly before a checkpoint to appear in its state; an event at exactly 70:00 is not included at the 70:00 checkpoint.

| Checkpoint | Score | New major events since the previous checkpoint |
|---|---|---|
| 0 | 0–0 | No new goal, card or substitution |
| 5 | 0–0 | No new goal, card or substitution |
| 10 | 0–0 | No new goal, card or substitution |
| 15 | 0–0 | No new goal, card or substitution |
| 20 | 0–0 | 18:28 card: Adam Lallana (yellow) |
| 25 | 0–0 | No new goal, card or substitution |
| 30 | 0–1 | 27:40 goal: Aaron Ramsey |
| 35 | 0–1 | 32:53 card: Mamadou Sakho (yellow) |
| 40 | 0–1 | No new goal, card or substitution |
| 45 | 0–1 | 44:43 card: Laurent Koscielny (yellow) |
| 50 | 0–1 | No new goal, card or substitution |
| 55 | 0–1 | No new goal, card or substitution |
| 60 | 0–1 | 58:00 substitution: Roberto Firmino → Christian Benteke |
| 65 | 0–1 | 61:36 card: Joel Campbell (yellow); 64:00 substitution: Héctor Bellerín → Calum Chambers |
| 70 | 0–1 | No new goal, card or substitution |
| 75 | 0–1 | 70:00 substitution: Adam Lallana → João Carlos; 73:28 card: Kolo Touré (yellow); 74:00 substitution: Joel Campbell → Alex Oxlade-Chamberlain |
| 80 | 1–1 | 78:23 goal: Emre Can |
| 85 | 2–1 | 82:45 goal: João Carlos |
| 90 | 2–1 | No new goal, card or substitution |

## Most useful comparisons

- **25, balanced/win:** Move, 0.35323. Flamini moves from left to right defensive midfield; Ramsey moves from right to left. The shape remains 4-2-3-1. This is an early role-fit example, not a new formation or a measured improvement in play.
- **55, balanced:** Bellerín → Chambers first passes at the displayed rounded benefit 0.150. Attack and defend do not recommend a change. Because it sits on the boundary, 60 is clearer for presenting that substitution.
- **60:** Balanced recommends Bellerín → Chambers (0.19406), defend also recommends it (0.19155), attack waits. This is an optional same-minute approach comparison, not proof that the balanced decision is professionally correct.
- **65, attack/win:** Campbell → Oxlade-Chamberlain, 0.19201; second option Koscielny → Gabriel, 0.18622. Third option Mertesacker → Gabriel scores 0.16036, above 0.15, but fails the tactical-loss quality gate. This is the strongest compact demonstration of alternatives and multiple decision gates.
- **70:** Attack selects Mertesacker → Gabriel (0.25916); defend selects Campbell → Oxlade-Chamberlain (0.21879). The approach can change the chosen player pair. Do not claim that attack always means adding a striker.
- **75:** The scripted Campbell → Oxlade-Chamberlain change at 74:00 is now in the actual replay XI. It was scripted independently of the earlier inspected recommendation. The scenario is authored; this overlap is not independent predictive validation.
- **80:** The 78:23 equalizer is visible; Koscielny → Gabriel is selected under all six contexts, with different scores.
- **85, attack/win:** Arsenal trails 2–1, with one substitution left. Repositioning scores 0.21695. The best swap contributes only 0.11498 beyond the best no-swap action. With objective draw, repositioning falls to 0.08678 and the best swap scores 0.14756, below 0.15, so the result is Wait. This is an observable policy boundary, not evidence that waiting while behind is the best football decision.
- **90:** All Arsenal contexts return Wait. In attack/win, the tactical benefit remains 0.11337 and best swap 0.06715; the need has not been artificially reset to zero. Both are below threshold.

## Liverpool cross-check

All six contexts were evaluated at every checkpoint as well. At 65, balanced/attack select repositioning in 4-3-3; defend selects Ibe → Lucas in 4-1-4-1 (0.18767). At 85, balanced selects Ibe → Lucas (0.16817), defend selects the same pair (0.17133), and attack waits. If an actual recommended formation change is essential to the film, Liverpool 85 balanced is a short optional insert; the main recording route stays with Arsenal.

## Limits to keep visible in the claims

The early Arsenal tactical recommendation repeatedly swaps the same two midfield positions. This deserves football review; do not present repeated identical advice as fresh discoveries. Yellow cards are shown and available to explanations, but are not an independently calibrated sending-off-risk penalty in the optimizer. There are no red cards in this authored scenario. The replay is fixed: inspection does not execute a recommendation or alter future goals. We have not changed the scenario, thresholds or ratings to improve the video.

Reproduce: `PYTHONPATH=src:scripts python scripts/audit_recording_route.py` on Unix, or set PYTHONPATH appropriately on Windows. The CSV includes every team/minute/approach/objective combination.
