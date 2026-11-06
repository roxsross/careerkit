from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
src=root/'skills/careerkit'; dst=root/'plugins/careerkit/skills/careerkit'
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(src,dst)
print('PASS: Claude plugin synchronized from canonical skill')
