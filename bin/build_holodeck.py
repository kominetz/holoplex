import os
import sys
import shutil
import yaml
import re
import datetime

# --- CONFIG ---
BUILD_VERSION = "1.0.0"
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

def normalize_name(name):
    """Convert character name to filename format"""
    # Remove anything in parentheses, then normalize, e.g. 'The Doctor (EMH)' -> 'thedoctoremh.md'
    base = re.sub(r'[^\w]', '', name.lower())
    return base + '.md'

def extract_character_metadata(character_name, characters_dir):
    """Extract full name and nickname from character file if available"""
    fname = normalize_name(character_name)
    fpath = os.path.join(characters_dir, fname)
    
    full_name = character_name  # Default fallback
    nickname = "--"  # Default if no nickname found
    
    if os.path.exists(fpath):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Look for full name patterns
                full_name_match = re.search(r'^fullname\s+(.+?)$', content, re.MULTILINE | re.IGNORECASE)
                if full_name_match:
                    full_name = full_name_match.group(1).strip()
                
                # Look for nickname patterns
                nickname_match = re.search(r'^nicknames?\s+(.+?)$', content, re.MULTILINE | re.IGNORECASE)
                if nickname_match:
                    nickname = nickname_match.group(1).strip()
                elif re.search(r'"([^"]+)"', content):  # Look for quoted nicknames in content
                    quote_match = re.search(r'"([^"]+)"', content)
                    if quote_match:
                        nickname = f'"{quote_match.group(1)}"'
                        
        except Exception as e:
            print(f'Warning: Could not extract metadata from {fname}: {e}')
    
    return full_name, nickname

def generate_holodeck_rc(manifest, characters_dir, out_path):
    """Generate the unified holodeck_rc.md file with all configuration and character manifest"""
    
    # Get current timestamp
    build_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Collect all characters with their metadata
    character_data = {}
    
    # Process main characters
    main_chars = manifest.get('main_characters', [])
    for char in main_chars:
        if char not in character_data:
            full_name, nickname = extract_character_metadata(char, characters_dir)
            character_data[char] = {
                'full_name': full_name,
                'nickname': nickname,
                'roles': [],
                'files': []
            }
        character_data[char]['roles'].append('Main')
        character_data[char]['files'].append('cast_main.md')
    
    # Process supporting characters
    supp_chars = manifest.get('supporting_characters', [])
    for char in supp_chars:
        if char not in character_data:
            full_name, nickname = extract_character_metadata(char, characters_dir)
            character_data[char] = {
                'full_name': full_name,
                'nickname': nickname,
                'roles': [],
                'files': []
            }
        character_data[char]['roles'].append('Supporting')
        character_data[char]['files'].append('cast_supporting.md')
    
    # Process groups
    groups = manifest.get('groups', {})
    for group_name, group_info in groups.items():
        # Process group members
        members = group_info.get('members', [])
        for char in members:
            if char not in character_data:
                full_name, nickname = extract_character_metadata(char, characters_dir)
                character_data[char] = {
                    'full_name': full_name,
                    'nickname': nickname,
                    'roles': [],
                    'files': []
                }
            role_name = group_info.get('description', group_name.replace('_', ' ').title())
            character_data[char]['roles'].append(f"{role_name} (Member)")
            character_data[char]['files'].append(f'cast_{group_name}.md')
        
        # Process group associates
        associates = group_info.get('associates', [])
        for char in associates:
            if char not in character_data:
                full_name, nickname = extract_character_metadata(char, characters_dir)
                character_data[char] = {
                    'full_name': full_name,
                    'nickname': nickname,
                    'roles': [],
                    'files': []
                }
            role_name = group_info.get('description', group_name.replace('_', ' ').title())
            character_data[char]['roles'].append(f"{role_name} (Associate)")
            character_data[char]['files'].append(f'cast_{group_name}.md')
    
    # Sort characters alphabetically by name
    sorted_characters = sorted(character_data.keys())
    
    # Generate the holodeck_rc.md file
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('# Holodeck Run Control\n\n')
        f.write('<!-- Generated from manifest.yaml - Do not edit manually -->\n')
        f.write(f'<!-- Build Version: {BUILD_VERSION} -->\n')
        f.write(f'<!-- Generated: {build_timestamp} -->\n\n')
        
        # Startup Sequence
        f.write('## Startup Sequence\n\n')
        f.write('1. Initialize cast manifest (see Cast section below)\n')
        f.write('2. Load `holodeck_protocols.md`.\n')
        f.write('3. Load `holodeck_program.md`.\n')
        f.write('4. Process user_prompt but keep response concise.\n\n')
        
        # File Dependencies
        f.write('## File Dependencies\n\n')
        f.write('### Core Files\n\n')
        f.write('- `holodeck_protocols.md` (required)\n')
        f.write('- `holodeck_program.md` (default program)\n')
        f.write('- `holodeck_persona_user.md`\n')
        f.write('- `holodeck_persona_computer.md`\n\n')
        
        f.write('### Cast Files\n\n')
        f.write('- `cast_main.md`\n')
        f.write('- `cast_supporting.md`\n')
        for group_name in groups.keys():
            f.write(f'- `cast_{group_name}.md`\n')
        f.write('\n')
        
        f.write('### Additional Files\n\n')
        additional_files = manifest.get('additional_files', [])
        for rel_path in additional_files:
            filename = os.path.basename(rel_path)
            f.write(f'- `{filename}`\n')
        f.write('\n')
        
        # Cast Manifest
        f.write('## Cast Manifest\n\n')
        f.write('Complete mapping of all characters, their metadata, roles, and file locations.\n\n')
        f.write('- Character lookups use cast manifest table as primary key\n')
        f.write('- Cast manifest provides authoritative character-to-file mapping\n')
        f.write('- File references validate against dependencies listed above\n\n')
        
        f.write('| Character Name | Full Name | Nickname(s) | Role(s) | Files |\n')
        f.write('|----------------|-----------|-------------|---------|-------|\n')
        
        for char_name in sorted_characters:
            data = character_data[char_name]
            
            # Format the data
            full_name = data['full_name']
            nickname = data['nickname']
            roles = ', '.join(data['roles'])
            files = ', '.join(sorted(set(data['files'])))  # Remove duplicates and sort
            
            f.write(f'| {char_name} | {full_name} | {nickname} | {roles} | {files} |\n')
        
        f.write('\n')
        
        
        # Build Metadata
        f.write('## Build Metadata\n\n')
        f.write(f'- Built: {build_timestamp}\n')
        f.write(f'- Build System: build_holodeck.py ({BUILD_VERSION})\n')
        f.write(f'- Total Characters: {len(sorted_characters)}\n')
        f.write(f'- Source Manifest: manifest.yaml\n')

