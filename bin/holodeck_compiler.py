import datetime
import os
import re
import sys
import shutil
import yaml

def build_full_file(holoname, output_dir):
    """
    Assemble a single markdown file (parse-first style):
    - holodeck_protocols.md first
    - Each imported file bracketed by '## START: filename' / '## END: filename'
    - Ends with Everybody character batch
    - Content normalization: replace lone '---' lines with blank lines for Markdown safety
    """
    full_filename = f"{holoname}_full.md"
    full_path = os.path.join(output_dir, full_filename)

    # ✅ Core files in exact order (protocols first)
    core_files = [
        "holodeck_protocols.md",
        f"{holoname}.md",
        "holodeck_cast.md",
        "holodeck_setting.md",
        "holodeck_script.md"
    ]

    everybody_file = "character_everybody.md"
    everybody_path = os.path.join(output_dir, everybody_file)

    created_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")

    def sanitize_separators(text: str) -> str:
        """Replace standalone '---' lines with a blank line to avoid MD misparse."""
        return re.sub(r"(?m)^\s*---\s*$", "", text)

    with open(full_path, "w", encoding="utf-8") as out:
        # File heading
        out.write(f"# {full_filename}\n\n")
        out.write(f"**Created on:** {created_on}\n\n")

        # Core file sections
        for fname in core_files:
            fpath = os.path.join(output_dir, fname)
            out.write(f"## START: {fname}\n")
            if os.path.isfile(fpath):
                with open(fpath, "r", encoding="utf-8") as coref:
                    contents = sanitize_separators(coref.read().strip())
                    out.write(contents)
                    out.write("\n")
            else:
                out.write(f"*Missing file: {fname}*\n")
            out.write(f"## END: {fname}\n\n")

        # Everybody section
        out.write(f"## START: {everybody_file}\n")
        out.write("## Characters -- Everybody\n\n")
        if os.path.isfile(everybody_path):
            with open(everybody_path, "r", encoding="utf-8") as ef:
                contents = sanitize_separators(ef.read().strip())
                out.write(contents)
                out.write("\n")
        else:
            out.write("*Missing 'Everybody' character file*\n")
        out.write(f"## END: {everybody_file}\n")

    print(f"Wrote parse-friendly single file: {full_filename}")

def copy_contents(src_dir, dest_dir):
    if not os.path.isdir(src_dir):
        print(f"Warning: Source directory {src_dir} does not exist, skipping.")
        return
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_path)
    print(f"Copied all files (non-recursive) from {src_dir} to {dest_dir}")

def normalize_character_filename(name, character_dir):
    return os.path.join(character_dir, re.sub(r"[^a-zA-Z0-9]", "", name.lower()) + ".md")

def character_filename_base(name):
    return re.sub(r"[^a-zA-Z0-9]", "", name.lower())

def batch_header(**kwargs):
    desc = ', '.join(f'{k}={v}' for k, v in kwargs.items() if v is not None)
    return f"## Batch: {desc}\n\n"

def extract_batch(names, character_dir, encoding, markdown_header, character_separator, batchhdr=None, missing_characters=set()):
    content = []
    for name in names:
        fname = normalize_character_filename(name, character_dir)
        if os.path.isfile(fname):
            with open(fname, encoding=encoding) as pf:
                charactertext = pf.read().strip()
                if markdown_header and not charactertext.lstrip().startswith("#"):
                    charactertext = f"# {name}\n\n" + charactertext
                content.append(charactertext)
        else:
            print(f'Warning: character file missing for {name} ({fname})')
            if missing_characters is not None:
                missing_characters.add(name)
    out = character_separator.join(content) + "\n" if content else ""
    return (batchhdr or "") + out if out else ""

def get_all_character_names_from_groups(groups):
    names = set()
    for group in groups:
        if not isinstance(group, dict):
            continue
        for k, v in group.items():
            if k in ('name', 'type'):
                continue
            if isinstance(v, list):
                names.update(v)
            elif isinstance(v, str):
                names.add(v)
    return sorted(names)

