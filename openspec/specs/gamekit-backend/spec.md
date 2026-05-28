# gamekit-backend Specification

## Purpose
TBD - created by archiving change mvp-gamekit. Update Purpose after archive.
## Requirements
### Requirement: Pyglet backend
The MVP SHALL use `pyglet` as the underlying backend for windowing, input events, image loading, OpenGL rendering, and shader-capable drawing.

#### Scenario: Dependency review
- **WHEN** the MVP is implemented
- **THEN** `pyproject.toml` includes `pyglet` as a runtime dependency

### Requirement: Backend hidden from beginner API
The MVP SHALL hide direct `pyglet` objects from the normal beginner-facing `Game` API.

#### Scenario: Beginner imports gamekit
- **WHEN** a student imports public names from `risovalka.gamekit`
- **THEN** they can use `Game` and gamekit value/asset wrappers without importing `pyglet`

### Requirement: OpenGL-backed rendering path
The MVP SHALL render through a backend window/canvas with an OpenGL context so texture and shader features can be supported.

#### Scenario: Game window opens
- **WHEN** `Game.open()` creates the window
- **THEN** the internal canvas is backed by the selected backend rendering context

### Requirement: Lightweight dependency footprint
The MVP SHALL NOT add a higher-level game framework dependency for the core `Game` API.

#### Scenario: Dependency review
- **WHEN** dependencies are reviewed after implementation
- **THEN** the core gamekit dependency list does not include Arcade, pygame-ce, ModernGL, or other higher-level graphics frameworks unless separately justified by a later change

