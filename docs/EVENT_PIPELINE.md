# From an event to a bench decision

The running coach room has a deterministic, inspectable pipeline. Player capabilities, recent performance, team deficits, estimated load and plan utility are different quantities. This walkthrough describes the automatic coach-room path, not every legacy research scorer in the repository.

## What comes in

An event contains an ID, match, team, player, period, minute/second and type. Depending on its type it can also contain start/end coordinates, success, recipient, linked key pass, xG, goal/on-target status, a card or a substitute's ID. The engine reads events, not broadcast video. It does not infer tracking positions from the pitch drawing.

The current `lively` scenario contains **1,593 events**:

| Type | Count | Interpretation |
|---|---:|---|
| Pass | 925 | Attempts, successful progression, box entries and receiving in the box |
| Carry | 153 | Progressive carries and entries into the box |
| Pressure | 238 | Individual pressing activity; pressure alone does not imply a turnover |
| Tackle | 72 | Successful tackles count as defensive actions |
| Recovery | 161 | Successful ball recoveries count as defensive actions |
| Miscontrol | 11 | A recorded ball action and ball loss |
| Shot | 22 | Includes the three goal events; xG is supplied by the generator |
| Card | 5 | Booking display/context; the current scenario has five yellows |
| Substitution | 4 | Update active players, entry time, used players and remaining substitutions |
| Period start | 2 | Timing and half-time boundaries |

The schema also represents dribbles, interceptions, blocks, clearances, own goals and red cards. The current scenario does not exercise every supported type. In particular, do not claim that this match demonstrates a live dribbling analysis or a ten-player optimizer.

## Event contributions

[`ComponentTracker`](../src/subintel/metrics.py) is the shared conversion layer:

| Input | Components credited |
|---|---|
| Successful open-play pass entering the box | `ball_actions`, `box_passes`, `prog_passes`; the receiver gets `box_presence` |
| Other successful forward pass | `prog_passes` only if the forward advance is at least 10 coordinate units and its start x is at least 48 |
| Failed open-play pass | `ball_actions` and `ball_losses`, without successful progression |
| Carry | `prog_carries` if it enters the box, or advances at least 10 units and ends at x >= 60; box entry also credits `box_presence` |
| Successful/failed dribble | `ball_actions`; failure also credits `ball_losses` |
| Miscontrol or dispossession | `ball_actions` and `ball_losses` |
| Non-penalty shot | Shooter receives its `npxg`; the linked key passer receives the same amount as `xa` |
| Pressure | One `pressures` contribution |
| Successful tackle, interception, recovery or block | One `def_actions` contribution |

Coordinates use the common 120 x 80 schema, with each acting team attacking toward x = 120. The box is x >= 102 and y between 18 and 62. Progression is a coordinate-based rule, not a learned estimate of pass value. Set-piece passes and penalty shots are excluded from these open-play capability components, while the match statistics and score are calculated separately.

`ball_actions` is an explicitly defined retention denominator: open-play passes, dribbles, miscontrols and dispossessions. It is not every touch, carry or shot. `xa` is the linked shot's supplied xG, not a separately trained assist model. A scored goal changes game state; the live threat vector uses the shot's npxG rather than an additional finishing bonus. Season-profile adjustments separately include observed goals and assists.

## Keeping a useful memory

[`MatchState`](../src/subintel/engine.py) keeps cumulative counts and a recent window. The recent window decays continuously:

```
decay = 0.5 ** (elapsed_minutes / 12)
```

An event from 12 minutes ago has half the weight of a new event. Exposure minutes decay consistently with counts, so a short spell is not compared with a full-match expectation. Substitutions stop accumulating time for the outgoing player and begin the incoming player's exposure. Only events before the checkpoint are fed into the state.

## Player capability and performance

[`demo_dataset.py`](../src/subintel/demo_dataset.py) produces a historical-derived baseline and a bounded recent-form adjustment. These profiles include authored transformations of historical source attributes and observed event evidence; they are not independent synthetic profiles.

[`demo_live.py`](../src/subintel/demo_live.py) compares each player's recent event counts with an expectation:

```
expected_p90 = (historical_count + 5 * role_prior_p90) / (historical_minutes / 90 + 5)
```

The rate is modestly adjusted by capability (`clip(recent_rating / 75, .65, 1.25)`). Attacking/defensive opportunity is adjusted by the team's share of counted ball actions relative to its baseline, bounded to .6–1.4. This is a separate opportunity proxy, not the displayed possession percentage.

