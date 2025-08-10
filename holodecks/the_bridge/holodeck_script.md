## The Bridge -- Script

This file defines the top-level narrative beats, acts, scenes, and standalone scenarios for the simulation.  
It is referenced by the_bridge.md in startup configuration, and draws on cast, setting, and manifest files for context and population.  
Personnel assignments are dynamically selected from [[holodeck_cast.md]].

### Scenario: Captain on the Bridge / Bridge

**Startup Mode:** RP Lite  
**Location:** Bridge / see [[holodeck_setting.md]]  

**Context:**  

- The bridge is active during morning turnover.  
- Specialists for this scene are drawn dynamically from [[holodeck_cast.md]]:

  - **Specialists Pool:** [[holodeck_cast.md#personas.bridge_cast_selection.specialists_pool]]
  - **Officer of the Watch Pool:** [[holodeck_cast.md#personas.bridge_cast_selection.officer_of_watch_pool]] (must be a department head not already selected as a specialist)

- Officer of the Watch holds the conn, awaiting the Captain.
- Captain (John Kominetz III as Captain) enters mid-scene to assume command.

**Flavor:**  

- Logs and banter are exchanged—Philly warmth + Starfleet professionalism.  
- Crew chatter includes sounds of LCARS panels, warm Wrath‑of‑Khan style lighting.  
- Simulation opens in “flavor mode” and **waits for the Captain/user to act**.

### Scene Hooks (Optional, User-Directed)

- A minor, non-critical sensor anomaly appears on one console (only if user decides to follow it).
- Off-duty chatter about Space Bar plans (flavor only unless prompted).
- Status report handover from OotW when Captain requests it.

### Template for Future Scenes/Acts

    ### Scene: [Title]
    Location: [location]
    Description: [setup, context, flavor cues]
    Cast: (reference [[holodeck_cast.md]] / appropriate group or selection pool)
    Mode: [RP Lite, Normal RP, Heavy RP]
    Hooks: [events, anomalies, dialogue beats]
    Action: [what triggers next act/scene]
