# barnacle x relevant

## Build Log

### 15:25 — Start
Words drawn: **barnacle** and **relevant**

First thoughts: Barnacles attach permanently — they make an irreversible choice about where to live. Relevance is about what matters, what sticks, what's worth paying attention to. There's something here about curation, about choosing what to hold onto.

I'm going to build an interactive piece where you're underwater, and fragments of text drift past in the current. You choose what to attach to your rock. What you collect becomes your identity — your personal reef. The things you let drift away are gone forever.

Not a game. More like a meditative digital tide pool. A daily act of curation.

### 15:25 — First scaffold
Basic HTML structure: full-viewport underwater scene. Dark ocean gradient background. A rock formation at the bottom (SVG). Fragments drift horizontally through the water. Tap to catch and attach to your reef. Seeded RNG from today's date so everyone sees the same fragments in the same order.

64 poetic fragments written across 8 thematic pools: things that stick, sea & tide, relevance & meaning, memory & identity, small beauties, connections, time, textures of thought.

### 15:27 — Atmosphere pass
Added caustic light patterns that shift slowly at the water surface. Floating plankton particles that drift and fade. Three animated seaweed strands swaying in the current. Richer reef SVG with texture lines and tiny barnacle circles on the rock. End card now staggers item reveals with animation delays. Bubbles now rise from near the reef instead of random positions.

### 15:28 — Iterating on feel
Making fragments drift at more varied speeds. Ensuring 2-3 fragments visible simultaneously. Widening the reef attachment area so items don't pile up.

### 15:29 — Depth and current
Fragments now vary in size and opacity based on "depth" — some feel closer, some further away. Added horizontal current lines that drift across the screen, giving a sense of water flow. Fragments that you let pass get a subtle releasing glow as they approach the edge, making the act of letting go feel intentional rather than accidental.

Reef items now fan out in an arc instead of random clustering. Each item gets placed at an angle radiating from the center of the rock.

### 15:30 — Visual feedback + intro
Added ripple effect on catch — concentric ring expands from the tap point. Added intro veil that shows "barnacle x relevant" for 2.5s before fading, creating a moment of stillness before the current begins. Fragments now start 3.5s in.

### 15:31 — Ghosts of the missed
When a fragment drifts off screen without being caught, its text appears as a barely-visible ghost in the top-left corner. A record of everything you let pass. The ghost text is almost invisible (8% opacity) — you'd have to look for it. This creates a subtle tension: the things you didn't choose are still there, haunting the edges.

Also expanded the fragment pool to 82 entries. Added: "a promise you kept quietly", "the wrong train, the right city", "a place that no longer exists", etc. More fragments now on screen simultaneously (faster spawn rate).

Share text now uses 🪨 emoji and "kept:" / "kept nothing." framing.

### 15:32 — Living reef + counter dots
Attached items now sway gently in the current (CSS animation with randomized delay). Counter replaced text "3/7" with seven small dots that fill amber as you collect — more thematic, less intrusive.

### 15:33 — Tinted categories + depth
Fragments now have a barely-perceptible color tint based on their category: sea-related ones are slightly blue, memory-related warm amber, thought-related soft green, and neutral ones stay sand-colored. The tint is at 8% opacity — subconscious, not conscious. Combined with the depth-based size variation (13-17px), each fragment feels slightly unique as it drifts past.

82 fragments now tagged across 4 tint categories. The shuffled order means the tints never cluster predictably.

### 15:33 — Mobile + end state
Responsive breakpoints for small screens (400px) and larger screens (768px). Fragment sizes, attached items, and collection layout all scale.

### 15:34 — Ocean warming + contextual endings
The ocean background color subtly shifts warmer as you collect more items — HSL values rotate from cool deep blue toward slightly warmer tones. The transition is 2 seconds so it's imperceptible in the moment but noticeable over the full session.

End card heading changes based on how many you kept: "Bare Rock" (0), "Sparse Reef" (1-2), "Your Reef" (3-4), "Rich Reef" (5-6), "Full Reef" (7). Every collection count feels named and intentional.

### 15:35 — Catch feedback polish
Added settling sparkles — 4 tiny amber dots scatter from the catch point. Fragment now sinks downward when caught (translateY + scale) instead of shrinking in place. Ripple + sparkles + bubbles create a satisfying multi-layered catch moment.

Ghost text area now has max-height overflow hidden to prevent mobile layout issues.

### 15:36 — Tidal rhythm + depth layers
Fragments now arrive in WAVES instead of at regular intervals. Groups of 3-4 fragments arrive quickly (600-1400ms apart), then a longer pause (3.5-5.5s) before the next wave. This creates a breathing rhythm — a real tide.

Added background atmosphere fragments: single abstract words ("memory", "attachment", "choice", "tide") drift very slowly at 4% opacity. Completely untappable. Just atmosphere. The ocean feels alive and deep now.

Hint text breathes with a subtle opacity animation.

### 15:36 — End card reef art
End card now generates a miniature SVG reef visualization — barnacle circles on a rock, one per collected item. Each circle has a subtle inner detail ring. The sizes and positions are randomized but constrained. For the "Bare Rock" state (0 items), it's just the empty rock. Beautiful either way.

Share text now includes a visual reef line using 🪨 emoji and has a cleaner format.

### 15:37 — Wave numbering + fragment glow
Subtle "wave 2", "wave 3" indicators appear during pauses between waves, at 20% opacity, then fade. Fragments get a soft amber glow on hover (box-shadow). Added meta description and theme-color.

