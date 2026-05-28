# gamekit-game-api Specification

## Purpose
TBD - created by archiving change mvp-gamekit. Update Purpose after archive.
## Requirements
### Requirement: Single Game entry point
`risovalka.gamekit` SHALL expose `Game` as the single required class for beginner-facing window, drawing, asset loading, and input operations.

#### Scenario: Import Game
- **WHEN** Python code runs `from risovalka.gamekit import Game`
- **THEN** the import succeeds

### Requirement: Default game singleton
`risovalka.gamekit` SHALL expose `game` as a default `Game` instance so simple programs can use the engine without constructing `Game`.

#### Scenario: Import default game
- **WHEN** Python code runs `from risovalka.gamekit import game`
- **THEN** `game` is ready to receive the same beginner-facing calls as a `Game` instance

### Requirement: Window title management
`Game` SHALL provide `set_window_title(title: str)` to set the current or next window title.

#### Scenario: Set title before open
- **WHEN** `set_window_title("Моя игра")` is called before `open()`
- **THEN** the opened window uses that title

### Requirement: Window logo management
`Game` SHALL provide `set_logo(image: Image)` to set the current or next window logo.

#### Scenario: Set logo before open
- **WHEN** `set_logo(game.load_image("logo.png"))` is called before `open()`
- **THEN** the opened window uses that image as its icon

### Requirement: Window size and fullscreen management
`Game` SHALL provide `set_window_size(width: int, height: int)` and `set_window_fullscreen(enabled: bool)` for window geometry control.

#### Scenario: Set size before open
- **WHEN** `set_window_size(800, 600)` is called before `open()`
- **THEN** `window_size` is `Size(800, 600)` after opening

#### Scenario: Toggle fullscreen
- **WHEN** `set_window_fullscreen(True)` is called
- **THEN** the game requests fullscreen mode from the backend window

### Requirement: Open window
`Game` SHALL provide `open()` to create and show the game window.

#### Scenario: Open game
- **WHEN** `Game().open()` is called in an environment with a display
- **THEN** a window is created with a canvas filling the whole window

### Requirement: Wait for close
`Game` SHALL provide `wait_close()` that blocks until the window close event is triggered.

#### Scenario: Keep static program open
- **WHEN** a program opens a window, draws one frame, and calls `game.wait_close()` at the end
- **THEN** the program keeps the window open until the user explicitly closes it

### Requirement: Close click state
`Game` SHALL provide `is_close_clicked()` indicating whether the window close button has been clicked.

#### Scenario: Detect close click
- **WHEN** the user clicks the window close button
- **THEN** `game.is_close_clicked()` returns true

### Requirement: Canvas dimensions
`Game` SHALL expose `window_size` as the current internal canvas dimensions.

#### Scenario: Read canvas dimensions
- **WHEN** the backend window is resized
- **THEN** `window_size` reflects the new canvas size

### Requirement: Clear and show canvas
`Game` SHALL provide `clear_canvas()` to clear the current viewport using the active fill mode and `show_canvas()` to present the drawn buffer and flush input events.

#### Scenario: Manual frame
- **WHEN** code calls `clear_canvas()`, draw methods, and `show_canvas()`
- **THEN** the drawn frame is presented to the window canvas

### Requirement: Manual frame loop
`show_canvas()` SHALL process backend window events and present the frame without requiring beginner code to call `pyglet.app.run()` or register event-loop callbacks.

#### Scenario: Manual animation loop
- **WHEN** beginner code repeatedly calls drawing methods and `show_canvas()` in a Python loop
- **THEN** the window remains responsive and frames are presented through that manual loop

### Requirement: Time helpers
`Game` SHALL provide `sleep(seconds)`, `get_time()`, `get_delta_time()`, and `get_fps(smoothness: float = 1)` for manual frame-by-frame animation.

#### Scenario: Read time helpers
- **WHEN** a beginner animation calls `game.get_time()` and `game.get_delta_time()`
- **THEN** both methods return numeric timing values managed by the game object

#### Scenario: Read smoothed FPS
- **WHEN** a beginner animation calls `game.get_fps()`
- **THEN** it returns frame rate averaged over the last `1` second by default

#### Scenario: Read FPS with custom smoothness
- **WHEN** `game.get_fps(0.5)` is called
- **THEN** it returns frame rate averaged over the last `0.5` seconds

#### Scenario: Sleep between frames
- **WHEN** `game.sleep(0.1)` is called
- **THEN** drawing code pauses for approximately that duration without requiring a separate timing import

### Requirement: Fill state
`Game` SHALL maintain hidden fill state selected by `set_fill_color(color)`, `set_fill_texture(image, start_position: Point = Point(0, 0), size: Size = image.original_size, rotation: Rotation = Rotation(0), repeat: bool = True)`, or `set_fill_shader(shader, start_position: Point = Point(0, 0), size: Size = game.window_size, rotation: Rotation = Rotation(0), repeat: bool = True)`.

#### Scenario: Fill mode changes
- **WHEN** `set_fill_texture(image, start_position=Point(0, 0), size=Size(100, 100), rotation=Rotation(30), repeat=True)` is called
- **THEN** subsequent fill-capable drawing uses the texture fill mode until another fill setter is called

#### Scenario: Fill defaults
- **WHEN** `set_fill_texture(image)` is called
- **THEN** the fill starts at `Point(0, 0)` and uses `image.original_size`
- **WHEN** `set_fill_shader(shader)` is called
- **THEN** the fill starts at `Point(0, 0)` and uses `game.window_size`

#### Scenario: Fill size is dimensions
- **WHEN** `set_fill_shader(shader, start_position=Point(10, 20), size=Size(100, 50), rotation=Rotation(0), repeat=True)` is called
- **THEN** the fill area is interpreted as x `10..110` and y `20..70`

#### Scenario: Repeating fills tile
- **WHEN** texture or shader fill is active with `repeat=True`
- **THEN** the fill pattern tiles across the canvas from the start position using the requested size as one tile
- **WHEN** texture or shader fill is active with `repeat=False`
- **THEN** the fill is limited to one requested fill area

### Requirement: Stroke state
`Game` SHALL provide `set_stroke_color(color)`, `set_stroke_width(width: float)`, and `set_stroke_style(params)` for outline drawing.

#### Scenario: Stroke mode changes
- **WHEN** stroke color, width, and style are set
- **THEN** subsequent stroke-capable drawing uses that stroke state

