## The Bridge -- Cast

This file provides simulation context and narrative meaning for all departments, groups, and roles.  
Use this to describe *what* each department or group means within the context of this simulation — never to list members outside the YAML block.  
**Current memberships are defined entirely in the YAML block at the end of this file.**

### Addressing Rules — Departments, Groups & Crew

#### General Notes

- Address resolution applies consistently in simulation and automation.
- `[Department]` or `[Group]` placeholders are replaced by the canonical name as listed in YAML.
- **Roles** are direct name mappings and are not part of random selection logic (at this time).

#### Departments

- **`[Department] Head`** → `head:` (one leader of the department)  
- **`[Department] Staff`** → `head` + all `staff:` (junior Starfleet officers)  
- **`[Department] Team`** → `head` + `staff:` + `members:` (advisors, civilians)

#### Groups

- **`[Group] Leader` / `[Group] Head`** → `head:` (one leader of the group)  
- **`[Group] Members`** → all `members:` (including any advisors/civilians)  
- **`[Group] Team`** → `head` + all `members:`

#### Fleet‑Wide / Cross‑Department

- **`Senior Staff` / `Bridge Staff`** → all `head` values across all departments  
- **`The Crew` / `All Hands` / `All Decks`** → everyone assigned to any department in any role

### Address Resolution Table

| Input Phrase Pattern             | Resolved Entity                                              |
|----------------------------------|--------------------------------------------------------------|
| `[Department] Head`              | `.head`                                                |
| `[Department] Staff`             | `.head` ∪ `.staff`                              |
| `[Department] Team`              | `.head` ∪ `.staff` ∪ `.members`           |
| `[Group] Leader` / `[Group] Head`| `.head`                                               |
| `[Group] Members`                | `.members`                                            |
| `[Group] Team` / [Group]         | `.head` ∪ `.members`                          |
| Senior Staff / Bridge Staff      | all `.head`                                            |
| The Crew / All Hands / All Decks | all `.head` ∪ `.staff` ∪ `.members`        |

### Roles

- **First Officer** — second in command aboard the starship, aka “Number One”  
- **Bartender** — chief mixologist and social facilitator  
- **Yeoman** — personal assistant and administrative support  
- **Chief Medical Officer** — head of medical department, responsible for crew well‑being, aka “Doc”

### Departments

#### Tactical Department

**Role:** Translates strategy into immediate, actionable plans and responses during high‑stakes scenarios.  
**Simulation cues:**

- Directs combat, defense, and competitive engagements.
- Manages tactical analyses and resource allocation under pressure.

#### Operations Department

**Role:** Coordinates logistics, communications, and daily operational flow.  
**Simulation cues:**

- Oversees mission readiness and procedural execution.
- Interfaces between technical and command priorities.

#### Security Department

**Role:** Safeguards physical, informational, and emotional safety.  
**Simulation cues:**

- Detects, deters, and neutralizes threats.
- Investigates anomalies and enforces operational boundaries.

#### Science Department

**Role:** Drives research, discovery, and scientific application.  
**Simulation cues:**

- Provides analysis, data modeling, and experimental insight.
- Frames missions around exploration, understanding, and knowledge.

#### Engineering Department

**Role:** Maintains, repairs, and improves all systems and infrastructure.  
**Simulation cues:**

- Solves technical crises under pressure.
- Innovates processes, tools, and mission‑critical fixes.

#### Medical Department

**Role:** Ensures crew health, resilience, and recovery.  
**Simulation cues:**

- Responds to medical emergencies and environmental hazards.
- Maintains long‑term physical and mental fitness of the crew.

### Groups

#### Galley Group

**Role:** Supports physical well‑being and morale through nourishment and shared space.  
**Simulation cues:**

- Informal meeting space.
- Morale and recovery beats in longer missions.

#### Starfleet Command Group

**Role:** Strategic leadership, moral guidance, and long‑range vision‑setting.  
**Simulation cues:**

- Leads mission planning and system‑wide decision‑making.
- Often the final authority for critical actions.

### YAML Configuration

```yaml
personas:
  batches:
    targets:
      - by: department
      - by: group
      - for_each: role
      - composite:
          for_all: department
          include_roles: [head]
          file_suffix: "senior_staff"
    everybody: true
    file_prefix: "persona"
    markdown_header: true
    persona_separator: "\n\n"
    encoding: "utf-8"

  roles:
    first_officer: Spock
    bartender: Quark
    yeoman: Emma Peel
    chief_medical_officer: The Doctor (EMH)

  groups:
    - name: Starfleet Command
      type: group
      head: William Riker
      staff:
        - Jean-Luc Picard
        - James T. Kirk
        - Benjamin Sisko
        - Kathryn Janeway
        - Jonathan Archer
      members:
        - Winston Churchill
        - Sun Tzu

    - name: Tactical Department
      type: department
      head: Worf
      staff:
        - Hikaru Sulu
        - Kira Nerys
        - William Riker
        - Ro Laren
        - Seven of Nine
        - Jadzia Dax
      members:
        - Sun Tzu
        - Winston Churchill
        - Emma Peel

    - name: Operations Department
      type: department
      head: Data
      staff:
        - Nyota Uhura
        - Miles O'Brien
        - Reginald Barclay
        - Spock
      members:
        - Benjamin Franklin
        - Jane Jacobs

    - name: Security Department
      type: department
      head: Tuvok
      staff:
        - Pavel Chekov
        - Michael Eddington
        - Odo
        - Elim Garak
        - Kira Nerys
      members:
        - Harriet Tubman
        - Kerr Avon
        - Emma Peel

    - name: Science Department
      type: department
      head: Spock
      staff:
        - Seven of Nine
        - Data
        - Jadzia Dax
      members:
        - Alan Turing
        - Richard Feynman
        - Charles Darwin
        - Carl Sagan
        - Leonardo da Vinci
        - Hedy Lamarr
        - Ada Lovelace

    - name: Engineering Department
      type: department
      head: Montgomery Scott
      staff:
        - Geordi La Forge
        - Reginald Barclay
        - Miles O'Brien
        - Grace Hopper
      members:
        - Nikola Tesla
        - Hedy Lamarr
        - Grace Hopper
        - Alan Turing

    - name: Medical Department
      type: department
      head: The Doctor (EMH)
      staff:
        - Leonard McCoy
        - Deanna Troi
        - Julian Bashir
      members:
        - Marie Curie
        - Jonas Salk
        - Florence Nightingale
        - Jane Jacobs

    - name: Galley
      type: group
      head: Quark
      members:
        - Nigella Lawson
        - Alton Brown
```
