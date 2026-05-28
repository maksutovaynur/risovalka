#version 330

// Simple fragment shader for a water-like background.
// Uniforms expected by gamekit: time.

uniform float time;
in vec2 uv;
out vec4 fragColor;

void main() {
    vec2 tiled_uv = fract(uv);
    float wave_x = sin((tiled_uv.x * 6.2831853 * 3.0) + time * 2.0) * 0.05;
    float wave_y = sin((tiled_uv.y * 6.2831853 * 4.0) - time * 1.5) * 0.04;
    float wave = wave_x + wave_y;
    vec3 deep = vec3(0.02, 0.12, 0.28);
    vec3 light = vec3(0.08, 0.55, 0.85);
    float vertical_band = 0.5 + sin(tiled_uv.y * 6.2831853) * 0.5;
    float mix_value = clamp(vertical_band + wave, 0.0, 1.0);
    fragColor = vec4(mix(deep, light, mix_value), 1.0);
}
