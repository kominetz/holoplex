# Markdown Scripting Guide

Mapping Computer Science Concepts onto Markdown Patterns for LLM Programming

## How to Use This Guide

This guide maps programming concepts to Markdown patterns for LLM simulations. Key principles:

- Headings define unique entities; use plain labels + key:value for data
- Use {variables} for runtime substitution; reserve [Type: id] for explicit cross-references  
- Prefer sets/lists/dictionaries over prose; keep examples minimal and literal
- Align with YAML/Python where it improves clarity (true/false/null, comments, multiline)
- Follow the Markdown Generation Policy at the end for lintability

---

## Basic Syntax

Recommended Practice:

- Maintain consistent 2-space indentation--no tabs.
- Use blank lines to separate sections
- Leverage markdown's semantic structure rather than fighting it.

### Whitespace Rules

LLMs process markdown more efficiently when following standard conventions. Use 2 spaces for indentation consistently. Avoid tabs, as they create parsing ambiguity. Markdown preserves meaningful whitespace within code blocks but collapses multiple spaces in regular text.

### Tokenization Impact

Markdown is often more token-efficient than JSON for LLMs, frequently reducing token counts by roughly 10–20% in common scenarios, though results vary by content and tokenizer. Well-structured, “clean” markdown can meaningfully improve retrieval quality in RAG-style systems and lower token usage, but the magnitude of improvement depends on the corpus, chunking strategy, and model. In general, leveraging hierarchical structure (headings, lists, sections) tends to help models maintain context more reliably than unstructured text.

### Attention/Emphasis Control

- **Bold**: High attention, primary information
- *Italic*: Contextual information, temporary state  
- Plain: Standard information, stable attributes
- `Backticks`: Genuine code elements (filenames, variable names, technical IDs, mode_ids)

### Structure Rules

- Headings: For unique entities only (singletons)
- Plain Labels: For repeated patterns within sections
- Plain key:value: For object properties
- List key:value: For enumerable collections

### Namespace Rules

- Use heading hierarchy for scope: `## Characters` → `### Character - Name`
- Use hyphens in headings: `Character - Picard` not `Character: Picard`
- Use colons for data: `rank: Captain` not `rank - Captain`

### File Organization

- One complex entity per file (scenarios, major characters)
- Multiple simple entities per file (grouped by function/location)
- Separate concerns: characters/, locations/, scenarios/, assets/

### Cross-Reference Format

- `[Character: picard]` for explicit links
- Consistent entity IDs across all files
- Document reference vocabulary in program config

