"""Enumerate all demo checkpoints/coach intents without changing the match.

Optional live checks call only health/evaluate, never the model. Output contains
computed summaries, not raw player-profile inputs. This is coverage, not coaching
accuracy or counterfactual outcome validation.
"""
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import subprocess
import time
import urllib.request

from synthetic_coach_room import create_synthetic_room
from subintel.auto_plans import AutoConfig
from subintel.match_facts import checkpoint_facts

ROOT=Path(__file__).resolve().parents[1]


def compact(plan):
    if not plan: return None
    return dict(kind=plan['plan_kind'],outgoing=(plan.get('out_player') or {}).get('name'),
                incoming=(plan.get('in_player') or {}).get('name'),formation=plan.get('formation'),
                benefit=plan.get('expected_benefit'),recommended=plan.get('recommended'),
                quality_gate=plan.get('quality_gate_passed'),clears_threshold=plan.get('clears_threshold'),
                moves=[dict(player=x['name'],before=x['before_position'],after=x['after_position']) for x in plan.get('repositioned',[])],
                tactical=(plan.get('score_components') or {}).get('tactical_benefit'),
                freshness=(plan.get('score_components') or {}).get('freshness_benefit'))


def signature(snapshot):
    return dict(recommendation=snapshot['recommendation'],state=snapshot['state'],
                selected=compact(snapshot.get('selected_plan')),threshold=snapshot['threshold'],
                alternatives=[compact(x) for x in snapshot['alternatives'][:3]])


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,default=ROOT/'docs/research/recording_route_audit_20261026.json')
    parser.add_argument('--live-base')
    args=parser.parse_args()
    baseline=subprocess.check_output(['git','rev-parse','origin/main'],cwd=ROOT,text=True).strip()
    bootstrap,evaluate=create_synthetic_room(scenario='lively')
    fixture=bootstrap['fixtures']['synthetic-demo']
    events=[e for e in fixture['events'] if e['kind'] in ('goal','card','substitution')]
    rows=[]; cached={}; start=time.monotonic()
    for tid,team in (('1','Arsenal'),('24','Liverpool')):
        for minute in range(0,91,5):
            facts=checkpoint_facts(fixture,minute,tid)
            for stance in ('balanced','attack','defend'):
                for objective in ('win','draw'):
                    config=AutoConfig(stance=stance,objective=objective)
                    snapshot=evaluate('synthetic-demo',tid,minute,config.model_dump_json())
                    cached[tid,minute,stance,objective]=signature(snapshot)
                    for plan in snapshot['alternatives']:
                        ids=[p['player_id'] for p in plan['proposed_lineup']]
                        assert len(ids)==len(set(ids))==11
                        assert plan['out_player']['id'] not in ids
                        assert plan['in_player']['id'] in ids
                    rows.append(dict(team=team,team_id=tid,minute=minute,stance=stance,objective=objective,
                                     **signature(snapshot),late_policy=snapshot['late_game_policy'],
                                     team_needs=snapshot['team_needs'],match_facts=facts,
                                     recommended_swaps=sum(p['recommended'] for p in snapshot['alternatives'])))
            print(f'Checked {team} {minute}: {len(rows)}/228',flush=True)
    live=[]; health_before={}; live_error=None
    if args.live_base:
        base=args.live_base.rstrip('/')
        def request(path,payload=None):
            body=None if payload is None else json.dumps(payload).encode()
            req=urllib.request.Request(base+path,data=body,headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req,timeout=60) as response:return json.load(response)
        health_before=request('/healthz')
        for tid,minute,stance,objective in [('1',25,'balanced','win'),('1',65,'attack','win'),('1',85,'attack','win'),('1',85,'attack','draw'),('24',85,'balanced','win')]:
            payload=dict(match_id='synthetic-demo',team_id=tid,minute=minute,config=AutoConfig(stance=stance,objective=objective).model_dump())
            try:
                actual=signature(request('/api/evaluate',payload))
            except OSError as error:
                live_error=type(error).__name__
                break
            expected=cached[tid,minute,stance,objective]
            assert actual==expected,(tid,minute,stance,objective)
            live.append(dict(team_id=tid,minute=minute,stance=stance,objective=objective,matched=True))
        if not live_error:
            health_after=request('/healthz')
            assert health_before['build_sha']==health_after['build_sha']
    counts={team:dict(Counter(r['recommendation'] for r in rows if r['team']==team)) for team in ('Arsenal','Liverpool')}
    result=dict(kind='CHECKPOINT_AND_INTENT_COVERAGE_NOT_COACHING_ACCURACY',source_baseline=baseline,generator=bootstrap['generator'],
                evaluations=len(rows),teams=2,checkpoints_per_team=19,intents_per_checkpoint=6,
                decision_counts=counts,live_checks=live,
                live_build=health_before.get('build_sha'),live_error=live_error,
                elapsed_seconds=round(time.monotonic()-start,2),key_events=events,rows=rows)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    csv_path=args.out.with_suffix('.csv')
    fields=['team','minute','stance','objective','goal_diff','subs_left','recommendation','plan','benefit','formation','recommended_swaps']
    with csv_path.open('w',encoding='utf-8-sig',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields);writer.writeheader()
        for row in rows:
            plan=row['selected'] or {}
            writer.writerow(dict(team=row['team'],minute=row['minute'],stance=row['stance'],objective=row['objective'],
                                 goal_diff=row['state']['goal_diff'],subs_left=row['state']['subs_left'],recommendation=row['recommendation'],
                                 plan=f"{plan['outgoing']} -> {plan['incoming']}" if plan.get('outgoing') else 'Reposition / wait',
                                 benefit=plan.get('benefit'),formation=plan.get('formation'),recommended_swaps=row['recommended_swaps']))
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','key_events')},indent=2))
    if live_error: raise SystemExit('Local coverage saved; requested live comparison was incomplete.')


if __name__=='__main__':main()
