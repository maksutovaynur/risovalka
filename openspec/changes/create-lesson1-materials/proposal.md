## Why

The course needs a concrete first lesson package that turns the existing course concept and `risovalka.gamekit` MVP into teachable student-facing materials. Lesson 1 is the entry point for motivation, environment setup, graphics basics, and the first practical programming experience, so its structure must be explicit before implementation begins.

## What Changes

- Add a complete `lessons/lesson1/` material package with Russian-only student-facing content.
- Define the required lesson file structure: intro Marp/PDF slides, first lesson Marp/PDF slides, guide, achievements, reusable samples, and repair-focused puzzles.
- Create a 20-minute discussion-oriented slide deck that gives the course overview, introduces programming motivation, defines today's project with required and variable parts, and explains raster/color/coordinates/vectors through practical graphics problems.
- Create a detailed lesson guide covering environment setup, running samples, VS Code basics, and beginner-friendly Python error interpretation.
- Add seven stable lecture/practice samples with concise Russian comments and six intentionally problematic playground-style puzzles whose comments describe only the problem and optional hint.
- Align lesson order with the currently available `risovalka.gamekit` capabilities instead of depending on future tools.

## Capabilities

### New Capabilities
- `lesson1-materials`: Covers the file structure, language policy, slide content, guide content, samples, puzzles, achievements, and generated PDFs for the first lesson.

### Modified Capabilities

## Impact

- Adds student-facing lesson materials under a new `lessons/lesson1/` directory.
- Adds Python sample and puzzle files that import and demonstrate `risovalka.gamekit`.
- May add or reuse maintainable hand-made diagrams and fixed generated PNG visuals when they directly explain course, graphics, color, raster, coordinates, vectors, or the announced lesson project.
- Adds PDF outputs generated in advance so students can open and read the materials without running build tooling.
