import os
import yaml
import re
import sys
import shutil

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

def normalize_persona_filename(name, persona_dir):
    return os.path.join(persona_dir, re.sub(r"[^a-zA-Z0-9]", "", name.lower()) + ".md")

def persona_filename_base(name):
    return re.sub(r"[^a-zA-Z0-9]", "", name.lower())

def batch_header(**kwargs):
    desc = ', '.join(f'{k}={v}' for k, v in kwargs.items() if v is not None)
    return f"## Batch: {desc}\n\n"

def extract_batch(names, persona_dir, encoding, markdown_header, persona_separator, batchhdr=None):
    content = []
    for name in names:
        fname = normalize_persona_filename(name, persona_dir)
        if os.path.isfile(fname):
            with open(fname, encoding=encoding) as pf:
                personatext = pf.read().strip()
                if markdown_header and not personatext.lstrip().startswith("#"):
                    personatext = f"# {name}\n\n" + personatext
                content.append(personatext)
        else:
            print(f'Warning: persona file missing for {name} ({fname})')
    out = persona_separator.join(content) + "\n" if content else ""
    return (batchhdr or "") + out if out else ""

def get_all_persona_names_from_groups(groups):
    names = set()
    for group in groups:
        if not isinstance(group, dict):
            continue
        # Exclude 'name' and 'type', gather all other values
        for k, v in group.items():
            if k in ('name', 'type'):
                continue
            if isinstance(v, list):
                names.update(v)
            elif isinstance(v, str):
                names.add(v)
    return sorted(names)

# --- MAIN ---
if len(sys.argv) != 2:
    print("Usage: python holodeck_batcher.py <holodeck>")
    sys.exit(1)

HOLONAME = sys.argv[1]
MANIFEST = os.path.join('build', HOLONAME, f'{HOLONAME}_manifest.yaml')
PERSONA_DIR = 'personas'
OUTPUT_DIR = os.path.join('build', HOLONAME)

os.makedirs(OUTPUT_DIR, exist_ok=True)
copy_contents(os.path.join('holodecks', 'common'), OUTPUT_DIR)
copy_contents(os.path.join('holodecks', HOLONAME), OUTPUT_DIR)

with open(MANIFEST, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

personas = manifest.get("personas", {})
batches_conf = personas.get("batches", {})
file_prefix = batches_conf.get("file_prefix", HOLONAME)
persona_separator = batches_conf.get("persona_separator", "\n---\n")
encoding = batches_conf.get("encoding", "utf-8")
markdown_header = batches_conf.get("markdown_header", True)
targets = batches_conf.get("targets") or []
everybody = batches_conf.get("everybody", True)

# 1. Individual members
members = personas.get("individuals", [])
for name in members:
    fname = f"{file_prefix}_{persona_filename_base(name)}.md"
    batchhdr = batch_header(by="member", person=name)
    out_path = os.path.join(OUTPUT_DIR, fname)
    with open(out_path, "w", encoding=encoding) as f:
        outstr = extract_batch([name], PERSONA_DIR, encoding, markdown_header, persona_separator, batchhdr)
        f.write(outstr)
    print(f"Wrote {fname}")

# 2. Group-based batching (if any)
groups = personas.get("groups", [])
if groups:
    # Build lookups for group_name/type, per-role, etc.
    group_lookup = {}
    role_lookup = {}

    # Group keys: list of dicts, each with 'type' and 'name' at minimum
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

    # Per-group batches (e.g. one per department or panel)
    for t in targets:
        if isinstance(t, dict) and t.get("by") in ("panel", "department", "group"):
            bytype = t.get("by")
            for gname, roles in group_lookup.items():
                gtype = None
                # Try to detect type from groups:
                for group in groups:
                    if group.get("name") == gname:
                        gtype = group.get("type")
                        break
                batch_personae = []
                for role, members in roles.items():
                    batch_personae.extend(members)
                unique_sorted = sorted(set(batch_personae))
                if unique_sorted:
                    roles_used = "+".join(r for r in roles.keys())
                    fname = f"{file_prefix}_{persona_filename_base(gname)}.md"
                    batchhdr = batch_header(by=bytype, type=gtype, group=gname, roles=roles_used)
                    out_path = os.path.join(OUTPUT_DIR, fname)
                    with open(out_path, "w", encoding=encoding) as f:
                        outstr = extract_batch(unique_sorted, PERSONA_DIR, encoding, markdown_header, persona_separator, batchhdr)
                        f.write(outstr)
                    print(f"Wrote {fname}")

    # Per-role batches (across all groups)
    for t in targets:
        if isinstance(t, dict) and t.get("by") == "role":
            for role, people in role_lookup.items():
                unique_people = sorted(people)
                if unique_people:
                    fname = f"{file_prefix}_{persona_filename_base(role)}.md"
                    batchhdr = batch_header(by="role", role=role)
                    out_path = os.path.join(OUTPUT_DIR, fname)
                    with open(out_path, "w", encoding=encoding) as f:
                        outstr = extract_batch(unique_people, PERSONA_DIR, encoding, markdown_header, persona_separator, batchhdr)
                        f.write(outstr)
                    print(f"Wrote {fname}")

    # Composite batches (combinations of roles, groups, etc.)
    for t in targets:
        composite = t.get("composite") if isinstance(t, dict) else None
        if not composite:
            continue
        group_param = composite.get("for_each") or composite.get("for_all")
        include_roles = set(composite.get("include_roles", []))
        file_suffix = composite.get("file_suffix", "")
        is_for_each = "for_each" in composite
        is_for_all = "for_all" in composite

        # For each group (e.g., each department or panel)
        if group_param == "group" or group_param in ("panel", "department"):
            if is_for_each:
                for gname, roles in group_lookup.items():
                    members = []
                    for role in include_roles:
                        members += roles.get(role, [])
                    unique_members = sorted(set(members))
                    if unique_members:
                        suffix = f"_{file_suffix}" if file_suffix else ""
                        fname = f"{file_prefix}_{persona_filename_base(gname)}{suffix}.md"
                        batchhdr = batch_header(by=group_param, group=gname, roles="+".join(include_roles))
                        out_path = os.path.join(OUTPUT_DIR, fname)
                        with open(out_path, "w", encoding=encoding) as f:
                            outstr = extract_batch(unique_members, PERSONA_DIR, encoding, markdown_header, persona_separator, batchhdr)
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
                        outstr = extract_batch(unique_members, PERSONA_DIR, encoding, markdown_header, persona_separator, batchhdr)
                        f.write(outstr)
                    print(f"Wrote {fname}")

# 3. "everybody" batch (all members from both members and groups)
if everybody:
    all_names = set()
    all_names.update(members)
    all_names.update(get_all_persona_names_from_groups(groups))
    if all_names:
        fname = f"{file_prefix}_everybody.md"
        batchhdr = batch_header(by="everybody")
        out_path = os.path.join(OUTPUT_DIR, fname)
        with open(out_path, "w", encoding=encoding) as f:
            outstr = extract_batch(sorted(all_names), PERSONA_DIR, encoding, markdown_header, persona_separator, batchhdr)
            f.write(outstr)
        print(f"Wrote {fname}")
