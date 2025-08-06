# MANIFEST_README.md

## Overview

Every holodeck’s manifest (`*_manifest.yaml`) describes:

- How personas are organized for batching,
- Which batch files should be produced and how,
- Which personas should always have a 1:1 batch file (for simulation),
- The structure and membership of all groups (departments, panels, etc.).

The manifest has three main sections under the `personas:` key:

- `batches:` (required) — specifies batching rules and file settings.
- `individuals:` (optional) — a flat list of personas that always get a standalone batch file.
- `groups:` (optional) — a list of groups (departments, panels, etc.), each with their own structure and members/roles.

## YAML Structure

```yaml
personas:
  batches:    # REQUIRED — see below
    ...
  individuals:  # OPTIONAL — always batched 1:1 as individual files
    - Name One
    - Name Two
    ...
  groups:     # OPTIONAL — list of group structures, can be empty or omitted
    - name: 
      type:  # e.g., panel, department, jury, etc.
      : 
      : 
      ...
```

## Section Details & Features

### 1. batches (REQUIRED)

Defines how personas are batched. Common options:

- `targets:` — controls the types of batches (see examples).
- `everybody:` — if true, creates a batch file with all personas.
- `file_prefix:` — prefix for all batch file names.
- NOTE: Further keys control batch formatting and output.

**Example:**

```yaml
batches:
  targets:
    - for_each: individual
    - by: department
    - by: role
    - composite:
        for_each: department
        include_roles: [head, staff]
        file_suffix: "senior_staff"
    - composite:
        for_all: department
        include_roles: [head, staff]
        file_suffix: "senior_staff"
  everybody: true
  file_prefix: "the_bridge"
  markdown_header: true
  persona_separator: "\n---\n"
  encoding: "utf-8"
```

#### Supported Batch Target Keys

- `for_each:`   — generates a batch for each listed persona or group (e.g., `individual`, `member`, `department`, `panel`).
- `by:`         — generates a batch for each group or role (e.g., `by: role`, `by: department`).
- `composite:`  — generates batches that combine multiple roles across groups, e.g. senior staff.
- `everybody:`  — if true, generates a complete "everybody" batch.

### 2. individuals (OPTIONAL)

A list of persona names, each of which always gets its own prefixed batch file (e.g., `the_bridge_spock.md`), whether or not the persona appears in any group.

**Example:**

```yaml
individuals:
  - Spock
  - Seven of Nine
```

### 3. groups (OPTIONAL)

A list of groupings; each is a dictionary that must have at least a `name:` and `type:`. Roles, members, or other keys are allowed as needed for that holodeck.

**Example (panel in forum):**

```yaml
groups:
  - name: Inquiry Panel
    type: panel
    chair: Carl Sagan
    principal:
      - Spock
      - Charles Darwin
    members:
      - Richard Feynman
      - Albert Einstein
```

**Example (department in bridge):**

```yaml
groups:
  - name: Science Department
    type: department
    head: Spock
    staff:
      - Seven of Nine
      - Data
    people:
      - Alan Turing
      - Richard Feynman
```

- You can use any roles or membership breakdown as keys under the group dictionary. Avoid using `members:` as top-level and group key at the same time to prevent confusion—use `people:` or similar within groups.

## Output File Naming and Batch Headings

- All batch files use the `file_prefix` defined in the manifest (e.g., `the_sandbox_`, `the_forum_`, etc.).
- For every batch file, a Markdown level-two heading (## ...) at the top specifies the keys used for batching (criteria, group, roles, etc.), e.g.:

  ```markdown
  ## Batch: by=department, group=Science Department, roles=head+staff

  ```markdown
- Individual persona files are named with prefix plus normalized name, e.g., `the_bridge_spock.md`.

## Examples

### Sandbox

```yaml
personas:
  batches:
    targets:
      - for_each: individual
    everybody: true
    file_prefix: "the_sandbox"
    ...
  individuals:
    - Reginald Barclay
    - The Doctor (EMH)
    - Tom Paris
    - Kathryn Janeway
    - Seven of Nine
```

**Produces:**

- `the_sandbox_reginaldbarclay.md`
- `the_sandbox_thedoctoremh.md`
- etc.
- `the_sandbox_everybody.md` (if `everybody: true`)

### Forum (Panels)

```yaml
personas:
  batches:
    targets:
      - by: panel
      - by: role
      - composite:
          for_each: panel
          include_roles: [chair, principal]
          file_suffix: "principal_team"
      - composite:
          for_all: panel
          include_roles: [chair, principal]
          file_suffix: "all_principals"
    everybody: true
    file_prefix: "the_forum"
    ...
  groups:
    - name: Inquiry Panel
      type: panel
      chair: Carl Sagan
      principal:
        - Spock
        - Charles Darwin
      members:
        - Richard Feynman
        - Albert Einstein
```

### Bridge (Departments)

```yaml
personas:
  batches:
    targets:
      - by: department
      - by: role
      - for_each: individual
      - composite:
          for_each: department
          include_roles: [head, staff]
          file_suffix: "senior_staff"
      - composite:
          for_all: department
          include_roles: [head, staff]
          file_suffix: "senior_staff"
    everybody: true
    file_prefix: "the_bridge"
    ...
  individuals:
    - Spock
  groups:
    - name: Science Department
      type: department
      head: Spock
      staff:
        - Seven of Nine
        - Data
      people:
        - Alan Turing
        - Richard Feynman
```

## Best Practices

- Always use `individuals` at the top level for 1:1 persona batch files (avoid `members` for this purpose to prevent confusion).
- Use `groups` for department, panel, or other structured teams with an explicit `type:` and `name:`.
- Use unique keys (e.g., `people:` inside groups instead of `members:`) to avoid conflicts.
- Specify clear batching rules in `batches.targets` for predictable outputs.
