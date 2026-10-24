"""Ten explanation locales: validated template translation, server-side values, labelled fallback."""
import json
from pathlib import Path
import re
from types import SimpleNamespace

import pytest

from integrated_app import ExplanationCache
from subintel import translation
from subintel.plan_narrative import LANGUAGES, TEMPLATES, explain_plan, source_text
from subintel.translation import LANGUAGE_NAMES, TRUSTED, TranslationCatalog, TranslationRejected, validate

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = {k: v for k, v in json.loads((ROOT/'tests/fixtures/translations.json').read_text(encoding='utf-8')).items() if not k.startswith('_')}
LRI, PDI = '⁦', '⁩'


def sample(benefit=.2):
    plan = dict(plan_kind='SUBSTITUTION', out_player=dict(id='off', name='Player Off'), in_player=dict(id='on', name='Player On'),
                formation='4-3-3', recommended=True, quality_gate_passed=True, clears_threshold=True, decision_basis='FRESH_LEGS',
                change_type='LIKE_FOR_LIKE', repositioned=[], proposed_lineup=[dict(player_id=str(i)) for i in range(11)],
                expected_benefit=benefit, lineup_changes=dict(threat=2, defense=-1), score_components=dict(tactical_benefit=.1, freshness_benefit=.1))
    return dict(minute=65, state=dict(goal_diff=-1), team_id='24', coach_config=dict(stance='attack', objective='win'),
                recommendation='SUBSTITUTION', alternatives=[plan], selected=plan, best_no_substitution=None, threshold=.15,
                provenance={}, formation_only={}, team_needs=dict(threat=.7))


def client(lang, mutate=None, fail=None):
    """Selection returns decision + freshness + score; translation answers from the reviewed fixtures."""
    calls = []
    by_source = {source_text(k): v for k, v in FIXTURES.get(lang, {}).items()}
    def create(**kwargs):
        calls.append(kwargs)
        if kwargs['response_format']['type'] == 'json_object' and 'fact_ids' in kwargs['messages'][0]['content']:
            content = '{"fact_ids":["decision","freshness","score"],"style":"direct"}'
        else:
            if fail:
                raise fail
            items = json.loads(kwargs['messages'][1]['content'])['items']
            out = {alias: by_source[english] for alias, english in items.items()}
            content = json.dumps(dict(translations=mutate(out) if mutate else out), ensure_ascii=False)
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=content))])
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create))), calls


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    for key in ('FOUNDRY_ENDPOINT', 'FOUNDRY_API_KEY', 'FOUNDRY_DEPLOYMENT'):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setattr(translation, 'SCHEMA_SUPPORTED', [True])


def test_the_page_offers_exactly_the_supported_locales():
    html = (ROOT/'web/coach-room/index.html').read_text(encoding='utf-8')
    select = re.search(r'<select id="explainLang"[^>]*>(.*?)</select>', html).group(1)
    assert tuple(re.findall(r'<option value="([\w-]+)"', select)) == LANGUAGES
    assert set(LANGUAGE_NAMES) == set(LANGUAGES) - set(TRUSTED) and len(LANGUAGES) == 10


@pytest.mark.parametrize('lang', sorted(FIXTURES))
def test_reviewed_fixtures_pass_validation(lang):
    validate(lang, {k: source_text(k) for k in FIXTURES[lang]}, FIXTURES[lang])
    covered = set(FIXTURES[lang])
    assert {'tpl:decision.swap.rejected', 'tpl:tradeoff', 'tpl:freshness.coach', 'tpl:stats.unavailable', 'tpl:score'} <= covered


@pytest.mark.parametrize('change,rule', [
    (lambda t: t.replace('{on}', 'X'), 'placeholders'),
    (lambda t: t + ' {minute}', 'placeholders'),
    (lambda t: t.replace('{off}', '{off} {off}'), 'placeholders'),
    (lambda t: t.replace('{on}', '{player}'), 'placeholders'),
    (lambda t: t.replace('{on}', '{{on}}'), 'braces'),
    (lambda t: t + ' 9', 'digits'),
    (lambda t: '', 'empty'),
])
def test_tampered_translations_are_rejected(change, rule):
    key = 'tpl:decision.swap.rejected'
    with pytest.raises(TranslationRejected) as error:
        validate('fr', {key: source_text(key)}, {key: change(FIXTURES['fr'][key])})
    assert error.value.rule == rule


