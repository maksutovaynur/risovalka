## ADDED Requirements

### Requirement: Object variable container
`risovalka.gamekit` SHALL provide `Object` as a dynamic variable container that accepts keyword attributes and exposes them through dot access.

#### Scenario: Create object with variables
- **WHEN** `Object(x=1, y=2, speed=3.0, power=10)` is created
- **THEN** `o.x`, `o.y`, `o.speed`, and `o.power` return those values

### Requirement: Object has no drawable inheritance
`Object` SHALL NOT inherit from a drawable concept and SHALL NOT own a special internal drawable view in the MVP.

#### Scenario: Object remains plain data
- **WHEN** `Object(shape="circle", x=1, y=2, radius=10)` is created
- **THEN** `shape`, `x`, `y`, and `radius` are regular object attributes rather than nested drawable state

### Requirement: No core Game object drawing
`Game` SHALL NOT provide `draw_object()` in the MVP.

#### Scenario: Core drawing stays explicit
- **WHEN** drawing with `Game`
- **THEN** drawing is done through explicit methods such as `draw_circle`, `draw_rectangle`, `draw_polygon`, `draw_line`, and `draw_image`

### Requirement: Secret tools object drawing
`risovalka.gamekit.secret_tools` SHALL provide `draw_object(game, object)` as an optional advanced helper that interprets object attributes by duck typing and delegates to explicit `Game.draw_*` methods.

#### Scenario: Secret draw circle object
- **WHEN** `secret_tools.draw_object(game, Object(shape="circle", position=Point(100, 100), radius=30))` is called
- **THEN** the helper delegates to `game.draw_circle(...)`

### Requirement: Secret object drawing is reimplementable
The secret `draw_object(game, object)` helper SHALL be simple enough that students can later implement a similar function themselves using `Object` attributes and explicit `Game.draw_*` methods.

#### Scenario: Student studies secret helper
- **WHEN** a curious student reads the helper
- **THEN** they can see that it checks attributes like `shape`, `position`, and `radius`, then calls explicit drawing methods
