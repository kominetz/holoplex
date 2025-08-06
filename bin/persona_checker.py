import os
import sys
import yaml
import re

def normalize_persona_filename(name, persona_dir='personas'):
    fname = re.sub(r'[^a-zA-Z0-9]', '', name.lower()) + '.md'
    return os.path.join(persona_dir, fname)

def collect_manifest_names(persona_meta):
    groups = []
    for key, val in persona_meta.items():
        if key == 'batches':
            continue
        if isinstance(val, list):
            groups = val
            break  # Use the first group list

    names = set()
    for group_obj in groups:
        if isinstance(group_obj, dict):
            # normal panel/department block: {group: {...}}
            for _, meta in group_obj.items():
                if isinstance(meta, dict):
                    for role, val in meta.items():
                        if role == 'name':
                            continue
                        if isinstance(val, list):
                            names.update(val)
                        elif isinstance(val, str):
                            names.add(val)
                elif isinstance(meta, list):
                    names.update(meta)
                elif isinstance(meta, str):
                    names.add(meta)
        elif isinstance(group_obj, str):
            # It's just a string: collect directly (Sandbox member case)
            names.add(group_obj)
    return names

def main():
    if len(sys.argv) < 2:
        print("Usage: python persona_checker.py <holodeck>")
        sys.exit(1)

    holoname = sys.argv[1]
    manifest_file = os.path.join('holodecks', holoname, f"{holoname}_manifest.yaml")
    persona_dir = 'personas'

    if not os.path.isfile(manifest_file):
        print(f"Error: Manifest file '{manifest_file}' not found.")
        sys.exit(2)

    with open(manifest_file, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    personas_meta = manifest.get('personas', {})
    needed_names = collect_manifest_names(personas_meta)

    missing = []
    for name in sorted(needed_names):
        fname = normalize_persona_filename(name, persona_dir)
        if not os.path.isfile(fname):
            missing.append((name, fname))

    if missing:
        print("Missing persona files for the following assigned names:")
        for name, fname in missing:
            print(f"  {name:25s} -> {fname}")
        sys.exit(3)
    else:
        print("All assigned personas are present.")

if __name__ == "__main__":
    main()
