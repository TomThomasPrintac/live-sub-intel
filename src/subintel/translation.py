"""Model translation of fixed English sentence templates, validated before use.

Only templates and vocabulary are translated, never values: player names, numbers,
plan identity and statuses are inserted by the server afterwards through
placeholders. A translation is accepted only if every placeholder survives exactly
once, no digit or ID is added or lost, and a negated English sentence stays
negated. Structural checks do not prove semantic fidelity; see
tests/fixtures/translations.json for reviewed examples.
"""
import json
import re
import threading
from collections import Counter

TRANSLATION_PROMPT_VERSION = 'template-translation-v5-forms'
TRUSTED = ('en', 'he')  # hand-written templates in plan_narrative
LANGUAGE_NAMES = {'ar': 'Arabic', 'es': 'Spanish', 'fr': 'French', 'de': 'German', 'it': 'Italian',
                  'pt': 'Portuguese', 'ja': 'Japanese', 'zh-Hans': 'Simplified Chinese'}
PLACEHOLDER = re.compile(r'\{(\w+)\}')
ENGLISH_NEGATION = re.compile(r"\b(not|no|never|nothing)\b|n't\b", re.IGNORECASE)
NEGATION = {
    'es': r'\b(no|ni|sin|nunca|ningún|ninguna|ninguno)\b',
    'fr': r"\b(ne|pas|non|aucun|aucune|sans|jamais)\b|\bn['’]",
    'de': r'\b(nicht|kein|keine|keinen|keinem|keiner|keines|ohne|nie)\b',
    'it': r'\b(non|senza|nessun|nessuna|nessuno|mai)\b',
    'pt': r'\b(não|nao|sem|nenhum|nenhuma|nunca)\b',
    'ar': r'(?<!\w)و?(لا|لم|لن|ليس|ليست|غير|دون|بدون)(?!\w)',
    'ja': r'(ない|ません|ず|未|不|無)',
    'zh-Hans': r'(不|未|没|无|非)',
}
# A sentence about the recommendation criteria must say "meets" with the language's ordinary verb:
# the first live run turned "passes the recommendation rules" into "violates", "contradicts" and "exceeds".
STATUS_SOURCE = re.compile(r'recommendation criteria', re.IGNORECASE)
STATUS_VERB = {
    'es': r'\b(cumple|cumplen|satisface|reúne)\b',
    'fr': r'\b(respecte|remplit|satisfait)\b',
    'de': r'\b(erfüllt|erfüllen|entspricht)\b',
    'it': r'\b(soddisfa|rispetta|soddisfano)\b',
    'pt': r'\b(cumpre|atende|satisfaz)\b',
    'ar': r'(يستوفي|تستوفي|يلبي|تلبي|يفي|تفي)',
    'ja': r'(満たし|満たす|適合)',
    'zh-Hans': r'(符合|满足)',
}
RECOMMENDATION_SOURCE = re.compile(r'The recommendation is \{on\} for \{off\}|This change is not recommended',re.IGNORECASE)
RECOMMENDATION_WORD = {
 'es':r'(recomend|recomiend)', 'fr':r'recommand', 'de':r'(empfohl|empfehl|empfiehl)',
 'it':r'(raccomand|consigli|sugger)', 'pt':r'recomend', 'ar':r'(يوصى|توصي|ينصح|الموصى|التوصية|موصى)',
 'ja':r'(推奨|勧め|すすめ|提案)', 'zh-Hans':r'(建议|推荐)',
}
STATUS_OPPOSITE = {
    'es': r'(viola|contradice)', 'fr': r'(viole|contredit)',
    'de': r'(widerspricht|verletzt|verstößt)', 'it': r'(viola|contraddice)',
    'pt': r'(viola|contraria|ultrapassa)', 'ar': r'(ينتهك|يخالف)',
    'ja': r'(違反|反する)', 'zh-Hans': r'(违反|违背)',
}

STATUS_EXAMPLE = {'es': 'cumple / no cumple', 'fr': 'respecte / ne respecte pas', 'de': 'erfüllt / erfüllt nicht',
                  'it': 'soddisfa / non soddisfa', 'pt': 'cumpre / não cumpre', 'ar': 'يستوفي / لا يستوفي',
                  'ja': '満たしています / 満たしていません', 'zh-Hans': '符合 / 不符合'}
