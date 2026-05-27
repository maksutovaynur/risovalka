## Why

`risovalka.gamekit` currently has only package scaffolding, but the course needs a concrete MVP engine before samples, tools, and sessions can rely on a stable API. The MVP should expose one approachable `Game` class while using a graphics backend that is efficient enough for textures and shaders without making the teaching code complex.

## What Changes

- Select `pyglet` as the underlying windowing, input, image, OpenGL, and shader-capable rendering backend for the MVP.
- Add the `risovalka.gamekit.Game` class as the single public entry point for beginner-facing engine operations.
- Add `risovalka.gamekit.game` as a default singleton game object for simple student programs.
- Add window management APIs for title, window size, fullscreen, opening a window, close waiting, close-click detection, and current canvas dimensions.
- Add drawing state APIs for fill color, fill texture, fill shader, stroke color, stroke width, and stroke style.
- Add drawing APIs for basic geometry, polylines, images, and sprites.
- Add color parsing helpers and small mutable tuple-like data types such as `Color`, `Point`, `Size`, and `Rotation`.
- Add `Image`, `Sprite`, and `Shader` asset wrappers.
- Add `geometry_tools` helpers for generated and transformed points/polygons.
- Add keyboard, mouse button, mouse position, mouse scroll, and close-click input APIs.
- Add `Object` as a convenient dynamic variable container.
- Keep object-style drawing out of the core `Game` API; reserve it for `risovalka.gamekit.secret_tools.draw_object(game, object)` via duck typing.
- Exclude physics/collision processing from this MVP.

## Capabilities

### New Capabilities
- `gamekit-backend`: Defines the chosen graphics/windowing backend and its dependency expectations.
- `gamekit-game-api`: Defines the `Game` class, window lifecycle, canvas dimensions, and drawing state behavior.
- `gamekit-drawing`: Defines geometry, line, image/sprite, transform, anchor, texture fill, and shader fill drawing behavior.
- `gamekit-assets`: Defines image, sprite, shader, color, point, and size asset/data wrappers.
- `gamekit-geometry-tools`: Defines helper functions for generated and transformed points/polygons.
- `gamekit-input`: Defines keyboard, mouse button, mouse position, and mouse scroll state behavior.
- `gamekit-object-model`: Defines `Object` helper behavior for grouping arbitrary variables and the optional secret-tools object drawing convention.

### Modified Capabilities

None.

## Impact

- Affected package: `risovalka.gamekit`.
- Affected dependencies: add a lightweight graphics dependency, expected to be `pyglet`.
- Affected teaching surface: examples can import `Game`, `Point`, `Size`, `Color`, `Object`, and related wrappers from `risovalka.gamekit`.
- Deferred systems: physics, collision processing, camera, audio, and advanced effects remain outside this MVP unless needed internally for rendering.
