# Holoplex

## Project Overview

- Builds a collection of files for role-based simulation and team management based on Star Trek's Holodeck concept.
- Source files are managed in a structured directory system, allowing for easy updates and extensibility.
- Files are built into a collection of markdown files, scripts, and resources that can be used for simulations, training, and team management.
- Build files are used by loading them into a Perplexity Space.

- During batching/build, the batcher script:
  - Automatically copies `holodecks/common/` into the build directory (e.g., `build/the_bridge/`).
  - Copies holodeck-specific resources (e.g., `holodecks/the_bridge/`) into the same build directory.
  - This is **recursive and selective**: if a source resource folder doesn't exist, it's skipped with a warning but does not stop the build.
- All these files are available at runtime or for packaging/export with the generated simulation group.

### Extensibility

- Add new holodeck directories under `holodecks/` for new simulation environments.
- Each holodeck directory should contain its manifest file (e.g., `holodeck_name.md`) and any specific resources.
- Add or update files in `holodecks/common/` to have them included in all builds.
- Place readmes, style guides, or scenario-specific assets in the holodeck directories—never in the characters directories.
- Automated validation, manifest generation, and batch file building.
- Flexible resource inclusion for each build or simulation context.

Holoplex is optimized for clarity, reproducibility, automation, and extensibility—suitable for everything from role-based simulation to real-world team scenario planning.


## Directory Structure

```plaintext
holoplex/
│
├── bin/                      # CLI tools/scripts (shell and Python)
│   ├── holodeck_compiler.py  # Main compiler script
│   └── holoplex              # Orchestrator CLI script
│
├── doc/                      # Documentation and guides
│   ├── ai_terminology.md
│   ├── MANIFEST_README.md
│   ├── markdown_scripting_guide.md
│   ├── perplexity_world_mode.md
│   └── holodeck_inspiration/ # interpretations of the holodeck portrayal
│
├── src/                      # Main source files
│   ├── characters/           # Individual character markdown files
│   │   ├── abrahamlincoln.md
│   │   ├── adalovelace.md
│   │   └── ...
│   ├── personas/             # Persona definitions
│   │   └── persona_computer.md
│   ├── private/              # Private or restricted files (if any)
│   ├── programs/             # Program scripts or scenario logic
│   ├── protocols/            # Protocol markdown files
│   │   ├── protocol_holodeck.md
│   │   └── protocol_roleplay.md
│   └── templates/            # Markdown templates
│       └── persona_user.md
│
├── tmp/                      # Temporary or backup files
│   ├── concepts_backup.md
│   └── my_ready_room.md
│
└── README.md                 # (this file)
```

## Holodecks Directory Explained

### Purpose

- The `holodecks/` directory contains **holodeck-specific manifests and resources** for different simulation environments.
- Each holodeck (like `the_bridge`, `the_forum`, `the_sandbox`) has its own subdirectory containing its manifest file and any specific resources.
- This ensures every generated build contains all necessary files for full scenario operation—**without cluttering the main source folders.**

### Structure

- `holodecks/common/`: Shared by all builds (e.g., protocol files, universal templates, shared resources).
- `holodecks/templates/`: Template files that can be manually copied into new holodecks.
- `holodecks/the_bridge/`: Contains The Bridge manifest and Bridge-specific resources.
- `holodecks/the_forum/`: Contains The Forum manifest and Forum-specific resources.
- `holodecks/the_sandbox/`: Contains The Sandbox (holodeck) resources.

### How Resources Are Used in Build

- During batching/build, the batcher script:
  - Automatically copies `holodecks/common/` into each build group’s holodeck dir, e.g., `build/the_bridge/`.
  - Copies group-specific resources (e.g., `holodecks/the_bridge/`) into `build/the_bridge/`.
  - This is **recursive and selective**: if a source resource folder doesn’t exist, it’s skipped with a warning but does not stop the build.
- All these files are available at runtime or for packaging/export with the generated simulation group.

## Quick Start

1. **Add/Update Charactere:**  
   Add markdown character files to `characters/`. Use normalized naming and keep them in sync with assignment manifests.

2. **Define Assignments:**  
   Group/department/panel assignments are maintained in markdown manifests (`holodecks/the_bridge/the_bridge.md`, etc.)—never in the character files themselves.

3. **Provide Resources (if desired):**  
   Place any needed supplementary files in `holodecks/the_bridge/` or `holodecks/common/` before building.

4. **Build:**  

   ```bash
   bin/holoplex build the_bridge
   ```

   - Cleans prior output, validates, extracts manifest, batches character files, copies holodecks resources.

5. **Check:**  

   ```bash
   bin/holoplex check the_bridge
   ```

   - Validates manifest and character file presence but does not batch or copy anything.

6. **Clean:**  

   ```bash
   bin/holoplex clean the_bridge
   ```

   - Removes all build artifacts (including resources and manifest) for the group.

## Key Features

- **Batch output and resources** are always safely isolated in `build//`, ready for deployment, sharing, or programmatic loading.
- **Resource system** is optional, robust, and flexible—lets you supply all the context, docs, and auxiliary files you need without code changes.
- **All scripting/logic is dynamic** (no hardcoded group names or roles!), so future panels or holodecks are trivial to add.

## Best Practices

- Store **all character and resource files under version control** (Git recommended).
- Never manually edit or delete anything in `build/`—always use the holodeck commands.
- Use resource folders for anything you might want per-group or in every build—this keeps builds reproducible and modular.

## Support

- See `holodecks/common/holodeck_protocols.md` for simulation/character standards.
- For trouble or enhancements, review log output from the Python and shell scripts—clear explanations and warnings are provided.

**Holoplex:** Advanced simulation and team management—structured, reproducible, and ready for any mission. Now with integrated resource support!