```
expected = expected_p90 * recent_exposure_minutes / 90 * opportunity_factor
z = (actual_recent_count - expected) / sqrt(variance)
```

Variance has a floor; xG-valued components use the configured .3 dispersion. Each dimension averages its component z values and applies `tanh(z / 2)` and `exposure / (exposure + 12)` shrinkage. Retention is additionally shrunk for few ball actions. No aerial evidence produces an unknown aerial live value, not an invented good or bad value.

The ability used in planning is `clip(recent_rating + 4 * live_dimension, 0, 100)`. There is **no separate calibrated 1–10 match rating**. Six dimensions are retained in cards; the current automatic plan utility uses threat, creation, progression, retention and defense. Aerial/transition/cross counters in legacy scorers must not be presented as extra dimensions in the current automatic utility.

## Estimated fatigue

Fatigue uses minutes played, source stamina and excess pressing/progressive carrying relative to that player’s expected rates:

```
excess(count, rate) = clip(count / max(rate * minutes / 90, 1) - 1, 0, 1)
intensity = 1 + .15 * pressure_excess + .10 * carry_excess
capacity = clip(1 + (stamina - 75) / 150, .8, 1.15)
load_ratio = (minutes / 90) * intensity / capacity
fatigue = clip((load_ratio - .5) / .7, 0, 1) ** 1.5
```

Excess activity is enabled after 15 minutes played. Time creates load even without on-ball events; intensity cannot exceed 1.25. SkillCorner-referenced synthetic distance is displayed as an estimate and is not a sensor input into this formula. The physical model is authored, not validated against tracking for these players.

## How a team weakness is identified

For attacking components, the deficit is expected activity minus actual activity, standardized by the configured variance. Retention compares actual ball losses with expected losses for the opportunities observed. Defensive deficit compares what the **opponent produces against the team** (npxG, box presence and progressive passes/carries) with the team's usual conceded rates. More tackles do not automatically mean that the team is defending well or badly.

[`coach_needs`](../src/subintel/coach_room.py) combines those deficits with approach, result objective, minute and score:

```
need = sigmoid(deficit_signal / 1.5 + 2 * log(importance))
```

A high need means a high current need to improve that dimension. It is not a low capability rating, and it is not simply the inverse of whole-match pass accuracy. A goal still being required is not cancelled by earlier attacking output. These are aggregate weaknesses relative to expectation, not an opponent-specific flank vulnerability detector.

## How this changes the recommendation

[`auto_plans.py`](../src/subintel/auto_plans.py) searches available one-for-one swaps and supported whole-XI assignments, respecting position suitability. It weighs the change in team capabilities by needs, role exposure, evidence and time, subtracts disruption costs, and adds bounded freshness. A swap must beat the best action without a substitution by at least .15 and satisfy the tactical-loss gate. Being tired does not alone guarantee a recommendation.

Yellow cards are display/explanation context, not an independent booking-risk score in this optimizer. Red cards update state and availability, but the automatic assignment solver requires eleven players and reports an unsupported player count after a dismissal rather than inventing a ten-player plan.

## Concrete reproducible trace

[The preserved trace](research/event_pipeline_trace_20261025.json) records actual event contributions, full-match descriptive totals and Arsenal checkpoint inputs. Full-match totals in that file are descriptive; they are not used as future information in checkpoint decisions.

- At 65, Joel Campbell has 64.75 played minutes, intensity 1.1198 and estimated fatigue .3041. His live progression signal is +.3910, adding 1.564 points to his recent progression rating; his threat signal is -.0492, subtracting .1968 points. A player can therefore be tired while still progressing the ball well.
- Calum Chambers entered at 64. At the 65 checkpoint he has one played minute and fatigue zero, with heavily shrunk live evidence.
- Arsenal at 85 attack/win has threat need .8080, creation .7479 and retention .1399; repositioning is preferred. At 90 threat need rises to .8425, but no plan clears the decision gates. A higher need does not guarantee a sufficiently useful bench option.

Reproduce with `python scripts/audit_event_pipeline.py`. The trace is evidence of what the code calculates, not a professional endorsement of its football conclusions. See [Methodology](METHODOLOGY.md), [Hebrew calculation walkthrough](research/CALCULATIONS_SANITY_HE_20261024.md) and [source provenance](submission/DATA_SOURCES.md).
