import os
import re
import logging
import yaml

# --- Set up logging ---
logging.basicConfig(
    level=logging.DEBUG,  # Default to DEBUG level
    format='%(levelname)s:%(message)s'
)

bridge_file = 'holodecks/the_bridge/the_bridge.md'

# Mapping from tag to role label for each department
TAG2ROLE = {
    '#head': 'Department Head',
    '#staff': 'Department Staff'
}

personae_roles = {}

dept_pattern = re.compile(r'^\s*###\s+(\w+)\s+Department\s*$', re.UNICODE)
tag_pattern = re.compile(r'(#[a-zA-Z]+)')
member_pattern = re.compile(r'^\s*-\s*(.+)$', re.UNICODE)

current_dept = None

with open(bridge_file, encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    dept_match = dept_pattern.match(line)
    if line.strip() == '---':
        break

    if dept_match:
        current_dept = dept_match.group(1)
        logging.debug(f"Matched department header: '{current_dept}' on line {idx + 1}")
        continue

    if current_dept:
        if line.strip().startswith('###'):
            logging.debug(f"End of department block detected for '{current_dept}' at line {idx + 1}")
            current_dept = None
            continue
        member_match = member_pattern.match(line)
        if member_match:
            member_section = member_match.group(1)
            name, *rest = re.split(r'(#head|#staff|,)', member_section)
            name = name.strip()
            tags = tag_pattern.findall(member_section)
            if '#head' in tags:
                role = f"{current_dept} Department Head"
            elif '#staff' in tags:
                role = f"{current_dept} Department Staff"
            else:
                role = f"{current_dept} Department"
            logging.debug(f"Matched member: '{name}' in '{current_dept}' as '{role}' on line {idx + 1}")
            if name not in personae_roles:
                personae_roles[name] = []
            if role not in personae_roles[name]:
                personae_roles[name].append(role)

# --- Write YAML output to build/the_bridge ---
output_dir = os.path.join('build')
os.makedirs(output_dir, exist_ok=True)
out_file = os.path.join(output_dir, 'the_bridge_manifest.yaml')

yaml_out = {'personae': []}
for name in sorted(personae_roles):
    yaml_out['personae'].append({
        'name': name,
        'assignments': personae_roles[name]
    })

with open(out_file, 'w', encoding='utf-8') as out:
    yaml.dump(yaml_out, out, allow_unicode=True, sort_keys=False)

logging.info(f"Manifest written to {out_file}")
