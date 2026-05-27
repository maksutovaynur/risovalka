## ADDED Requirements

### Requirement: Geometry tools package
`risovalka.gamekit` SHALL provide `geometry_tools` for helper functions that generate and transform points without adding rotation parameters to basic draw methods.

#### Scenario: Import geometry tools
- **WHEN** Python code runs `from risovalka.gamekit import geometry_tools`
- **THEN** the import succeeds

### Requirement: Rotate point
`geometry_tools` SHALL provide `rotate_point(point: Point | tuple, angle: float = 0, anchor: Point | tuple = Point(0, 0)) -> Point` and SHALL also accept the explicit `rotate_point(point, anchor, angle)` form.

#### Scenario: Rotate point around anchor
- **WHEN** `geometry_tools.rotate_point(Point(1, 0), Point(0, 0), 90)` is called
- **THEN** it returns the point rotated around the anchor by 90 degrees

#### Scenario: Rotate point around origin by default
- **WHEN** `geometry_tools.rotate_point(Point(1, 0), 90)` is called
- **THEN** it returns the point rotated around `Point(0, 0)` by 90 degrees

### Requirement: Generate regular polygon
`geometry_tools` SHALL provide `generate_regular_polygon(center: Point | tuple, radius: float, sides: int) -> list[Point]`.

#### Scenario: Generate hexagon
- **WHEN** `generate_regular_polygon(Point(100, 100), 40, 6)` is called
- **THEN** it returns six points

### Requirement: Generate star
`geometry_tools` SHALL provide `generate_star(center: Point | tuple, lower_radius: float, higher_radius: float, num_ends: int) -> list[Point]`.

#### Scenario: Generate five-point star
- **WHEN** `generate_star(Point(100, 100), 20, 40, 5)` is called
- **THEN** it returns points for a five-ended star polygon

### Requirement: Transform polygon
`geometry_tools` SHALL provide `rotate_polygon(points, angle: float = 0, anchor: Point | tuple = Point(0, 0))`, `move_polygon(points, delta: Point | tuple = Point(0, 0))`, and `scale_polygon(points, scale = 1, anchor: Point | tuple = Point(0, 0))`.

#### Scenario: Rotate polygon
- **WHEN** `rotate_polygon(points, 45, Point(0, 0))` is called
- **THEN** it returns a new list of rotated points

#### Scenario: Move and scale polygon
- **WHEN** `move_polygon(points, Point(10, 0))` and `scale_polygon(points, 2, Point(0, 0))` are called
- **THEN** each function returns a new transformed point list
