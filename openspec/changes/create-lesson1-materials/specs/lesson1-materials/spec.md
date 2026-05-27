## ADDED Requirements

### Requirement: Lesson 1 directory structure
The repository SHALL provide a top-level `lesson1/` directory containing the complete first lesson package.

#### Scenario: Lesson package files exist
- **WHEN** a contributor lists `lesson1/`
- **THEN** the directory contains `lesson1_slides.marp.md`, `lesson1_slides.pdf`, `lesson1_guide.md`, `lesson1_guide.pdf`, `achivements.md`, `achivements.pdf`, `samples/`, and `puzzles/`

#### Scenario: Lesson examples are numbered
- **WHEN** a contributor lists `lesson1/samples/` and `lesson1/puzzles/`
- **THEN** Python files use two-digit numeric prefixes such as `01_<name>.py`

### Requirement: Russian student-facing language
All lesson 1 student-facing materials SHALL be written in Russian.

#### Scenario: Student-facing lesson content is reviewed
- **WHEN** a reviewer opens lesson 1 slides, guide, achievements, samples, or puzzles
- **THEN** visible instructional text and code comments intended for students are in Russian

### Requirement: Lesson 1 slides
`lesson1/lesson1_slides.marp.md` SHALL provide a specific, visual, diagram-heavy, student-addressed, approximately 20-minute theory deck for the first lesson.

#### Scenario: Slide deck has required progression
- **WHEN** a reviewer reads the slide deck
- **THEN** the beginning includes a plan of what students achieve today, the middle includes a motivation hook explaining why the topic matters, and the end includes concrete links or references to lesson samples and puzzles

#### Scenario: Slide deck covers first lesson concepts
- **WHEN** a reviewer reads the slide deck
- **THEN** it covers the course overview, programming motivation, today's project announcement, raster graphics, color on a computer, coordinate grid, vectors, basic programming operations, variables, function calls, and basics of `risovalka.gamekit`

#### Scenario: Slide deck uses relevant visuals
- **WHEN** a reviewer inspects slide images or diagrams
- **THEN** each visual directly explains a lesson concept or the lesson project and is not unrelated decorative filler

#### Scenario: Slide deck avoids vague filler
- **WHEN** a reviewer reads the slide deck
- **THEN** each slide has one concrete teaching point and avoids broad motivational filler, generic stock-like imagery, and long text blocks

#### Scenario: Slide deck uses diagrams for graphics concepts
- **WHEN** a reviewer inspects slides about raster graphics, color, coordinates, vectors, or drawing order
- **THEN** those slides use diagrams, annotated screenshots, visual examples, or generated explanatory images rather than prose-only explanation

### Requirement: Lesson 1 guide
`lesson1/lesson1_guide.md` SHALL provide a detailed practical guide for completing the first lesson without spoiling discovery-based insights.

#### Scenario: Guide covers setup and first run
- **WHEN** a student follows the guide
- **THEN** it explains how to install Python, VS Code, recommended VS Code plugins, open the project, and run a lesson sample

#### Scenario: Guide covers editor basics
- **WHEN** a student reads the guide before editing code
- **THEN** it explains syntax highlighting, autocomplete, saving files, running code, and reading the terminal in simple Russian

#### Scenario: Guide covers beginner Python errors
- **WHEN** a student reaches the error help section
- **THEN** it explains common beginner errors such as `SyntaxError`, `NameError`, `IndentationError`, `TypeError`, file path mistakes, and letter case mistakes in simple Russian

### Requirement: Lesson 1 achievements
`lesson1/achivements.md` SHALL provide a practical checklist or checkbox grid of achievements for lesson 1.

#### Scenario: Achievements guide practical progress
- **WHEN** students work during the practical part
- **THEN** they can mark completed outcomes for environment setup, running a sample, changing drawing parameters, using coordinates, using colors, fixing at least one puzzle, and making a small personal change to today's project

### Requirement: Lesson 1 samples
`lesson1/samples/` SHALL contain runnable Python examples demonstrated during lecture and reusable during practice.

#### Scenario: Samples demonstrate available gamekit basics
- **WHEN** a student runs the sample files
- **THEN** the samples demonstrate available `risovalka.gamekit` basics such as opening a window, clearing the canvas, setting fill/stroke color, drawing shapes, drawing text, using coordinates, using variables, calling functions, and using `Point` or `Vector`

#### Scenario: Samples have concise Russian comments
- **WHEN** a reviewer reads sample source code
- **THEN** comments are concise, understandable, and written in Russian

### Requirement: Lesson 1 puzzles
`lesson1/puzzles/` SHALL contain runnable Python puzzle files with intentional beginner-level errors for students to fix.

#### Scenario: Puzzle comments do not spoil solutions
- **WHEN** a reviewer reads puzzle source code comments
- **THEN** comments contain only the problem description and optional hint, without step-by-step solution spoilers

#### Scenario: Puzzles match lesson concepts
- **WHEN** students attempt the puzzle files
- **THEN** the broken code exercises lesson 1 concepts such as function calls, arithmetic, variables, coordinates, colors, simple conditions, simple loops, or `gamekit` drawing calls

### Requirement: Lesson 1 PDFs
The repository SHALL include PDF outputs for the first lesson slides, guide, and achievements.

#### Scenario: PDF deliverables exist
- **WHEN** a contributor lists `lesson1/`
- **THEN** `lesson1_slides.pdf`, `lesson1_guide.pdf`, and `achivements.pdf` are present next to their source files
