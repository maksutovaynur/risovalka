## Context

The repository already contains course concept documents, starter presentations, a Russian student-facing language policy, and an MVP `risovalka.gamekit` API. Lesson 1 must convert that intent into a concrete lesson package students can open, read, run, and practice with. Existing P0/P1 Marp decks are useful as topic inventory, but their current style is too text-heavy, vague, and visually generic for the lesson 1 target.

The target lesson is introductory: students need motivation for programming, a course overview, first contact with computer graphics, basic Python expressions, and a small announced project. The materials should avoid relying on future raster/vector editor tools and instead build around the available `risovalka.gamekit` operations: opening a window, setting colors, drawing shapes/text/images, using coordinates, using `Point`/`Vector`, variables, functions, simple arithmetic, optional loops, and optional `if`.

## Goals / Non-Goals

**Goals:**

- Create a complete `lesson1/` source tree with slides, guide, achievements, samples, and puzzles.
- Keep all student-facing content in Russian.
- Make slides specific, visual, diagram-heavy, and discussion-oriented for about 20 minutes.
- Make the guide practical enough for first-time setup and self-repetition at home.
- Include samples that can be demonstrated during lecture and reused during practice.
- Include puzzles with intentionally broken beginner-level code and minimal comments that describe the problem or give a hint.
- Generate PDF outputs next to the Markdown/Marp sources.
- Replace vague motivational filler with concrete project goals, diagrams, screenshots, visual examples, and references to exact lesson samples/puzzles.

**Non-Goals:**

- Do not implement new `risovalka.gamekit` features for lesson 1.
- Do not design the full multi-lesson curriculum.
- Do not introduce a new course packaging system unless PDF generation requires a small local script or documented command.
- Do not add unrelated decorative imagery; every visual asset used by slides must explain a lesson concept.
- Do not preserve the current P0/P1 wording or imagery when it is generic, unrelated, or text-heavy.

## Decisions

1. Use a top-level `lesson1/` directory with the exact filenames requested by the user.

   Rationale: the user provided the desired structure, and a single folder is easier for students and teachers to navigate than splitting lesson assets across `presentations/`, `student_materials/`, and `sessions/`.

   Alternative considered: keep using the existing `presentations/` layout. This would preserve older concept structure, but it would scatter lesson 1 outputs and make the requested package harder to verify.

2. Treat `lesson1_slides.marp.md`, `lesson1_guide.md`, and `achivements.md` as source files, with sibling PDF files as generated deliverables.

   Rationale: Markdown/Marp sources are reviewable, while PDFs are convenient for students and offline classroom use.

   Alternative considered: ship only sources and document PDF generation. This would be lighter, but it would not satisfy the requested lesson structure.

3. Sequence samples from static graphics to variables/functions, then optional loops and conditions.

   Rationale: this follows available `gamekit` primitives and lets graphics concepts be discovered through concrete drawing tasks instead of abstract lecture.

   Alternative considered: start with general Python syntax before graphics. That is less motivating for this course and delays the first visible result.

4. Keep puzzles as runnable broken programs, not prose worksheets.

   Rationale: the practical skill is reading code, running it, interpreting errors, and repairing behavior. Puzzle comments should avoid explaining the full solution.

   Alternative considered: put puzzles only in the guide. That would be easier to author but less useful for hands-on debugging practice.

5. Build the new slide deck around concrete visual artifacts instead of prose explanation.

   Rationale: lesson 1 concepts are visual by nature: raster pixels, RGB channels, coordinate axes, vector arrows, draw-call order, and a finished scene can all be shown directly. Students should see the idea before reading about it.

   Alternative considered: revise the existing P0/P1 decks in place. This would reuse files, but the requested lesson package needs a coherent first-lesson deck and the existing decks mix course overview and graphics with too much broad exposition.

## Risks / Trade-offs

- PDF generation may depend on external tools such as Marp CLI or a Markdown-to-PDF path. -> Mitigation: document the exact command used and keep source files as the canonical materials.
- The requested `achivements` filename is misspelled. -> Mitigation: preserve the requested spelling for compatibility and refer to the content as achievements inside the document.
- Lesson 1 can become too broad. -> Mitigation: make slides a guided overview and reserve detailed setup/debugging steps for the guide.
- Visual slides can become decorative instead of instructional. -> Mitigation: require each image or diagram to map directly to a concept such as raster pixels, RGB color, coordinates, vectors, or the lesson project.
- The deck may still drift into long explanations. -> Mitigation: require each slide to have one concrete point, with diagrams/images doing the main teaching work and text limited to short labels, prompts, or commands.
