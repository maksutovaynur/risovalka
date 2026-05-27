## 1. Backend and Package Setup

- [x] 1.1 Add `pyglet` as the runtime graphics/windowing dependency.
- [x] 1.2 Split `risovalka.gamekit` into focused internal modules while keeping public exports available from `risovalka.gamekit`.
- [x] 1.3 Export `Game`, `Color`, `Point`, `Size`, `Rotation`, `Image`, `Sprite`, `Shader`, `Object`, `geometry_tools`, `get_hex`, and `get_rgba` from `risovalka.gamekit`.
- [x] 1.4 Add `risovalka.gamekit.secret_tools` for optional advanced helpers that are not part of the core beginner API.
- [x] 1.5 Export `game` as a default singleton `Game` instance from `risovalka.gamekit`.

## 2. Core Data and Assets

- [x] 2.1 Implement mutable tuple-like `Point`, `Size`, and `Rotation` value types with named and indexed getter/setter access.
- [x] 2.2 Implement `Color`, named color support, RGB/RGBA hex parsing, `rgb()`/`rgba()` helpers or tuple support, `get_hex`, and `get_rgba`.
- [x] 2.3 Implement `Image` wrapper with only backend data and `original_size`.
- [x] 2.4 Implement `Sprite` wrapper as a list of images with `current_frame`, `frame_number`, `current_image`, `next_frame`, and `prev_frame`.
- [x] 2.5 Implement `Shader` wrapper with built-in shader names, shader file paths, and named parameter support.

## 3. Game Window and Frame Lifecycle

- [x] 3.1 Implement `Game` construction with default window settings, canvas size state, fill state, stroke state, and input state.
- [x] 3.2 Implement `set_window_title`, `set_window_size`, `set_window_fullscreen`, `open`, `wait_close`, `is_close_clicked`, and `window_size`.
- [x] 3.3 Implement `clear_canvas()` and `show_canvas()` with manual frame-by-frame event processing, buffer presentation, and input click/scroll flushing.
- [x] 3.4 Implement `sleep`, `get_time`, and `get_delta_time`.

## 4. Drawing State and Drawing API

- [x] 4.1 Implement `set_fill_color`, `set_fill_texture(image, start_position, size, rotation, repeat)`, `set_fill_shader(shader, start_position, size, rotation, repeat)`, `set_stroke_color`, `set_stroke_width`, and `set_stroke_style`.
- [x] 4.2 Implement draw argument normalization for top-left `Point`, `Size`, tuple-like inputs, lists, and variadic points without geometry rotation parameters.
- [x] 4.3 Implement explicit `draw_circle`, `draw_rectangle`, `draw_polygon`, and `draw_line` methods with no short shape aliases and no `draw_star`/`draw_regular_polygon`.
- [x] 4.4 Implement `draw_image(image, position, size, rotation)` and `draw_sprite(sprite, position, size, rotation)` as texture-backed rotated rectangle drawing that restores previous fill state.
- [x] 4.5 Implement texture and shader fill handling for all MVP fill-capable geometry shapes without color-fill fallbacks.
- [x] 4.6 Ensure polygon and rectangle texture/shader fills clip to shape geometry; circle clipping may be approximate in MVP.
- [x] 4.7 Implement `geometry_tools.rotate_point`, `generate_star`, `generate_regular_polygon`, `rotate_polygon`, `move_polygon`, and `scale_polygon`.

## 5. Object and Secret Helpers

- [x] 5.1 Implement `Object` as a plain dynamic dot-access container for arbitrary keyword attributes.
- [x] 5.2 Ensure `Object` has no drawable inheritance, no internal drawable view, and no special transform forwarding.
- [x] 5.3 Ensure `Game` does not expose `draw_object()`.
- [x] 5.4 Implement `risovalka.gamekit.secret_tools.draw_object(game, object)` as a duck-typed helper that delegates to explicit `Game.draw_*` methods.

## 6. Input API

- [x] 6.1 Implement keyboard pressed and clicked state tracking.
- [x] 6.2 Implement mouse button pressed and clicked state tracking for `left`, `right`, and `middle`.
- [x] 6.3 Implement `get_mouse_position()` and `get_mouse_scroll()`.
- [x] 6.4 Ensure `show_canvas()` flushes clicked and scroll delta state while preserving currently held keys/buttons.

## 7. Samples and Documentation

- [x] 7.1 Add a minimal `risovalka.samples` MVP example that opens a window, clears canvas, draws shapes, and reads input.
- [x] 7.1a Update the MVP sample to use `from risovalka.gamekit import game` instead of constructing `Game`.
- [x] 7.2 Add concise developer-facing comments only where backend or transform behavior is not self-explanatory.
- [x] 7.3 Keep any student-facing sample text in Russian.

## 8. Verification

- [x] 8.1 Add tests for color parsing, mutable tuple-like value types, asset wrappers, sprite frame transitions, geometry tools, `Object`, and `secret_tools.draw_object`.
- [x] 8.2 Add tests or smoke checks for import/export API availability.
- [x] 8.3 Add a display-gated smoke check for creating a `Game` window when a display is available.
- [x] 8.4 Verify no physics or collision processing is introduced in the MVP.
- [x] 8.5 Verify the public drawing API uses only explicit geometry draw methods without rotation parameters, public coordinates are top-left, RGBA hex uses `#RRGGBBAA`, timing helpers and close helpers exist, shader loading supports built-ins and file paths, and `Game.draw_object`/core drawable classes are absent.
- [x] 8.6 Run the project test suite and `openspec validate mvp-gamekit --strict`.
