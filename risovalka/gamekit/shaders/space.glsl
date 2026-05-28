#version 330

// Simple fragment shader for a tiled animated star sky.
// Uniforms expected by gamekit: time.

uniform float time;
in vec2 uv;
out vec4 fragColor;

float hash(vec2 point) {
    return fract(sin(dot(point, vec2(127.1, 311.7))) * 43758.5453123);
}

void main() {
    vec2 tile_uv = fract(uv);
    vec2 star_grid = tile_uv * 18.0;
    vec2 cell = floor(star_grid);
    vec2 local = fract(star_grid) - 0.5;

    float seed = hash(cell);
    float star_size = mix(0.06, 0.16, seed);
    float star_core = smoothstep(star_size, 0.0, length(local));
    float sparkle = 0.65 + 0.35 * sin(time * 2.0 + seed * 6.2831853);
    float star = star_core * step(0.82, seed) * sparkle;

    vec3 top = vec3(0.01, 0.01, 0.06);
    vec3 bottom = vec3(0.02, 0.04, 0.16);
    vec3 sky = mix(top, bottom, tile_uv.y);
    vec3 color = sky + vec3(star);

    fragColor = vec4(color, 1.0);
}