For semantics and examples, see [Cross-Reference Links](#cross-reference-links).

## Data Types

There is no concept of explicit data types. The LLM infers types from context. When in doubt, follow python and yaml conventions for booleans and null.”

## Data Structures

On Dictionary vs Object:

- Dictionary: Use when you need multiple instances of the same entity type
- Object: Use for single entity with multiple properties
- Simple key:value: Use for configuration or state variables

Example Clarification:

```markdown
## Character Registry (Dictionary - multiple entities)
### Character - Picard
### Character - Data

### Character - Picard (Object - single entity properties)
name: Jean-Luc Picard
rank: Captain

## Session State (Simple key:value - configuration)
user_location: bridge
current_mission: diplomatic
```

For complete authoring patterns, see [Program Structures](#program-structures).

### Array/List of items

Use: label + ordered/unordered list

```markdown
Mission Steps:

- Brief the crew
- Conduct reconnaissance  
- Execute objective
- Extract and debrief
```

Use a blank line after a name/label when it’s introducing a list; omit it only when the label is itself a list item.

- Label introducing a list (recommended): put a blank line between the label and the list so the list starts as a new block. This avoids ambiguity across renderers and reliably parses as: paragraph (label), then list.

  ```markdown
  Example:

  - Mission Steps
    - Brief the crew
  - Conduct reconnaissance
  ```

- Label as part of the first list item: do not use a blank line; instead, put the label text inside the first item. This is appropriate only if the label is semantically the first item rather than a separate heading/label.

  ```markdown
  Example:

  - Mission steps: brief the crew
  - Conduct reconnaissance
  ```

- What not to do: a label line followed immediately by “-item” (no space) or other malformed markers. Without the required space after the marker, the lines won’t be parsed as list items. Always use a space after the marker (“- item”).

Rule of thumb: If the label is a title/descriptor for the list, insert a blank line. If the label is itself an item, omit the blank line and keep it in the item text.

Examples in this document may omit blank lines after labels and headings to conserve space.

### HashMap/Dictionary of items

Use: Map name + key:value pairs (one per line). Use when items are looked up by ID.

```markdown
Character Registry:
picard: active
data: active
troi: active
```

When entries need multiple properties, either reference separate object definitions:

```markdown
Character Registry:
picard: character
data: character
troi: character

### Character - picard
name: Jean-Luc Picard
rank: Captain
status: Active

### Character - data
name: Data
rank: Lt. Cmdr
status: Active
```

Or inline the objects under the map:

```markdown
Character Registry:
picard:
  name: Jean-Luc Picard
  rank: Captain
  status: Active
data:
  name: Data
  rank: Lt. Cmdr
  status: Active
```

### Set of Items

Use: Named collection where order does not matter and duplicates are not allowed. Prefer a set when semantics are membership/containment rather than sequence/priority.

#### Pattern A — Label + one ID per line (compact, clearly unordered)

```markdown
Bridge Crew Set:
picard
riker
data
worf
```

Guidelines:

- One member per line under the set label.
- Treat each line as a unique member; avoid duplicates.
- Use lowercase, snake_case IDs for stable referencing.

#### Pattern B — Label + toggled membership (map of IDs to true)

```markdown
Enabled Features Set:
chat: true
rag: true
evals: true
```

Guidelines:

- Use when tooling may toggle membership programmatically or when explicit uniqueness validation is desired.
- Keep values boolean; avoid mixing additional properties here (use an object/record if needed).

Operations (conventional verbs for clarity; record them where you handle state)

```markdown
add_to: Bridge Crew Set → la_forge
remove_from: Bridge Crew Set → riker
contains?: Bridge Crew Set → data
```

Notes:

- Do not imply order; if order matters, use a list instead.
- Do not attach properties to set members in the set block; define properties in an object/record or a separate dictionary keyed by the same IDs.
- Keep one pattern per set: either one-ID-per-line or toggled membership, not both mixed in the same block.

### Object/Record with properties

Use: Heading + plain key:value pairs

```markdown
### Character - Picard
name: Jean-Luc Picard
rank: Captain
department: Command
status: Active
```

### Database table/records

Use: Markdown table with header row

```markdown
| Name    | Rank      | Department | Status  |
|---------|-----------|------------|---------|
| Picard  | Captain   | Command    | Active  |
| Data    | Lt. Cmdr  | Operations | Active  |
```

### Tree/hierarchy structure

Use: Nested heading levels

```markdown
# Program Root
## Characters (namespace)
### Character - Picard (unique entity)
## Locations (namespace)  
### Location - Bridge (unique entity)
```

## Data Access Patterns

### Primary key/unique identifier

Use: Contextual heading (Character/Location/Scenario + hyphen + name)

```markdown
### Character - Picard
```

How does this differ from the Data Structure Pattern?

```markdown
### Primary Key Pattern (Unique Identification)
# Purpose: Enable cross-referencing between entities
### Character - picard (unique identifier)
### Location - bridge (unique identifier)

### Data Structure Pattern (Organization)
# Purpose: Group related information
Bridge Crew (collection):
- picard
- riker
- data
- worf
```

### Foreign key/reference

Use: Key:value with entity ID as value

```markdown
current_location: bridge
commanding_officer: picard
```

### Collection membership

Use: collection name + list of entity IDs

```markdown
Bridge Crew:
- picard
- riker  
- data
- worf
```

### Lookup table

Use: Table with key columns

```markdown
| Command  | Function        | Access Level |
|----------|-----------------|--------------|
| arch     | Program control | Director     |
| freeze   | Pause execution | Any user     |
| end      | Terminate       | Director     |
```

## Control Structures

### Conditional logic

Use: Heading + conditional descriptions

```markdown
### Character Behavior - Data
Default State: Helpful, analytical, curious
If User Asks Personal Question: Shows increased interest, asks follow-up
If Logical Contradiction Detected: Requests clarification, offers analysis
```

### Switch/case logic

Use: Conditional descriptions with If/When patterns

```markdown
### User Action Responses
If "question Data": Technical analysis, logical perspective, curious follow-up
If "consult Troi": Emotional insight, interpersonal guidance, empathetic response  
If "review displays": Current ship status, tactical options, data interpretation
```

### Function/procedure definition

Use: Heading + structured attributes

```markdown
### Emergency Protocol Alpha
Prerequisites: Red alert status, captain's authorization
Steps:
- Evacuate non-essential personnel
- Seal critical sections
- Prepare for emergency separation
Result: Ship prepared for emergency procedures
```

### Sequential execution

Use: Numbered list (implies order)

```markdown
1. Initialize character relationships
2. Load starting location
3. Present initial scenario
4. Wait for user input
```

### Parallel/unordered operations

Use: Unordered list (no implied sequence)

```markdown
Available Actions:
- Question Data about technical details
- Consult with Troi about crew psychology
- Review tactical displays
- Contact other departments
```

## Loop Structures

Use various patterns to represent iterative operations in markdown for LLM simulations.

Implementation Notes:

- Mermaid diagrams are highly effective for complex loops as they provide explicit visual logic that reduces misinterpretation by LLMs
- Use conditional patterns for simple while/until loop equivalents  
- Use counter patterns for traditional for-loop behavior
- Nested structures work well with markdown's heading hierarchy
- Always specify exit conditions clearly to prevent infinite loop interpretation
- Consider event-driven patterns for reactive simulations where the LLM should respond to changing conditions

Performance Tip: LLMs process conditional repetition patterns more reliably when exit conditions are stated positively (e.g., "When complete" rather than "While not complete").

### Pattern 1: Conditional Repetition

Use: Heading + loop condition + action block

```markdown
### Repeat Until Complete
Condition: While mission_status != "complete"
Actions:
- Assess current situation
- Execute next step
- Update mission_status based on results
Exit: When mission_status == "complete"
```

### Pattern 2: Counter-Based Iteration  

Use: Heading + counter specification + numbered actions

```markdown
### Security Sweep Protocol
Loop: For each deck (1 through 12)
Counter: current_deck
Actions:
1. Scan for anomalies on deck {current_deck}
2. Report findings to security chief
3. Move to next deck
Exit: When current_deck > 12
```

### Pattern 3: Collection Iteration

Use: Heading + collection reference + item processing

```markdown
### Process All Crew Members
Loop: For each member in bridge_crew
Current Item: crew_member
Actions:
- Check {crew_member} status
- Update {crew_member} assignment
- Log interaction with {crew_member}
Exit: When all crew members processed
```

### Pattern 4: Mermaid Flow Diagrams (Recommended for Complex Loops)

Use: Mermaid flowchart with explicit loop paths

```mermaid
### Diagnostic Loop Flow
flowchart TD
    A[Start Diagnostics] --> B[Run System Check]
    B --> C{All Systems Green?}
    C --> |No| D[Identify Issues]
    D --> E[Apply Repairs]
    E --> B
    C --> |Yes| F[Complete Diagnostics]
    F --> G[End]
```

### Pattern 5: Event-Driven Loops

Use: Heading + trigger conditions + response actions

```markdown
### Continuous Monitoring Loop
Trigger: While ship_status == "active"
Monitor: 
- Incoming communications
- Sensor readings  
- Crew reports
Response: Execute appropriate handler for each event
Exit: When ship_status changes to "docked"
```

### Pattern 6: Nested Loop Structure

Use: Heading hierarchy + multiple loop levels

```markdown
### Complete Ship Inspection
Outer Loop: For each deck in ship_decks
  Inner Loop: For each section in current_deck
    Actions:
    - Inspect section for damage
    - Test all systems in section
    - Record inspection results
  Inner Exit: When all sections on deck completed
Outer Exit: When all decks inspected
```

## Error Handling and Validation

### Input validation

Use: Section + list of valid options

```markdown
### Valid User Roles
- Visiting Officer (default)
- Starfleet Academy Cadet  
- Diplomatic Attaché
- Medical Consultant
```

### Fallback behavior

Use: Conditional defaults

```markdown
### Default Responses
If User Input Unclear: Request clarification politely
If Character Unavailable: Suggest alternative character or location
If Scenario Stalled: Provide gentle narrative prompt
```

## Program Structures

Use clear section names to indicate mutability. Prefer semantic headings that make intent obvious: "Program Configuration" for static setup values and "Current Session State" for dynamic values that evolve during execution.

Do not mix static and dynamic keys in the same section. If a configuration value is overridden at runtime, reflect the effective value in session state rather than mutating configuration.

### Program Configuration

Use: Section heading + key:value pairs for static setup values

```markdown
## Program Configuration
include_file: holodeck_protocols.md
default_mode: text_mode
default_location: ready_room
```

### Current Session State

Use: Section heading + key:value pairs for dynamic runtime values

```markdown
## Current Session State
active_mode: roleplay_light
current_characters: picard, data
user_preferences: casual_interaction
```

### Event Handlers

Use: label + procedural list

```markdown
on_mode_change:
- Update session state
- Notify active characters
- Log transition

on_error:
- Display helpful message
- Suggest recovery options
- Maintain current state
```

## Advanced Syntax

### YAML and Python Syntax Alignment

LLMs have extensive training on YAML and Python syntax. Leveraging familiar patterns from these languages enhances parsing reliability and reduces cognitive load during interpretation.

#### Syntax Convergence Benefits

Current Alignment Strengths:

- **Key:Value Pairs**: `rank: Captain` matches YAML exactly, familiar from Python dictionaries
- **List Syntax**: `- item` aligns perfectly with YAML arrays  
- **Nested Objects**: Indented structures mirror both YAML nesting and Python dict literals
- **Variable Substitution**: `{variable}` parallels Python f-string syntax
- **Hierarchical Documents**: Heading structure reflects YAML document organization

#### Enhanced Boolean and Null Patterns

Use: Explicit boolean and null values for clear state representation

```markdown
## System Status
shields_active: true
warp_core: false
navigation: null
emergency_power: true
```

Boolean Value Guidelines:

- `true` / `false` for explicit boolean states (not "enabled"/"disabled")
- `null` for undefined, missing, or not-applicable values
- Distinguish `false` (explicitly disabled) from `null` (undefined/not-set)
- LLMs recognize these from JSON/YAML training data

#### Null Value Semantics

Use: `null` to represent missing, optional, or undefined data

```markdown
### Character - guest_officer
name: null  # To be assigned during scenario
rank: Lieutenant
department: null  # Depends on mission requirements
clearance_level: standard
```

Null Usage Patterns:

- Optional character attributes not yet defined
- Placeholder values for runtime assignment
- Missing data that may be filled later
- Distinguish from empty strings `""` or zero values `0`

#### Inline Documentation

Use: Hash comments for inline documentation and context

```markdown
## Scenario Configuration
# Diplomatic mission with moderate tension
scenario_type: diplomatic_crisis
difficulty: moderate  # Suitable for intermediate players
estimated_duration: 45  # Minutes
player_role: cultural_liaison

# Character availability depends on previous choices
characters_available:
- picard  # Always available
- troi    # Available if diplomatic_protocols: true
- data    # Available if technical_analysis: required
```

Comment Guidelines:

- Use `# comment` for line-level documentation
- Place comments above the item they describe
- Use for explaining conditional logic, constraints, or context
- Enhance LLM understanding of intent and relationships

#### Multiline String Values

Use: Pipe syntax for multiline narrative content

```markdown
### Character - picard
background_story: |
  Captain Jean-Luc Picard commands the Federation flagship USS Enterprise.
  A veteran of numerous diplomatic missions, he prefers negotiation to conflict.
  His experience with the Borg has given him unique insights into assimilation threats.

mission_briefing: |
  The Romulan delegation has requested emergency talks regarding territorial disputes.
  Intelligence suggests internal political pressures may affect their negotiating position.
  Recommend cultural sensitivity protocols and empathic support presence.
```

Multiline Guidelines:

- Use `|` (pipe) to indicate multiline content starts on next line
- Maintain consistent indentation for continuation lines
- Ideal for character descriptions, mission briefings, dialogue
- Preserves formatting and line breaks within content
- LLMs recognize this from YAML training data

#### Environment and Configuration Layering

Use: Nested configuration for different simulation contexts

```markdown
## Environment Configuration
development:
  debug_mode: true
  rapid_progression: true
  safety_overrides: enabled
  logging_level: verbose

production:
  debug_mode: false
  rapid_progression: false
  safety_overrides: disabled
  logging_level: standard

# Current active environment
active_environment: development
```

Environment Pattern Benefits:

- Multiple configuration profiles in single file
- Easy switching between simulation modes
- Familiar pattern from DevOps and deployment systems
- Clear separation of concerns for different contexts

#### Type Hints and Validation

Use: Inline type annotations for complex data (optional)

```markdown
## Character Stats
# Format: name: value  # type: expected_range
strength: 85       # int: 1-100
intelligence: 95   # int: 1-100
diplomacy: 90      # int: 1-100
combat_skill: 70   # int: 1-100
species: human     # string: valid_species_list
rank: captain      # enum: starfleet_ranks
```

Type Annotation Guidelines:

- Use sparingly, only when validation is critical
- Format: `# type: constraint` for documentation
- Help LLMs understand expected value types and ranges
- Useful for numerical stats, enumerations, and constrained values

#### YAML-Style References

Use: Anchor-like patterns for reusable configurations

```markdown
## Standard Configurations

### Configuration - diplomatic_standard
safety_level: moderate
cultural_protocols: enabled
universal_translator: active
escort_required: false

### Configuration - high_risk_diplomatic  
safety_level: maximum
cultural_protocols: strict
universal_translator: active
escort_required: true

## Scenario Applications
# Reference standard configurations by name
routine_contact: diplomatic_standard
first_contact: high_risk_diplomatic
treaty_negotiation: diplomatic_standard
```

Reference Pattern Benefits:

- Reduces duplication across scenarios
- Consistent configuration sets
- Easy to update standard patterns
- Clear separation of templates from applications

### Variable References and Templating

Use variable references to create reusable, dynamic content that avoids hard-coding entity names. This enables flexible event definitions, cross-file references, and maintainable simulations.

#### Variable Syntax

Use: Curly braces for variable substitution

```markdown
Event Template:
action: "{character_list}, report to {location}"
timing: "immediately"
authority: "{commanding_officer}"
```

Guidelines:

- Use lowercase, snake_case for variable names
- Keep variable names descriptive and unambiguous  
- Variables can reference single entities or collections
- Variables resolve at simulation runtime, not parse time

#### Intra-File References

Use: Variable names that match entity IDs within the same file

```markdown
### Character - picard
name: Jean-Luc Picard
rank: Captain

### Event - Emergency_Drill
participants: "{bridge_crew}"
location: "{main_bridge}"
command: "{picard}, initiate emergency protocols"
```

Resolution Rules:

- Variables resolve to entity IDs defined in the same file
- Use the exact ID from headings (Character - picard → picard)
- Collections resolve to all members of that set/list
- Undefined variables should fail gracefully with clear error messages

#### Inter-File References

Use: Namespace prefixes for cross-file entity references

```markdown
#### Event - Diplomatic_Mission
participants: "{characters:picard}, {characters:troi}"
location: "{locations:conference_room}"
briefing_materials: "{assets:diplomatic_protocols}"
```

File Organization:

- Prefix format: `{filename:entity_id}`
- Files should declare their namespace in a header comment
- Use consistent file naming: characters.md, locations.md, scenarios.md
- Document cross-file dependencies in program configuration

### Collection Variables

Use: Collection names for dynamic list expansion

```markdown
Bridge Crew:
- picard
- riker
- data
- worf

#### Event - General_Quarters
announcement: "All hands, {bridge_crew}, report to stations"
locations: "{all_decks}"
duration: "{standard_drill_time}"
```

Expansion Behavior:

- `{bridge_crew}` expands to: "picard, riker, data, worf"
- `{all_decks}` expands to all members of the all_decks collection
- Use consistent comma-separated format for list expansion
- Empty collections expand to empty string, not error

#### Conditional References

Use: If/when patterns with variable substitution

```markdown
### Event - Security_Alert
If threat_level == "yellow":
  participants: "{security_team}"
  location: "{tactical_stations}"
If threat_level == "red":
  participants: "{all_senior_staff}"
  location: "{battle_bridge}"
```

#### Reference Validation

Use: Validation section to define required entities

```markdown
### Event Dependencies
Required Characters:
- picard (commanding_officer role)
- data (technical_analysis role)

Required Locations:
- main_bridge (primary_location)
- ready_room (private_meeting_space)

Optional References:
- guest_characters (diplomatic scenarios only)
```

#### Cross-Reference Links

Use: Square brackets for explicit cross-file navigation (distinct from variables)

```markdown
Character Background:
commanding_officer: picard
mentor_relationship: [Character: guinan]
previous_assignment: [Location: stargazer_bridge]
```

Guidelines:

- `[Type: entity_id]` format for explicit links
- Reserve square brackets for intentional cross-references, not variable substitution
- Use when the reference needs to be clickable/navigable
- Distinguish from variables which expand inline

#### Variable Syntax Analysis

Sigil Selection Rationale:

- `{}` (curly braces): RECOMMENDED - no markdown conflicts, high LLM familiarity from Python format strings
- `` ` `` (backticks): AVOID - conflicts with code literals (275+ uses in guide)
- `[]` (square brackets): CAUTION - potential conflicts with markdown links
- `*/**` (asterisks): AVOID - conflicts with emphasis syntax
- `$` (dollar signs): AVOID - LaTeX math conflicts in some renderers
- `%` (percent signs): POSSIBLE but less intuitive for LLMs

The curly brace syntax provides zero conflict with existing markdown patterns while leveraging LLMs' strong familiarity with template string conventions from Python and other systems.

### Optional Markdown Extensions

These patterns are not essential for core functionality but may enhance specific use cases. Evaluate based on your simulation requirements and tooling constraints.

#### Boolean State Tracking

Use: Task list syntax for on/off states (optional)

```markdown
Ship Systems Status:
- [x] Shields operational
- [x] Weapons online
- [ ] Warp drive offline
- [ ] Life support backup mode
```

Benefits:

- More visually clear than `shield_status: active`
- Familiar checkbox metaphor for LLMs
- Interactive appearance in some renderers

Considerations:

- Not universally supported across all markdown processors
- May interfere with some automated parsing tools
- Alternative: standard key:value pairs work reliably everywhere

#### System Messages and Meta-Information

Use: Blockquotes for system-level information (optional)

```markdown
#### Event - Diplomatic_Crisis

> System: This scenario requires cultural sensitivity protocols
> Warning: High-stakes diplomatic consequences possible
> Note: Troi's empathic abilities are essential for success

Participants: "{diplomatic_team}"
Location: "{conference_room}"
```

Benefits:

- Visually distinct from regular content
- Useful for LLM behavioral guidance
- Clear indication of meta-information

Considerations:

- Consider whether special formatting adds meaningful value
- Alternative: Use standard labels (System Note:, Warning:) for similar effect

#### Conditional/Disabled Content

Use: Strikethrough for disabled or conditional elements (optional)

```markdown
Available Actions:
- Negotiate with diplomats
- ~~Activate weapons systems~~ (disabled during diplomatic mission)
- Consult with cultural advisor
- ~~Evacuate civilians~~ (unavailable until red alert)
```

Benefits:

- Clear visual indication of disabled states
- Maintains context while showing restrictions
- Useful for conditional menu systems

Considerations:

- May not render consistently across all environments
- Alternative: Use conditional sections or comments for disabled content

#### Alternative State Patterns

Consider these alternatives to the optional extensions above:

```markdown
Ship Systems (Standard Approach):
shields: operational
weapons: online
warp_drive: offline
life_support: backup_mode

System Notes (Standard Approach):
behavioral_guidance: cultural_sensitivity_required
stakes_level: high
required_abilities: empathic_sensing

Conditional Content (Standard Approach):
available_actions:
- negotiate_with_diplomats
- consult_cultural_advisor

disabled_actions:
- activate_weapons (reason: diplomatic_mission_active)
- evacuate_civilians (reason: requires_red_alert)
```

Recommendation: Start with standard patterns and add optional extensions only when they provide clear, measurable benefits for your specific use case.

## Markdown Generation Policy (for LLMs)

Follow these directives when generating or editing Markdown in this project. The goal is strict, deterministic Markdown optimized for machine parsing and linting.

- Structure, not style
  - Use headings, blank lines, lists, and key:value lines to convey structure.
  - Do not use emphasis (bold/italic) for structural labels or sectioning.
  - Avoid any stylistic flourishes, emojis, or decorative characters.
  - Never use ligatures or html entities.

- Headings
  - Use Markdown headings only for unique entities or section titles.
  - Headings must be unique within the file. Do not simulate headings with bold text.

- Labels and data blocks
  - Use plain label lines ending with a colon, followed by content on subsequent lines.
  - Examples:
    - Label introducing a list:
  
      ```markdown
      Label:
      - item
      ```

    - Map/dictionary:

      ```markdown
      Map Name:
      key1: value1
      key2: value2
      ```

    - Set (unordered membership):

      ```markdown
      Set Name:
      member_a
      member_b
      ```

- Lists
  - Use “- ” (hyphen + single space) for unordered list items.
  - Insert a blank line between a label and the list it introduces.
  - Never use “-item” (no space) or tabs for indentation.
  - Keep lists “tight” unless multi‑paragraph items are required.

- Dictionaries and sets
  - Dictionary: “Map Name:” + one key:value per line.
  - Set: “Set Name:” + one ID per line (no bullets), or a toggle map (id: true) if tooling requires.
  - Do not mix simple values and inline objects in the same dictionary; keep one pattern per map.

- Objects/records
  - Define objects under unique headings only when they represent single entities.
  - Use plain key:value pairs under the object heading.
  - If reusing objects, reference them from maps by ID/type, and define them once.

- Code fences and diagrams
  - Place opening and closing fences on their own lines, with no trailing characters.
  - Add a blank line before and after fenced blocks.
  - Use the correct language tag (“```text”, “```mermaid”) and do not HTML‑escape within fences.

- Whitespace and indentation
  - Use spaces only (no tabs). Indentation must be consistent (2 spaces).
  - Add blank lines to separate logical blocks; do not rely on extra spaces for layout.
  - Do not include non‑breaking spaces or zero‑width characters.

- Consistency rules
  - Use a single convention per construct within a file (e.g., one set format, one dictionary style).
  - Do not alternate between bolded labels and plain labels; use plain labels only.
  - Do not switch between inline and block forms of the same construct without a stated reason.

- Mutability semantics
  - Configuration (static) and Session State (dynamic) must be separate sections.
  - Do not mutate configuration at runtime; reflect changes in session state.

- Error avoidance
  - No emphasis‑as‑headings (avoids MD036).
  - No list items without space after the marker.
  - No headings inside code fences unless demonstrating literal Markdown.
  - No prose and code fences on the same line.

- If in doubt, choose the simpler, more explicit form
  - Prefer plain label + colon over styled labels.
  - Prefer separate blocks over overloaded mixed formats.
  - Prefer explicit exit conditions and positive phrasing in control patterns.

You MUST confirm adherence by validating:

- Headings are unique and only used for sections/entities.
- Lists have a blank line after labels and a space after markers.
- Code fences are isolated on their own lines with correct language tags and unescaped content.
- No bold/italic used for structure; labels are plain “Label:”.

If any requested output conflicts with these rules, prioritize this policy and note the deviation.