def test_lost_negation_missing_and_extra_ids_are_rejected():
    key = 'tpl:decision.swap.rejected'
    with pytest.raises(TranslationRejected, match='negation'):
        validate('fr', {key: source_text(key)}, {key: "L'option est {on} à la place de {off} ; elle respecte les règles de recommandation."})
    with pytest.raises(TranslationRejected, match='negation'):
        validate('zh-Hans', {key: source_text(key)}, {key: '该选项是用 {on} 换下 {off}；它符合推荐规则。'})
    with pytest.raises(TranslationRejected, match='ids'):
        validate('fr', {key: source_text(key), 'tpl:score': source_text('tpl:score')}, {key: FIXTURES['fr'][key]})
    with pytest.raises(TranslationRejected, match='ids'):
        validate('fr', {key: source_text(key)}, {key: FIXTURES['fr'][key], 'extra': 'x'})


@pytest.mark.parametrize('lang', sorted(FIXTURES))
def test_translated_explanation_keeps_server_values_and_identity(lang):
    stub, calls = client(lang)
    catalog = TranslationCatalog()
    r = explain_plan(sample(), 'swap:off:on', 'analyst', lang, client=stub, deployment='gpt-4.1-mini', catalog=catalog)
    assert r['source'] == 'llm' and r['translation'] == dict(status='model', model='gpt-4.1-mini', cached=False)
    assert r['output_lang'] == lang and r['plan_id'] == 'swap:off:on'
    for value in ('Player On', 'Player Off', '0.200', '0.150', FIXTURES[lang]['term:dim.defense']):
        assert value in r['text']
    assert 'Bringing on' not in r['text']
    assert (LRI + 'Player On' + PDI in r['text']) == (lang == 'ar')
    request = calls[1]
    assert request['response_format']['type'] == 'json_schema' and request['response_format']['json_schema']['strict']
    assert 'Player On' not in request['messages'][1]['content'] and '0.200' not in request['messages'][1]['content']
    again = explain_plan(sample(), 'swap:off:on', 'analyst', lang, client=stub, deployment='gpt-4.1-mini', catalog=catalog)
    assert again['translation']['cached'] and len(calls) == 3 and again['text'] == r['text']


def test_negative_scores_are_inserted_verbatim():
    stub, _ = client('ar')
    r = explain_plan(sample(-.056), 'swap:off:on', 'analyst', 'ar', client=stub, deployment='d', catalog=TranslationCatalog())
    assert f'{LRI}-0.056{PDI}' in r['text']
    stub, _ = client('de')
    assert '-0.056' in explain_plan(sample(-.056), 'swap:off:on', 'analyst', 'de', client=stub, deployment='d', catalog=TranslationCatalog())['text']


def test_rejected_translation_falls_back_to_labelled_english():
    stub, calls = client('fr', mutate=lambda out: {k: v.replace('{on}', '') for k, v in out.items()})
    catalog = TranslationCatalog()
    r = explain_plan(sample(), 'swap:off:on', 'analyst', 'fr', client=stub, deployment='d', catalog=catalog)
    assert r['output_lang'] == 'en' and r['text'].startswith('The recommendation is Player On for Player Off')
    assert r['translation']['status'] == 'fallback' and r['translation']['note'] == 'TRANSLATION_REJECTED'
    diagnostic = r['translation']['diagnostic']
    assert diagnostic['code'] == 'TRANSLATION_REJECTED' and diagnostic['rule'] == 'placeholders' and diagnostic['item'] == 'tpl:decision.swap.recommended'
    # Selection, the first translation and one retry; the broken template is never cached, the valid ones are.
    assert r['source'] == 'llm' and len(calls) == 3
    assert catalog.missing('fr', ['tpl:decision.swap.recommended', 'tpl:score']) == ['tpl:decision.swap.recommended']


def test_one_retry_translates_only_the_rejected_template():
    answers = []
    def mutate(out):
        answers.append(dict(out))
        return {k: v.replace('{on}', '') for k, v in out.items()} if len(answers) == 1 else out
    stub, calls = client('fr', mutate=mutate)
    catalog = TranslationCatalog()
    r = explain_plan(sample(), 'swap:off:on', 'analyst', 'fr', client=stub, deployment='d', catalog=catalog)
    assert r['output_lang'] == 'fr' and r['translation'] == dict(status='model', model='d', cached=False, retried=True)
    retry = calls[2]
    assert list(json.loads(retry['messages'][1]['content'])['items'].values()) == [source_text('tpl:decision.swap.recommended')]
    assert translation.RETRY_HINT['placeholders'] in retry['messages'][0]['content']
    assert translation.RETRY_HINT['placeholders'] not in calls[1]['messages'][0]['content']


