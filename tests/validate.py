#!/usr/bin/env python3
"""Check metadata, required skill files and Claude plugin mirror. --sync copies canonical skill to mirror."""
import argparse, json, pathlib, shutil, sys
root=pathlib.Path(__file__).resolve().parents[1]
canonical=root/'skills/careerkit'
mirror=root/'plugins/careerkit/skills/careerkit'
parser=argparse.ArgumentParser(); parser.add_argument('--sync',action='store_true'); args=parser.parse_args()
if args.sync:
    if mirror.exists(): shutil.rmtree(mirror)
    shutil.copytree(canonical,mirror)
for path in [root/'.claude-plugin/marketplace.json',root/'plugins/careerkit/.claude-plugin/plugin.json']:
    json.loads(path.read_text())
meta=json.loads((root/'.claude-plugin/marketplace.json').read_text())
assert meta['plugins'][0]['source']=='./plugins/careerkit'
assert meta['plugins'][0]['name']=='careerkit'
assert (canonical/'SKILL.md').read_text().startswith('---\nname: careerkit\n')
for f in canonical.rglob('*'):
    if f.is_file():
        other=mirror/f.relative_to(canonical)
        assert other.exists() and f.read_bytes()==other.read_bytes(),f'Mismatch: {f}'
assert (mirror/'SKILL.md').exists()
print('PASS: marketplace JSON, skill metadata, and synchronized Claude/Codex skill files')
