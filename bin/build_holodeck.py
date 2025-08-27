
import os
import sys
import shutil
import yaml
import re

# --- CONFIG ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(PROJECT_ROOT, 'src')
PROGRAMS_DIR = os.path.join(SRC_DIR, 'programs')
CHARACTERS_DIR = os.path.join(SRC_DIR, 'characters')
PERSONAS_DIR = os.path.join(SRC_DIR, 'personas')
BUILD_DIR = os.path.join(PROJECT_ROOT, 'build')


def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def copytree(src, dst):
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)

def copy_files(src, dst):
    if os.path.exists(src):
        for fname in os.listdir(src):
            fpath = os.path.join(src, fname)
            if os.path.isfile(fpath):
                shutil.copy2(fpath, dst)

def concat_character_files(names, out_path):
    import re
    def normalize(name):
        # Remove anything in parentheses, then append it, e.g. 'The Doctor (EMH)' -> 'thedoctoremh.md'
        base = re.sub(r'[^\w]', '', name.lower())
        return base + '.md'

    with open(out_path, 'w', encoding='utf-8') as out:
        for name in names:
            fname = normalize(name)
            fpath = os.path.join(CHARACTERS_DIR, fname)
            if os.path.exists(fpath):
                with open(fpath, 'r', encoding='utf-8') as f:
                    out.write(f'\n# {name}\n')
                    out.write(f.read())
                    out.write('\n')
            else:
                print(f'Warning: Character file not found: {fname}')

def concat_group_character_files(group_name, members, associates, out_path, group_description=None):
    with open(out_path, 'w', encoding='utf-8') as out:
        if group_description:
            out.write(f'# {group_name}: {group_description}\n')
        else:
            out.write(f'# {group_name}\n')
        if members:
            out.write('\n## Members\n')
            for name in members:
                fname = re.sub(r'[^\w]', '', name.lower()) + '.md'
                fpath = os.path.join(CHARACTERS_DIR, fname)
                if os.path.exists(fpath):
                    with open(fpath, 'r', encoding='utf-8') as f:
                        out.write(f.read())
                        out.write('\n')
                else:
                    print(f'Warning: Character file not found: {fname}')
        if associates:
            out.write('\n## Associates\n')
            for name in associates:
                fname = re.sub(r'[^\w]', '', name.lower()) + '.md'
                fpath = os.path.join(CHARACTERS_DIR, fname)
                if os.path.exists(fpath):
                    with open(fpath, 'r', encoding='utf-8') as f:
                        out.write(f.read())
                        out.write('\n')
                else:
                    print(f'Warning: Character file not found: {fname}')

def main():
    if len(sys.argv) != 2:
        print('Usage: python build_holodeck.py <program_name>')
        sys.exit(1)
    program = sys.argv[1]
    program_dir = os.path.join(PROGRAMS_DIR, program)
    manifest_path = os.path.join(program_dir, 'manifest.yaml')
    if not os.path.exists(manifest_path):
        print(f'Manifest not found: {manifest_path}')
        sys.exit(1)
    build_program_dir = os.path.join(BUILD_DIR, program)
    if os.path.exists(build_program_dir):
        shutil.rmtree(build_program_dir)
    os.makedirs(build_program_dir)

    # Copy common files
    copytree(os.path.join(PROGRAMS_DIR, 'common'), build_program_dir)
    # Copy program files
    copy_files(program_dir, build_program_dir)

    # Parse manifest
    manifest = load_yaml(manifest_path)
    main_chars = manifest.get('main_characters', [])
    supp_chars = manifest.get('supporting_characters', [])

    # Copy persona files if present, always as personas_user.md and personas_computer.md
    persona_map = {
        'user_persona': 'personas_user.md',
        'computer_persona': 'personas_computer.md',
    }
    for persona_key, dest_filename in persona_map.items():
        persona_path = manifest.get(persona_key)
        if persona_path:
            src_path = os.path.join(SRC_DIR, persona_path)
            dest_path = os.path.join(build_program_dir, dest_filename)
            if os.path.exists(src_path):
                shutil.copy2(src_path, dest_path)
            else:
                print(f'Warning: Persona file not found: {src_path}')

    # Copy protocols file if present, always as protocol_holodeck.md
    protocol_path = manifest.get('holodeck_protocols')
    if protocol_path:
        src_path = os.path.join(SRC_DIR, protocol_path)
        dest_path = os.path.join(build_program_dir, 'protocols_holodeck.md')
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
        else:
            print(f'Warning: Protocols file not found: {src_path}')

    # Concatenate character files
    concat_character_files(main_chars, os.path.join(build_program_dir, 'characters_main.md'))
    concat_character_files(supp_chars, os.path.join(build_program_dir, 'characters_supporting.md'))

    # For each group, create a characters_{group_name}.md file with members and associates labeled
    import re
    groups = manifest.get('groups', {})
    for group_name, group_info in groups.items():
        group_file = os.path.join(build_program_dir, f'characters_{group_name}.md')
        members = group_info.get('members', []) if isinstance(group_info.get('members'), list) else []
        associates = group_info.get('associates', []) if isinstance(group_info.get('associates'), list) else []
        group_description = group_info.get('description', None)
        if members or associates:
            concat_group_character_files(group_name, members, associates, group_file, group_description)

    # Copy additional files if specified
    additional_files = manifest.get('additional_files', [])
    for rel_path in additional_files:
        src_path = os.path.join(SRC_DIR, rel_path)
        dest_path = os.path.join(build_program_dir, os.path.basename(rel_path))
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
        else:
            print(f'Warning: Additional file not found: {src_path}')

if __name__ == '__main__':
    main()
