---
published: true
title: "Hacking Starry Night: An AI Co-pilot"
tags:
  - reflection
  - interface
description: "A deep dive into building a computer vision co-pilot to solve a 2,000-piece Van Gogh puzzle, exploring the intersection of human intuition and machine pattern matching."
---

![[Pasted image 20260211125423.png]]


* system went OOM while analysing Google Art Project export of Starry Night
* Reference data is generated and the server is working. I can also see it already analyzed pieces (Row 22 Col 9 at 29% and Row 35 Col 16 at 22.4%). Those confidence levels are low, which is expected since we're matching the whole photo (including the wooden table) rather than just the piece.

Now let me build the piece extraction system. Here's my approach:

**Piece Extraction Strategy:**

- The background is a warm wooden table (high R, medium G, low B — brown/beige tones)
- The puzzle piece has Van Gogh colors (blues, greens, yellows — very different from wood)
- Use color-distance from the dominant background color to create a mask
- Clean up the mask with morphological operations (erosion/dilation)

---
# Hacking Starry Night: Building an AI Co-Pilot for a 2,000-Piece Puzzle

> *This project is part of my "eBrain" series — experiments where I build tools that augment human cognition through code. Not to replace the human, but to make the human better.*

---

`[IMAGE: Hero shot — the puzzle box next to the scattered 2,000 pieces on the dining table]`

## Attempt #3

My wife and I have owned this 2,000-piece Van Gogh *Starry Night* puzzle for over **8 years**.

We've attempted it twice before. Both times, we gave up. Not because we lacked patience — we're stubborn people — but because the puzzle is genuinely, unfairly hard. Two thousand impressionist brush strokes, 80% of which are some shade of turbulent blue.

But this time is different. This time, I've decided: **we are finishing this puzzle.**

