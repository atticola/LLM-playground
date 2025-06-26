# Prompt Engineering for Video Generation

This guide provides detailed techniques, patterns, and frameworks for crafting effective prompts for AI video generation. Unlike image generation, video prompts must account for temporal elements, motion, and narrative flow.

## Core Principles of Video Prompts

### 1. Spatial + Temporal Description

Video prompts need to describe both **what** appears and **how** it moves or changes over time.

| Element | Description | Example |
|---------|-------------|---------|
| Subject | What/who is in the scene | "A red fox" |
| Setting | Where the action takes place | "in a snowy forest" |
| Action | What the subject is doing | "running and leaping through deep snow" |
| Camera | How the scene is framed/viewed | "in slow motion, tracking shot" |
| Transition | How the scene evolves | "gradually transitioning from day to night" |

### 2. Level of Specificity

More detailed prompts generally produce more predictable results, but may limit creativity:

- **Low specificity**: "A cityscape at night"
- **Medium specificity**: "A cyberpunk city with neon signs and flying cars at night, raining"
- **High specificity**: "A detailed cyberpunk Tokyo cityscape at night with pink and blue neon signs reflecting on wet streets, holographic advertisements on skyscrapers, flying cars with red taillights, constant rain, shot on 70mm film, tracking shot moving through the street"

### 3. Balancing Control vs. Generation Quality

Overly controlling prompts can result in lower quality. Find the right balance:

- **Too vague**: "Beautiful scene"
- **Balanced**: "Sunset over mountains, golden light, cinematic wide shot"
- **Too constrained**: "Sunset over mountains with exactly three peaks, golden light hitting from precisely 30 degrees, with a pine tree on the left exactly 1/3 into the frame, cinematic 2.39:1 aspect ratio, no clouds, completely still camera..."

---

## Video Prompt Framework

### Basic Structure

```
[Style] [Subject] [Action] [Setting] [Atmosphere] [Camera Movement] [Technical Specifications]
```

### Expanded Structure

```
[Visual Style][Art direction] of [Subject][Subject details] [Action/Motion] in/on/at [Setting][Setting details], [Atmosphere][Lighting], [Camera specs][Camera movement], [Technical quality][Film type/Processing]
```

### Example Using Framework

```
Cinematic 8K footage of a lone astronaut [subject] slowly walking [action] across a red Martian landscape [setting] with dust swirling around their suit [atmosphere], shot with a drone slowly rising [camera movement], shallow depth of field, volumetric lighting [technical]
```

---

## Style Reference Techniques

### Director/Cinematographer References

| Reference Type | Example Prompt |
|----------------|----------------|
| Film Director | "In the style of Wes Anderson: symmetric composition, pastel colors..." |
| Cinematographer | "Cinematography like Roger Deakins: naturalistic lighting, strong silhouettes..." |
| Specific Film | "Visual style of Blade Runner 2049: neon lighting in fog, strong color contrast..." |
| Era | "1980s music video aesthetic: VHS quality, bright colors, synthesizer-inspired visuals..." |

### Visual Artist References

| Artist Type | Example Prompt |
|-------------|----------------|
| Painter | "In the style of Monet: impressionistic, soft colors, emphasis on light..." |
| Illustrator | "Style of Moebius: detailed line work, vibrant colors, strange perspectives..." |
| Photographer | "Like Annie Leibovitz portrait: dramatic lighting, emotional intensity..." |
| Studio | "Studio Ghibli aesthetic: whimsical natural settings, magical elements..." |

### Technical References

| Technical Aspect | Example Prompt |
|------------------|----------------|
| Camera | "Shot on ARRI Alexa with anamorphic lenses, shallow depth of field..." |
| Film Stock | "16mm film look with natural grain and slightly desaturated colors..." |
| Processing | "Technicolor process: vibrant, saturated colors with slight color separation..." |
| Time Period | "Early 1900s black and white footage, slightly sped up, scratchy film..." |

---

## Motion Control Techniques

### Camera Movement

| Movement Type | Description | Example Prompt |
|---------------|-------------|----------------|
| Static | No camera movement | "static shot of a flower blooming" |
| Pan | Camera rotates horizontally | "slow pan across the cityscape from left to right" |
| Tilt | Camera rotates vertically | "camera tilt from the forest floor up to the canopy" |
| Tracking | Camera follows subject | "tracking shot following the runner through the crowd" |
| Dolly | Camera moves toward/away | "slow dolly zoom in on the character's face" |
| Aerial/Drone | Bird's eye perspective | "aerial shot descending from above the mountains" |
| Handheld | Slightly unstable movement | "handheld documentary-style footage following the chef" |

