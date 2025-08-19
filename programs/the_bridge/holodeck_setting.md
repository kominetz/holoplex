## The Bridge --Setting

U.S.S. Philadelphia, NCC-1965

### General Description

The **U.S.S. Philadelphia** is a Miranda-class light cruiser (NCC-1965), serving in the late 2300s. Originally a classic Miranda, she's been rebuilt and modernized multiple times, blending a "Wrath of Khan" Starfleet aesthetic with updated 24th-century technologies and amenities.

The ship is authentic, rugged, and reliable—with just enough Borg-inspired tech upgrades for efficiency, but still reflecting her vintage lines. Crew uniforms are DS9-era style or STO’s Sierra Black variant.

Cultural flavor is strong:  

- Philly-style replicator food
- "Gritty" mascot references
- In-jokes about the "Philadelphia Experiment"
The ship is proud of her namesake, and banter often reflects local humor and traditions.

### Motifs & Atmosphere

- Lighting: Warm, analog feel mixed with modern control surfaces.
- Background sounds: Gentle bridge hum, LCARS chimes.
- Crew interactions: Mix of formal Starfleet with Philly warmth and humor.

### Simulation Hooks

- Default era: Late 2300s, active Starfleet duty.
- Starting location is the Bridge (see the_bridge.md / startup parameters).
- All starting flavor should be context only for RP Lite—simulation awaits further user commands for events or scene development.

### Key Locations

#### Runabout Delaware

A modern, versatile support craft named for the Delaware River. An updated version of the Danube-class runabout, featuring advanced systems and a streamlined design.

#### Shuttlecraft Schuylkill

An old Type F shuttlecraft (TOS era), reliable and nostalgic, named for the Schuylkill River.

#### Ready Room — U.S.S. Philadelphia

**Location:** Ready Room  
**Access:** Adjacent to the Bridge; Captain’s office and private conference space

**Physical Description:**  
A compact, utilitarian chamber inspired by the NX‑01 — functional lines, brushed metal walls, and a focus on efficiency. Kirk’s refit Enterprise influences the warm lighting, desk orientation, and subtle personal touches:  

- Work desk facing the single viewport with a sliver of the starfield beyond  
- Shelving with urban planning books, mission logs, and Philadelphia memorabilia  
- Discreet etched or holo‑projected map of Philadelphia near the door  
- Rainbow flag pin beside a framed Starfleet commendation  
- 3D model of the city skyline and a plaque reading “City of Brotherly Love”  
- Holographic display and a worn leather‑bound notebook for mission ideas and sketches  
- Desk console glowing gently, ready for the Captain’s first command

**Atmosphere & Motifs:**  

- Lighting shifts with ship’s chronometer — bright and warm during day cycle, dim and meditative at night  
- Blend of Starfleet practicality and grounded personal identity  
- Signs of resilience: reinforced panels, preserved hull fragment from an early refit inscribed with the ship’s motto

**Cultural & Narrative Hooks:**  

- Used for strategic planning, reflection, and informal conversations  
- Officers may stop by for quick briefings or private discussions  
- Personal history and Philly culture are present but understated, giving the space warmth without compromising formality

**Startup Context:**  
When the holodeck launches in **Talk** or **RP Lite** mode with no active scenario:
  Ready Room -- U.S.S. Philadelphia, {{startdate}} {{slang military time}}
  The room is softly lit, with the hum of the ship's systems providing a constant background noise. Through the viewport, stars streak by as the ship travels at warp speed. The desk console flickers to life, displaying the day's agenda and pending tasks and awaits your command.

#### Bridge

Primary command center.  
Classic Miranda layout with updated LCARS panels, day-bright WoK-style lighting, and a dedication plaque honoring every refit. Atmosphere is purposeful, efficient, and slightly irreverent.

#### Briefing Room

Located adjacent to the Bridge—used for mission planning, briefings, and after-action reviews. Features an interactive mission table and tactical display wall.

#### Other Locations (placeholders; details to come)

- Sickbay
- Engineering
- Science Lab
- Galley
- Space Bar (social lounge)
- Holodeck

### YAML Location Configuration Data

```yaml
locations:
  bridge:
    on_enter: execute bridge_cast_selection
    starting_cast: locations.bridge_cast_selection
    starting_mode: Talk
    starting_time: local

  bridge_cast_selection:
    specialists_pool:
      engineering: Engineering Department.staff
      operations: Operations Department.staff
      tactical: Tactical Department.staff
      science: Science Department.staff
      security: Security Department.staff
    officer_of_watch_pool: senior_staff
    selection_instruction: "At startup, one specialist is chosen at random from each pool. Officer of the Watch is a department head not already selected. The operations officer handles communication; there is no separate comms officer."
```
