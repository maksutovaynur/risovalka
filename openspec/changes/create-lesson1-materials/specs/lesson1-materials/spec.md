## ADDED Requirements

### Requirement: Lesson 1 directory structure
The repository SHALL provide a `lessons/lesson1/` directory containing the complete first lesson package.

#### Scenario: Lesson package files exist
- **WHEN** a contributor lists `lessons/lesson1/`
- **THEN** the directory contains `lesson0_slides.marp.md`, `lesson0_slides.pdf`, `lesson1_slides.marp.md`, `lesson1_slides.pdf`, `lesson1_guide.md`, `lesson1_guide.pdf`, `achivements.md`, `achivements.pdf`, `samples/`, and `puzzles/`

### Requirement: Intro slides
`lessons/lesson1/lesson0_slides.marp.md` SHALL provide a Russian introductory lecture titled "Как код оживляет игры" about why programming matters in the age of AI agents.

#### Scenario: Intro deck covers course motivation
- **WHEN** a reviewer reads the intro slide deck
- **THEN** it explains that programming is precise instruction, computers are literal, programs follow input-processing-output, programming languages are communication tools, games give immediate visual feedback, and AI agents still need a person who understands goals and checks results

#### Scenario: Lesson examples are numbered
- **WHEN** a contributor lists `lessons/lesson1/samples/` and `lessons/lesson1/puzzles/`
- **THEN** Python files use two-digit numeric prefixes such as `01_<name>.py`

### Requirement: Russian student-facing language
All lesson 1 student-facing materials SHALL be written in Russian.

#### Scenario: Student-facing lesson content is reviewed
- **WHEN** a reviewer opens lesson 1 slides, guide, achievements, samples, or puzzles
- **THEN** visible instructional text and code comments intended for students are in Russian

### Requirement: Lesson 1 slides
`lessons/lesson1/lesson1_slides.marp.md` SHALL provide a specific, visual, diagram-heavy, student-addressed, approximately 20-minute theory deck for the first lesson.

#### Scenario: Slide deck has required progression
- **WHEN** a reviewer reads the slide deck
- **THEN** the beginning includes a plan of what students achieve today, the middle includes a motivation hook explaining why the topic matters, and the end includes concrete links or references to lesson samples and puzzles

#### Scenario: Slide deck covers first lesson concepts
- **WHEN** a reviewer reads the slide deck
- **THEN** it covers the course overview, programming motivation, today's project definition, raster graphics, color on a computer, coordinate grid, vectors, basic programming operations, variables, function calls, and basics of `risovalka.gamekit`

#### Scenario: Slide deck teases future control flow
- **WHEN** a reviewer reads slides that mention loops or `if`
- **THEN** those concepts are presented only as teaser concepts for questions or future lessons, not as required lesson 1 practice topics

#### Scenario: Slide deck uses relevant visuals
- **WHEN** a reviewer inspects slide images or diagrams
- **THEN** each visual directly explains a lesson concept or the lesson project and is not unrelated decorative filler

#### Scenario: Slide deck avoids vague filler
- **WHEN** a reviewer reads the slide deck
- **THEN** each slide has one concrete teaching point and avoids broad motivational filler, generic stock-like imagery, and long text blocks

#### Scenario: Slide deck uses diagrams for graphics concepts
- **WHEN** a reviewer inspects slides about raster graphics, color, coordinates, vectors, or drawing order
- **THEN** those slides use maintainable hand-made diagrams, annotated screenshots, visual examples, or fixed generated PNG images rather than prose-only explanation

#### Scenario: Slide deck balances visual asset types
- **WHEN** a reviewer inspects the deck visuals
- **THEN** the deck uses both maintainable hand-made diagrams and fixed generated PNG visuals, with neither type dominating the visual explanation

### Requirement: Lesson 1 project definition
Lesson 1 SHALL define today's project as a first game scene plus a small manual animation, with optional variable parts tracked by achievements.

#### Scenario: Project required part is clear
- **WHEN** a student reads the slides or guide
- **THEN** they can identify that the required lesson 1 result is a first game scene and a small manual animation

