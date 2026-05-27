## Purpose

Define the Python package topology for the Risovalka engine, tools, samples, and teaching sessions.

## Requirements

### Requirement: Top-level risovalka package
The project SHALL provide an importable `risovalka` Python package as the root namespace for engine, tools, and samples.

#### Scenario: Import root package
- **WHEN** Python is run in the project environment
- **THEN** `import risovalka` succeeds

### Requirement: Gamekit engine package
The project SHALL provide `risovalka.gamekit` as the canonical import path for the educational 2D game engine.

#### Scenario: Import engine package
- **WHEN** Python is run in the project environment
- **THEN** `import risovalka.gamekit` succeeds

### Requirement: Raster tool package
The project SHALL reserve `risovalka.tools.raster` as the package for a ready-to-use raster drawing tool for images, textures, and sprites.

#### Scenario: Import raster tool package
- **WHEN** Python is run in the project environment
- **THEN** `import risovalka.tools.raster` succeeds

### Requirement: Vector tool package
The project SHALL reserve `risovalka.tools.vector` as the package for a vector drawing tool that can export SVG and gamekit drawing-code samples.

#### Scenario: Import vector tool package
- **WHEN** Python is run in the project environment
- **THEN** `import risovalka.tools.vector` succeeds

### Requirement: Samples package
The project SHALL provide `risovalka.samples` as the package for examples that demonstrate use of the engine.

#### Scenario: Import samples package
- **WHEN** Python is run in the project environment
- **THEN** `import risovalka.samples` succeeds

### Requirement: Sessions package
The project SHALL provide an importable top-level `sessions` package for teaching session templates.

#### Scenario: Import sessions package
- **WHEN** Python is run in the project environment
- **THEN** `import sessions` succeeds

### Requirement: Dependency-free structural setup
The package layout setup SHALL NOT add new third-party runtime dependencies.

#### Scenario: Review dependency changes
- **WHEN** the package structure change is implemented
- **THEN** `pyproject.toml` does not gain new third-party dependencies for the scaffolding itself
