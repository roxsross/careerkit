#!/usr/bin/env python3
"""Validate structure and metadata for CareerKit."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = ['SKILL.md','README.md','LICENSE','CONTRIBUTING.md','CHANGELOG.md','workflows/linkedin-audit.md','workflows/photo-prompts.md','workflows/career-transition.md','references/linkedin-guide.md','references/photo-styles.md','references/career-transition-guide.md','templates/linkedin-output.md','templates/photo-output.md','templates/career-plan.md','examples/requests.md','examples/walkthrough-linkedin.md']
issues=[f'Missing: {p}' for p in required if not (ROOT/p).is_file()]
s=(ROOT/'SKILL.md').read_text()
if not s.startswith('---\nname: careerkit\ndescription: ') or '\n---\n' not in s[4:]: issues.append('Invalid SKILL.md frontmatter')
for p in ROOT.rglob('*.md'):
 if not p.read_text().strip(): issues.append(f'Empty file: {p}')
if issues:
 print('FAIL\n'+'\n'.join(issues));sys.exit(1)
print(f'PASS: {len(required)} required files, metadata and Markdown files verified')