def concat_character_files(names, out_path):
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
        print('Usage: python build_holodeck.py <program>')
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

    print(f'Holodeck Build System v{BUILD_VERSION}')
    print(f'Building program: {program}')
    print(f'Timestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

    # Generate holodeck_rc.md with unified configuration and cast manifest
    holodeck_rc_path = os.path.join(build_program_dir, 'holodeck_rc.md')
    generate_holodeck_rc(manifest, CHARACTERS_DIR, holodeck_rc_path)
    print(f'Generated holodeck run control: {holodeck_rc_path}')

    # Copy persona files with new naming convention
    persona_map = {
        'user_persona': 'holodeck_persona_user.md',
        'computer_persona': 'holodeck_persona_computer.md',
    }

    for persona_key, dest_filename in persona_map.items():
        persona_path = manifest.get(persona_key)
        if persona_path:
            src_path = os.path.join(SRC_DIR, persona_path)
            dest_path = os.path.join(build_program_dir, dest_filename)
            if os.path.exists(src_path):
                shutil.copy2(src_path, dest_path)
                print(f'Copied persona: {dest_filename}')
            else:
                print(f'Warning: Persona file not found: {src_path}')

    # Copy protocols file with new naming convention
    protocol_path = manifest.get('holodeck_protocols')
    if protocol_path:
        src_path = os.path.join(SRC_DIR, protocol_path)
        dest_path = os.path.join(build_program_dir, 'holodeck_protocols.md')
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f'Copied protocols: holodeck_protocols.md')
        else:
            print(f'Warning: Protocols file not found: {src_path}')

    # Concatenate character files with new "cast_" naming convention
    concat_character_files(main_chars, os.path.join(build_program_dir, 'cast_main.md'))
    print(f'Generated cast_main.md with {len(main_chars)} characters')
    
    concat_character_files(supp_chars, os.path.join(build_program_dir, 'cast_supporting.md'))
    print(f'Generated cast_supporting.md with {len(supp_chars)} characters')

    # For each group, create cast_{group_name}.md files
    groups = manifest.get('groups', {})
    for group_name, group_info in groups.items():
        group_file = os.path.join(build_program_dir, f'cast_{group_name}.md')
        members = group_info.get('members', []) if isinstance(group_info.get('members'), list) else []
        associates = group_info.get('associates', []) if isinstance(group_info.get('associates'), list) else []
        group_description = group_info.get('description', None)

        if members or associates:
            concat_group_character_files(group_name, members, associates, group_file, group_description)
            print(f'Generated cast_{group_name}.md with {len(members)} members and {len(associates)} associates')

    # Copy additional files if specified
    additional_files = manifest.get('additional_files', [])
    for rel_path in additional_files:
        src_path = os.path.join(SRC_DIR, rel_path)
        dest_path = os.path.join(build_program_dir, os.path.basename(rel_path))
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f'Copied additional file: {os.path.basename(rel_path)}')
        else:
            print(f'Warning: Additional file not found: {src_path}')
    
    print(f'Build complete! Output in: {build_program_dir}')

if __name__ == '__main__':
    main()