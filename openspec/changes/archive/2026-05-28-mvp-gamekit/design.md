## Context

`risovalka.gamekit` is currently a placeholder package. The course concept requires a beginner-friendly Python game library that is close to PyGame in spirit, but simpler and more pedagogically controlled. The requested MVP needs efficient 2D drawing, image/texture rendering, shader headroom, easy window management, and a single beginner-facing `Game` class.

The backend choice matters because it will shape the whole engine. Official `pyglet` documentation describes it as a cross-platform windowing and multimedia library for games and visually rich applications, with window event handling, OpenGL graphics, image loading, and audio/video support. Its window module creates windows with OpenGL contexts, and its rendering docs expose shader program support. This fits the MVP better than a CPU-first drawing stack.

## Goals / Non-Goals

**Goals:**
- Choose a lightweight graphics/window/input backend.
- Implement the first usable `risovalka.gamekit` MVP around `Game`.
- Support window lifecycle, drawing state, basic geometry, images, sprites, texture fills, shader fills, and input.
- Use explicit manual frame-by-frame drawing through `clear_canvas()` and `show_canvas()` as the required beginner model.
- Provide simple time helpers for manual animation: `sleep()`, `get_time()`, and `get_delta_time()`.
- Use top-left canvas coordinates for the public API.
- Keep advanced concepts (`Shader`, texture fills, shader fills, and secret object drawing helpers) available but optional.
- Keep student-facing API names simple enough for course examples.

**Non-Goals:**
- Do not implement physics or collision processing in this change.
- Do not build a scene graph, ECS, editor, or visual constructor.
- Do not expose backend objects as the primary teaching API.
- Do not add `Drawable`, concrete drawable shape classes, or `Game.draw_object()` to the MVP core API.
- Do not implement full asset pipelines, audio, camera, tile maps, or effects.

## Decisions

1. Use `pyglet` as the MVP backend.
   - Rationale: `pyglet` provides cross-platform windows, event handling, OpenGL-backed graphics, image loading, and shader support in one dependency. It is lower-level than Arcade, but less dependency-heavy and better aligned with a custom educational API.
   - Alternative: Arcade. It offers a higher-level 2D game framework and modern graphics layer, but it would compete with `risovalka.gamekit` as the teaching abstraction.
   - Alternative: pygame-ce. It has approachable 2D APIs and window support, but shader/texture pipelines require a stronger OpenGL path and more custom integration.
   - Alternative: ModernGL plus a window helper. It is powerful for shaders, but too graphics-programming-focused for this beginner-facing MVP.

2. Keep `Game` as the only required beginner-facing class.
   - Rationale: students should learn one object first: `game`. Helper classes exist for values/assets, but normal examples should read as `game.draw_circle(...)`, `game.is_key_down(...)`, and `game.show_canvas()`.
   - Alternative: module-level functions. This is simpler at first, but makes multiple windows, state, and tests harder.

3. Use only explicit `draw_*` public drawing method names.
   - Rationale: the prefix makes drawing commands discoverable and keeps examples consistent. Object-style helpers can exist outside the core API in `secret_tools`, but there should be no short `circle()` method alias on `Game`.
   - Alternative: add aliases like `circle()` and `rectangle()`. This increases surface area and makes student materials less consistent.

4. Use a retained internal drawing state.
   - Rationale: `set_fill_color`, `set_stroke_color`, and similar calls are easy to teach. Explicit draw calls can use the current state without adding an object-drawing state model to MVP.
   - Alternative: require every draw call to pass all style parameters. That is explicit but noisy for children.

5. Use top-left public coordinates.
   - Rationale: `(0, 0)` at the top-left matches most beginner canvas mental models and common screen-coordinate explanations. Internally, the backend can convert to OpenGL coordinates.
   - Alternative: expose pyglet/OpenGL bottom-left coordinates. This reduces conversion code but is less intuitive for children.

6. Represent coordinates, sizes, and rotations with small mutable tuple-like value types.
   - Rationale: `Point(x, y)`, `Size(width, height)`, and `Rotation(angle, anchor)` make examples readable, allow per-property assignment such as `point.x = 10`, and still support indexed access like `point[0]`.
   - `Size` always means width and height, never a bottom-right point or end position.
   - Alternative: only accept tuples. Tuples are short but unclear in teaching materials.

7. Use wrapper asset classes for images, sprites, and shaders.
   - Rationale: wrappers hide backend details while preserving useful properties such as original size, current frame, and shader parameters.
   - Alternative: expose raw pyglet image/sprite/shader objects. This leaks backend concepts too early.

8. Shader loading accepts built-in shader names and shader file paths.
   - Rationale: built-ins make secret effects easy for curious students, while file paths let advanced students inspect and customize shader code later.
   - Alternative: raw GLSL strings only. This is flexible but too abrupt for an educational MVP.

9. `show_canvas()` drives manual frame processing.
   - Rationale: the course must start with explicit frame-by-frame drawing. `show_canvas()` should process backend events and present the frame without requiring students to call `pyglet.app.run()`. Students can later build their own event loop after understanding individual frames.
   - Alternative: require event callbacks. This is more idiomatic for GUI systems but too abstract for early lessons.

10. Add `sleep()`, `get_time()`, and `get_delta_time()` to `Game`.
   - Rationale: these helpers keep frame-by-frame animation teachable without forcing students to import timing utilities from elsewhere.
   - Alternative: use Python's `time` module directly in lessons. That works, but splits beginner attention away from the single `game` object.

