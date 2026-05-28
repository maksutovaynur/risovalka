# SOUL

Risovalka is an educational Python project for learning game programming through small, visible, joyful results.

## Principles

1. Simplicity first.

   The code must stay readable for educational use. A beginner should be able to open a file, follow the idea, and change something without fighting hidden architecture.

2. Simple does not mean small.

   The engine should leave room for many kinds of 2D games, creative experiments, secret effects, and advanced discoveries. Extra power is welcome when it does not make the first steps harder.

3. Practice before theory.

   Programming concepts appear when they solve an immediate game-making problem: coordinates place a hero, variables remember state, conditions react to input, loops animate frames, and lists manage many objects.

4. Samples teach concepts without overload.

   Samples should stay light on explanation and heavy on visible, focused learning. Each sample should make the newly learned concept clear without surrounding it with too much information at once.

5. Puzzles mostly teach algorithms and architecture.

   Only a few puzzles should be about syntax. Most puzzles should train correct algorithms, project structure, and architectural choices that belong to the current topic or project.

6. Lesson materials must stay consistent as a set.

   When changing any slides, guides, achievements, samples, or puzzles, always check the related files and make sure names, goals, references, concepts, and expected student work remain consistent across all of them.

7. Student-facing Russian is mandatory.

   All UI components, student guides, student examples, session materials, workbook text, in-app hints, and teaching-session templates MUST be written in Russian.

8. English has narrow uses.

   English is allowed for user prompts, OpenSpec metadata, package/module names, public Python identifiers when appropriate, and core project comments for contributors.

9. The engine is honest code, not a visual constructor.

   `risovalka.gamekit` should feel simpler than raw PyGame, but it should still teach a real programming model: game state, drawing, input, movement, collisions, and time.

10. The concept folder is the source of intent.

   Before changing the engine, tools, samples, or course structure, read the relevant files in `concept/`. They explain the course rhythm, game API direction, helper tools, quality principles, and production priorities.

## Package Map

- `risovalka`: root Python package.
- `risovalka.gamekit`: educational 2D game engine.
- `risovalka.tools.raster`: raster drawing tool for images, textures, and sprites.
- `risovalka.tools.vector`: vector drawing tool with SVG export and `game.draw_*` code export.
- `risovalka.samples`: examples of using the engine.
- `sessions`: teaching session templates and course session structure.
