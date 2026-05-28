## Context

The repository already contains course concept documents, legacy starter presentations, a Russian student-facing language policy, and an MVP `risovalka.gamekit` API. Lesson 1 must convert that intent into a concrete lesson package students can open, read, run, and practice with. Existing legacy P0/P1 Marp decks are useful as topic inventory, but their current style is too text-heavy, vague, and visually generic for the lesson 1 target.

The target lesson is introductory: students need motivation for programming, a course overview, first contact with computer graphics, basic Python expressions, and a defined first project with required and variable parts. Following `concept/02_sessions_plan.md`, the practical result is a first game scene plus a small manual animation. The variable part is represented by `achivements.md`, so students can personalize the result without losing the core lesson path. The materials should avoid relying on future raster/vector editor tools and instead build around the available `risovalka.gamekit` operations: opening a window, setting colors, drawing shapes/text/images, using coordinates, using `Point`/`Vector`, variables, functions, and simple arithmetic. Loops and `if` may appear in slides only as teaser concepts for student questions; deeper practice belongs to the next lesson.

## Goals / Non-Goals

**Goals:**

- Create a complete `lessons/lesson1/` source tree with slides, guide, achievements, samples, and puzzles.
- Keep all student-facing content in Russian.
- Make slides specific, visual, diagram-heavy, and discussion-oriented for about 20 minutes.
- Make the guide practical enough for first-time setup and self-repetition at home.
- Include samples that can be demonstrated during lecture and reused during practice.
- Include puzzles with intentionally broken beginner-level code and minimal comments that describe the problem or give a hint.
- Generate PDF outputs next to the Markdown/Marp sources.
- Replace vague motivational filler with concrete project goals, diagrams, screenshots, visual examples, and references to exact lesson samples/puzzles.
- Target seven samples and six puzzles.
- Make every sample keep its game window open until the student closes it.
- Make samples stable and predictable, while puzzles are intentionally unstable, broken, or surprising playgrounds for diagnosis and repair.

**Non-Goals:**

- Do not implement new `risovalka.gamekit` features for lesson 1.
- Do not design the full multi-lesson curriculum.
- Do not introduce a new course packaging system unless PDF generation requires a small local script or documented command.
- Do not add unrelated decorative imagery; every visual asset used by slides must explain a lesson concept.
- Do not preserve the current P0/P1 wording or imagery when it is generic, unrelated, or text-heavy.
- Do not teach loops or `if` deeply in lesson 1; mention them only as teaser concepts if useful.

## Decisions

1. Use a `lessons/lesson1/` directory with the exact filenames requested by the user.

   Rationale: the user provided the desired structure, and a single folder is easier for students and teachers to navigate than splitting lesson assets across legacy presentations, `student_materials/`, and `sessions/`.

   Alternative considered: keep using the legacy presentation layout. This would preserve older concept structure, but it would scatter lesson 1 outputs and make the requested package harder to verify.

2. Treat `lesson1_slides.marp.md`, `lesson1_guide.md`, and `achivements.md` as source files inside `lessons/lesson1/`, with sibling PDF files as generated deliverables.

   Rationale: Markdown/Marp sources are reviewable, while PDFs are convenient for students and offline classroom use. PDFs should be generated in advance so students can open and read them without installing documentation tooling.

   Alternative considered: ship only sources and document PDF generation. This would be lighter, but it would not satisfy the requested lesson structure.

3. Sequence samples from static graphics to variables/functions, with loops and conditions only teased in slides.

   Rationale: this follows available `gamekit` primitives and lets graphics concepts be discovered through concrete drawing tasks instead of abstract lecture. Setup, graphics, colors, coordinates, variables, functions, and error reading are already enough for the first lesson.

   Alternative considered: include loops and `if` as full practical topics. That would overload the first lesson and duplicate the next lesson's deeper material.

4. Keep puzzles as runnable broken programs, not prose worksheets.

   Rationale: the practical skill is reading code, running it, interpreting errors, and repairing behavior. Puzzle comments should avoid explaining the full solution.

   Alternative considered: put puzzles only in the guide. That would be easier to author but less useful for hands-on debugging practice.

5. Build the new slide deck around concrete visual artifacts instead of prose explanation.

   Rationale: lesson 1 concepts are visual by nature: raster pixels, RGB channels, coordinate axes, vector arrows, draw-call order, and a finished scene can all be shown directly. Students should see the idea before reading about it.

   Alternative considered: revise the existing P0/P1 decks in place. This would reuse files, but the requested lesson package needs a coherent first-lesson deck and the existing decks mix course overview and graphics with too much broad exposition.

6. Use a roughly 50/50 mix of maintainable hand-made diagrams and fixed generated PNG visuals.

   Rationale: hand-made diagrams are easy to maintain when concepts change, while fixed PNGs can quickly communicate richer visual states such as a finished scene or pixel/color examples.

   Alternative considered: use only generated images. This would make the deck more visual quickly, but it would be harder to edit precisely and risks repeating the current problem of visuals that do not carry the lesson.

7. Define today's project as a concrete required scene plus achievement-driven variation.

   Rationale: students need a clear finish line and enough room to make the result their own. The required part keeps the class aligned; `achivements.md` covers optional variations. The project should follow session 1 from `concept/02_sessions_plan.md`: create a first game scene and a small manual cartoon/animation.

   Alternative considered: leave the project open-ended. This is more creative but risky for a first lesson because beginners need a precise target.

8. Make Windows the primary setup path, with brief macOS/Linux notes.

   Rationale: beginner setup instructions must be concrete, and the target student environment is Windows. Short macOS/Linux notes preserve portability without making the main guide hard to follow.

   Alternative considered: write equal setup instructions for all operating systems. This would be more complete but noisier for the expected classroom path.

9. Separate samples and puzzles by behavior contract.

   Rationale: samples should be stable reference material students can reuse during practice. Puzzles should do the opposite: expose a problem, bug, or surprising behavior that students can find and repair like a playground exercise.

   Alternative considered: make puzzles small failing unit-like examples. That is easier to verify, but less aligned with the intended exploratory debugging practice.

## Risks / Trade-offs

- PDF generation may depend on external tools such as Marp CLI or a Markdown-to-PDF path. -> Mitigation: generate PDFs in advance, document the exact command used when possible, and keep source files as the canonical materials.
- The requested `achivements` filename is misspelled. -> Mitigation: preserve the requested spelling for compatibility and refer to the content as achievements inside the document.
- Lesson 1 can become too broad. -> Mitigation: make slides a guided overview and reserve detailed setup/debugging steps for the guide.
- Visual slides can become decorative instead of instructional. -> Mitigation: require each image or diagram to map directly to a concept such as raster pixels, RGB color, coordinates, vectors, or the lesson project.
- The deck may still drift into long explanations. -> Mitigation: require each slide to have one concrete point, with diagrams/images doing the main teaching work and text limited to short labels, prompts, or commands.
- First-lesson samples may confuse students if some programs exit immediately and others stay open. -> Mitigation: require every sample to keep its window open until the student closes it.
