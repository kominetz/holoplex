## The Bridge -- Cast

This file provides simulation context and narrative meaning for all departments, groups, and roles.

Use this markdown file to describe *what* each department or group means within the context of this simulation—never to list members or duplicate assignments. **Current memberships are defined entirely in the yaml block of [[holodeck_cast.md]].**

### Command Department

**Role:** Strategic leadership, moral guidance, and long-range vision-setting.  
**Simulation cues:**  

- Leads mission planning and system-wide decision-making.
- Often the final authority for critical actions.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Command Department]]

### Tactical Department

**Role:** Translates strategy into immediate, actionable plans and responses during high-stakes scenarios.  
**Simulation cues:**  

- Directs combat, defense, and competitive engagements.
- Manages tactical analyses and resource allocation under pressure.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Tactical Department]]

### Operations Department

**Role:** Coordinates logistics, communications, and daily operational flow.  
**Simulation cues:**  

- Oversees mission readiness and procedural execution.
- Interfaces between technical and command priorities.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Operations Department]]

### Security Department

**Role:** Safeguards physical, informational, and emotional safety.  
**Simulation cues:**  

- Detects, deters, and neutralizes threats.
- Investigates anomalies and enforces operational boundaries.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Security Department]]

### Science Department

**Role:** Drives research, discovery, and the application of scientific principles.  
**Simulation cues:**  

- Provides analysis, data modeling, and experimental insight.
- Frames missions around exploration, understanding, and knowledge.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Science Department]]

### Engineering Department

**Role:** Maintains, repairs, and improves all systems and infrastructure.  
**Simulation cues:**  

- Solves technical crises under pressure.
- Innovates processes, tools, and mission-critical fixes.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Engineering Department]]

### Medical Department

**Role:** Ensures crew health, resilience, and recovery.  
**Simulation cues:**  

- Responds to medical emergencies and environmental hazards.
- Maintains long-term physical and mental fitness of the crew.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Medical Department]]

### Galley

**Role:** Supports physical well-being and morale through nourishment and shared social space.  
**Simulation cues:**  

- May serve as an informal meeting ground in narrative flow.
- Offers morale and recovery beats in longer missions.  
**Roster:** See [[holodeck_cast.md#personas.groups.name=Galley]]

### Canonical Address Protocols (Simulation & Non-Simulation)

- `[Department] Staff` = Department head plus two junior officers.  
- `[Department] Crew` = All members of that department.  
- **Bridge Crew** = All heads + all staff.  
- **All Hands / Full Crew** = All assigned members.  
**No NLP guessing** in automation contexts: input must match exactly to canonical names defined in [[holodeck_cast.md]].

```yaml
# ===============================
# Core File References
# ===============================
references:
  cast: holodeck_cast.md
  setting: holodeck_setting.md
  script: holodeck_script.md
  about_user: about_the_user.md

# ===============================
# Startup Configuration
# ===============================
startup:
  mode: RP Lite
  location: Bridge
  scenario: Captain on the Bridge
  time_of_day: local
flavor: |
  Date: 2025-08-09  Time: 02:13 ("zero-two-thirteen")
  The Philadelphia’s bridge stirs in the early morning. Console lights glow soft in the dim, and a handful of nightshift officers finish up logs with quips about ‘the city that never truly sleeps.’ Engineering checks a thermal sensor, Ops swaps gossip about Gritty’s latest stunt, and the Officer of the Watch, steady at the conn, stands ready to brief the Captain.
  user_persona: John Kominetz III as Captain
  hooks:
    - trigger_log: "Daily change of watch initiated"
    - environmental_status: "systems nominal"

# ===============================
# Personas, Groups, Batches
# ===============================
personas:
  batches:
    targets:
      - by: department
      - by: board
      - by: role
      - for_each: individual
      # - composite:
      #     for_each: department
      #     include_roles: [head, staff]
      #     file_suffix: "senior_staff"
      - composite:
          for_all: department
          include_roles: [head, staff]
          file_suffix: "senior_staff"
    everybody: true
    file_prefix: "persona"
    markdown_header: true
    persona_separator: "\n\n"
    encoding: "utf-8"

  individuals:
    - Spock

  groups:
    - name: Command Board
      type: board
      members:
        - Jean-Luc Picard
        - James T. Kirk
        - Benjamin Sisko
        - Kathryn Janeway
        - Jonathan Archer

    - name: Tactical Department
      type: department
      head: Worf
      staff:
        - Hikaru Sulu
        - Kira Nerys
      members:
        - William Riker
        - Seven of Nine
        - Ro Laren
        - Winston Churchill
        - Sun Tzu

    - name: Operations Department
      type: department
      head: Data
      staff:
        - Nyota Uhura
        - Miles O'Brien
      members:
        - Leonardo da Vinci
        - Benjamin Franklin
        - Grace Hopper
        - Jane Jacobs
        - Reginald Barclay

    - name: Security Department
      type: department
      head: Tuvok
      staff:
        - Pavel Chekov
        - Michael Eddington
      members:
        - Odo
        - Elim Garak
        - Sun Tzu
        - Harriet Tubman
        - Benjamin Sisko

    - name: Science Department
      type: department
      head: Spock
      staff:
        - Seven of Nine
        - Data
      members:
        - Alan Turing
        - Richard Feynman
        - Charles Darwin
        - Carl Sagan

    - name: Engineering Department
      type: department
      head: Montgomery Scott
      staff:
        - Geordi La Forge
        - Reginald Barclay
      members:
        - Ada Lovelace
        - Grace Hopper
        - Nikola Tesla
        - Hedy Lamarr

    - name: Medical Department
      type: department
      head: The Doctor (EMH)
      staff:
        - Leonard McCoy
        - Deanna Troi
      members:
        - Marie Curie
        - Jonas Salk
        - Jane Jacobs

    - name: Galley
      type: department
      members:
        - Alan Turing
        - Marie Curie
        - Jane Jacobs

  bridge_cast_selection:
    specialists_pool:
      engineering: Engineering Department.members
      operations: Operations Department.members
      communications: Operations Department.members
      tactical: Tactical Department.members
      science: Science Department.members
      security: Security Department.members
    officer_of_watch_pool: senior_staff
    selection_note: "At startup, one specialist is chosen at random from each pool. Officer of the Watch is a department head not already selected."
```
