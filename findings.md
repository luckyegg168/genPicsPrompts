# Findings

## OpenRouter API
- Base URL: `https://openrouter.ai/api/v1`
- Compatible with OpenAI SDK (`openai` Python package with custom base_url)
- Auth: `Authorization: Bearer <OPENROUTER_API_KEY>`
- Endpoint: `/chat/completions` (OpenAI-compatible format)

## Qwen3 Model (`qwen/qwen3.6-plus-preview:free`)
- **Context:** 131,072 tokens
- **Modality:** Text input/output ONLY — no vision/image support
- **Thinking mode:** Outputs `<think>...</think>` blocks before actual response
  - Must strip `<think>...</think>` before JSON parsing
  - Regex: `re.compile(r"<think>.*?</think>", re.DOTALL)`
- **Stop tokens:** `<|im_start|>`, `<|im_end|>`
- **Good at:** Math, coding, reasoning, creative writing, multilingual
- **Knowledge cutoff:** March 2025

## Vision Model (`bytedance-seed/seed-2.0-mini`)
- **Input:** text + image + video
- **Context:** 262,144 tokens
- Used for: image analysis tab in GUI

## Prompt Structure for Image Generation
A good image prompt for tools like Midjourney/Stable Diffusion/ComfyUI should contain:
1. **Subject** — Who (character description)
2. **Action** — What they are doing
3. **Expression** — Emotional state on face
4. **Scene/Environment** — Where, lighting, atmosphere
5. **Style** — Art style, quality tags
6. **Camera** — Angle, lens, framing

## Continuity Design
For sequential frames (storyboard/animation):
- Track last action → suggest natural next action
- Track emotional arc (e.g., neutral → surprised → happy)
- Track scene consistency (same location or transition cue)
- Seed character description once, reuse across frames

## Bilingual Strategy
- Generate English prompt first (better for image AI models)
- Translate to Chinese for human readability
- Store both versions in record
