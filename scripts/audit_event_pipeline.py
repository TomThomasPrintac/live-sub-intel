"""Trace actual component contributions and checkpoint inputs; no model calls.

    python scripts/audit_event_pipeline.py --out /path/to/trace.json

This is an audit of computation, not a benchmark of football decision quality.
"""
import argparse
from collections import Counter, defaultdict
from dataclasses import asdict
import json
from pathlib import Path

from integrated_app import ExplainRequest, IntegratedApp
from run_synthetic_demo import DEFAULT_SEED, simulate
from synthetic_coach_room import create_synthetic_room
from subintel.demo_data import load_demo_profiles
from subintel.metrics import ComponentTracker
from subintel.schema import Event

ROOT = Path(__file__).resolve().parents[1]


def build_trace():
    dataset = load_demo_profiles()
    evidence = json.loads((ROOT / 'demo_data/source_evidence.json').read_text(encoding='utf-8'))
    raw, _ = simulate(dataset, evidence, apply_substitutions=False, collect_snapshots=False, scenario='lively')
    tracker = ComponentTracker()
    totals, examples, event_types = defaultdict(Counter), {}, Counter()
    for item in raw:
        event = Event.model_validate(item)
        event_types[event.type.value] += 1
        contributions = list(tracker.feed(event))
        for contribution in contributions:
            totals[contribution.team_id][contribution.component] += contribution.value
        if contributions and event.type.value not in examples:
            examples[event.type.value] = dict(event=event.model_dump(exclude_none=True),
                                              contributions=[asdict(c) for c in contributions])

    bootstrap, evaluate = create_synthetic_room(scenario='lively')
    app = IntegratedApp(bootstrap, evaluate)
    profiles = {str(p['player_id']): p for p in dataset['players']}
    checkpoints = []
    for minute in (30, 65, 85, 90):
        snapshot = app.snapshot(ExplainRequest(match_id='synthetic-demo', team_id='1', minute=minute,
            config=dict(stance='attack', objective='win', formation='auto', freshness_cap=1), plan_id='wait'))
        players = []
        for pid, live in snapshot['player_live'].items():
            if profiles[pid]['primary_role'] == 'GK':
                continue
            recent = profiles[pid]['recent']['ratings']
            players.append(dict(id=pid, name=profiles[pid]['name'], minutes=live['minutes_played'],
                fatigue=live['fatigue'], intensity=live['intensity'], load_ratio=live['load_ratio'], recent=recent,
                live_dimensions=live['dimensions'], effective={d: round(max(0, min(100, recent[d] + 4*v)), 4)
                    for d, v in live['dimensions'].items() if v is not None},
                recent_window_minutes=live['recent_window_minutes'], recent_window=live['recent_window']))
        checkpoints.append(dict(minute=minute, state=snapshot['state'], needs=snapshot['team_needs'],
            importance=snapshot['importance'], deficit_z=snapshot['performance_deficit_z'],
            recommendation=snapshot['recommendation'], selected_plan_id=snapshot['selected_plan_id'], players=players))
    return dict(kind='REPRODUCIBLE_EVENT_PIPELINE_TRACE_NOT_FOOTBALL_VALIDATION', seed=DEFAULT_SEED,
        generator=bootstrap['generator'], scenario='lively', event_counts=dict(event_types),
        full_match_component_totals={team: dict(values) for team, values in totals.items()},
        contribution_examples=examples, arsenal_checkpoints=checkpoints)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ROOT / 'docs/research/event_pipeline_trace_20261025.json')
    args = parser.parse_args()
    report = build_trace()
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(events=sum(report['event_counts'].values()), event_counts=report['event_counts'],
                          checkpoint_count=len(report['arsenal_checkpoints'])), ensure_ascii=True))


if __name__ == '__main__':
    main()
