# gamekit-drawing Specification

## Purpose
TBD - created by archiving change mvp-gamekit. Update Purpose after archive.
## Requirements
### Requirement: Circle drawing
`Game` SHALL provide `draw_circle` that accepts either `draw_circle(center: Point, radius: float)` or `draw_circle(x, y, radius)` argument forms.

#### Scenario: Draw circle with coordinates
- **WHEN** `game.draw_circle(100, 120, 30)` is called
- **THEN** a circle is queued or drawn using the current fill and stroke state

### Requirement: Rectangle drawing
`Game` SHALL provide `draw_rectangle` that accepts `draw_rectangle(x, y, width, height)`, `draw_rectangle(point1: Point, point2: Point)`, and `draw_rectangle(point: Point, size: Size)` forms.

#### Scenario: Draw rectangle with point and size
- **WHEN** `game.draw_rectangle(Point(10, 20), Size(100, 50))` is called
- **THEN** a rectangle is queued or drawn using the current fill and stroke state

### Requirement: Polygon drawing
`Game` SHALL provide `draw_polygon` that accepts either `draw_polygon(list[Point])` or variadic point arguments.

#### Scenario: Draw polygon from variadic points
- **WHEN** `game.draw_polygon(Point(0, 0), Point(50, 0), Point(25, 40))` is called
- **THEN** a polygon is queued or drawn using the current fill and stroke state

### Requirement: Common polygon shortcuts
`Game` SHALL NOT provide `draw_star` or `draw_regular_polygon` shortcuts; generated stars and regular polygons SHALL be created through `geometry_tools` and drawn with `draw_polygon`.

#### Scenario: Draw generated regular polygon
- **WHEN** code calls `points = geometry_tools.generate_regular_polygon(Point(100, 100), 40, 6)` and then `game.draw_polygon(points)`
- **THEN** a six-sided polygon is queued or drawn

### Requirement: Polyline drawing
`Game` SHALL provide `draw_line` that accepts either variadic points or a list of points.

#### Scenario: Draw line from list
- **WHEN** `game.draw_line([Point(0, 0), Point(10, 10), Point(20, 0)])` is called
- **THEN** connected line segments are queued or drawn using the current stroke state

### Requirement: Image and sprite drawing
`Game` SHALL provide `draw_image(image: Image, position: Point, size: Size = image.original_size, rotation: Rotation = Rotation(0))` and `draw_sprite(sprite: Sprite, position: Point, size: Size = sprite.current_image.original_size, rotation: Rotation = Rotation(0))`.

#### Scenario: Draw image with texture-backed rectangle
- **WHEN** `game.draw_image(image, Point(100, 100), Size(64, 64), Rotation(15, Point(132, 132)))` is called
- **THEN** the image is drawn as a texture-filled rotated rectangle while preserving the previous fill state afterward

#### Scenario: Draw image with defaults
- **WHEN** `game.draw_image(image, Point(100, 100))` is called
- **THEN** the image is drawn at `image.original_size` without requiring an explicit rotation

#### Scenario: Draw sprite current frame
- **WHEN** `game.draw_sprite(sprite, Point(100, 100), Size(64, 64))` is called
- **THEN** the sprite's current image frame is drawn at the requested position

### Requirement: Geometry draw methods do not accept rotation
Basic geometry draw methods SHALL NOT accept rotation or anchor parameters; rotation for geometry SHALL be achieved by transforming points before drawing.

#### Scenario: Draw rotated polygon explicitly
- **WHEN** code rotates polygon points with `geometry_tools.rotate_polygon(points, angle, anchor)` and passes them to `game.draw_polygon(...)`
- **THEN** the rotated geometry is drawn without a `rotation` parameter on `draw_polygon`

### Requirement: Explicit draw method names
`Game` SHALL expose beginner-facing drawing methods with the `draw_` prefix and SHALL NOT expose short aliases such as `circle()`, `rectangle()`, or `polygon()`.

#### Scenario: Drawing API is explicit
- **WHEN** a student looks for shape drawing methods on `Game`
- **THEN** the available beginner-facing shape methods are named with the `draw_` prefix

### Requirement: Top-left drawing coordinates
Public drawing coordinates SHALL use a top-left origin, with positive `x` moving right and positive `y` moving down.

#### Scenario: Draw near top-left
- **WHEN** `game.draw_circle(0, 0, 10)` is called
- **THEN** the circle is positioned relative to the top-left canvas origin

### Requirement: Texture fill rotation composition
When texture or shader fill is active, fill rotation SHALL be controlled by the `Rotation` passed to `set_fill_texture` or `set_fill_shader`.

#### Scenario: Draw rotated textured rectangle
- **WHEN** texture fill rotation is `Rotation(30, Point(50, 50))` and `game.draw_rectangle(...)` is called
- **THEN** the fill is rotated around the fill rotation anchor

### Requirement: Texture fills for supported geometry
Texture fill SHALL render visually for every MVP fill-capable geometry method, including circles, rectangles, and polygons.

#### Scenario: Draw textured polygon
- **WHEN** texture fill is active and `game.draw_polygon(...)` is called
- **THEN** the polygon is rendered with the active texture fill rather than falling back to plain color

#### Scenario: Draw textured circle
- **WHEN** texture fill is active and `game.draw_circle(...)` is called
- **THEN** the circle is rendered with texture fill, with exact circular clipping allowed to be approximate in the MVP

### Requirement: Shader fills for supported geometry
Shader fill SHALL render visually for every MVP fill-capable geometry method, including circles, rectangles, and polygons.

#### Scenario: Draw shader-filled circle
- **WHEN** shader fill is active and `game.draw_circle(...)` is called
- **THEN** the circle is rendered with the active shader fill rather than falling back to plain color

### Requirement: Polygon fill clipping
Polygon and rectangle texture and shader fills SHALL clip to the generated OpenGL geometry for the shape.

#### Scenario: Draw shader-filled polygon
- **WHEN** shader fill is active and `game.draw_polygon(...)` is called
- **THEN** pixels outside the polygon geometry are not visibly filled by that draw call