SENTENCE_JOIN = {'ja': '', 'zh-Hans': ''}  # these scripts do not put spaces between sentences
# Where each kind of vocabulary is inserted, so a term is translated in the form its sentences need
# (the live run of 24 October produced "sind führt", and "defending" as a verb after "weaker"). Never values.
NOTES = {
    'term:dim.': 'A noun phrase naming a team quality. It fills {dim} in "at the cost of weaker {dim}" and "The weaker {dim} would '
                 'outweigh the fresh legs". Translate it as a noun (for example "defending" means the team\'s defence), never as a verb or participle.',
    'term:aim.': 'An infinitive verb phrase. It fills {aim} in "The aim is to {aim}" and "The plan aims to {aim}, at the cost of weaker {dim}". '
                 'Write the whole phrase that follows "is to" in your language, including any infinitive particle, so no other verb is needed around it.',
    'term:intent.': 'An infinitive verb phrase. It fills {objective} in "the priority is to {objective}". '
                    'Write the whole phrase that follows "is to" in your language, including any infinitive particle.',
    'term:situation.': 'The score situation. It fills {situation} in "{team} are {situation} at {score}" and "With {team} {situation}, the '
                       'recommendation is ...". Choose one form that reads naturally in both, and keep {situation} in those sentences.',
    'term:position.': 'A football position in its basic form, as on a team sheet. It fills {before}, {after} and {position} in '
                      '"{player} moves from {before} to {after}" and "taking the {position} role".',
    'term:stance.': "The coach's brief: how attacking the team should be.",
    'term:objective.': "The coach's objective for the result.",
    'term:role.': 'A broad football role.',
    'tpl:move.item': 'One item of a list that the app joins with semicolons; no final punctuation. Position names are inserted in their basic '
                     'form, so phrase it so they need no case ending (for example "from the {before} position to the {after} position").',
}
# Notes for templates, by the placeholders they contain.
PLACEHOLDER_NOTES = {
    'team': '{team} is a club name: use the verb agreement your language normally uses for a club (usually singular), although British English says "are".',
    'aim': '{aim} is replaced by a complete infinitive phrase that already has any particle it needs; do not wrap it in another verb.',
    'objective': '{objective} is replaced by a complete infinitive phrase that already has any particle it needs; do not wrap it in another verb.',
}
# Where the infinitive form of a language is easy to get wrong (24 October live run: "den Angriff verstärken zu erreichen", "増すであり").
INFINITIVE_FORM = {'de': ' In German, include "zu" (for example "den Angriff zu verstärken").',
                   'ja': ' In Japanese, end it with "こと" so it reads as a noun (for example "攻撃の脅威を増すこと").'}
RETRY_HINT = {
    'placeholders': 'A previous answer dropped, repeated or renamed a {placeholder}; copy every {placeholder} exactly once.',
    'braces': 'A previous answer added braces; use braces only for the {placeholder} names given.',
    'digits': 'A previous answer added or removed digits; keep exactly the digits of the English text.',
    'negation': 'A previous answer lost a negation; keep every negated sentence negated.',
    'status': 'A previous answer changed whether a change is recommended; a recommendation stays a recommendation and a rejected change stays rejected.',
    'length': 'A previous answer was too long; keep each translation close to the English length.',
    'empty': 'A previous answer left an item empty; translate every item.',
}


class TranslationRejected(ValueError):
    def __init__(self, rule, item=None, accepted=None):
        self.rule, self.item = rule, item
        self.accepted = accepted or {}  # items of the same answer that passed every check on their own
        super().__init__(rule)  # never the model's text


def check(lang, key, source, text):
    """Raise TranslationRejected unless one translation keeps its source's structure, negation and status."""
    if not isinstance(text, str) or not text.strip():
        raise TranslationRejected('empty', key)
    if len(text) > 4*len(source) + 60:
        raise TranslationRejected('length', key)
    if Counter(PLACEHOLDER.findall(text)) != Counter(PLACEHOLDER.findall(source)):
        raise TranslationRejected('placeholders', key)
    if text.count('{') != text.count('}') or text.count('{') != len(PLACEHOLDER.findall(source)):
        raise TranslationRejected('braces', key)
    if Counter(re.findall(r'\d', text)) != Counter(re.findall(r'\d', source)):
        raise TranslationRejected('digits', key)
    negated = bool(ENGLISH_NEGATION.search(source))
    if negated and not re.search(NEGATION[lang], text, re.IGNORECASE):
        raise TranslationRejected('negation', key)
    if RECOMMENDATION_SOURCE.search(source):
        if (not re.search(RECOMMENDATION_WORD[lang],text,re.IGNORECASE)
                or re.search(STATUS_OPPOSITE[lang],text,re.IGNORECASE)
                or (not negated and re.search(NEGATION[lang],text,re.IGNORECASE))):
            raise TranslationRejected('status',key)
    if STATUS_SOURCE.search(source):
        # The recommendation status must keep its polarity: the "meets" verb, negated only when the source is.
        if not re.search(STATUS_VERB[lang], text, re.IGNORECASE) or (not negated and re.search(NEGATION[lang], text, re.IGNORECASE)):
            raise TranslationRejected('status', key)


def validate(lang, sources, translations):
    """Raise TranslationRejected unless every translation passes; the error carries the items that did."""
    if not isinstance(translations, dict) or set(translations) != set(sources):
        raise TranslationRejected('ids')
    accepted, first = {}, None
    for key, source in sources.items():
        try:
            check(lang, key, source, translations[key])
            accepted[key] = translations[key]
        except TranslationRejected as error:
            first = first or error
    if first:
        raise TranslationRejected(first.rule, first.item, accepted)


