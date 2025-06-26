# Prompt Engineering for Image Generation

This guide provides detailed strategies, techniques, and frameworks for creating effective prompts for AI image generation. Mastering prompt engineering can dramatically improve your results across different image generation platforms.

## The Anatomy of an Effective Image Prompt

### Basic Prompt Structure

A well-formed image generation prompt typically includes several core elements:

```
[Subject] in/with [Environment/Context] in the style of [Style Reference], [Technical Specifications], [Quality Indicators]
```

This structure can be adapted based on your needs and the specific model you're using.

### Core Prompt Elements

#### 1. Subject
The main focus of your image - what you want to see.
- Be specific about attributes (color, size, age, materials)
- Describe pose, action, or expression if applicable
- Include important details that define the subject

**Examples:**
- Basic: `a cat`
- Better: `a fluffy orange tabby cat`
- Best: `a fluffy orange tabby cat with green eyes, sitting alert with its tail wrapped around its paws`

#### 2. Environment/Context
Where the subject exists or what surrounds it.
- Describe the setting or background
- Include atmospheric elements (weather, time of day)
- Mention spatial relationships between elements

**Examples:**
- Basic: `in a garden`
- Better: `in a lush English garden`
- Best: `in a lush English garden with blooming roses, dappled sunlight filtering through old oak trees, morning dew on the grass`

#### 3. Style Reference
The artistic style, genre, medium, or aesthetic you want.
- Reference specific artists, art movements, or media
- Describe the mood or emotional tone
- Mention technical aspects of the desired style

**Examples:**
- Basic: `watercolor painting`
- Better: `impressionist watercolor painting`
- Best: `impressionist watercolor painting in the style of Claude Monet, with visible brushstrokes and soft color blending`

#### 4. Technical Specifications
Camera and rendering details that shape the image output.
- Camera angle, lens type, and distance
- Lighting conditions and sources
- Rendering approach or simulation style

**Examples:**
- Basic: `closeup photo`
- Better: `closeup photo with shallow depth of field`
- Best: `closeup macro photograph, shot on Canon 5D with 100mm macro lens, f/2.8 aperture, soft natural lighting from the left, shallow depth of field`

#### 5. Quality Indicators
Terms that help ensure high-quality output.
- Resolution and detail level descriptors
- Professional terminology from photography/art
- Composition and framing descriptors

**Examples:**
- Basic: `high quality`
- Better: `highly detailed, professional photography`
- Best: `8K resolution, highly detailed, professional photography, sharp focus, studio lighting, award-winning photo`

## Model-Specific Prompt Techniques

### DALL-E 3 Prompting

DALL-E 3 (built on GPT-4) understands conversational, detailed prompts and complex instructions.

#### Effective Approaches:
- Use natural language, even complete sentences or paragraphs
- Provide rich descriptive details about the scene
- Include specific instructions about what to include/exclude
- Clearly state compositional elements you want
- Use artistic references for style guidance

#### Example DALL-E 3 Prompt:
```
Create an image of an ancient library filled with magical books and scrolls. The library should have towering bookshelves reaching up to a domed ceiling with intricate astronomical paintings. Warm golden light filters in through stained glass windows, illuminating dust particles in the air. In the center, a wizened librarian with a long silver beard is showing a mysterious glowing tome to a young apprentice in blue robes. The scene should be rendered in the style of Alan Lee's fantasy illustrations, with careful attention to light and shadow. The composition should draw the eye to the book at the center.
```

### Midjourney Prompting

Midjourney works well with structured, comma-separated parameter lists and has special commands.

#### Effective Approaches:
- Use comma-separated descriptive terms
- Include strong style references and quality descriptors
- Leverage Midjourney-specific parameters (--stylize, --chaos, etc.)
- Use :: to weight term importance
- Structure complexity from most to least important

#### Example Midjourney Prompt:
```
ornate mechanical clockwork dragonfly, copper and brass materials, intricate gears visible through transparent wings, steampunk aesthetic, hovering above an antique pocket watch, detailed craftsmanship, watch mechanism visible, warm amber lighting, macro photography, dramatic depth of field, 8k render --ar 16:9 --stylize 750
```

### Stable Diffusion Prompting

Stable Diffusion benefits from detailed, weighted prompts and negative prompts.

#### Effective Approaches:
- Use detailed descriptions with weights in parentheses
- Add (term:1.2) for emphasis, (term:0.8) for de-emphasis
- Include both positive and negative prompts
- Reference specific models and approaches in community
- Use established tags that work well with SD models

