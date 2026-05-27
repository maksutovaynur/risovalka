## Why

The project needs a stable foundation before the engine, tools, samples, and teaching sessions grow in different directions. A short project soul document and explicit Python package layout will keep the code simple enough for education while preserving room for advanced game-building features.

## What Changes

- Add `SOUL.md` at the repository root with the project's core principles:
  - educational simplicity with room for expressive projects;
  - Russian-only student-facing UI components, guides, examples, and session materials;
  - English reserved for user prompts, OpenSpec metadata, and core project comments;
  - alignment with the existing `concept/` documents.
- Establish the import/package structure:
  - `risovalka` as the top-level package;
  - `risovalka.gamekit` as the educational 2D game engine;
  - `risovalka.tools.raster` for a raster drawing tool;
  - `risovalka.tools.vector` for a vector drawing tool with SVG export and gamekit drawing-code export;
  - `risovalka.samples` for engine usage samples;
  - `sessions` as a package for teaching session templates.
- Preserve the current beginner-first engine direction while preparing clear places for future tools and examples.
- No breaking runtime behavior is intended; current engine code should be moved or bridged carefully if imports change.

## Capabilities

### New Capabilities
- `project-soul`: Defines the repository-level principles, language rules, and relationship to the concept documents.
- `python-package-layout`: Defines the Python package topology for the engine, tools, samples, and teaching sessions.

### Modified Capabilities

None.

## Impact

- Affected files and directories: root `SOUL.md`, `pyproject.toml`, current `engine/gamekit` package, new `risovalka/` package tree, and `sessions/`.
- Affected APIs: package imports should converge on `risovalka.gamekit` while avoiding unnecessary churn for existing materials.
- Dependencies: no new third-party dependencies are required for this structural change.
- Teaching materials: future student-facing strings and guides must remain in Russian.
