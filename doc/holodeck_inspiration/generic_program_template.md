# Program – Neutral Simulation Suite

id: neutral_sim_suite
version: 1.0
theme: Neutral Exploration and Interaction
tone: Balanced, context-driven, adaptable
safety_level: Standard
runtime_target: 60–120 minutes
user_role: Participant (Exploration/Decision-Maker)

## Program Configuration

purpose: A generic holodeck framework demonstrating exploration, interaction, and resolution patterns across multiple locations and scenarios.
narrative_style: Branchable, context-aware, character-driven
memory_persistence: character_relationships, discovered_facts, unresolved_threads
branching_complexity: moderate
conflict_intensity: low-to-moderate
success_criteria: Resolution of primary scenario objectives or meaningful partial outcomes

## Global Parameters

- pacing_default: medium
- difficulty_default: moderate
- hint_frequency: low
- debrief_enabled: true
- logging_scope: key_decisions, outcomes, relationship_shifts

## Character Registry (References by ID)

cast_required:

- guide_npc
- analyst_npc
- sentinel_npc

cast_optional:

- attendant_npc
- courier_npc
- caretaker_npc

cast_overrides:

- id: guide_npc
  current_focus: orientation_support
- id: analyst_npc
  current_focus: pattern_detection
- id: sentinel_npc
  current_focus: safety_and_compliance

## Locations

### Location – Atrium Hub

id: atrium_hub
primary_function: Orientation, gathering, transitions
atmosphere: Open, calm, bright ambient
access: Open
key_elements:

- info_kiosk
- seating_zones
- directional_signage
interactions:
- request_overview
- receive_suggestions
- coordinate_next_steps
hooks:
- “A new notice has been posted to the central display.”
- “An attendant requests a brief confirmation from participants.”

### Location – Workshop Gallery

id: workshop_gallery
primary_function: Hands-on tasks, prototypes, collaborative problem-solving
atmosphere: Constructive, focused, tool-rich
access: Open with supervision
key_elements:

- prototype_table
- diagnostics_panel
- parts_storage
interactions:
- inspect_prototype
- run_diagnostics
- assemble_components
hooks:
- “A device shows irregular behavior, inviting investigation.”
- “A collaborator suggests a safer assembly sequence.”

### Location – Observation Deck

id: observation_deck
primary_function: Analysis, reflection, external monitoring
atmosphere: Quiet, contemplative, panoramic display
access: Controlled
key_elements:

- view_consoles
- event_timeline
- archive_access
interactions:
- review_event_feed
- query_archives
- annotate_findings
hooks:
- “A faint anomaly appears on the far display.”
- “An archived entry aligns with newly observed data.”

## Scenarios

### Scenario – Orientation and Calibration

id: scenario_orientation
summary: Introduces the environment, calibrates participant preferences, and establishes initial objectives.
estimated_duration: 15–30 minutes
phases:

- Setup:
  - Present brief overview in Atrium Hub
  - Offer guided or self-directed onboarding
  - Establish initial communication norms
- Development:
  - Calibrate interaction style (concise vs. detailed, fast vs. measured)
  - Identify preliminary interests: exploration, analysis, assembly
  - Provide optional micro-task to validate tools/processes
- Resolution:
  - Confirm participant preferences and save profile
  - Suggest next steps by interest (Workshop Gallery vs. Observation Deck)
  - Log initial relationships (guide_npc, analyst_npc)

outcomes:

- preferences_profile_created: true
- recommended_path: workshop_focus or observation_focus
- relationship_shifts:
  - guide_npc: acquainted
  - analyst_npc: acquainted

### Scenario – Systems Integrity Check

id: scenario_integrity_check
summary: A suspected discrepancy triggers investigative tasks across locations, requiring both hands-on and analytical approaches.
estimated_duration: 30–60 minutes
phases:

- Setup:
  - Notify participants of minor anomaly detected
  - Provide broad context without prescriptive solution
  - Assign flexible objectives (isolate, confirm, resolve)
- Development:
  - At Workshop Gallery: inspect_prototype, run_diagnostics, apply_fix
  - At Observation Deck: review_event_feed, correlate_signals, validate_hypotheses
  - At Atrium Hub: coordinate, request_overview, summarize_findings