#### Example Stable Diffusion Prompt:
```
Portrait of a (cyberpunk:1.2) (female:1.1) hacker, (neon blue hair:1.3), serious expression, (sitting:1.1) in a (dimly lit:1.2) apartment, multiple holographic screens, (cybernetic implants:1.2) on face, wearing (high-tech:1.1) jacket, (volumetric lighting:1.3), blue and purple color scheme, highly detailed, octane render, 8k resolution, sharp focus

Negative prompt: blurry, low quality, disfigured face, bad anatomy, extra limbs, poorly drawn hands, too many fingers
```

## Advanced Prompting Techniques

### 1. Weighted Terms

Emphasize or de-emphasize certain elements using platform-specific syntax:

- **Midjourney**: Use `::` to weight terms
  - `cyberpunk city::1.5, rainy::0.8`
- **Stable Diffusion**: Use parentheses with weights
  - `(cyberpunk city:1.5), (rainy:0.8)`
- **DALL-E 3**: Use emphasis words and repetition
  - `extremely detailed cyberpunk city with light rain`

### 2. Negative Prompting

Specify what you don't want in the image:

- **Stable Diffusion**: Use the negative prompt field
  - `Negative: blurry, low quality, deformed, disfigured`
- **DALL-E 3**: Include in your prompt
  - `...avoid blurry details, deformities, and unrealistic anatomy`
- **Midjourney**: Use the `--no` parameter
  - `--no blur, artifacts, text, watermarks`

### 3. Style Fusion

Combine multiple styles for unique results:

- **Combining Artists**:
  - `in the style of Salvador Dali meets Studio Ghibli`
  - `combining Art Nouveau and cyberpunk aesthetics`

- **Mixing Media**:
  - `digital art with watercolor textures`
  - `photography with comic book elements`

### 4. Compositional Control

Direct the visual composition explicitly:

- **Framing**:
  - `cinematic wide shot`
  - `intimate close-up portrait`
  - `overhead aerial view`

- **Focus**:
  - `shallow depth of field with background bokeh`
  - `tilt-shift effect focusing on the central figure`
  - `all elements in sharp focus`

- **Perspective**:
  - `dramatic one-point perspective`
  - `fish-eye lens distortion`
  - `isometric view`

### 5. Multi-Step Generation

Use a sequence of generations to refine results:

1. **Initial Concept**: Generate base image with core elements
2. **Variation**: Create variations of promising results
3. **Inpainting/Outpainting**: Edit specific areas or expand canvas
4. **Style Transfer**: Apply specific styles to refined compositions

## Prompt Templates by Image Type

### Portrait Photography

```
Portrait of [subject description] with [expression/pose], wearing [clothing/accessories], [environment/background], [lighting condition], [camera details], [style reference]

Example: Portrait of a middle-aged indigenous woman with weathered features and a serene expression, wearing traditional handwoven textiles and silver jewelry, standing in front of her mountain village home, golden hour lighting creating warm highlights, shot on Hasselblad medium format camera with 80mm lens, in the documentary style of Steve McCurry
```

### Landscape/Environment

```
[Time of day] [weather] scene of [location type], featuring [key elements], [atmospheric details], [perspective], [style/rendering], [quality indicators]

Example: Misty dawn scene of an ancient redwood forest, featuring moss-covered giant trees and a winding path, gentle sunbeams filtering through the canopy creating volumetric god rays, wide-angle perspective with foreground detail, digital matte painting in the style of Caspar David Friedrich, photorealistic, volumetric lighting, 8K
```

### Concept Art

```
Concept art of [subject/scene], [key visual elements], [color palette/mood], [artistic style], [rendering technique], [quality descriptors]

Example: Concept art of a futuristic underwater research facility, bioluminescent sea creatures visible through massive curved glass windows, scientists working on holographic displays, teal and deep blue color palette with pops of neon accents, in the style of Syd Mead meets Moebius, digital painting with clean linework and atmospheric perspective, highly detailed
```

### Product Visualization

```
[Product type] with [defining features], [materials], [environment/context], [lighting setup], [photographic style], [technical specifications]

Example: Modern minimalist smartphone with edge-to-edge display and titanium frame, sitting on a white marble surface, studio product photography with three-point lighting setup emphasizing sleek contours, soft shadows, shot on Phase One medium format camera, advertising photography style, ultra-detailed, photorealistic rendering
```

### Character Design

