## ADDED Requirements

### Requirement: Centered player viewport
The `mvp_gamekit.py` sample SHALL render the player at the current window center during active gameplay while representing player travel as world/camera movement.

#### Scenario: Player remains centered while moving
- **WHEN** the player holds a movement key during active gameplay
- **THEN** the player sprite is drawn at the window center instead of drifting toward the window edge

#### Scenario: Center follows window size
- **WHEN** the window size changes before or during gameplay
- **THEN** the player is drawn at the center derived from the current `game.window_size`

### Requirement: World-relative rendering
The `mvp_gamekit.py` sample SHALL draw background, enemies, bullets, sparks, and explosions relative to the camera so they appear to move around the centered player without replacing their stored world positions with screen positions.

#### Scenario: Background scrolls opposite movement
- **WHEN** the player moves through the world
- **THEN** the shader background visibly shifts relative to the screen

#### Scenario: Gameplay objects keep relative positions
- **WHEN** an enemy, bullet, spark, or explosion has a world position near the player
- **THEN** it is drawn at the corresponding screen position relative to the centered player

#### Scenario: Drawing preserves world positions
- **WHEN** the sample draws a frame with camera-relative positions
- **THEN** enemy, bullet, spark, and explosion world positions remain unchanged by drawing

### Requirement: World-space gameplay simulation
The `mvp_gamekit.py` sample SHALL keep movement, enemy pursuit, bullet travel, collision checks, and timed effects coherent in world coordinates.

#### Scenario: Enemies pursue player in infinite field
- **WHEN** enemies update while the player has moved away from the original screen area
- **THEN** enemies move toward the player's world position

#### Scenario: Bullet collision uses world positions
- **WHEN** a bullet intersects an enemy after the camera has moved
- **THEN** the enemy is removed and an explosion is created at the hit world position

#### Scenario: Hero collision uses world positions
- **WHEN** an enemy reaches the player's world position after the camera has moved
- **THEN** the game enters the game-over state

### Requirement: Screen input maps to world targets
The `mvp_gamekit.py` sample SHALL convert mouse screen positions into world positions before creating bullets.

#### Scenario: Shooting follows visible cursor
- **WHEN** the player clicks at a visible cursor position after moving through the world
- **THEN** new bullets travel from the centered player toward the corresponding world-space cursor target

### Requirement: Camera-relative enemy spawning and cleanup
The `mvp_gamekit.py` sample SHALL spawn and retain dynamic objects using the camera viewport rather than fixed absolute screen bounds.

#### Scenario: Initial enemies spawn outside visible viewport
- **WHEN** the world is created
- **THEN** initial enemies start just outside the current visible viewport in world coordinates

#### Scenario: Enemies spawn outside visible viewport
- **WHEN** a new enemy is created after the player has moved through the world
- **THEN** the enemy starts just outside the current visible viewport in world coordinates

#### Scenario: Bullets are not removed by original screen bounds
- **WHEN** the player has moved away from the original screen area and fires a bullet
- **THEN** the bullet remains alive based on age and camera-relative visibility rather than absolute `0..window_size` coordinates