- Resolution:
  - Present integrated analysis (root cause + mitigation path)
  - Offer resolution choices (preventive vs. corrective measures)
  - Capture lessons learned and update knowledge base

outcomes:

- anomaly_status: resolved or mitigated or deferred_with_notes
- decision_record:
  - strategy: preventive or corrective or deferred
- relationship_shifts:
  - analyst_npc: trusts_problem_solving
  - sentinel_npc: confirms_compliance

### Scenario – Choice Under Constraint

id: scenario_choice_constraint
summary: A time-limited condition requires prioritization—balancing quality, speed, and safety across available paths.
estimated_duration: 30–45 minutes
constraints:

- time_limit: moderate
- resource_limit: constrained_components
- quality_target: acceptable_threshold or optimal_target
phases:
- Setup:
  - Trigger: resource bottleneck or time-sensitive opportunity
  - Present trade-offs clearly but neutrally
- Development:
  - Branch A (Quality Focus): additional verification at Observation Deck
  - Branch B (Speed Focus): accelerated assembly at Workshop Gallery
  - Branch C (Safety Focus): sentinel_npc oversight, stricter thresholds
- Resolution:
  - Outcome varies by chosen priority (quality/speed/safety)
  - Debrief compares alternative outcomes, suggests follow-ups
  - Log priority profile for future scenarios

outcomes:

- chosen_priority: quality or speed or safety
- result_quality: met_threshold or exceeded or under_threshold
- follow_up:
  - recommend: reinforce_quality or streamline_process or formalize_safeguards

## Interaction Protocols

initiative_rules:

- location_lead: present_npc_may_prompt if participant_idle
- participant_lead: participant_actions_take_priority
address_style:
- neutral, concise by default
- expand_detail_on_request
- adopt_formality: adaptive_to_participant
safety_and_constraints:
- safety_level: standard_enforced
- escalation: require_confirmation for risky_actions

## State and Memory

### Session State (mutable)

session_variables:

- preferences_profile: { pacing, detail_level, interaction_style }
- relationship_map: { guide_npc, analyst_npc, sentinel_npc }
- discovered_facts: []
- active_objectives: []
- unresolved_threads: []

### Resolution Order (highest wins)

1. session_state (current run)
2. scenario_overrides (local to scenario)
3. location_defaults (when in location scope)
4. global_program_defaults (this file’s configuration)

## Ambient and Paging

mentions:

- attendant_npc (logistics updates, non-intrusive)
- courier_npc (delivery notices, scheduling pings)
- caretaker_npc (maintenance status, availability)

## Debrief and Logging

debrief:

- summarize_objectives
- compare_paths_taken_vs_available
- highlight_tradeoffs_and_outcomes
- propose_next_scenarios
logging:
- key_decisions
- outcomes
- relationship_shifts
- discovered_facts

## Appendix – Prompts and Actions (Examples)

participant_actions_examples:

- “Request overview of current anomalies.”
- “Run diagnostics on the prototype.”
- “Review historical events related to this signal.”
- “Summarize trade-offs for the time-limited task.”
- “Recommend next steps based on our preferences profile.”

npc_prompts_examples:

- guide_npc: “Would you like orientation or a direct task?”
- analyst_npc: “A correlation stands out. Shall I expand the analysis?”
- sentinel_npc: “Confirm safety parameters before proceeding?”

## File Organization (Suggested)

- program_config.md (this file)
- locations/
  - atrium_hub.md
  - workshop_gallery.md
  - observation_deck.md
- scenarios/
  - orientation_and_calibration.md
  - systems_integrity_check.md
  - choice_under_constraint.md
- characters/
  - guide_npc.md
  - analyst_npc.md
  - sentinel_npc.md

## Notes for Authors

- Keep headings unique for singletons (locations, scenarios).
- Use key:value for attributes; use bold label + list for procedures.
- Store long persona details in character files; apply scenario overrides locally.
- Use mentions for off-screen characters without loading full personas.
- Keep token budgets manageable by loading only relevant locations, scenarios, and present cast.
