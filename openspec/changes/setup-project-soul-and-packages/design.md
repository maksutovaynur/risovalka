## Context

The repository currently contains concept documents, course/session materials, presentations, assets, and a minimal `engine/gamekit` placeholder. The `pyproject.toml` project is already named `risovalka`, but the importable Python package layout does not yet match that name.

The course targets children learning Python through 2D games. Student-facing materials and tool UI must be Russian, while OpenSpec metadata, user prompts, and core project comments may remain English.

## Goals / Non-Goals

**Goals:**
- Create a concise `SOUL.md` that records the project principles and language policy.
- Establish `risovalka` as the top-level import package.
- Place the engine under `risovalka.gamekit`.
- Reserve `risovalka.tools.raster`, `risovalka.tools.vector`, and `risovalka.samples` for ready-to-use tools and examples.
- Make `sessions` importable as a package for future teaching-session templates.
- Keep the implementation simple and dependency-free at this stage.

**Non-Goals:**
- Implement the full game engine API.
- Implement raster or vector editor features.
- Rewrite the existing course materials.
- Add packaging or publishing workflows beyond the local source layout.

## Decisions

1. Use `risovalka/` as the source package at the repository root.
   - Rationale: the project name is already `risovalka`, and a root package keeps imports direct for learners and examples.
   - Alternative considered: keep `engine/gamekit` and expose it through path configuration. This adds hidden packaging complexity and does not match the requested package names.

2. Move or recreate the current placeholder under `risovalka/gamekit`.
   - Rationale: the existing engine contains no substantial implementation, so a clean package location is easier than maintaining an adapter layer.
   - Alternative considered: keep `engine/gamekit` as canonical and create `risovalka.gamekit` as a bridge. This is only useful if there is meaningful legacy code to preserve.

3. Create empty package scaffolds for tools and samples now.
   - Rationale: explicit package boundaries let future changes add raster/vector tools and samples without inventing structure later.
   - Alternative considered: wait until each tool is implemented. That would leave imports and ownership ambiguous while the concept docs already name these areas.

4. Keep `sessions/` as a top-level package rather than nesting it inside `risovalka`.
   - Rationale: the user explicitly requested package `sessions`, and teaching-session templates are course content rather than engine runtime code.
   - Alternative considered: `risovalka.sessions`, which would group everything under one namespace but conflict with the requested topology.

## Risks / Trade-offs

- Existing materials might reference `engine.gamekit` or local file paths -> Search for references and update only references affected by the package move.
- Root-level packages can mix runtime code and course content -> Keep the package folders minimal and use `__init__.py` docstrings to state ownership.
- Language rules can be violated accidentally in future UI/materials -> Put the rule in `SOUL.md` and encode it in specs so future changes can be reviewed against it.