def test_no_retry_when_the_first_translation_used_the_time_budget(monkeypatch):
    from subintel import plan_narrative
    monkeypatch.setattr(plan_narrative, 'RETRY_WITHIN_SECONDS', -1)
    stub, calls = client('fr', mutate=lambda out: {k: v.replace('{on}', '') for k, v in out.items()})
    r = explain_plan(sample(), 'swap:off:on', 'analyst', 'fr', client=stub, deployment='d', catalog=TranslationCatalog())
    assert r['translation']['status'] == 'fallback' and len(calls) == 2


def test_vocabulary_is_sent_with_usage_notes_and_never_with_values():
    stub, calls = client('es')
    explain_plan(sample(), 'swap:off:on', 'analyst', 'es', client=stub, deployment='d', catalog=TranslationCatalog())
    payload = json.loads(calls[1]['messages'][1]['content'])
    noted = {payload['items'][a]: text for a, text in payload['notes'].items()}
    assert 'never as a verb or participle' in noted['defending']
    assert all(alias in payload['items'] for alias in payload['notes'])
    assert '{on} is the substitute coming on' in calls[1]['messages'][0]['content']
    for value in ('Player On', 'Player Off', '0.200', '0.150'):
        assert value not in calls[1]['messages'][1]['content']


def test_notes_name_the_infinitive_form_and_club_agreement_where_the_live_run_went_wrong():
    from subintel.translation import note
    aim = 'term:aim.threat'
    assert '"zu"' in note(aim, source_text(aim), 'de') and 'こと' in note(aim, source_text(aim), 'ja')
    assert '"zu"' not in note(aim, source_text(aim), 'fr')
    stats = 'tpl:stats.attack.context'
    assert 'usually singular' in note(stats, source_text(stats), 'it')
    assert 'case ending' in note('tpl:move.item', source_text('tpl:move.item'), 'de')
    assert 'von der Position {before} auf die Position {after}' in note('tpl:move.item', source_text('tpl:move.item'), 'de')
    assert 'von der Position' not in note('tpl:move.item', source_text('tpl:move.item'), 'fr')
    assert note('tpl:score', source_text('tpl:score'), 'de') is None


def test_japanese_does_not_repeat_the_nominaliser():
    from subintel.plan_narrative import Term, render
    # Verbatim shape from the third live run: the aim ends in こと and the template adds another.
    text = render('tradeoff.gain', {'aim': Term('aim.threat'), 'dim': Term('dim.defense')}, 'ja',
                  {'tradeoff.gain': 'このプランは{dim}の弱体化を代償にして{aim}ことを目指しています。'},
                  {'aim.threat': '攻撃の脅威を増すこと', 'dim.defense': '守備力'})
    assert text == 'このプランは守備力の弱体化を代償にして攻撃の脅威を増すことを目指しています。'


@pytest.mark.parametrize('lang,item,expected', [
    # Verbatim shapes from the live run of 24 October: the model ended each item with a full stop.
    ('de', '{player} wechselt von {before} zu {after}.', 'A wechselt von L zu R; B wechselt von R zu L.'),
    ('ja', '{player}は{before}から{after}に移動します。', 'Aは左から右に移動します；Bは右から左に移動します。'),
    ('ar', 'ينتقل {player} من {before} إلى {after}', 'ينتقل ⁦A⁩ من L إلى R؛ ينتقل ⁦B⁩ من R إلى L.'),
])
def test_translated_moves_use_the_locale_list_punctuation(lang, item, expected):
    from subintel.plan_narrative import Moves, localized
    left, right = ('左', '右') if lang == 'ja' else ('L', 'R')
    fmap = {'moves': ('moves', {'moves': Moves((('A', 'position.Left Wing', 'position.Right Wing'), ('B', 'position.Right Wing', 'position.Left Wing')))})}
    catalog = TranslationCatalog()
    catalog.add(lang, {'tpl:moves': '{moves}。' if lang == 'ja' else '{moves}.', 'tpl:move.item': item,
                       'term:position.Left Wing': left, 'term:position.Right Wing': right})
    assert localized(fmap, ['moves'], lang, catalog, 'analyst') == expected


