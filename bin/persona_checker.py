import os
import sys
import yaml
import re
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

if len(sys.argv) != 2:
    print("Usage: python persona_checker.py <group>")
    print("Example: python persona_checker.py the_bridge")
    sys.exit(1)

group = sys.argv[1]  # "the_bridge" or "the_forum" etc.
manifest_path = os.path.join('build', f'{group}_manifest.yaml')
persona_dir = 'persona'

# Load the manifest YAML
try:
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = yaml.safe_load(f)
except FileNotFoundError:
    logging.error(f"Manifest file not found: {manifest_path}")
    sys.exit(2)

personae = manifest.get('personae', [])

def normalize_name_to_filename(name):
    normalized = re.sub(r'[^a-zA-Z0-9]', '', name.lower())
    return os.path.join(persona_dir, f'{normalized}.md')

missing = []
for persona in personae:
    name = persona['name']
    filename = normalize_name_to_filename(name)
    if not os.path.isfile(filename):
        logging.error(f'Missing persona file for \"{name}\": {filename}')
        missing.append(name)

if not missing:
    logging.info('All persona files found.')
else:
    logging.warning(f'Missing {len(missing)} persona files: {missing}')
