## The Bridge -- Simulation Map

### Startup Configuration

- **User Profile:** about_the_user.md
- **Cast File:** holodeck_cast.md
- **Setting File:** holodeck_setting.md
- **Script File:** holodeck_script.md / see [[holodeck_script.md]] → "Captain on the Bridge" scene
- **Starting Location:** bridge
- **Starting Scenario:** captain on the bridge / see [[holodeck_script.md]] "Captain on the Bridge"
- **Starting Mode:** normal
- **Initial Cast Override:** bridge crew
- **Roleplay Mode:** RP Lite   # Default startup mode; waits for user to direct simulation
- **User Persona:** John Kominetz III as Captain
- **Startup Hooks:**
  - trigger_log: "Daily change of watch initiated"
  - environmental_status: "systems nominal"

### Location Defaults / Bridge

The Bridge is defined in holodeck_setting.md

- Mode: Normal
- Crew: bridge crew / see holodeck_cast.md for member selection logic
- Lighting: Wrath-of-Khan ambiance with modern LCARS panels
- Status: All stations manned, systems nominal

### Purpose and Authority

This file serves as the **Simulation Map** for the Holodeck system — the single manifest automation reads to assemble and start a session.

- Points to all core simulation files:
  - [[holodeck_cast.md]] — roster, department membership/flavor, automation batches
  - [[holodeck_setting.md]] — location/world details, motifs
  - [[holodeck_script.md]] — narrative arcs, acts, and scenes
  - [[about_the_user.md]] — user biography and RP persona
- Declares the startup scenario, location, mode, cast subset, RP mode, and persona.
- **No rosters, bios, or protocols** are duplicated here — always refer to the source files above.
- All simulation/session/mode logic is governed by [[holodeck_protocols.md]].

### Core Files

| File                | Purpose                                                        |
|---------------------|----------------------------------------------------------------|
| [[holodeck_cast.md]]           | roster, department membership/flavor, automation batches       |
| [[holodeck_setting.md]]        | Locations, world-building, motifs, hooks                       |
| [[holodeck_script.md]]         | Acts, scenes, and standalone scenarios                         |
| [[about_the_user.md]]          | User biography/context for persona and RP mode                 |

### Location Defaults — The Bridge

The **Bridge** is defined as a primary location in the [[holodeck_setting.md]] file.  
When the simulation starts here, the following defaults may be applied unless overridden:

- **Default Mode:** Normal
- **Default Crew Set:** Bridge Crew (see [[holodeck_cast.md]] for members)
- **Lighting/Atmosphere:** Operational readiness, warm Wrath‑of‑Khan lighting with modern LCARS panels
- **Bridge Ready Status:** All stations manned; systems nominal

WARNING! **(These defaults can be overridden in the Startup Parameters above or in scenario/episode files.)**

### Overrides (Optional)

If specific to this run, declare overrides here — they only apply during the active simulation and do not modify any underlying files.

Example (YAML syntax):

    overrides:
      starting_location: engineering
      cast_override: engineering staff
      rp_mode: normal
