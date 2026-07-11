## Why

The current `mvp_gamekit.py` sample keeps the hero, enemies, bullets, effects, and background in screen coordinates, so the playable space is bounded by the window. An infinite-field sample should teach the common game pattern where the player stays fixed at screen center while movement scrolls the world around them.

## What Changes

- Add an infinite game field behavior to `risovalka/samples/mvp_gamekit.py`.
- Keep the player visually static at the center of the screen during normal gameplay.
- Convert movement so arrow keys shift world/camera coordinates instead of moving the player sprite away from center.
- Render the shader background, enemies, bullets, spark trail, and explosions relative to the shifted world.
- Keep mouse aiming, shooting, enemy pursuit, collisions, scoring, and HUD behavior coherent after introducing the world-to-screen transform.
- No breaking changes to public `risovalka.gamekit` APIs.

## Capabilities

### New Capabilities
- `mvp-infinite-field`: Defines the gameplay behavior for an infinite-field `mvp_gamekit.py` sample with a centered player and movable world/background.

### Modified Capabilities
- None.

## Impact

- Affects `risovalka/samples/mvp_gamekit.py`.
- May add focused sample tests in `tests/test_samples.py` if existing test patterns support importing or static validation of the sample.
- Does not require new dependencies or changes to core gamekit drawing, input, geometry, asset, or backend APIs.
