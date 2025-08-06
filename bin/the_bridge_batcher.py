import os
import shutil
import yaml
from collections import defaultdict

# --- CONFIGURATION ---
MANIFEST = os.path.join('build', 'the_bridge_manifest.yaml')
PERSONA_DIR = 'personas'
OUTPUT_DIR = os.path.join('build', 'the_bridge')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_manifest(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f).get('personae', [])

def normalize_persona_filename(name):
    import re
    return os.path.join(PERSONA_DIR, re.sub(r'[^a-zA-Z0-9]', '', name.lower()) + '.md')

def extract_batch(personae, names):
    # Concatenate full persona files for all given names in order
    content = []
    for name in names:
        fname = normalize_persona_filename(name)
        if os.path.isfile(fname):
            with open(fname, encoding='utf-8') as pf:
                content.append(pf.read().strip())
        else:
            print(f'Warning: persona file missing for {name} ({fname})')
    return '\n\n'.join(content) + '\n' if content else ''

def copy_contents(src_dir, dest_dir):
    if not os.path.isdir(src_dir):
        print(f"Warning: Source directory {src_dir} does not exist, skipping.")
        return
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isdir(src_path):
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)
    print(f"Copied contents of {src_dir} to {dest_dir}")

personae = load_manifest(MANIFEST)

department_groups = defaultdict(list)
all_names = set()
heads, staff, senior_staff = set(), set(), set()

for persona in personae:
    name = persona['name']
    all_names.add(name)
    for assignment in persona.get('assignments', []):
        department = assignment.split(' Department')[0]
        if assignment.endswith('Department Head'):
            department_groups[department + '_head'].append(name)
            heads.add(name)
            senior_staff.add(name)
            department_groups[department].append(name)
        elif assignment.endswith('Department Staff'):
            department_groups[department + '_staff'].append(name)
            staff.add(name)
            senior_staff.add(name)
            department_groups[department].append(name)
        elif assignment.endswith('Department'):
            department_groups[department].append(name)
        else:
            department_groups[assignment].append(name)

# 1. Copy common and holodeck protocols and additional resources directly into build/the_bridge
copy_contents('holodecks/common', OUTPUT_DIR)
copy_contents('holodecks/the_bridge', OUTPUT_DIR)

# 2. Write full crew batch
batchpath = os.path.join(OUTPUT_DIR, 'the_bridge_full_crew.md')
with open(batchpath, 'w', encoding='utf-8') as bf:
    bf.write(extract_batch(personae, sorted(all_names)))
print(f'Wrote {batchpath}')

# 3. Write per-department batches (dynamic)
for group in department_groups:
    if group.endswith('_head') or group.endswith('_staff'):
        continue
    dpath = os.path.join(OUTPUT_DIR, f'the_bridge_{group.lower()}.md')
    members = list(dict.fromkeys(department_groups[group]))
    with open(dpath, 'w', encoding='utf-8') as bf:
        bf.write(extract_batch(personae, members))
    print(f'Wrote {dpath}')

# 4. Write bridge_heads batch
heads_path = os.path.join(OUTPUT_DIR, 'the_bridge_heads.md')
with open(heads_path, 'w', encoding='utf-8') as bf:
    bf.write(extract_batch(personae, sorted(heads)))
print(f'Wrote {heads_path}')

# 5. Write senior staff batch (heads + staff, deduped)
senior_path = os.path.join(OUTPUT_DIR, 'the_bridge_senior_staff.md')
with open(senior_path, 'w', encoding='utf-8') as bf:
    bf.write(extract_batch(personae, sorted(senior_staff)))
print(f'Wrote {senior_path}')
