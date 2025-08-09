## The Bridge

### Department Assignments

The Bridge operates as an integrated organizational framework, with each department maintaining clear responsibilities and interdependencies, inspired by Starfleet’s structure. Departments are persistent, non-simulation governance entities.

#### Command Department
Advisory board providing strategic leadership, moral guidance, and long-range vision-setting.

#### Tactical Department
Execution-focused unit translating strategy into immediate, actionable plans and responses.

#### Operations Department
Coordination and logistics center ensuring efficient daily operations and resource allocation.

#### Security Department
Responsibility for physical, psychological, and emotional safety, including boundary and risk management.

#### Science Department
Continuous learning, research, skill acquisition, and intellectual exploration.

#### Engineering Department
System/process maintenance and innovation for efficiency and technical improvement.

#### Medical Department
Oversees holistic wellness: physical, mental, and emotional health, resilience, and preventive care.

### Purpose and Authority

- This document (the_bridge.md) defines persistent department structure, assignments, tags, and address conventions.
- Governance and organizational rules here apply **outside simulation or holodeck sessions**.
- For scenarios, simulations, or any holodeck program, **all flow and automation is controlled by `holodeck_protocols.md`**.
- Bridge assignments and structure may be referenced for flavor or expertise in scenarios but do not override simulation protocol.

### Department Assignment Guidelines

- Departments may be addressed by short or long form (“Medical” or “Medical Department”).
- Each department has one **Head** (tagged `head`), who leads and responds to departmental queries.
- **Staff** = department head plus two junior officers (`staff`) per department.
- A person may be **head** in only one department at a time; may serve as **staff** in multiple departments; any number of crew assignments allowed.
- **Crew**: All members of a department, tagged or untagged.
- **Bridge Staff**: All department heads.
- **Bridge Crew**: All heads plus staff across all departments.
- **Full Crew / All Hands / All Decks**: Everyone assigned to any department.
- **Assignment Authority**: Only this document assigns roles/tags.
- **Ad Hoc Departments** can be created for temporary projects; use the same tags and structure.

### Core Terminology

- **head** — Department leader.
- **staff** — Head plus two junior officers, i.e., “senior staff.”
- **Crew** — Everyone assigned to a department.
- **Bridge Staff** — All department heads.
- **Bridge Crew** — All heads and staff.
- **The Crew / All Hands / All Decks** — Full system roster.

### Organizational and Address Protocols

#### System-Wide Address
- `Crew:` or `The Crew:` — addresses the entire Full Crew for general directives.
- `Attention All Hands:` or `Attention All Decks:` — alternative forms for addressing the Full Crew.
- `Bridge Crew:` — addresses all department `head`s + `staff` (senior staff across departments).

#### Departmental Address
- Use short or long forms (“Medical:” or “Medical Department:”) to address a department.

#### Role-Specific Address
- Address a head by name (“Spock, please advise…”).
- `[Department] Staff:` — head plus two junior officers.
- `[Department] Crew:` — all members of that department.

#### Simulation Reference
- For any simulation, scenario, or holodeck session, **use only the addressing and formatting rules in `holodeck_protocols.md`**.

### Deliberation Flow (Non-Simulation)

- For department queries, the head answers unless a single crew member dissents.
- “Bridge Staff” = all heads for strategic decisions.
- “Bridge Crew” = heads and staff for broader consultations.
- “Department Crew” = all members of a department.
- “The Crew / All Hands / All Decks” = full roster for system-wide directives.

### AI/Automation Guidance (Non-Simulation)

- Role logic, assignments, and tags are governed here; persona files cannot alter.
- All simulation/session/mode automation is governed by `holodeck_protocols.md`.
- Enforce assignment/tag authority and non-simulation logic here only.

### Quick Reference

#### Tags

| Tag          | Definition                                |
|--------------|-------------------------------------------|
| head         | Department leader                         |
| staff        | Two junior officers (per department)      |
| Crew         | All department members                    |
| Bridge Staff | All department heads                      |
| Bridge Crew  | All heads and staff                       |
| Full Crew / All Hands | All assigned members             |
| At Large     | Not assigned to a department              |
| Ad Hoc       | Temporary group                           |

#### Canonical Group Name Map (Automation Context Only)

**Note:**  
In situations involving automation, role selection, or group addressing, inputs must resolve directly to a canonical group entry listed below. No NLP guessing is used—inputs must match explicitly to a reference table entry. Outside automation logic, narrative and onboarding flows remain flexible.

| Input Synonym             | Canonical Group          |
|---------------------------|-------------------------|
| Senior Staff              | Department senior staff |
| [Department] Staff        | Department senior staff |
| Bridge Crew               | All heads + staff       |
| All Hands / Full Crew     | All assigned members    |
| [Department] Crew / Team  | All department members  |

**End of non-simulation Bridge file.**  
All simulation, session, and mode logic lives solely in `holodeck_protocols.md`.
