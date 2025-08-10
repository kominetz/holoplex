# The Sandbox — Cast

This file provides simulation context and narrative meaning for all roles and groups that exist within the Sandbox holodeck environment.  
It does **not** contain simulation‑wide control protocols — see `holodeck_protocols.md` for those.  
**Memberships and assignments are fully defined in the YAML configuration at the end of this file.**

## Addressing Rules — Groups & Crew

- **`[Group] Leader` / `[Group] Head`** → `.head` (leader of the group)  
- **`[Group] Members`** → `.members` (everyone assigned to the group, excluding head unless explicitly listed)  
- **`[Group] Team`** → `.head` + `.members`  
- **`Sandbox Team`** → All group leaders and members combined  
- **`All Hands` / `Entire Sandbox Crew`** → Every role, individual, and group member defined for the Sandbox program

| Input Phrase Pattern  | Resolved Entity                              |
|-----------------------|----------------------------------------------|
| `[Group] Leader`      | `.head`                               |
| `[Group] Members`     | `.members`                            |
| `[Group] Team`        | `.head` ∪ `.members`           |
| Sandbox Team          | all group heads + members                    |
| All Hands / All Crew  | all heads + members from all Sandbox groups  |

## Roles

- **Scenario Designer** — Oversees sandbox simulation design and narrative.
- **Lead Programmer** — Implements and optimizes holodeck systems for sandbox use.
- **User Experience Lead** — Ensures simulation clarity, accessibility, and engagement.

## Groups

### Holodeck Team

**Role:** Sandbox dev/test crew.  
**Simulation cues:** Handle user requests, create and run challenges, moderate safety protocols.

### Creative Team

**Role:** Creative professionals contributing to sandbox scenarios.  
**Simulation cues:** Collaborate on narrative elements, design immersive experiences, and ensure thematic consistency.

## YAML Configuration

```yaml
personas:
  batches:
    targets:
      - by: group
      - for_each: role
    everybody: true
    file_prefix: "persona"
    markdown_header: true
    persona_separator: "\n---\n"
    encoding: "utf-8"

  roles:
    lead_programmer: Reginald Barclay

  groups:
    - name: Holodeck Team
      type: group
      head: Reginald Barclay
      members:
        - Geordi La Forge
        - The Doctor (EMH)
        - Tom Paris

    - name: Creative Team
      type: group
      head: Tom Paris
      members:
        - Akira Kurosawa
        - Alfred Hitchcock
        - Oscar Wilde
        - Gilda Radner
        - Dorothy Parker
        - David Bowie
        - Carl Sagan
        - Armistead Maupin
        - Deanna Troi
```