If I could hire a professional puzzle solver on UrbanCompany (India's TaskRabbit), I would. Since that's not a service that exists (yet), I decided to build the next best thing.

This time, ~~cheating~~ *collaboration with AI* is not just allowed — it's the strategy.

`[IMAGE: Close-up of two nearly identical blue pieces side by side]`

---

## Why Starry Night Is Brutal

If you've never attempted a Van Gogh puzzle, let me explain why it's a special kind of torture.

Most puzzles have obvious "regions" — a blue sky, green trees, a red barn. You sort by color, and you're halfway done. *Starry Night* doesn't give you that luxury. The entire painting is a continuous flow of swirling gradients. There are no sharp boundaries. Every piece bleeds into the next.

### My Human Strategy

After two failed attempts, I had developed an intuition: **brush strokes matter more than color.**

If I stared at the reference poster for 1-2 minutes while holding a piece, I could sometimes sense where it belonged — not by matching the blue (everything is blue), but by reading the *direction* and *texture* of Van Gogh's brush work. Pieces with distinct white highlights (the stars, the moon) were easiest. The dark village silhouette at the bottom was manageable. But the sky — that massive, swirling, undifferentiated sky — was where pieces went to die.

`[IMAGE: You holding a piece up next to the reference poster, "staring" at it]`

This realization changed everything: **my brain was doing pattern matching on texture and flow, not exact color matching.** That is precisely what computer vision excels at.

I didn't need an AI that could "see" the puzzle. I needed one that could "stare" better than me.

---

## The Decision: Two Projects, Not One

I could have hacked together a script that worked for this specific puzzle. But I'm an engineer, and engineers generalize.

I built two distinct projects:

### `kaaroPuzzle` — The Engine

A generalized backend service that handles:

- Image upload and preprocessing

- Feature extraction (color histograms, edge gradients, texture frequency)

- Probabilistic matching against a reference image

- Heatmap generation showing likely placement locations

It knows nothing about Van Gogh. It only knows about *textures, colors, and probabilities.*

### `kaaroVanGogh` — The Instance

The specific configuration for our puzzle:

- The high-resolution reference image of *Starry Night*

- Tuned parameters for impressionist textures (high variance, low edge contrast)

- The 2,000-piece grid mapping

- Our progress state (which pieces we've placed so far)

By separating engine from instance, I ensured two things:

1. The core logic is reusable (next puzzle: Monet's Water Lilies, maybe?)

2. The messy, puzzle-specific tuning doesn't pollute the clean architecture

`[IMAGE: Screenshot of the two project folders side by side in VS Code]`

---

## The Hard Part: Real-World Chaos

Here's what tutorials never tell you about computer vision: **the algorithms are the easy part. The real world is the hard part.**

When you snap a photo of a puzzle piece sitting on your dining table:

| Challenge | Reality |

|---|---|

| **Lighting** | Your table lamp casts a warm shadow on the left half of the piece |

| **Rotation** | The piece is upside-down because you just grabbed it from a pile |

| **Perspective** | You're holding your phone at a 30° angle, not perfectly flat |

| **Background** | The wooden table bleeds into the brown border of the piece |

| **Scale** | The piece in your photo is 400x400 pixels; the reference image region is 12x12 pixels |

Standard template matching — the kind where you slide a small image over a big image looking for an exact pixel match — fails 100% of the time in these conditions.

`[IMAGE: Side-by-side — a photo of a piece (messy, rotated, warm lighting) vs. the "ideal" crop from the reference image]`

---

## The Solution: Probabilistic Matching (Digital Staring)

Instead of asking "where does this piece *exactly* match?", `kaaroPuzzle` asks: **"where does this piece *most likely* belong?"**

The engine mimics my own staring strategy, but at machine speed:

```

PIECE IMAGE

↓

┌─────────────────────┐

│ Feature Extraction │ → Dominant colors, brush stroke direction,

│ │ edge density, texture frequency

└─────────────────────┘

↓

┌─────────────────────┐

│ Reference Scan │ → Sliding window over the high-res

│ │ original painting

└─────────────────────┘

↓

┌─────────────────────┐

│ Probability Scoring │ → For each window position, calculate

│ │ a "Feature Distance Vector"

└─────────────────────┘

↓

┌─────────────────────┐

│ Heatmap Output │ → Top 3 candidate regions with

│ │ confidence percentages

└─────────────────────┘

```

The **Feature Distance Vector** combines three signals:

1. **Color Histogram Distance** — Is this region the right shade of blue?

2. **Edge Density Match** — Is the turbulence level similar? (Calm field vs. raging sky)

3. **Gradient Orientation** — Do the brush strokes flow in the same direction?

The magic is in the *weighting*. For Van Gogh, gradient orientation (brush direction) gets 3x the weight of color — because that's exactly how my own brain solves it. The "staring" insight translated directly into the algorithm.

`[IMAGE: Screenshot of the heatmap output — the Starry Night image with colored probability overlay]`

---

## The Stack

Everything is optimized for one constraint: **one-handed use on a phone, while the other hand holds a puzzle piece.**

| Layer | Tech | Why |

|---|---|---|

| **Frontend** | React + Vite | Fast hot-reload during development, mobile-first PWA |

| **Backend** | Node.js + Express | Lightweight, handles file uploads and API orchestration |

| **AI/CV** | Google Cloud Vision + Gemini | Robust feature extraction that handles lighting variance |

| **Data** | File-based JSON store | No database overhead — puzzle state is just a JSON file |

| **Network** | Local WiFi | Phone and laptop on the same network; zero cloud latency |

`[IMAGE: Screenshot of the mobile UI showing the camera capture screen]`

---

## The Result: Flow State, Restored

Let me be clear: **the goal was never to have the AI solve the puzzle for me.**

If I wanted the answer, I could just look at the box. The joy of puzzling is the *hunt* — the satisfaction of finding where a piece goes. The frustration was in the *searching* — scanning 2,000 candidates with tired eyes.

KaaroPuzzle removes the searching but preserves the hunting. It says, "Try the bottom-left quadrant, near the church spire. 87% confidence." I still have to find the exact spot. I still get the *click* of the piece locking into place. But I'm no longer staring at an ocean of blue for 20 minutes per piece.

It's a co-pilot, not an autopilot.

`[IMAGE: The puzzle in progress — a section completed, with the app visible on the phone next to it]`

---

## What I Learned

Building for the physical world is humbling. I spend my days writing code that operates on clean data in predictable environments. This project forced me to deal with *noise* — optical noise, environmental noise, human noise. The algorithms that looked elegant on paper fell apart the first time a lamp cast a shadow.

But the deeper lesson is this: **the best tools don't replace human ability — they extend it.** My "staring strategy" was correct all along. The AI just stares faster.

Eight years. Three attempts. One AI co-pilot.

We're going to finish this puzzle.

---

*This project is open source. Check out the code on GitHub: [kaaro-puzzle →](link)*

*If you're working on something similar or just want to chat about applied CV, reach out — I'd love to hear what "impossible" problems you're engineering your way through.*

![[Pasted image 20260211144815.png]]

## Related
[[computeTheory]] · [[Moments per second - Rate of understanding]] · [[Interface Patterns and Ubiquitous Compute]]