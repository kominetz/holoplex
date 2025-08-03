# Holoplex

## Project Overview

**Holoplex** is a modular persona and simulation management system for collaborative environments, scenario simulation, and complex role-based automation. Inspired by holodeck and bridge/crew structures, Holoplex enables:

- Definition of detailed persona files and group assignments.
- Automated validation, manifest generation, and batch file building.
- Flexible resource inclusion for each build or simulation context.

Holoplex is optimized for clarity, reproducibility, automation, and extensibility—suitable for everything from role-based simulation to real-world team scenario planning.

## Directory Structure

```
holoplex/
│
├── bin/                      # All CLI tools/scripts (shell and Python)
│   ├── holodeck              # Orchestrator CLI script
│   ├── persona_checker.py
│   ├── the_bridge_extractor.py
│   ├── the_bridge_batcher.py
│   ├── the_forum_extractor.py
│   ├── the_forum_batcher.py
│   └── ... (other scripts)
│
├── persona/                  # Individual persona files (markdown)
│   ├── worf.md
│   ├── thedoctor.md
│   └── ...
│
├── resources/                # Shared and group-specific static resources
│   ├── common/               # Templates, images, or files shared by all builds
│   └── the_bridge/           # Bridge-specific resources (docs, config, data, etc.)
│   └── the_forum/            # Forum-specific resources (docs, images, etc.)
│
├── build/                    # All build artifacts (auto-generated)
│   ├── the_bridge/           # All runtime/init files for The Bridge
│   │   ├── the_bridge_full_crew.md
│   │   ├── the_bridge_heads.md
│   │   ├── resources/
│   │   │   ├── common/
│   │   │   └── the_bridge/
│   │   └── ... (batches, configs, protocol)
│   ├── the_forum/            # Artifacts for The Forum
│   │   ├── resources/
│   │   │   ├── common/
│   │   │   └── the_forum/
│   │   └── ...
│   ├── the_bridge_manifest.yaml     # Manifest for The Bridge (not used at runtime)
│   └── the_forum_manifest.yaml      # Manifest for The Forum (not used at runtime)
│
├── the_bridge.md             # Markdown manifest for The Bridge
├── the_forum.md              # Manifest for The Forum
├── protocol_holodeck.md      # Simulation/persona protocol reference
└── README.md                 # (this file)
```

## Resources Directory Explained

### Purpose

- The `resources/` directory enables **inclusion of extra static files and data** (templates, media, config, docs) in simulation builds for specific holodecks or globally.
- This ensures every generated build (such as `build/the_bridge/`) contains all necessary auxiliary files for full scenario operation, deployment, or richer experience—**without cluttering primary source folders.**

### Structure

- `resources/common/`: Shared by all builds (e.g., universal templates, shared images, global readmes).
- `resources/the_bridge/`: Specific to The Bridge (e.g., special docs, scenario sheets, panels).
- `resources/the_forum/`: Specific to The Forum, and so on.

### How Resources Are Used in Build

- During batching/build, the batcher script:
  - Automatically copies `resources/common/` into each build group’s `resources/common/`.
  - Copies group-specific resources (e.g., `resources/the_bridge/`) into `build/the_bridge/resources/the_bridge/`.
  - This is **recursive and selective**: if a source resource folder doesn’t exist, it’s skipped with a warning but does not stop the build.
- All these files are available at runtime or for packaging/export with the generated simulation group.

### Extensibility

- Add as many resource folders as you need for new holodecks/panels.
- Add or update files in `resources/common/` to instantly have them included in all future builds.
- Place readmes, style guides, or scenario-specific assets here—never in the persona or manifest directories.

## Quick Start

1. **Add/Update Personae:**  
   Add markdown persona files to `persona/`. Use normalized naming and keep them in sync with assignment manifests.

2. **Define Assignments:**  
   Group/department/panel assignments are maintained in markdown manifests (`the_bridge.md`, etc.)—never in the persona files themselves.

3. **Provide Resources (if desired):**  
   Place any needed supplementary files in `resources/common/` or `resources//` before building.

4. **Build:**  
   ```bash
   bin/holodeck build the_bridge.md
   ```
   - Cleans prior output, validates, extracts manifest, batches persona files, copies config/protocol/resources.

5. **Check:**  
   ```bash
   bin/holodeck check the_bridge.md
   ```
   - Validates manifest and persona file presence but does not batch or copy anything.

6. **Clean:**  
   ```bash
   bin/holodeck clean the_bridge.md
   ```
   - Removes all build artifacts (including resources and manifest) for the group.

## Key Features

- **Batch output and resources** are always safely isolated in `build//`, ready for deployment, sharing, or programmatic loading.
- **Resource system** is optional, robust, and flexible—lets you supply all the context, docs, and auxiliary files you need without code changes.
- **All scripting/logic is dynamic** (no hardcoded group names or roles!), so future panels or holodecks are trivial to add.

## Best Practices

- Store **all persona and resource files under version control** (Git recommended).
- Never manually edit or delete anything in `build/`—always use the holodeck commands.
- Use resource folders for anything you might want per-group or in every build—this keeps builds reproducible and modular.

## Support

- See `protocol_holodeck.md` for simulation/persona standards.
- For trouble or enhancements, review log output from the Python and shell scripts—clear explanations and warnings are provided.

**Holoplex:** Advanced simulation and team management—structured, reproducible, and ready for any mission. Now with integrated resource support!
