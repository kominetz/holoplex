# Markdown-as-Code for LLMs: Quick Reference

Mapping Computer Science Concepts onto Markdown Patterns for LLM Programming

## Basic Syntax

Recommended Practice:

- Maintain consistent 2-space indentation--no tabs.
- Use blank lines to separate sections
- Leverage markdown's semantic structure rather than fighting it.

### Whitespace Rules

LLMs process markdown more efficiently when following standard conventions. Use 2 spaces for indentation consistently. Avoid tabs, as they create parsing ambiguity. Markdown preserves meaningful whitespace within code blocks but collapses multiple spaces in regular text.

### Tokenization Impact

Markdown is often more token-efficient than JSON for LLMs, frequently reducing token counts by roughly 10–20% in common scenarios, though results vary by content and tokenizer. Well-structured, “clean” markdown can meaningfully improve retrieval quality in RAG-style systems and lower token usage, but the magnitude of improvement depends on the corpus, chunking strategy, and model. In general, leveraging hierarchical structure (headings, lists, sections) tends to help models maintain context more reliably than unstructured text.

## Data Types

There is no concept of explicit data types. The LLM infers types from context.

### Session variables

Use: State section + variable assignments

```markdown
## Session State
user_reputation: respected
last_location: ten_forward
active_mission: diplomatic_contact
trust_levels: picard_high, data_medium, worf_low
```

### Global constants

Use: Configuration section + constant definitions

```markdown
## Program Configuration
ship_name: Enterprise-D
time_period: TNG Season 5
safety_protocols: enabled
maximum_session_length: 120_minutes
```

## Data Structures

On Hash Map vs Object/Record:

- Hash map/dictionary: Use when you need multiple instances of the same entity type
- Object/Record: Use for single entity with multiple properties
- Simple key:value: Use for configuration or state variables

Example Clarification:

```markdown
## Character Registry (Hash Map - multiple entities)
### Character - Picard
### Character - Data

### Character - Picard (Object - single entity properties)
name: Jean-Luc Picard
rank: Captain

## Session State (Simple key:value - configuration)
user_location: bridge
current_mission: diplomatic
```

This creates clear semantic boundaries for LLM interpretation

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
  Mission Steps:

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

## Control Structures

### Conditional logic

Use: Heading + conditional descriptions

```markdown
### Character Behavior - Data
Default State: Helpful, analytical, curious
If User Asks Personal Question: Shows increased interest, asks follow-up
If Logical Contradiction Detected: Requests clarification, offers analysis
```

### If you want: Switch/case logic

Use: Conditional descriptions with If/When patterns

```markdown
### User Action Responses
If "question Data": Technical analysis, logical perspective, curious follow-up
If "consult Troi": Emotional insight, interpersonal guidance, empathetic response  
If "review displays": Current ship status, tactical options, data interpretation
```

## Looping

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

## Programming Constructs

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

### If you want: Sequential execution

Use: Numbered list (implies order)

```markdown
1. Initialize character relationships
2. Load starting location
3. Present initial scenario
4. Wait for user input
```

### If you want: Parallel/unordered operations

Use: Unordered list (no implied sequence)

```markdown
Available Actions:
- Question Data about technical details
- Consult with Troi about crew psychology
- Review tactical displays
- Contact other departments
```

## Application Constructs

Use clear section names to imply mutability; explicit “(Static)/(Dynamic)” tags are optional. Prefer semantic headings that make intent obvious: “Program Configuration” (static setup, rarely changes at runtime) and “Current Session State” (dynamic values that evolve during execution). This is sufficient for most simulations and keeps documents readable.

Add explicit markers only when precision is required for automation or collaboration: multiple configuration layers (global vs scenario), mixed files where both appear, or when parsers/CI need deterministic extraction and validation. If adopting markers, apply them consistently (“Program Configuration (Static)”, “Current Session State (Dynamic)”) and avoid visual noise elsewhere.

Do not mix static and dynamic keys in the same section. Defaults belong in configuration; active values belong in session state. If a configuration value is overridden at runtime, reflect the effective value in session state rather than mutating configuration. For rare cases that require per-key control, add minimal inline attributes (e.g., “mutability: static|dynamic” or “derived: true”) next to the specific key instead of tagging the whole section.

Rule of thumb: small or solo projects—names alone; larger, layered, or parser-dependent workflows—use explicit markers or a declared “mutability policy” at the top and keep headings clean.

### Configuration/settings

Use: Section heading + key:value pairs

```markdown
## Program Configuration
runtime: 60-90 minutes
complexity: Medium
safety_level: Standard
user_role: Visiting officer
```

### State management

Use: Section heading + state variables

```markdown
## Current Session State
user_location: Ten Forward
active_scenario: diplomatic_crisis
relationship_picard: professional_respect
plot_progress: 45_percent_complete
```

### Event handlers/triggers

Use: label + procedural list

```markdown
on_red_alert:
- Seal blast doors
- Activate emergency lighting
- Route power to shields
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

## Simulation Constructs

### If you want: Character memory

Use: Character section + memory attributes

```markdown
### Character - Guinan
Remembers About User:
- Prefers diplomatic solutions
- Shows curiosity about ship operations
- Demonstrated respect for crew privacy
```

Use: Constraint list with clear boundaries

### Boundary constraints

```markdown
### Safety Boundaries
- Characters cannot permanently die
- User cannot access classified information
- Scenarios must resolve within time limit
- Physical harm limited to dramatic tension
```

## Quick Syntax Rules

### Attention/Emphasis Control

- `**Bold**`: High attention, primary information (85% extraction accuracy)
- `*Italic*`: Contextual information, temporary state (60% extraction accuracy)  
- `Plain`: Standard information, stable attributes (70% extraction accuracy)

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

### Markdown Generation Policy (for LLMs)

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
  - Use the correct language tag (“```text”, “``````mermaid”) and do not HTML‑escape within fences.

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
