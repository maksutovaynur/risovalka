## Context

`risovalka/samples/mvp_gamekit.py` currently uses window coordinates as the only coordinate system. The hero position changes directly when the player presses arrow keys, enemies spawn around the visible window, bullets target the mouse position in that same screen space, and the shader background is drawn with a fixed canvas fill.

To support an infinite game field, the sample needs a simple camera model without changing the beginner-facing gamekit APIs. The most readable approach is to keep gameplay objects in world coordinates and convert to screen coordinates when reading pointer targets or drawing objects.

## Goals / Non-Goals

**Goals:**
- Keep the hero visually centered in the window during active play.
- Move the world/camera in response to player movement input.
- Preserve existing gameplay: enemy pursuit, shooting toward the mouse, bullet/enemy collision, hero collision, spark/explosion effects, score, and HUD.
- Keep the sample approachable as a single-file MVP example.

**Non-Goals:**
- Add a reusable camera API to `risovalka.gamekit`.
- Add map boundaries, terrain streaming, chunk persistence, or procedural world content.
- Change asset loading, window management, or input APIs.
- Change the game-over restart flow.

## Decisions

### Use world coordinates for simulation

The world stores `hero.position`, enemy positions, bullet positions, sparks, and explosions in world coordinates. Movement changes `hero.position` in world space as before, but drawing places the hero at the current screen center by translating world positions through the camera.

Alternative considered: keep hero world position fixed and move every other object when input occurs. That makes the visual requirement direct, but it couples input to every entity list and increases the chance of missing bullets or timed effects. A camera transform keeps entity motion local to each entity update.

### Derive camera offset from hero position and screen center

Each frame computes the screen center from `game.window_size` and maps `hero.position` to that center. A helper such as `world_to_screen(world, point)` returns `point - camera_position + screen_center`, where `camera_position` is the hero position for the MVP.

Alternative considered: store mutable `camera.position` separately from the hero. That is more flexible for camera smoothing, but unnecessary for the requested static-centered player and adds another state object for beginners to track.

### Convert mouse targets into world coordinates before shooting

The mouse remains a screen-space input. Shooting converts the current mouse point into a world target before creating a bullet, so bullet velocity and collision checks stay in world coordinates.

Alternative considered: keep bullets in screen coordinates. That would complicate collisions because enemies are naturally in world coordinates after the camera change.

### Spawn enemies around the camera viewport in world coordinates

Enemy spawn positions are generated around the visible viewport, then converted into world coordinates using the current camera. This applies to both initial enemies and later spawned enemies, preserving the current feel of enemies entering from off-screen while allowing the hero to travel indefinitely.

Alternative considered: spawn enemies at absolute world ranges around the hero. That is similar, but expressing the spawn ring through the viewport makes the existing sample behavior easier to preserve.

### Scroll the shader background via fill origin

The background shader should visually move when the hero moves. The sample can set the shader fill start position from the negative camera offset or another camera-derived value before clearing the canvas.

Alternative considered: add shader-specific uniform support for camera coordinates. The current sample already uses fill state and a time uniform, so changing the fill origin keeps the change local.

## Risks / Trade-offs

- Mouse/world conversion mistakes -> Add focused helpers for `world_to_screen` and `screen_to_world`, and use them consistently at draw and input boundaries.
- Rendering conversion mutates gameplay state -> Keep conversion helpers pure and pass converted screen positions into drawing routines instead of overwriting entity world positions.
- Off-screen lifetime checks may remove bullets too early after movement -> Evaluate bullet lifetime by age and distance from camera viewport rather than fixed absolute window bounds.
- Window resizing can shift the center -> Compute screen center from `game.window_size` each frame instead of caching it once.
- Background scrolling may depend on shader fill semantics -> Keep the background update isolated so the gameplay remains correct even if the visual offset needs adjustment.