11. Add close handling through `wait_close()` and `is_close_clicked()`.
   - Rationale: programs without a game loop need a simple way to keep the window open until the user explicitly closes it. Programs with a manual loop need a readable close-click check without overloading `show_canvas()` return values.
   - Alternative: make `show_canvas()` return open/closed state. This is compact, but it hides the close condition inside a rendering method and is less explicit for beginners.
   - Alternative: expose only `game.is_open`. This is readable, but the user specifically needs edge-style close-click detection.

12. Full texture and shader fills are part of MVP acceptance.
   - Rationale: texture and shader fills are important "secret" capabilities for curious students and should be available from the first MVP rather than deferred. MVP tasks are not complete until geometry, strokes, texture fills, and shader fills render visually correctly for the supported draw methods.
   - Alternative: ship only rectangle/full-canvas texture and shader fills first. This weakens the promised advanced headroom and leaves a visible gap in the drawing model.

13. MVP fill clipping requirements are shape-specific.
   - Rationale: polygon, rectangle, star, and regular-polygon texture/shader fills must clip correctly through generated OpenGL geometry. Circle fill clipping can be approximate in MVP, but must not block the feature.
   - Alternative: require perfect circle clipping in MVP. This raises implementation cost for a visual detail that is less important than making the secret fill modes available.

14. Hex alpha order is `#RRGGBBAA`.
   - Rationale: this matches the user's requested `#ffaadd00` interpretation and keeps RGB and RGBA hex formats as direct extensions of one another.
   - Alternative: `#AARRGGBB`, which is common in some platforms but less consistent with RGB-first notation.

15. Keep `Object` as a plain dynamic variable container; do not attach drawable state to it.
   - Rationale: mixing object variables with a separate drawable view creates ambiguity over which position, rotation, and style should win. The core engine should only draw through explicit `game.draw_*` methods.
   - Alternative: `Object` owns a `Drawable` or inherits from `Drawable`. Both approaches introduce hidden OOP/design concerns and conflict with the simple variable-container model.

16. Put object-style duck-typed drawing in `risovalka.gamekit.secret_tools`, not `Game`.
   - Rationale: curious students can discover or reimplement `draw_object(game, object)`, which interprets properties such as `shape`, `position`, `radius`, `rotation`, and calls explicit `game.draw_*` methods. This keeps the core API unambiguous while preserving an advanced secret path.
   - Alternative: `Game.draw_object(object)`. This makes object interpretation part of the core engine API and weakens the explicit drawing model.

17. Do not expose rotation on basic geometry draw methods.
   - Rationale: for circles, rectangles, polygons, and lines, rotation is best taught as explicit point geometry. This avoids a uniform-but-noisy parameter that is unnecessary for many shapes.
   - Alternative: every draw method accepts rotation and anchor. This is uniform but hides the point-transformation concept.

18. Move generated/rotated polygon helpers into `geometry_tools`.
   - Rationale: `geometry_tools.generate_star(...)`, `generate_regular_polygon(...)`, `rotate_point(...)`, `rotate_polygon(...)`, `move_polygon(...)`, and `scale_polygon(...)` make geometry explicit and useful beyond polygons later.
   - Alternative: keep `draw_star()` and `draw_regular_polygon()` on `Game`. This is convenient, but it hides the idea that these are just generated points passed to `draw_polygon()`.

19. Image and sprite drawing is texture-backed rectangle drawing.
   - Rationale: `Image` should only hold backend data and original size. `draw_image(image, position, size, rotation)` and `draw_sprite(sprite, position, size, rotation)` can temporarily set texture fill, draw a rotated rectangle using the rotation anchor, and restore the previous fill state.
   - Alternative: images own current width/height and resize state. This creates mutable asset state that is less clear than passing size at draw time.

## Risks / Trade-offs

- `pyglet` uses OpenGL, so old or restricted school computers may have driver issues -> Keep backend checks explicit and make failures understandable, but do not remove texture/shader MVP requirements.
- Shader support can pull students into advanced concepts too early -> Keep `load_shader` and `set_fill_shader` documented as advanced and optional.
- A rich `Game` class can become too large -> Split internal implementation across modules while re-exporting one coherent public class.
- Flexible argument forms can create ambiguity -> Normalize arguments through small parser helpers and test each accepted form.
- Top-left coordinates differ from backend coordinates -> Centralize coordinate conversion and cover it with tests or smoke checks.
- Removing rotation from geometry draw methods can surprise users expecting uniform transforms -> Provide `geometry_tools` helpers and document that geometry rotation is point transformation.
- Object-style drawing can blur the boundary between data and view -> Keep it out of the core `Game` API and place duck-typed interpretation in `secret_tools`.
- Headless CI may not support opening a real window -> Separate pure tests for color/data parsing from smoke tests that can be skipped when no display is available.

## Migration Plan

1. Add `pyglet` to runtime dependencies.
2. Implement `risovalka.gamekit` modules and exports.
3. Add focused unit tests for color parsing, value types, assets, sprite frame state, object/drawable behavior, and API signatures.
4. Add a minimal smoke sample that opens a window only when a display is available.
5. Keep existing course materials unchanged unless they reference a different gamekit API.

## Open Questions

- Exact stroke dash/dotted rendering fidelity can be minimal in the MVP if backend support requires custom geometry, but solid stroke rendering must work.
- Shader built-in names and exact starter shader collection can start small and expand later.
