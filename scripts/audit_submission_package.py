"""Read-only checks of tracked submission files; never prints matched secrets.

Run from a Git checkout. Findings are packaging issues, not legal clearance or
an exhaustive security audit. Remote links and ignored local files are excluded.
"""
import collections
import gzip
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = {
    'private_key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'github_token': re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{50,}\b'),
    'openai_key': re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_-]{40,}\b'),
}


def audit():
    names = subprocess.check_output(['git', 'ls-files'], cwd=ROOT, text=True).splitlines()
    issues = []
    counts = collections.Counter()
    for name in names:
        path = ROOT / name
        if not path.exists():
            issues.append(dict(file=name, kind='MISSING_TRACKED_FILE'))
            continue
        data = path.read_bytes()
        if name.endswith(('.json', '.json.gz')):
            try:
                json.loads(gzip.decompress(data) if name.endswith('.gz') else data)
                counts['json_documents'] += 1
            except (ValueError, OSError, EOFError, UnicodeError):
                issues.append(dict(file=name, kind='INVALID_JSON'))
        if name.endswith('.svg'):
            try:
                ET.fromstring(data)
                counts['svg_documents'] += 1
            except ET.ParseError:
                issues.append(dict(file=name, kind='INVALID_SVG'))
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                issues.append(dict(file=name, kind='POSSIBLE_SECRET', pattern=label))
        if not name.endswith('.md'):
            continue
        counts['markdown_documents'] += 1
        without_fences = re.sub(r'```.*?```', '', text, flags=re.S)
        for target in re.findall(r'\]\(([^\n]+?)\)', without_fences):
            target = target.split(' "')[0].strip('<>')
            if target.startswith(('https:', 'http:', 'mailto:', '#', 'codex:')):
                continue
            target = unquote(target.split('#')[0])
            if not (path.parent / target).exists():
                issues.append(dict(file=name, kind='BROKEN_LOCAL_LINK', target=target))
    return dict(tracked_files=len(names), checked=dict(counts), issues=issues,
                scope='Tracked files; relative Markdown file links; JSON/gzip JSON; SVG XML; selected secret patterns. No remote-link, anchor, exhaustive secret or legal certification.')


if __name__ == '__main__':
    result = audit()
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(result['issues']))