def test_french_elision_and_italian_ad_apply_to_vocabulary_but_never_to_names():
    from subintel.plan_narrative import Term, render
    terms = {'aim.threat': 'ajouter une menace offensive', 'intent.extend': 'augmenter l’avance'}
    templates = {'gain': "L'objectif est de {aim}.", 'state.lead': '{team} mène {score} ; la priorité est de {objective}.',
                 'name': 'Le remplacement de {off}.'}
    assert render('gain', {'aim': Term('aim.threat')}, 'fr', templates, terms) == "L'objectif est d'ajouter une menace offensive."
    assert render('state.lead', {'team': 'Arsenal', 'score': '1–0', 'objective': Term('intent.extend')}, 'fr', templates, terms).endswith("est d'augmenter l’avance.")
    assert render('name', {'off': 'Aaron Ramsey'}, 'fr', templates, terms) == 'Le remplacement de Aaron Ramsey.'
    assert render('gain', {'aim': Term('aim.threat')}, 'it', {'gain': 'Il piano mira a {aim}.'}, {'aim.threat': 'aumentare la minaccia'}) == 'Il piano mira ad aumentare la minaccia.'
    assert render('gain', {'aim': Term('aim.threat')}, 'it', {'gain': 'Il piano mira a {aim}.'}, {'aim.threat': 'creare più occasioni'}) == 'Il piano mira a creare più occasioni.'


def test_chinese_and_japanese_drop_spaces_between_their_own_characters_only():
    from subintel.plan_narrative import Term, render
    templates = {'stats': '{team} 在 {score} 时处于 {situation} 状态。'}
    text = render('stats', {'team': 'Arsenal', 'score': '1–0', 'situation': Term('situation.lead')}, 'zh-Hans', templates, {'situation.lead': '领先'})
    assert text == 'Arsenal 在 1–0 时处于领先状态。'


@pytest.mark.parametrize('error,code', [(TimeoutError('slow'), 'NETWORK_TIMEOUT'), (ValueError('not json'), 'UNEXPECTED_CLIENT_ERROR')])
def test_translation_failures_fall_back_to_english(error, code):
    stub, _ = client('ja', fail=error)
    r = explain_plan(sample(), 'swap:off:on', 'coach', 'ja', client=stub, deployment='d', catalog=TranslationCatalog())
    assert r['output_lang'] == 'en' and r['translation']['note'] == 'TRANSLATION_UNAVAILABLE'
    assert r['translation']['diagnostic']['code'] == code


def test_no_model_means_no_translation_but_trusted_languages_still_work():
    r = explain_plan(sample(), 'swap:off:on', 'broadcaster', 'es', catalog=TranslationCatalog())
    assert r['output_lang'] == 'en' and r['translation'] == dict(status='fallback', note='TRANSLATION_NOT_CONFIGURED', diagnostic=None)
    he = explain_plan(sample(), 'swap:off:on', 'broadcaster', 'he', catalog=TranslationCatalog())
    assert he['output_lang'] == 'he' and he['translation'] == dict(status='trusted')
    with pytest.raises(ValueError):
        explain_plan(sample(), 'swap:off:on', 'broadcaster', 'xx')


def test_a_failed_selection_call_does_not_trigger_a_second_slow_call():
    calls = []
    def create(**kwargs):
        calls.append(kwargs)
        raise TimeoutError('provider down')
    stub = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    r = explain_plan(sample(), 'swap:off:on', 'analyst', 'it', client=stub, deployment='d', catalog=TranslationCatalog())
    assert len(calls) == 1 and r['translation']['note'] == 'TRANSLATION_UNAVAILABLE' and r['note'] == 'LLM_UNAVAILABLE'


def test_schema_refusal_downgrades_to_json_object_once():
    error = RuntimeError('bad request'); error.status_code = 400; error.param = 'response_format'
    stub, calls = client('pt', fail=error)
    explain_plan(sample(), 'swap:off:on', 'analyst', 'pt', client=stub, deployment='d', catalog=TranslationCatalog())
    assert translation.SCHEMA_SUPPORTED == [False]
    stub, calls = client('pt')
    r = explain_plan(sample(), 'swap:off:on', 'analyst', 'pt', client=stub, deployment='d', catalog=TranslationCatalog())
    assert calls[1]['response_format'] == {'type': 'json_object'} and r['translation']['status'] == 'model'


def test_fallback_translations_are_not_cached_for_long():
    now = [0.]; calls = []
    def fn(*args):
        calls.append(1)
        return dict(source='llm', text='english', translation=dict(status='fallback'))
    cache = ExplanationCache(fn, clock=lambda: now[0])
    cache.get('k', None, None, None, None); now[0] = 31.; cache.get('k', None, None, None, None)
    assert len(calls) == 2


def test_hebrew_is_hand_written_with_the_same_placeholders():
    from subintel.plan_narrative import TERMS
    assert set(TEMPLATES['he']) == set(TEMPLATES['en']) and set(TERMS['he']) == set(TERMS['en'])
    for key, english in TEMPLATES['en'].items():
        assert sorted(re.findall(r'\{(\w+)\}', english)) == sorted(re.findall(r'\{(\w+)\}', TEMPLATES['he'][key])), key


