## Purpose

Define the repository-level project principles, language policy, and relationship to the concept documents.

## Requirements

### Requirement: Root project principles document
The repository SHALL include a root-level `SOUL.md` that defines the project principles for educational simplicity, expressive game-building potential, language policy, and alignment with the `concept/` documents.

#### Scenario: Project soul is available
- **WHEN** a contributor opens the repository root
- **THEN** `SOUL.md` is present and describes the principles that guide engine, tool, sample, and session development

### Requirement: Educational simplicity with expressive headroom
`SOUL.md` SHALL state that the project favors simple, teachable code for beginner education while preserving enough engine and tool capability to build many different games.

#### Scenario: Contributor checks implementation direction
- **WHEN** a contributor reads `SOUL.md` before adding engine or tool code
- **THEN** they can identify that beginner-friendly simplicity is required and advanced opportunities must not make the code unnecessarily complex

### Requirement: Russian student-facing language policy
`SOUL.md` SHALL state that all UI components, student guides, examples intended for students, and teaching session materials MUST be written in Russian.

#### Scenario: Student-facing text is created
- **WHEN** a new student-facing screen, guide, example, or session template is added
- **THEN** its visible instructional text is written in Russian

### Requirement: English exceptions
`SOUL.md` SHALL state that English is allowed for user prompts, OpenSpec metadata, and core project comments.

#### Scenario: Contributor writes non-student-facing metadata
- **WHEN** a contributor adds OpenSpec metadata or core implementation comments
- **THEN** English text is allowed

### Requirement: Concept document alignment
`SOUL.md` SHALL direct contributors to use the `concept/` folder as the source of project intent for the course, engine, tools, sessions, and quality principles.

#### Scenario: Contributor needs project context
- **WHEN** a contributor needs to understand the intended shape of the project
- **THEN** `SOUL.md` points them to the `concept/` folder for deeper guidance
