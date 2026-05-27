## 1. Lesson Structure

- [x] 1.1 Create `lessons/lesson1/`, `lessons/lesson1/samples/`, and `lessons/lesson1/puzzles/` directories
- [x] 1.2 Add source placeholders or final sources for `lesson1_slides.marp.md`, `lesson1_guide.md`, and `achivements.md`
- [x] 1.3 Add generated-in-advance `lesson1_slides.pdf`, `lesson1_guide.pdf`, and `achivements.pdf` next to their source files

## 2. Slide Deck

- [x] 2.1 Draft a Russian `lesson1_slides.marp.md` deck with a beginning plan, middle motivation hook, first-game-scene plus manual-animation project requirements, and final references to exact sample and puzzle files
- [x] 2.2 Replace vague P0/P1-style exposition with concrete lesson 1 details: today's required first game scene and small manual animation, variable achievement-driven parts, and what code files students will touch
- [x] 2.3 Add concept visuals or diagrams for raster pixels, RGB/HEX color, coordinate grid, vectors, draw order, and the gamekit frame workflow
- [x] 2.4 Keep each slide focused on one concrete teaching point with short Russian labels instead of long paragraphs
- [x] 2.5 Use a balanced mix of maintainable hand-made diagrams and fixed generated PNG visuals
- [x] 2.6 Ensure every image, diagram, or screenshot directly explains a course, graphics, programming, or project concept
- [x] 2.7 Mention loops and `if` only as teaser concepts for questions or the next lesson, not as lesson 1 practice topics

## 3. Lesson Guide

- [x] 3.1 Write `lessons/lesson1/lesson1_guide.md` in Russian with Windows-primary setup steps for Python, VS Code, recommended plugins, opening the project, and running a sample, plus brief macOS/Linux notes
- [x] 3.2 Add a first-run workflow explaining how to run a lesson sample and interpret terminal output
- [x] 3.3 Add a code-editing workflow covering syntax highlighting, autocomplete, saving, rerunning, and small safe changes
- [x] 3.4 Add beginner-friendly explanations of common Python errors including `SyntaxError`, `NameError`, `IndentationError`, `TypeError`, file path mistakes, and filename letter-case mistakes
- [x] 3.5 Keep the guide practical and TODO-oriented without spoiling puzzle solutions

## 4. Samples

- [x] 4.1 Add about five numbered runnable sample files under `lessons/lesson1/samples/`
- [x] 4.2 Cover available `risovalka.gamekit` basics: window setup, canvas clearing, fill/stroke colors, shape drawing, text drawing, coordinates, variables, function calls, and `Point` or `Vector`
- [x] 4.3 Ensure every sample keeps its game window open until the student closes it
- [x] 4.4 Ensure samples are stable, predictable reference programs suitable for reuse during practice
- [x] 4.5 Keep sample comments concise, understandable, and in Russian

## 5. Puzzles

- [x] 5.1 Add about five numbered runnable puzzle files under `lessons/lesson1/puzzles/` with intentional beginner-level errors
- [x] 5.2 Include puzzle coverage for function calls, arithmetic, variables, coordinates, colors, and gamekit drawing calls
- [x] 5.3 Make puzzles intentionally broken, unstable, or surprising playgrounds where students diagnose and repair the problem
- [x] 5.4 Keep puzzle comments limited to the problem description and optional hint, without solution steps

## 6. Achievements

- [x] 6.1 Write `achivements.md` as a Russian checkbox list or grid
- [x] 6.2 Include achievements for environment setup, running a sample, changing drawing parameters, using coordinates, using colors, fixing at least one puzzle, completing the first game scene and small manual animation, and personalizing today's project

## 7. Verification

- [x] 7.1 Verify all student-facing text and code comments in lesson 1 are Russian
- [x] 7.2 Run or syntax-check all lesson sample files
- [x] 7.3 Confirm puzzle files fail or behave incorrectly for the intended beginner-fix reason
- [x] 7.4 Confirm PDFs exist and correspond to the current Markdown/Marp sources
- [x] 7.5 Run OpenSpec validation/status for `create-lesson1-materials`