def test_rejected_plan_stays_negated_after_translation():
    snap = sample()
    snap['alternatives'][0].update(recommended=False, quality_gate_passed=False)
    snap['recommendation'] = 'NO_SUBSTITUTION'
    stub, _ = client('fr')
    r = explain_plan(snap, 'swap:off:on', 'analyst', 'fr', client=stub, deployment='d', catalog=TranslationCatalog())
    assert r['translation']['status'] == 'model' and 'n’est pas recommandé' in r['text'] and FIXTURES['fr']['tpl:quality.loss'] in r['text']


@pytest.mark.parametrize('lang,key,text', [
    # Verbatim from the first live run (24 October): a recommended plan rendered as violating/contradicting/exceeding the rules.
    ('ar', 'tpl:decision.swap.recommended', 'إدخال {on} بدلاً من {off} ينتهك قواعد التوصية.'),
    ('de', 'tpl:decision.swap.recommended', 'Der Wechsel von {off} zu {on} widerspricht den Empfehlungsregeln.'),
    ('pt', 'tpl:decision.swap.recommended', 'Entrar com {on} no lugar de {off} ultrapassa as regras de recomendação.'),
    # A recommended plan must not be negated; a rejected one must keep the "meets" verb under its negation.
    ('fr', 'tpl:decision.swap.recommended', "Faire entrer {on} à la place de {off} ne respecte pas les règles de recommandation."),
    ('es', 'tpl:decision.swap.rejected', 'La opción es {on} en lugar de {off}; no viola las reglas de recomendación.'),
    ('zh-Hans', 'tpl:decision.wait', '目前没有任何变化违反推荐规则。'),
])
def test_recommendation_status_cannot_flip_in_translation(lang, key, text):
    with pytest.raises(TranslationRejected) as error:
        validate(lang, {key: source_text(key)}, {key: text})
    assert error.value.rule == 'status'


def test_status_sentences_with_the_right_polarity_pass():
    for lang, key, text in (('de', 'tpl:decision.swap.recommended', 'Empfohlen wird {on} für {off}.'),
                            ('ar', 'tpl:decision.wait', 'لا يوجد تغيير يستوفي معايير التوصية حاليًا.'),
                            ('ja', 'tpl:decision.wait', '現時点で推奨基準を満たす変更はありません。')):
        validate(lang, {key: source_text(key)}, {key: text})


def test_japanese_and_chinese_sentences_are_not_space_separated():
    for lang in ('ja', 'zh-Hans'):
        stub, _ = client(lang)
        text = explain_plan(sample(), 'swap:off:on', 'analyst', lang, client=stub, deployment='d', catalog=TranslationCatalog())['text']
        assert '。 ' not in text and '。' in text
    stub, _ = client('fr')
    assert '. ' in explain_plan(sample(), 'swap:off:on', 'analyst', 'fr', client=stub, deployment='d', catalog=TranslationCatalog())['text']


def test_translation_request_is_deterministic_and_carries_the_status_glossary():
    stub, calls = client('de')
    explain_plan(sample(), 'swap:off:on', 'analyst', 'de', client=stub, deployment='d', catalog=TranslationCatalog())
    request = calls[1]
    assert request['temperature'] == 0 and 'erfüllt / erfüllt nicht' in request['messages'][0]['content']


def test_translated_moves_keep_both_position_terms_and_server_inserted_name():
    from subintel.plan_narrative import Moves, localized, source_keys
    fmap = {'moves': ('moves', {'moves': Moves((('Player Name', 'position.Left Wing', 'position.Right Midfield'),))})}
    keys = source_keys(fmap, ['moves'])
    assert keys == {'tpl:moves', 'tpl:move.item', 'term:position.Left Wing', 'term:position.Right Midfield'}
    assert all('Player Name' not in source_text(k) for k in keys)
    mapping = {'tpl:moves':'{moves}.', 'tpl:move.item':'{player} wechselt von {before} zu {after}',
               'term:position.Left Wing':'Linksaußen', 'term:position.Right Midfield':'rechtem Mittelfeld'}
    validate('de', {k:source_text(k) for k in keys}, mapping)
    catalog = TranslationCatalog(); catalog.add('de', mapping)
    assert localized(fmap, ['moves'], 'de', catalog, 'analyst') == 'Player Name wechselt von Linksaußen zu rechtem Mittelfeld.'
