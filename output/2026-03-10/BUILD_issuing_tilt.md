# issuing × tilt

## Build Log

### 16:15 — Start
Words drawn: **issuing** and **tilt**

### 16:16 — Initial concept
Physics toy: particles issue from a central source, gravity shifts with device tilt/pointer. Four colored vessels at the bottom to catch matching particles. 45-second rounds.

### 16:18 — First working version
Canvas-based particle sim with tilt input (deviceorientation + pointer fallback), vessel collision, scoring, trails, burst mode every ~10s. Intro screen, end card with breakdown.

### 16:19 — Color theme change
Switched from dark neon to warm organic tones — cream background, olive/earth/rust particle types.

### 16:24 — Gameplay juice
Combo system, screen shake, floating score text, shaped particles (diamond/circle/triangle/square).

### 16:27 — First version polish
Burst waves, trails, vessel fill visualization, progression rating.

### 16:36 — First version shipped (21 min)

---

### 17:00 — Round 2: Agency overhaul
Feedback: "it's a deluge of particles so it doesn't feel like the user has much control." Total rewrite of game logic.

### 17:04 — Wave system
Replaced continuous particle stream with **wave-based spawning**. Each wave issues 2-5 particles of ONE color. Player knows exactly where to aim. Between waves: 1.2s pause to breathe and prepare.

### 17:08 — Spatial design
Vessels spread asymmetrically across lower screen — far left/right at different heights vs center-left/right lower. Direction is now the core decision: left vs right, high vs low.

### 17:10 — No more walls
Removed wall bouncing. Particles that leave the screen are **lost forever**. Forces precision over chaos. Added edge glow warning (red vignette) when particles approach boundaries.

### 17:13 — Visual feedback layer
- Catch ripples (concentric rings on correct catch)
- Sparkle bursts on catch
- Pulsing warning ring on particles near edge
- Speed-responsive trail thickness
- Last particle in wave gets a brighter glow + pulsing ring

### 17:16 — Difficulty curve
- Wave 1-4: 2 particles (steady)
- Wave 5-8: 2-3 particles (rising)
- Wave 9-12: 3-4 particles (surge)
- Wave 13+: 3-5 particles
- After wave 6: 35% chance of **mixed wave** (2 colors at once)
- Phase labels in wave indicator: steady → rising → surge

### 17:19 — Feel tuning
- Nonlinear tilt response curve (power 1.4) — gentle for small inputs, dramatic for large
- Smooth tilt interpolation with slight lag for analog feel
- Gentle attraction toward correct vessel when particle is within 2.5x radius (prevents frustrating "almost" misses)
- Catch zone indicator (dashed circle) appears on active vessel

### 17:22 — Information design
- Source morphs into the shape of the current wave color
- Spawn count dots orbit source showing remaining particles to spawn
- Between-wave preview: dashed line from source to next target vessel
- Next vessel pulses during pause so you can prepare
- Gravity flow field (tiny directional strokes across canvas)
- Tilt crosshair indicator at bottom center

### 17:26 — Perfect wave mechanic
Catch all particles in a wave = PERFECT WAVE bonus (25 × particle count). Big sparkle burst, score multiplied. Creates real tension on the last particle — which is visually emphasized.

### 17:30 — Bug fixes & polish
- Vessel fill preserved on window resize
- Cleaned up unused variables
- Fixed early-return save/restore in draw loop
- Proper reset of all wave/combo/mixed state between games
- Extended timer to 60 seconds for slower pacing

## Summary

**What it is:** A 60-second tilt game where colored particles issue from a source in deliberate waves. Each wave is one color (or two in late game). You tilt to steer gravity and guide particles into matching vessels spread across the screen. Waves get bigger and more complex as time progresses.

**What changed in round 2:** Replaced chaotic particle deluge with intentional wave-by-wave pacing. Every tilt is now a decision — which direction, how hard, when to correct. The game previews each wave so you can prepare. Particles that escape are permanently lost, making precision matter. Perfect wave bonuses reward clean play.

**What it isn't:** Not random anymore. Not a screensaver with a score counter. It's a skill toy where you feel the weight of gravity shifting under your fingertips.