```
[Character type] with [physical traits], wearing [clothing/armor/outfit], [pose/action], [expression/emotion], [accessories/props], [environment hints], [stylistic approach]

Example: Battle-hardened female elven ranger with piercing green eyes and a scar across her cheek, wearing lightweight leather armor with leaf motifs and a flowing green cloak, drawing a curved bow, determined expression, quiver of arrows and enchanted daggers at her belt, glimpse of misty forest in background, stylized digital painting in the style of modern fantasy concept art, detailed textures
```

## Troubleshooting Common Issues

### Problem: Inconsistent Anatomy/Proportions

- **Solution**: 
  - Add `anatomically correct` or `realistic proportions` to your prompt
  - Include `detailed anatomy` and references to realistic art
  - For Stable Diffusion, add anatomy issues to negative prompt
  - Use ControlNet (SD) or reference images for better structure

### Problem: Text/Writing is Illegible

- **Solution**:
  - Avoid requesting readable text in images
  - If needed, add `clear legible text` but expect mixed results
  - Place text in post-processing instead of generation
  - Use inpainting for text areas after generating the main image

### Problem: Too Busy/Cluttered

- **Solution**:
  - Simplify your prompt, focus on fewer key elements
  - Add `minimalist`, `clean composition`, or `uncluttered` 
  - Specifically request `focus on [main element]`
  - Request `negative space` or `simple background`

### Problem: Style Not Matching Reference

- **Solution**:
  - Use more specific artist or style references
  - Include technical terms from the art style
  - Add qualifiers like `exactly in the style of`
  - Create compound style references: `style A meets style B`
  - Try img2img with a reference image (if available)

### Problem: Colors Not as Expected

- **Solution**:
  - Be very specific about color names and relationships
  - Use precise color terminology (`cerulean` vs `blue`)
  - Describe color quality (`vibrant`, `muted`, `pastel`)
  - Mention color theory terms (`complementary colors`, `monochromatic`)
  - Reference specific color palettes (`autumn color palette`)

## Prompt Engineering Workflow

### 1. Define Your Vision
- Identify the core concept
- Collect reference images
- Determine key visual elements
- Choose style and mood

### 2. Start Simple
- Begin with a basic version of your prompt
- Focus on subject and basic style
- Generate initial results
- Analyze what works and what doesn't

### 3. Iterate and Refine
- Add details based on initial results
- Adjust style references
- Experiment with technical parameters
- Incorporate successful elements from previous generations

### 4. Optimize for Your Model
- Add model-specific syntax and parameters
- Include appropriate quality boosters
- Use effective negative prompts
- Add weights to important elements

### 5. Document Success
- Save successful prompts
- Note which techniques worked best
- Create personal templates for future use
- Build a prompt library

## Prompt Library: Example Snippets

Use these prompt fragments as building blocks for your own creations:

### Lighting Effects
- `dramatic rim lighting with strong shadows`
- `soft diffused daylight through a north-facing window`
- `vibrant golden hour sunlight with lens flare`
- `moody low-key lighting with strong contrast`
- `ethereal volumetric lighting with visible light rays`

### Camera Settings
- `shot on Hasselblad medium format, 80mm lens, f/2.8 aperture`
- `35mm film photograph, slight grain, Kodak Portra 400`
- `macro photography with extreme shallow depth of field`
- `wide-angle drone shot, aerial perspective`
- `tilt-shift photography with selective focus`

### Quality Boosters
- `8K resolution, ultra detailed, photorealistic`
- `award-winning photography, featured in National Geographic`
- `hyperrealistic, studio quality, professional lighting`
- `masterful composition, perfect color harmony`
- `intricate details, high definition, sharp focus`

### Style References
- `digital art in the style of Artgerm and WLOP`
- `cinematic realism in the style of Roger Deakins cinematography`
- `manga illustration in the style of Junji Ito`
- `impressionist painting in the style of Claude Monet`
- `retro pixel art in the style of 16-bit SNES games`

---

## Platform-Specific Cheat Sheets

### DALL-E 3 Quick Reference
- Use natural language, conversational style
- Include detailed descriptions and context
- Provide specific instructions within the prompt
- Be explicit about style and artistic references
- Describe what to avoid or exclude

### Midjourney Quick Reference
- Use v5/v6 and appropriate settings (--v 6, etc.)
- Add --ar [ratio] for aspect ratio control
- Control stylization with --stylize [number]
- Use --chaos [number] for variation level
- Format: [content prompts] --parameter values

### Stable Diffusion Quick Reference
- Use weights: (term:1.5)
- Create strong negative prompts
- Sampler: DPM++ 2M Karras, Euler a, DDIM
- Steps: 20-50 (model dependent)
- CFG Scale: 7-12 for balanced results

---

*This guide will be updated as prompt engineering techniques evolve and new models become available.* 