#### Scenario: Project variation is achievement-driven
- **WHEN** a student reads `achivements.md`
- **THEN** they can choose optional variations or improvements that personalize today's project

### Requirement: Lesson 1 guide
`lessons/lesson1/lesson1_guide.md` SHALL provide a detailed practical guide for completing the first lesson without spoiling discovery-based insights.

#### Scenario: Guide covers setup and first run
- **WHEN** a student follows the guide
- **THEN** it explains how to install Python, VS Code, recommended VS Code plugins, open the project, and run a lesson sample with Windows as the primary setup path and brief macOS/Linux notes

#### Scenario: Guide covers editor basics
- **WHEN** a student reads the guide before editing code
- **THEN** it explains syntax highlighting, autocomplete, saving files, running code, and reading the terminal in simple Russian

#### Scenario: Guide covers beginner Python errors
- **WHEN** a student reaches the error help section
- **THEN** it explains common beginner errors such as `SyntaxError`, `NameError`, `IndentationError`, `TypeError`, file path mistakes, and letter case mistakes in simple Russian

### Requirement: Lesson 1 achievements
`lessons/lesson1/achivements.md` SHALL provide a practical checklist or checkbox grid of achievements for lesson 1.

#### Scenario: Achievements guide practical progress
- **WHEN** students work during the practical part
- **THEN** they can mark completed outcomes for environment setup, running a sample, changing drawing parameters, using coordinates, using colors, fixing at least one puzzle, and making a small personal change to today's project

### Requirement: Lesson 1 samples
`lessons/lesson1/samples/` SHALL contain seven runnable Python examples demonstrated during lecture and reusable during practice.

#### Scenario: Samples are stable references
- **WHEN** a student runs any lesson 1 sample file
- **THEN** the sample demonstrates predictable behavior suitable for reuse during practice

#### Scenario: Samples demonstrate available gamekit basics
- **WHEN** a student runs the sample files
- **THEN** the samples demonstrate available `risovalka.gamekit` basics such as opening a window, clearing the canvas, setting fill/stroke color, drawing shapes, drawing text, using coordinates, using variables, calling functions, and using `Point` or `Vector`

#### Scenario: Samples include repeated-code function motivation
- **WHEN** a reviewer lists the lesson 1 samples
- **THEN** one sample shows repeated drawing of the same complex object without a function and another sample shows the same repeated problem solved with a small function

#### Scenario: Samples stay open
- **WHEN** a student runs any lesson 1 sample file
- **THEN** the game window remains open until the student closes it

#### Scenario: Samples have concise Russian comments
- **WHEN** a reviewer reads sample source code
- **THEN** comments are concise, understandable, and written in Russian

### Requirement: Lesson 1 puzzles
`lessons/lesson1/puzzles/` SHALL contain six runnable Python puzzle files with intentional beginner-level errors or broken scene behavior for students to fix.

#### Scenario: Puzzles are diagnostic playgrounds
- **WHEN** a student runs or edits any lesson 1 puzzle file
- **THEN** the puzzle exposes an intentional problem, broken behavior, or surprising result for the student to diagnose and repair

#### Scenario: Puzzle comments do not spoil solutions
- **WHEN** a reviewer reads puzzle source code comments
- **THEN** comments contain only the problem description and optional hint, without step-by-step solution spoilers

#### Scenario: Puzzles match lesson concepts
- **WHEN** students attempt the puzzle files
- **THEN** the broken code exercises lesson 1 concepts such as drawing order, canvas clearing, frame timing, coordinates, colors, image paths, or `gamekit` drawing calls

### Requirement: Lesson 1 PDFs
The repository SHALL include generated-in-advance PDF outputs for the first lesson slides, guide, and achievements.

#### Scenario: PDF deliverables exist
- **WHEN** a contributor lists `lessons/lesson1/`
- **THEN** `lesson0_slides.pdf`, `lesson1_slides.pdf`, `lesson1_guide.pdf`, and `achivements.pdf` are present next to their source files

#### Scenario: Students can read PDFs without build tooling
- **WHEN** a student opens the lesson 1 PDF files
- **THEN** the files are readable without installing Marp or Markdown build tools
