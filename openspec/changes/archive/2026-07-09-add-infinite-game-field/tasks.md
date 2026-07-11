## 1. Coordinate Model

- [x] 1.1 Add helper functions in `risovalka/samples/mvp_gamekit.py` for current screen center, world-to-screen conversion, screen-to-world conversion, and camera-relative viewport bounds.
- [x] 1.2 Keep gameplay state positions in world coordinates and derive the camera from `world.hero.position` each frame.
- [x] 1.3 Initialize the hero in world coordinates while ensuring first-frame rendering places the hero at the current window center.

## 2. Gameplay Updates

- [x] 2.1 Convert the current mouse screen position into `world.mouse_world` before shooting.
- [x] 2.2 Update bullet creation to aim from the hero world position toward the mouse world target.
- [x] 2.3 Update initial and timed enemy spawning to choose positions just outside the current camera viewport in world coordinates.
- [x] 2.4 Update bullet cleanup so bullets are retained by age and camera-relative visibility instead of original absolute screen bounds.
- [x] 2.5 Verify enemy pursuit, bullet collision, hero collision, sparks, and explosions continue to use world positions consistently.

## 3. Rendering Updates

- [x] 3.1 Apply a camera-derived shader fill origin so the background scrolls when the hero moves.
- [x] 3.2 Convert enemies, bullets, spark trail entries, and explosions from world to screen positions before drawing.
- [x] 3.3 Draw the hero at the current screen center while preserving texture rotation around the visible hero center.
- [x] 3.4 Keep the cursor and HUD in screen coordinates.
- [x] 3.5 Ensure game-over text remains screen-positioned and not affected by camera movement.
- [x] 3.6 Ensure drawing uses converted screen positions without mutating stored world positions.

## 4. Verification

- [x] 4.1 Update `tests/test_samples.py` fake-game assertions for the new shader fill arguments and centered hero rendering behavior.
- [x] 4.2 Add or update focused tests for world/screen conversion helpers, mouse-to-world shooting behavior, initial camera-relative enemy spawning, and non-mutating drawing conversion if they can be imported without opening a real window.
- [x] 4.3 Run the relevant sample tests and OpenSpec validation for `add-infinite-game-field`.
- [x] 4.4 Manually run `risovalka/samples/mvp_gamekit.py` when a display is available and confirm the hero stays centered while the background and objects move.