### Subject Motion

| Motion Type | Description | Example Prompt |
|-------------|-------------|----------------|
| Slow Motion | Slowed down movement | "ballet dancer leaping in extreme slow motion" |
| Time-lapse | Sped up movement | "time-lapse of flower blooming over time" |
| Fluid | Smooth flowing movement | "fluid dance movements with ribbons trailing" |
| Mechanical | Precise, rigid movement | "robot walking with precise, mechanical movements" |
| Organic | Natural, living movement | "organic movement of seaweed underwater" |
| Chaotic | Unpredictable movement | "chaotic movement of particles in a storm" |
| Transformative | Changing form | "character smoothly transforming from human to wolf" |

---

## Advanced Prompt Techniques

### Scene Transitions

| Transition Type | Example Prompt |
|-----------------|----------------|
| Match Cut | "Office worker typing transforms into pianist playing, matching finger movements" |
| Dissolve | "Forest scene gradually dissolving into an ocean view" |
| Morphing | "Woman's face smoothly morphing into a tiger's face" |
| Time Shift | "Day to night transition over the same city street" |
| Environment Change | "Desert landscape slowly transitioning into an arctic scene" |

### Negative Prompting

Specifying what you DON'T want in video generation:

```
[Main prompt], no camera shake, no flickering, no distortion, consistent lighting
```

### Motion Specification

```
[Main subject] [motion type: fluid/robotic/natural] movement with [speed: slow/medium/fast] pace
```

### Time Manipulation

```
[Scene description] transitioning from [time of day/season/year] to [different time]
```

---

## Style-Specific Prompt Examples

### Cinematic/Film

```
Epic cinematic shot of a lone warrior standing on a cliff edge overlooking a vast battlefield, golden hour lighting, slow motion, helicopter shot circling around the character, shallow depth of field, shot on ARRI Alexa with anamorphic lenses, 2.39:1 aspect ratio
```

### Animation/Stylized

```
Stylized 3D animation of a cute robot exploring a colorful alien forest, Studio Ghibli inspired, vibrant colors, smooth movement, soft shadows, ambient occlusion, global illumination, whimsical atmosphere, following camera
```

### Music Video

```
Neon-soaked music video aesthetic, female dancer silhouette performing against urban backdrop, strobe lighting effects, quick cuts, glitch transitions, anamorphic lens flares, dramatic fog, synchronizing movement to beat
```

### Nature/Documentary

```
Breathtaking nature documentary footage of a jaguar stalking prey through Amazon rainforest, dappled light through canopy, 8K resolution, professional wildlife videography, telephoto lens, shallow depth of field, natural ambient lighting
```

### Surreal/Experimental

```
Surreal dreamlike sequence: ordinary objects floating and dissolving in a void, inspired by Salvador Dali, impossible physics, objects morphing into each other, shifting perspectives, ethereal atmosphere, dreamy soft focus
```

---

## Prompt Templates by Video Type

### Character Animation

```
[Character description] [performing action] in [setting], [animation style], [motion quality], [camera movement]

Example: A steampunk robot engineer fixing gears inside a giant clock tower, 3D animation style, fluid mechanical movements, slow camera dolly moving around the scene
```

### Scene Transformation

```
[Initial scene description] gradually transforming into [final scene description], [transition style], [mood/atmosphere], [camera position]

Example: Busy urban street gradually transforming into an overgrown post-apocalyptic version of itself, nature reclaiming the city, melancholic atmosphere, static wide shot
```

### Dynamic Action

```
[Subject] [performing dynamic action] in/on [environment], [speed modification], [camera technique], [visual style], [technical specifications]

Example: Martial artist performing elaborate kung fu sequence in ancient temple courtyard, alternating between slow motion and normal speed, circular tracking shot, cinematic lighting with light rays, shot on RED camera
```

### Ambient/Looping Scenes

```
Seamlessly looping [scene description], [subtle motion elements], [mood/atmosphere], [lighting condition], [visual style]

Example: Seamlessly looping cozy cafe scene with gentle steam rising from cups, soft rain hitting windows, warm amber lighting, shallow depth of field focusing on raindrops
```