### 15:38 — Canvas caustics
Replaced the static CSS caustic gradient with a real-time canvas-based caustic simulation. 8 soft teal circles drift in Lissajous curves at low resolution (1/3 width, 1/6 height) for performance. At 6% opacity over the top half of the ocean, it creates a gentle, living light-through-water effect. The circles pulse in size over time.

Also added deep atmosphere text — abstract words ("memory", "attachment", "drift") at 4% opacity drifting very slowly across the background. Untappable. Just ambiance.

### 15:39 — End card: "what drifted past"
Added a toggleable section on the end card that reveals everything you let pass, each word appearing with a staggered 50ms delay in teal at 30% opacity. The missed fragments have a spectral quality — present but faded.

Wave transitions now briefly brighten the caustics (6% → 10% → 6% over 1.5s) as a new wave arrives, creating a subtle light-breathing effect.

End card now fades the ocean elements to 30% before revealing itself, creating a soft transition. Added "stats" line: "3 kept · 21 released".

### 15:40 — Bug fixes
Removed unused variable. Fixed CSS animation vs. inline style conflict on hint (animation was overriding opacity: 0). Now uses class toggle + !important.

### 15:40 — Vignette + final atmosphere
Added dark vignette (radial gradient, 40% opacity at edges) to frame the underwater scene. Occasional tiny fish silhouette (♩ character at 6% opacity) drifts across the background on a ~15-20s interval with a wobbling sine wave for movement.

### 15:41 — Haptics + end state polish + bug fixes
Added `navigator.vibrate(15)` for a micro-pulse on mobile when catching fragments. Canvas caustics now stop animating when session ends (saves battery/CPU).

The "nothing" end state now shows three poetic lines instead of one: "you let everything pass", "the rock remains", "waiting for tomorrow's tide" — making the empty reef feel intentional and contemplative.

Intro veil now also shows the date (2026-03-10) with a delayed fade-in.

### 15:42 — Typography by category
Memory-category fragments now render in italics. Thought-category fragments get 0.5px letter-spacing. Combined with the size and tint variations, each fragment now has a unique visual fingerprint based on its emotional register.

### 15:42 — Water surface + reef art detail
Animated SVG water surface line at the top (gently undulating sine wave at 20% opacity). Reef art SVG now has center dots and small seaweed sprigs. Double ripple effect on catch (two concentric rings with staggered delay).

### 15:43 — Persistence + empty state
LocalStorage saves your collection after completing. Refreshing shows the end card with your reef instead of replaying. Key: `barnacle-2026-03-10`. "Release your reef" button clears localStorage and reloads.

The "Bare Rock" empty state now shows three poetic lines that cascade in: "you let everything pass" → "the rock remains" → "waiting for tomorrow's tide".

### 15:44 — Reflective prompts + save state fix
Between waves, a brief italic question fades in at 15% opacity: "what are you looking for?", "does it matter?", "what would you keep forever?", etc. They create a reflective pause between the action waves.

Fixed saved-state flow — when loading from localStorage, renders the end card directly without trying to call endSession (which depends on live game state).

88 fragments total now. Added: "the view from a bridge", "permission you gave yourself", "a recipe you know by heart", "the last bus home", "sunlight on a closed eyelid", "the version of you they remember", "what you'd save in a fire".

### 15:45 — Performance + accessibility
Animation loop and caustics canvas stop when session ends. Added `prefers-reduced-motion` media query that disables all animations.

### 15:46 — Ocean warming fix + reef breathing
Replaced the CSS `background` transition (which doesn't work with gradients) with a separate amber radial gradient overlay that fades in via opacity. Now the ocean genuinely warms as you collect more.

Reef SVG now breathes with a 6-second opacity pulse (1 → 0.85 → 1). Subtle but it makes the rock feel alive even when empty.

### 15:47 — Bug fix + refactor
Found a missing closing brace in the seaweed sprigs generation. Fixed. Also fixed the animation loop — it now continues until all active fragments clear the screen instead of stopping immediately when ended flag is set.

### 15:48 — Reef art refactor
Extracted reef art SVG generation into `generateReefArt()` function. Now used by both the live endSession path and the localStorage saved-state path. Previously, refreshing after completion showed the end card but without the reef art.

Added "release your reef" button at 15% opacity — lets you clear localStorage and replay. Text shadow on fragments for better readability against caustic light. End card shows "barnacle x relevant" in tiny uppercase at the bottom.

### 15:49 — Film grain + vignette separation
Added SVG-based film grain texture overlay at 4% opacity with overlay blend mode, giving the whole scene a subtle analog quality. Separated from the vignette (which remains at z-index 8).

### 15:55 — Final polish
Last pass: verified all code paths, cleaned up edge cases. Final file: ~1370 lines of self-contained HTML/CSS/JS.

**What it is:** An interactive underwater meditation on attachment and relevance. 88 poetic fragments drift through an ocean in 7 tidal waves. You tap to catch what resonates — up to 7 pieces that cement to your reef. What you let drift is recorded as ghosts. The ocean warms as you collect. At the end, you see your reef: "Bare Rock" to "Full Reef", with a miniature SVG visualization, a "what drifted past" toggle, and a shareable text format.

**What it isn't:** A game. There's no score, no win condition, no right answers. Just choices.

---

*Built in 30 minutes from the words "barnacle" and "relevant". March 10, 2026.*