def note(key, source, lang):
    """Fixed usage notes for one item; they describe where it goes, never a value."""
    parts = [text for prefix, text in NOTES.items() if key.startswith(prefix)]
    if key.startswith(('term:aim.', 'term:intent.')):
        parts = [parts[0] + INFINITIVE_FORM.get(lang, '')]
    if key.startswith('tpl:'):
        parts += [PLACEHOLDER_NOTES[name] for name in sorted(set(PLACEHOLDER.findall(source))) if name in PLACEHOLDER_NOTES]
    return ' '.join(parts) or None


class TranslationCatalog:
    """Validated translations per (locale, source key); process-local and versioned through its keys."""
    def __init__(self):
        self.lock = threading.Lock()
        self.entries = {}

    def missing(self, lang, keys):
        with self.lock:
            return sorted({k for k in keys if (lang, k) not in self.entries})

    def add(self, lang, mapping):
        with self.lock:
            self.entries.update({(lang, k): v for k, v in mapping.items()})

    def lookup(self, lang, prefix):
        with self.lock:
            return {k[len(prefix):]: v for (l, k), v in self.entries.items() if l == lang and k.startswith(prefix)}

    def counts(self):
        with self.lock:
            return dict(Counter(lang for lang, _ in self.entries))


SCHEMA_SUPPORTED = [True]  # downgraded once if the deployment refuses json_schema


def translate(client, deployment, lang, sources, retry=None):
    """One bounded call: aliases t0..tn keep property names simple; returns validated translations.

    sources maps catalog keys ('tpl:…', 'term:…') to English; retry names the rule a previous answer broke.
    """
    keys = sorted(sources)
    alias = {f't{i}': k for i, k in enumerate(keys)}
    items = {a: sources[k] for a, k in alias.items()}
    notes = {a: text for a, k in alias.items() if (text := note(k, sources[k], lang))}
    schema = dict(type='object', additionalProperties=False, required=['translations'], properties=dict(
        translations=dict(type='object', additionalProperties=False, required=list(items), properties={a: dict(type='string') for a in items})))
    response_format = ({'type': 'json_schema', 'json_schema': dict(name='template_translations', strict=True, schema=schema)}
                       if SCHEMA_SUPPORTED[0] else {'type': 'json_object'})
    system = (f'Translate football analysis sentence templates and terms from English into {LANGUAGE_NAMES[lang]}. '
              'Return JSON only: {"translations": {"<id>": "<translation>"}} with exactly the same ids. '
              'Keep every {placeholder} exactly as written, untranslated, once each. Do not add numbers, names, facts or explanations. '
              'Keep negations and uncertainty ("estimated", "not a probability") in meaning. Keep "xG" as is. '
              '"Meets the recommendation criteria" means the plan satisfies the rules and is recommended; translate it with the ordinary '
              f'verb for "meets/satisfies" ({STATUS_EXAMPLE[lang]}), never as violating, contradicting or exceeding the rules. '
              '"Bringing on A for B" means A comes on and B goes off. "Weaker" always means a loss. '
              'A recommendation must remain a recommendation, and a change described as not recommended must stay rejected. Never reverse player movement direction (from/to). '
              'Placeholders: {on} is the substitute coming on and {off} the player going off, so "{on} for {off}" means bringing on {on} in place of {off}; '
              '{team}, {team_name} and {opponent} are team names (grammatically singular); {player} is a player name; {score} is a score such as 1–0; '
              'the others are numbers, a formation, a list of movements, or one of the terms. '
              'Terms are short phrases inserted into the sentences; "notes" says where each one goes, so translate it in the form that reads naturally there. '
              'Use a neutral, professional sports-analysis register.' + (' ' + RETRY_HINT[retry] if retry in RETRY_HINT else ''))
    try:
        response = client.chat.completions.create(model=deployment, max_completion_tokens=1500, temperature=0, response_format=response_format,
                                                  messages=[{'role': 'system', 'content': system},
                                                            {'role': 'user', 'content': json.dumps(dict(items=items, notes=notes), ensure_ascii=False)}])
    except Exception as error:
        if getattr(error, 'status_code', None) == 400 and getattr(error, 'param', None) == 'response_format':
            SCHEMA_SUPPORTED[0] = False
        raise
    try:
        data = json.loads(response.choices[0].message.content or '')
    except json.JSONDecodeError:
        raise TranslationRejected('json') from None
    translated = data.get('translations') if isinstance(data, dict) else None
    try:
        validate(lang, items, translated)
    except TranslationRejected as error:
        # Report catalog keys (server-defined IDs), not aliases.
        raise TranslationRejected(error.rule, alias.get(error.item), {alias[a]: t for a, t in error.accepted.items()}) from None
    return {alias[a]: text for a, text in translated.items()}
