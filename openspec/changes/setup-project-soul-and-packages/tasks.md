## 1. Project Principles

- [x] 1.1 Create root `SOUL.md` with the educational simplicity principle, expressive engine goal, Russian student-facing language rule, English exceptions, and `concept/` alignment.
- [x] 1.2 Review `SOUL.md` against `concept/01_overview.md`, `concept/03_game_api_concept.md`, `concept/06_course_file_structure.md`, `concept/09_quality_principles.md`, and `concept/12_helper_tools.md`.

## 2. Package Structure

- [x] 2.1 Create the `risovalka` top-level package.
- [x] 2.2 Move or recreate the current gamekit placeholder under `risovalka/gamekit`.
- [x] 2.3 Create `risovalka/tools/raster` package scaffold for the raster drawing tool.
- [x] 2.4 Create `risovalka/tools/vector` package scaffold for the vector drawing tool.
- [x] 2.5 Create `risovalka/samples` package scaffold for engine usage samples.
- [x] 2.6 Add `sessions/__init__.py` so teaching sessions are importable as a top-level package.

## 3. Packaging and References

- [x] 3.1 Update `pyproject.toml` package settings if needed so the new packages are discoverable in the project environment.
- [x] 3.2 Search for existing references to `engine.gamekit`, `engine/gamekit`, or old package assumptions and update only the references affected by this structural change.

## 4. Verification

- [x] 4.1 Verify `import risovalka`, `import risovalka.gamekit`, `import risovalka.tools.raster`, `import risovalka.tools.vector`, `import risovalka.samples`, and `import sessions` succeed.
- [x] 4.2 Verify the structural change does not add new third-party dependencies.
- [x] 4.3 Run OpenSpec validation for `setup-project-soul-and-packages`.
