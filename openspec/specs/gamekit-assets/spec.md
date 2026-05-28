# gamekit-assets Specification

## Purpose
TBD - created by archiving change mvp-gamekit. Update Purpose after archive.
## Requirements
### Requirement: Color value and conversion helpers
`risovalka.gamekit` SHALL provide `Color`, `get_hex(any_color_format)`, and `get_rgba(any_color_format)` supporting named colors, RGB hex in `#RRGGBB` format, RGBA hex in `#RRGGBBAA` format, `rgb()` tuples, `rgba()` tuples, and transparent color input.

#### Scenario: Parse hex color
- **WHEN** `get_rgba("#ffaadd00")` is called
- **THEN** it returns a normalized RGBA representation where red is `ff`, green is `aa`, blue is `dd`, and alpha is `00`

#### Scenario: Parse named color
- **WHEN** `get_hex("orange")` is called
- **THEN** it returns a normalized hex representation for orange

### Requirement: Point Size Vector and Rotation value types
`risovalka.gamekit` SHALL provide mutable tuple-like `Point(x: float, y: float)`, `Size(width: float, height: float)`, `Vector(x: float, y: float)`, and `Rotation(angle: float, anchor: Point = Point(0, 0))` value types.

#### Scenario: Create point and size
- **WHEN** `Point(1, 2)`, `Size(100, 50)`, `Vector(3, 4)`, and `Rotation(45, Point(10, 10))` are created
- **THEN** their named fields are accessible as `x`, `y`, `width`, `height`, `angle`, and `anchor`

#### Scenario: Mutate value properties
- **WHEN** `p = Point(1, 2)` then `p.x = 5` and `p[1] = 6` are executed
- **THEN** `p.x` is `5` and `p.y` is `6`

#### Scenario: Vector has magnitude
- **WHEN** `Vector(3, 4).size()` is called
- **THEN** it returns `5`

#### Scenario: Value addition and scalar multiplication are commutative
- **WHEN** `Point(1, 2) + Vector(3, 4)` and `Vector(3, 4) + Point(1, 2)` are called
- **THEN** both return `Point(4, 6)`
- **AND** `2 * Vector(3, 4)` returns the same value as `Vector(3, 4) * 2`

#### Scenario: Size means width and height
- **WHEN** `Size(100, 50)` is used with a start position `Point(10, 20)`
- **THEN** it represents an area from x `10` to `110` and y `20` to `70`, not a bottom-right point at `100, 50`

### Requirement: Load image
`Game` SHALL provide `load_image(image_path)` returning an `Image` wrapper.

#### Scenario: Load image
- **WHEN** `image = game.load_image("hero.png")` is called with an existing image path
- **THEN** an `Image` wrapper is returned

### Requirement: Image wrapper properties
`Image` SHALL expose only backend image `data` and `original_size`.

#### Scenario: Load image original size
- **WHEN** `image = game.load_image("hero.png")` is called
- **THEN** `image.original_size` describes the source image dimensions

### Requirement: Load sprite
`Game` SHALL provide `load_sprite(*image_paths)` and support a single list of image paths.

#### Scenario: Load sprite from list
- **WHEN** `load_sprite(["a.png", "b.png"])` is called
- **THEN** the returned `Sprite` has two image frames

### Requirement: Sprite frame state
`Sprite` SHALL expose `images`, `current_frame`, `frame_number`, `current_image`, `next_frame(cycle=False)`, and `prev_frame(cycle=False)`.

#### Scenario: Advance sprite without cycle
- **WHEN** `next_frame(cycle=False)` is called on the last frame
- **THEN** `current_frame` remains on the last frame

#### Scenario: Advance sprite with cycle
- **WHEN** `next_frame(cycle=True)` is called on the last frame
- **THEN** `current_frame` becomes the first frame

### Requirement: Load shader
`Game` SHALL provide `load_shader(shader_source)` returning a `Shader` wrapper that can load a built-in shader by name or a shader from a file path and accept named parameters.

#### Scenario: Load built-in shader
- **WHEN** `game.load_shader("portal")` is called for a supported built-in shader name
- **THEN** a `Shader` wrapper for that built-in shader is returned

#### Scenario: Load shader file
- **WHEN** `game.load_shader("shaders/my_effect.glsl")` is called with an existing shader file path
- **THEN** a `Shader` wrapper for that shader file is returned

#### Scenario: Set shader parameter
- **WHEN** `shader.set_param("time", 12)` is called
- **THEN** the shader stores the `time` parameter for use during rendering

