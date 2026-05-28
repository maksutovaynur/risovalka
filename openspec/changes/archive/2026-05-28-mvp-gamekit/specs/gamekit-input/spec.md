## ADDED Requirements

### Requirement: Keyboard down state
`Game` SHALL provide `is_key_down(key_name)` indicating whether a key is currently pressed.

#### Scenario: Key is held
- **WHEN** a key is pressed and held
- **THEN** `is_key_down(key_name)` returns true for that key

### Requirement: Keyboard clicked state
`Game` SHALL provide `is_key_clicked(key_name)` indicating whether a key was clicked since the previous `show_canvas()`.

#### Scenario: Key click is consumed by frame
- **WHEN** a key is pressed between two calls to `show_canvas()`
- **THEN** `is_key_clicked(key_name)` returns true until the next `show_canvas()` flushes click state

### Requirement: Mouse button states
`Game` SHALL provide `is_mouse_down(button_name)` and `is_mouse_clicked(button_name)` for `left`, `right`, and `middle` buttons.

#### Scenario: Mouse button click
- **WHEN** the left mouse button is clicked between two calls to `show_canvas()`
- **THEN** `is_mouse_clicked("left")` returns true until click state is flushed

### Requirement: Mouse position
`Game` SHALL provide `get_mouse_position()` returning a `Point`.

#### Scenario: Read mouse position
- **WHEN** the mouse moves over the canvas
- **THEN** `get_mouse_position()` returns the latest known canvas position

### Requirement: Mouse scroll delta
`Game` SHALL provide `get_mouse_scroll()` returning the wheel movement accumulated since the previous `show_canvas()`.

#### Scenario: Read scroll delta
- **WHEN** the mouse wheel moves by a positive amount between frames
- **THEN** `get_mouse_scroll()` returns that positive accumulated delta until scroll state is flushed
