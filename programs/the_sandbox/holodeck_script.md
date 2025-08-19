## The Sandbox — Script

This file defines the top-level narrative beats, acts, scenes, and standalone scenarios for the Sandbox simulation.  
It is referenced by the Sandbox simulation map in startup configuration, and draws on `holodeck_cast.md` and `holodeck_setting.md` for cast and location context.  
Personnel assignments are dynamically selected from Sandbox’s groups, not Starfleet departments.

---

### Scenario: Welcome to the Sandbox

**Startup Mode:** Sandbox Mode  
**Location:** Sandbox Lab (see `holodeck_setting.md`)  

**Context:**

- The lab is live but idle, configured for free-form development and experimentation.
- Team Leaders and group members are available for brainstorming, testing modules, and running mini-simulations.
- Scenario begins with **no scripted objective**; user sets the tone by creating or loading activities.

**Casting Logic:**

- **Holodeck Team**: primary “on-duty” group at startup
- **Creative Team**: available for narrative, design, or mixed-use tasks

**Flavor:**

- The center table is strewn with digital sketchpads and holographic mockups.
- Side consoles show paused test environments — frozen mid-explosion, half-constructed landscapes, and zero-gravity ball games — each waiting for a command.
- Through transparent walls, the Observation Deck offers a backdrop of streaking starlines.
- The system is waiting: *What will you build, test, or break today?*

---

### Scene Hooks (Optional, User-Directed)

- **Spawn Module:** Instantiates a new simulation template (user may name and theme it).
- **Random Challenge:** System pulls a pre-made creative challenge (e.g., design a device, run a dangerous salvage op, invent a game).
- **Debug Mode:** Anomalies appear in props or subroutines — fix them or exploit them.
- **Guest Designer Arrival:** Bring in a persona from Creative Team to collaborate.

---

### Template for Future Scenes/Acts

    ### Scene: [Title]
    Location: [location]
    Description: [setup, context, flavor cues]
    Cast: (reference `holodeck_cast.md` / appropriate group or selection pool)
    Mode: [Sandbox, Talk, RP Lite, Heavy RP]
    Hooks: [events, challenges, collaboration beats]
    Action: [conditions that move to next scene/act]
