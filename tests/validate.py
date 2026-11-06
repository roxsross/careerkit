from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
skill=root/'skills/careerkit'; plugin=root/'plugins/careerkit/skills/careerkit'
errors=[]
for rel in ('SKILL.md','workflows/browser-import.md','workflows/pdf-import.md','workflows/linkedin.md','workflows/capabilities.md','workflows/photos.md','workflows/transition.md','references/source-policy.md','references/linkedin-guide.md','references/photo-styles.md','references/career-transition-guide.md','templates/audit.md','templates/photo-output.md','templates/career-plan.md'):
 if not (skill/rel).is_file(): errors.append('missing '+rel)
for p in skill.rglob('*'):
 if p.is_file():
  q=plugin/p.relative_to(skill)
  if not q.is_file() or q.read_bytes()!=p.read_bytes(): errors.append('unsynced '+str(p.relative_to(skill)))
try:
 market=json.loads((root/'.claude-plugin/marketplace.json').read_text())
 manifest=json.loads((root/'plugins/careerkit/.claude-plugin/plugin.json').read_text())
 assert market['plugins'][0]['source']=='./plugins/careerkit'
 assert manifest['name']=='careerkit' and manifest['version']=='1.3.0'
 front=(skill/'SKILL.md').read_text().split('---',2)[1]
 assert 'name: careerkit' in front and 'description:' in front
except Exception as exc: errors.append('metadata: '+str(exc))
if errors:
 print('FAIL:', *errors, sep='\n- ');sys.exit(1)
print('PASS: manifests, skill metadata, required paths and Claude/Codex sync')
