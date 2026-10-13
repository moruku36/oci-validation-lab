"""Offline documentation checks; never connects to OCI or GitHub."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
files = sorted(root.rglob('*.md'))
for path in files:
    if '.git' in path.parts:
        continue
    content = path.read_text(encoding='utf-8-sig')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        if re.match(r'^[a-z][a-z0-9+.-]*:', target, flags=re.I) or target.startswith('#'):
            continue
        local = target.split('#')[0].strip('<>')
        if local and not (path.parent / local).exists():
            errors.append(f'{path.relative_to(root)}: missing target {target}')
    if content.count('```') % 2:
        errors.append(f'{path.relative_to(root)}: unbalanced code fences')
    for forbidden in ('-----BEGIN PRIVATE KEY-----', '-----BEGIN RSA PRIVATE KEY-----'):
        if forbidden in content:
            errors.append(f'{path.relative_to(root)}: private-key marker')
    if re.search(r'ocid1\.[a-z0-9]+\.[^\s`]+', content):
        errors.append(f'{path.relative_to(root)}: raw OCID-like value')
for name in ('README.md', 'README.ja.md'):
    content = (root / name).read_text(encoding='utf-8')
    for fact in ('2026-10-13', '1Z0-1085-26', '1Z0-1085-26-JPN', 'Level 1', 'Level 2', 'Level 3'):
        if fact not in content:
            errors.append(f'{name}: missing shared fact {fact}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(files)} Markdown files; local file links, fences, basic secret markers, README shared facts')
print('External URLs, anchors, exam coverage, semantic parity and secret completeness need manual review.')