---

## Tool-Specific Optimization

### Runway Gen-2

Runway Gen-2 often performs well with:
- Detailed cinematic descriptions
- Specific camera movements
- Film industry terminology
- Professional visual references

```
Example: Cinematic aerial shot descending through clouds to reveal a futuristic city on a floating island, volumetric god rays streaming through clouds, hyperrealistic detail, shot on RED camera with 8K resolution, inspired by Blade Runner 2049
```

### Pika Labs

Pika Labs excels with:
- Character-based prompts
- Clear action descriptions
- Style references
- Animation-related terminology

```
Example: Cute cartoon fox character excited jumping up and down in a forest clearing, 3D animation style, squash and stretch animation principles, bouncy movement, soft directional lighting, tracking shot, vibrant colors
```

### Stable Video Diffusion

SVD works well with:
- Simpler, clearer descriptions
- Less complex camera movements
- Careful attention to subject motion
- Image-like descriptions with motion added

```
Example: Close-up of a blooming red rose with dew drops, gentle movement, soft breeze, natural morning light, shallow depth of field, static camera
```

---

## Troubleshooting Common Video Prompt Issues

### Problem: Temporal Inconsistency (Flickering)

**Solution Prompts:**
- Add "consistent lighting throughout, no flickering"
- Use "static environment with only [subject] moving"
- Specify "stable camera" or "tripod shot"

### Problem: Subject Changes Appearance

**Solution Prompts:**
- Add "consistent [subject] appearance throughout"
- Use very specific subject descriptions
- Add "maintaining same [color/size/shape] throughout sequence"

### Problem: Unnatural Motion

**Solution Prompts:**
- Specify "natural, physics-based movement"
- Add motion references: "moving like [reference]"
- Use established terms: "following principles of real-world physics"

### Problem: Poor Composition

**Solution Prompts:**
- Add composition specifications: "rule of thirds composition"
- Reference cinematic framing: "balanced frame with subject centered"
- Specify shot type: "medium shot focusing on subject"

---

## Advanced Prompt Chaining

For complex video concepts, build a sequence of related prompts:

1. **Establish scene:** "Epic wide shot of futuristic Tokyo cityscape at night, raining"
2. **Transition to subject:** "Descending from cityscape to street level, approaching a neon-lit market"
3. **Follow action:** "Tracking through the market as a mysterious hooded figure walks through the crowd"
4. **Climax/focus:** "Close-up on the figure removing hood to reveal glowing cybernetic eyes"

---

## Experimental Techniques

### Visual Mash-ups

```
"The aesthetic of [style 1] combined with elements of [style 2]: [specific elements to combine]"

Example: "The aesthetic of 1950s film noir combined with elements of cyberpunk: rain-soaked streets with detective examining holographic evidence, black and white with selective neon highlights"
```

### Impossible Camera Moves

```
"Impossible camera movement: [describe creative camera movement]"

Example: "Impossible camera movement: seamlessly moving through solid objects, transitioning from outside a house, through the wall, into the living room in one continuous shot"
```

### Narrative Transitions

```
"Scene transitioning from [scenario 1] to [scenario 2] through [transition method]"

Example: "Scene transitioning from underwater ocean scene to space nebula through bubbles morphing into stars"
```

---

## Glossary of Video Prompt Terms

| Term | Definition | Example Usage in Prompt |
|------|------------|-------------------------|
| Aspect Ratio | Width-to-height ratio | "16:9 aspect ratio" or "2.39:1 cinemascope" |
| Bokeh | Aesthetic quality of blur | "creamy bokeh in the background" |
| Dolly Zoom | Camera effect creating disorientation | "dramatic dolly zoom as character realizes the truth" |
| Golden Hour | Warm natural lighting near sunset | "golden hour lighting casting long shadows" |
| Rack Focus | Shifting focus between subjects | "rack focus from foreground character to background action" |
| Steadicam | Smooth camera movement | "smooth steadicam following character through crowd" |
| Volumetric Lighting | Visible light beams | "volumetric lighting through forest canopy" |
| Vignette | Darkened corners | "subtle vignette drawing attention to center" |

---

_This is a living document that will be updated as video generation models and prompt techniques evolve._ 