def extract_yaml_from_md(filename):
    print(f"Extracting YAML from {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        # Extract the first YAML fenced code block
        match = re.search(r'```yaml\s*\n(.*?)\n```', content, re.IGNORECASE | re.DOTALL)
        if not match:
            raise ValueError(f"No YAML code block found in {filename}")
        yaml_str = match.group(1)
        return yaml.safe_load(yaml_str)

# --- MAIN ---

if len(sys.argv) != 2:
    print("Usage: python holodeck_compiler.py <holodeck_name>")
    sys.exit(1)

HOLONAME = sys.argv[1]
BUILD_DIR = os.path.join('build', HOLONAME)
CHARACTER_DIR = 'characters'
OUTPUT_DIR = BUILD_DIR

os.makedirs(OUTPUT_DIR, exist_ok=True)

copy_contents(os.path.join('programs', 'common'), OUTPUT_DIR)
copy_contents(os.path.join('programs', HOLONAME), OUTPUT_DIR)
MANIFEST = os.path.join(BUILD_DIR, 'holodeck_cast.md')
manifest = extract_yaml_from_md(MANIFEST)

characters = manifest.get("characters", {})
batches_conf = characters.get("batches", {})

file_prefix = batches_conf.get("file_prefix", HOLONAME)
character_separator = batches_conf.get("character_separator", "\n\n")
encoding = batches_conf.get("encoding", "utf-8")
markdown_header = batches_conf.get("markdown_header", True)
targets = batches_conf.get("targets") or []
everybody = batches_conf.get("everybody", True)
missing_characters = set()

# 1. Individual members
members = characters.get("roles", {}).values()
for name in members:
    fname = f"{file_prefix}_{character_filename_base(name)}.md"
    batchhdr = batch_header(by="member", person=name)
    out_path = os.path.join(OUTPUT_DIR, fname)
    with open(out_path, "w", encoding=encoding) as f:
        outstr = extract_batch(
            [name], CHARACTER_DIR, encoding, markdown_header, character_separator, batchhdr, missing_characters)
        f.write(outstr)
    print(f"Wrote {fname}")

# 2. Group-based batching (if any)
groups = characters.get("groups", [])
if groups:
    group_lookup = {}
    role_lookup = {}
    for group in groups:
        gname = group.get("name")
        gtype = group.get("type")
        group_lookup[gname] = {}
        for role, memberslist in group.items():
            if role in ("name", "type"):
                continue
            if isinstance(memberslist, list):
                group_lookup[gname][role] = list(memberslist)
            elif isinstance(memberslist, str):
                group_lookup[gname][role] = [memberslist]
            if role not in role_lookup:
                role_lookup[role] = set()
            if isinstance(memberslist, list):
                role_lookup[role].update(memberslist)
            elif isinstance(memberslist, str):
                role_lookup[role].add(memberslist)

    for t in targets:
        if isinstance(t, dict) and t.get("by") in ("panel", "department", "group"):
            bytype = t.get("by")
            for gname, roles in group_lookup.items():
                gtype = None
                for group in groups:
                    if group.get("name") == gname:
                        gtype = group.get("type")
                        break
                batch_charactere = []
                for role, members in roles.items():
                    batch_charactere.extend(members)
                unique_sorted = sorted(set(batch_charactere))
                if unique_sorted:
                    roles_used = "+".join(r for r in roles.keys())
                    fname = f"{file_prefix}_{character_filename_base(gname)}.md"
                    batchhdr = batch_header(by=bytype, type=gtype, group=gname, roles=roles_used)
                    out_path = os.path.join(OUTPUT_DIR, fname)
                    with open(out_path, "w", encoding=encoding) as f:
                        outstr = extract_batch(
                            unique_sorted, CHARACTER_DIR, encoding, markdown_header, character_separator, batchhdr, missing_characters)
                        f.write(outstr)
                    print(f"Wrote {fname}")

    # Per-role batches
    for t in targets:
        if isinstance(t, dict) and t.get("by") == "role":
            for role, people in role_lookup.items():
                unique_people = sorted(people)
                if unique_people:
                    fname = f"{file_prefix}_{character_filename_base(role)}.md"
                    batchhdr = batch_header(by="role", role=role)
                    out_path = os.path.join(OUTPUT_DIR, fname)
                    with open(out_path, "w", encoding=encoding) as f:
                        outstr = extract_batch(
                            unique_people, CHARACTER_DIR, encoding, markdown_header, character_separator, batchhdr, missing_characters)
                        f.write(outstr)
                    print(f"Wrote {fname}")

    # Composite batches
    for t in targets:
        composite = t.get("composite") if isinstance(t, dict) else None
        if not composite:
            continue
        group_param = composite.get("for_each") or composite.get("for_all")
        include_roles = set(composite.get("include_roles", []))
        file_suffix = composite.get("file_suffix", "")
        is_for_each = "for_each" in composite
        is_for_all = "for_all" in composite

        if group_param == "group" or group_param in ("panel", "department"):
            if is_for_each:
                for gname, roles in group_lookup.items():
                    members = []
                    for role in include_roles:
                        members += roles.get(role, [])
                    unique_members = sorted(set(members))
                    if unique_members:
                        suffix = f"_{file_suffix}" if file_suffix else ""
                        fname = f"{file_prefix}_{character_filename_base(gname)}{suffix}.md"
                        batchhdr = batch_header(by=group_param, group=gname, roles="+".join(include_roles))
                        out_path = os.path.join(OUTPUT_DIR, fname)
                        with open(out_path, "w", encoding=encoding) as f:
                            outstr = extract_batch(
                                unique_members, CHARACTER_DIR, encoding, markdown_header, character_separator, batchhdr, missing_characters)
                            f.write(outstr)
                        print(f"Wrote {fname}")
            elif is_for_all:
                all_members = set()
                for roles in group_lookup.values():
                    for role in include_roles:
                        all_members |= set(roles.get(role, []))
                unique_members = sorted(all_members)
                if unique_members:
                    fname = f"{file_prefix}_{file_suffix}.md"
                    batchhdr = batch_header(by=f"all_{group_param}", roles="+".join(include_roles))
                    out_path = os.path.join(OUTPUT_DIR, fname)
                    with open(out_path, "w", encoding=encoding) as f:
                        outstr = extract_batch(
                            unique_members, CHARACTER_DIR, encoding, markdown_header, character_separator, batchhdr, missing_characters)
                        f.write(outstr)
                    print(f"Wrote {fname}")

# 3. "everybody" batch (all members from both members and groups)
if everybody:
    all_names = set()
    all_names.update(members)
    all_names.update(get_all_character_names_from_groups(groups))
    if all_names:
        fname = f"{file_prefix}_everybody.md"
        batchhdr = batch_header(by="everybody")
        out_path = os.path.join(OUTPUT_DIR, fname)
        with open(out_path, "w", encoding=encoding) as f:
            outstr = extract_batch(
                sorted(all_names), CHARACTER_DIR, encoding, markdown_header, character_separator, batchhdr, missing_characters)
            f.write(outstr)
        print(f"Wrote {fname}")

# --- At end of main (after character batches), call:
build_full_file(HOLONAME, OUTPUT_DIR)

# === Post-Compile Character Check Report ===

if missing_characters:
    print("\n=== Post-Compile Character Check Report ===")
    print(f"Total missing character files: {len(missing_characters)}")
    for mp in sorted(missing_characters):
        print(f" - {mp}")
else:
    print("\nAll character files accounted for.")
