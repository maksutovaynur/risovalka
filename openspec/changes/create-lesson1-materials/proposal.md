## Why

The course needs a concrete first lesson package that turns the existing course concept and `risovalka.gamekit` MVP into teachable student-facing materials. Lesson 1 is the entry point for motivation, environment setup, graphics basics, and the first practical programming experience, so its structure must be explicit before implementation begins.

## What Changes

- Add a complete `lesson1/` material package with Russian-only student-facing content.
- Define the required lesson file structure: Marp slides, PDFs, guide, achievements, reusable samples, and repair-focused puzzles.
- Create a 20-minute discussion-oriented slide deck that gives the course overview, introduces programming motivation, frames today's project, and explains raster/color/coordinates/vectors through practical graphics problems.
- Create a detailed lesson guide covering environment setup, running samples, VS Code basics, and beginner-friendly Python error interpretation.
- Add lecture/practice samples with concise Russian comments and puzzles whose comments describe only the problem and optional hint.
- Align lesson order with the currently available `risovalka.gamekit` capabilities instead of depending on future tools.

## Capabilities

### New Capabilities
- `lesson1-materials`: Covers the file structure, language policy, slide content, guide content, samples, puzzles, achievements, and generated PDFs for the first lesson.

### Modified Capabilities

## Impact

- Adds student-facing lesson materials under a new `lesson1/` directory.
- Adds Python sample and puzzle files that import and demonstrate `risovalka.gamekit`.
- May add or reuse presentation images/assets when they directly explain course, graphics, color, raster, coordinates, vectors, or the announced lesson project.
- May add build instructions or scripts only if needed to generate the required PDF outputs from Markdown/Marp sources.
