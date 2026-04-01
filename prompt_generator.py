"""Generate bilingual image prompts with continuity, expressions, and scenes."""
from __future__ import annotations

import uuid
from pathlib import Path
from typing import Optional

import agent
import image_utils
from models import Character, CinemaSettings, PromptFrame, PromptSequence, VideoPromptFrame

# ---------------------------------------------------------------------------
# System prompts
# ---------------------------------------------------------------------------

AUTOCOMPLETE_SYSTEM_PROMPT = """You are a creative character and scene designer for AI image generation.

The user gives a SHORT description (e.g. "A asian woman", "old samurai", "cute robot").
Your job: expand it into a complete, vivid character profile AND suggest a scene/theme.

Return ONLY valid JSON, no extra text:
{
  "name": "suggested character name",
  "description_en": "detailed English character description (appearance, clothing, hair, age, mood)",
  "description_zh": "中文角色描述（外觀、服裝、髮型、年齡、氛圍）",
  "theme_en": "suggested dramatic story theme or scene direction",
  "theme_zh": "建議的戲劇性故事主題或場景方向",
  "style": "recommended art style tags for image generator"
}"""


SYSTEM_PROMPT = """You are a professional cinematographer and image prompt writer for AI image generation tools (Midjourney, Stable Diffusion, ComfyUI, Flux).

Generate a detailed image prompt in BOTH English and Chinese (Traditional).
The user will provide cinematic settings (resolution, aspect ratio, camera, lighting) — weave them naturally into the prompt.

Rules:
1. English prompt: rich visual details, include all cinematic specs at the end as comma-separated tags.
2. Chinese prompt: human-readable translation.
3. Always include: character action, facial expression, scene/environment, lighting, camera angle, depth of field.
4. For sequences: maintain continuity (same character look, natural action flow, emotional arc).
5. Return ONLY valid JSON. No extra text outside the JSON block.

JSON format:
{
  "action_en": "...",
  "action_zh": "...",
  "expression_en": "...",
  "expression_zh": "...",
  "scene_en": "...",
  "scene_zh": "...",
  "prompt_en": "... (full assembled English prompt with cinematic tags at end)",
  "prompt_zh": "... (full assembled Chinese prompt)",
  "continuity_note_en": "...",
  "continuity_note_zh": "..."
}"""


VIDEO_SYSTEM_PROMPT = """You are a professional film director and AI video prompt writer for tools like Runway Gen-3, Kling AI, Pika Labs, Sora, and Luma Dream Machine.

Generate a detailed VIDEO prompt in BOTH English and Chinese (Traditional).
The user provides: character, scene, camera movement, duration, technical specs.

Rules:
1. English prompt: start with camera movement instruction, then scene & subject, then technical specs.
   Format: [CAMERA MOVEMENT], [SUBJECT & ACTION], [SCENE & ATMOSPHERE], [TECHNICAL SPECS]
2. Chinese prompt: director-style description, natural Chinese.
3. subject_motion: specifically describe HOW the character moves during the clip.
4. Be specific about motion — avoid vague words. Use cinematic vocabulary.
5. Return ONLY valid JSON. No extra text.

JSON format:
{
  "action_en": "...",
  "action_zh": "...",
  "expression_en": "...",
  "expression_zh": "...",
  "scene_en": "...",
  "scene_zh": "...",
  "subject_motion_en": "specific body/facial motion during the clip",
  "subject_motion_zh": "角色在片段中的具體動作描述",
  "prompt_en": "... (full video prompt, camera movement first)",
  "prompt_zh": "... (full Chinese video prompt)",
  "negative_prompt": "...",
  "continuity_note_en": "...",
  "continuity_note_zh": "..."
}"""


def _build_user_prompt(
    character: Character,
    theme: str,
    frame_index: int,
    previous_frame: Optional[PromptFrame],
    style: str,
    cinema: Optional[CinemaSettings] = None,
) -> str:
    c = cinema or CinemaSettings()
    parts = [
        f"Character: {character.description} (中文: {character.description_zh})",
        f"Frame index: {frame_index}",
        f"Theme / story direction: {theme}",
        f"Art style: {style}",
        f"Cinematic specs: {c.to_prompt_tags()}",
    ]

    if previous_frame:
        parts.append(
            f"\nPrevious frame context:"
            f"\n  - Action: {previous_frame.action_en}"
            f"\n  - Expression: {previous_frame.expression_en}"
            f"\n  - Scene: {previous_frame.scene_en}"
            f"\n  - Continuity note: {previous_frame.continuity_note_en}"
            f"\nGenerate the NEXT frame that naturally continues from the above."
        )
    else:
        parts.append("\nThis is the FIRST frame. Establish the character, scene, and initial emotional state.")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_frame(
    character: Character,
    theme: str,
    frame_index: int = 0,
    previous_frame: Optional[PromptFrame] = None,
    style: str = "cinematic photography, highly detailed",
    session_id: str = "",
    cinema: Optional[CinemaSettings] = None,
) -> PromptFrame:
    """Generate a single image prompt frame."""
    c = cinema or CinemaSettings()
    user_prompt = _build_user_prompt(character, theme, frame_index, previous_frame, style, c)
    data = agent.chat(system_prompt=SYSTEM_PROMPT, user_prompt=user_prompt)

    return PromptFrame(
        frame_index=frame_index,
        session_id=session_id or str(uuid.uuid4())[:8],
        character=character,
        cinema=c,
        action_en=data.get("action_en", ""),
        action_zh=data.get("action_zh", ""),
        expression_en=data.get("expression_en", ""),
        expression_zh=data.get("expression_zh", ""),
        scene_en=data.get("scene_en", ""),
        scene_zh=data.get("scene_zh", ""),
        style_en=style,
        style_zh="電影攝影，高度細節",
        prompt_en=data.get("prompt_en", ""),
        prompt_zh=data.get("prompt_zh", ""),
        continuity_note_en=data.get("continuity_note_en", ""),
        continuity_note_zh=data.get("continuity_note_zh", ""),
    )


def generate_video_prompt(
    character: Character,
    theme: str,
    cinema: Optional[CinemaSettings] = None,
    duration: str = "5s",
    fps: str = "24fps",
    camera_movement: str = "Static",
    motion_intensity: str = "Moderate",
    negative_prompt: str = "",
    frame_index: int = 1,
    previous_frame: Optional[VideoPromptFrame] = None,
    session_id: str = "",
) -> VideoPromptFrame:
    """Generate a video prompt for AI video tools (Runway, Kling, Pika, Sora, Luma)."""
    c = cinema or CinemaSettings()
    sid = session_id or str(uuid.uuid4())[:8]

    prev_ctx = ""
    if previous_frame:
        prev_ctx = (
            f"\nPrevious clip context:"
            f"\n  - Action: {previous_frame.action_en}"
            f"\n  - Camera: {previous_frame.camera_movement}"
            f"\n  - Scene: {previous_frame.scene_en}"
            f"\n  - Subject motion: {previous_frame.subject_motion_en}"
            f"\n  - Continuity: {previous_frame.continuity_note_en}"
            f"\nGenerate the NEXT clip continuing naturally."
        )

    user_prompt = (
        f"Character: {character.description} (中文: {character.description_zh})\n"
        f"Story / theme: {theme}\n"
        f"Cinematic specs: {c.to_prompt_tags()}\n"
        f"Duration: {duration} | FPS: {fps}\n"
        f"Camera movement: {camera_movement}\n"
        f"Motion intensity: {motion_intensity}\n"
        f"Frame index: {frame_index}"
        + prev_ctx
    )

    data = agent.chat(system_prompt=VIDEO_SYSTEM_PROMPT, user_prompt=user_prompt)

    return VideoPromptFrame(
        frame_index=frame_index,
        session_id=sid,
        character=character,
        cinema=c,
        duration=duration,
        fps=fps,
        camera_movement=camera_movement,
        motion_intensity=motion_intensity,
        action_en=data.get("action_en", ""),
        action_zh=data.get("action_zh", ""),
        expression_en=data.get("expression_en", ""),
        expression_zh=data.get("expression_zh", ""),
        scene_en=data.get("scene_en", ""),
        scene_zh=data.get("scene_zh", ""),
        subject_motion_en=data.get("subject_motion_en", ""),
        subject_motion_zh=data.get("subject_motion_zh", ""),
        prompt_en=data.get("prompt_en", ""),
        prompt_zh=data.get("prompt_zh", ""),
        negative_prompt=negative_prompt or data.get("negative_prompt", "static, blurry, low quality, watermark, deformed, flickering"),
        continuity_note_en=data.get("continuity_note_en", ""),
        continuity_note_zh=data.get("continuity_note_zh", ""),
    )


VISION_SYSTEM_PROMPT = """You are an expert image prompt writer for AI image generation tools (Midjourney, Stable Diffusion, ComfyUI).

Analyze the provided reference image and generate a detailed image prompt in BOTH English and Chinese (Traditional).

Rules:
1. Describe what you observe: character(s), their actions, expressions, scene, lighting, colors, mood.
2. Expand the description into a rich, detailed prompt suitable for image generators.
3. Chinese prompt is the human-readable version of the English prompt.
4. Return ONLY valid JSON. No extra text outside the JSON block.

JSON format:
{
  "action_en": "...",
  "action_zh": "...",
  "expression_en": "...",
  "expression_zh": "...",
  "scene_en": "...",
  "scene_zh": "...",
  "prompt_en": "... (full assembled English prompt)",
  "prompt_zh": "... (full assembled Chinese prompt)",
  "continuity_note_en": "suggested next action or scene continuation",
  "continuity_note_zh": "建議的下一個動作或場景延伸"
}"""


def generate_from_image(
    image_source: str | Path | bytes,
    theme: str = "",
    style: str = "cinematic photography, highly detailed, 8k",
    session_id: str = "",
    frame_index: int = 1,
    image_mime: str = "image/jpeg",
) -> PromptFrame:
    """Analyze a reference image and generate a bilingual prompt from it.

    Args:
        image_source: File path (str/Path) OR raw bytes from upload.
        theme: Optional extra direction for the AI.
        style: Art style tags.
        session_id: Session identifier.
        frame_index: Frame number in sequence.
        image_mime: MIME type when image_source is bytes.
    """
    if isinstance(image_source, bytes):
        b64, mime = image_utils.bytes_to_base64(image_source, image_mime)
    else:
        b64, mime = image_utils.load_image_as_base64(image_source)

    user_prompt_parts = [f"Art style to use: {style}"]
    if theme:
        user_prompt_parts.append(f"Story direction / theme: {theme}")
    user_prompt_parts.append("Analyze this image and generate the prompt.")

    data = agent.chat_with_image(
        system_prompt=VISION_SYSTEM_PROMPT,
        user_prompt="\n".join(user_prompt_parts),
        image_base64=b64,
        image_mime=mime,
    )

    sid = session_id or str(uuid.uuid4())[:8]
    return PromptFrame(
        frame_index=frame_index,
        session_id=sid,
        character=Character(
            description=data.get("action_en", "character from image"),
            description_zh=data.get("action_zh", "圖片中的角色"),
        ),
        action_en=data.get("action_en", ""),
        action_zh=data.get("action_zh", ""),
        expression_en=data.get("expression_en", ""),
        expression_zh=data.get("expression_zh", ""),
        scene_en=data.get("scene_en", ""),
        scene_zh=data.get("scene_zh", ""),
        style_en=style,
        style_zh="電影攝影，高度細節，8K",
        prompt_en=data.get("prompt_en", ""),
        prompt_zh=data.get("prompt_zh", ""),
        continuity_note_en=data.get("continuity_note_en", ""),
        continuity_note_zh=data.get("continuity_note_zh", ""),
    )


def autocomplete_character(short_input: str) -> dict:
    """Expand a short description into a full character + theme profile.

    Args:
        short_input: e.g. "A asian woman", "老武士", "cute robot girl"

    Returns:
        dict with keys: name, description_en, description_zh, theme_en, theme_zh, style
    """
    data = agent.chat(
        system_prompt=AUTOCOMPLETE_SYSTEM_PROMPT,
        user_prompt=f'Short description: "{short_input}"\nExpand this into a full character profile.',
    )
    return {
        "name": data.get("name", "Hero"),
        "description_en": data.get("description_en", short_input),
        "description_zh": data.get("description_zh", short_input),
        "theme_en": data.get("theme_en", "a dramatic moment"),
        "theme_zh": data.get("theme_zh", "戲劇性的時刻"),
        "style": data.get("style", "cinematic photography, highly detailed, 8k"),
    }


def generate_sequence(
    character: Character,
    theme: str,
    num_frames: int = 4,
    style: str = "cinematic photography, highly detailed, 8k",
) -> PromptSequence:
    """Generate a sequence of N frames with continuity."""
    session_id = str(uuid.uuid4())[:8]
    sequence = PromptSequence(session_id=session_id, character=character)

    previous: Optional[PromptFrame] = None
    for i in range(num_frames):
        frame = generate_frame(
            character=character,
            theme=theme,
            frame_index=i + 1,
            previous_frame=previous,
            style=style,
            session_id=session_id,
        )
        sequence.frames.append(frame)
        previous = frame

    return sequence


# ---------------------------------------------------------------------------
# AI Continuation / Smart-complete
# ---------------------------------------------------------------------------

CONTINUATION_SYSTEM_PROMPT = """You are a professional cinematographer and AI image prompt writer.

The user provides a BASE PROMPT with LOCKED fields (fields marked as fixed that must not change)
and UNLOCKED fields (empty or flagged for AI to fill in).

Your task:
1. Keep LOCKED fields exactly as provided.
2. Fill in UNLOCKED fields creatively, maintaining visual and narrative consistency with locked fields.
3. If a direction hint is given (e.g. "sad expression", "night scene", "next action"), apply it to the relevant unlocked fields.
4. Assemble a complete, vivid prompt from all fields.

Return ONLY valid JSON:
{
  "subject_en": "character description (who, appearance, clothing)",
  "subject_zh": "主體描述",
  "action_en": "what the character is doing",
  "action_zh": "角色動作",
  "expression_en": "facial expression and emotion",
  "expression_zh": "臉部表情與情緒",
  "scene_en": "environment, background, atmosphere",
  "scene_zh": "場景環境",
  "style_en": "art style and technical tags",
  "style_zh": "風格標籤",
  "prompt_en": "FULL assembled English prompt — all fields merged, cinematic tags at end",
  "prompt_zh": "FULL assembled Chinese prompt"
}"""


def generate_continuation(
    locked_fields: dict,
    unlock_targets: list[str],
    direction_hint: str = "",
    style: str = "cinematic photography, highly detailed, 8k",
    negative_prompt: str = "",
) -> dict:
    """Generate AI continuation/smart-complete for a prompt.

    Args:
        locked_fields: dict of field_name → value that AI must keep unchanged.
                       Keys: subject_en, subject_zh, action_en, action_zh,
                             expression_en, expression_zh, scene_en, scene_zh,
                             style_en, style_zh
        unlock_targets: list of field names AI should fill/modify.
        direction_hint: free-text user hint like "surprise expression" or "next dramatic scene".
        style: default style if style fields are unlocked.
        negative_prompt: passed through unchanged.

    Returns:
        dict with all prompt fields + prompt_en + prompt_zh.
    """
    # Build user prompt
    locked_lines = []
    for k, v in locked_fields.items():
        if v:
            locked_lines.append(f"  [LOCKED] {k}: {v}")

    unlock_lines = [f"  [FILL] {t}: (AI should generate this)" for t in unlock_targets]

    hint_line = f"\nDirection hint: {direction_hint}" if direction_hint.strip() else ""
    style_line = f"\nDefault style (use if style is unlocked): {style}"

    user_prompt = (
        "Base prompt fields:\n"
        + "\n".join(locked_lines)
        + "\n"
        + "\n".join(unlock_lines)
        + hint_line
        + style_line
        + "\n\nFill the [FILL] fields and output the complete JSON."
    )

    data = agent.chat(
        system_prompt=CONTINUATION_SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )

    # Merge locked fields back (override any AI hallucination on locked fields)
    result = dict(data)
    for k, v in locked_fields.items():
        if v:
            result[k] = v

    # Rebuild assembled prompts
    parts_en = [
        result.get("subject_en", ""),
        result.get("action_en", ""),
        result.get("expression_en", ""),
        result.get("scene_en", ""),
        result.get("style_en", style),
    ]
    parts_zh = [
        result.get("subject_zh", ""),
        result.get("action_zh", ""),
        result.get("expression_zh", ""),
        result.get("scene_zh", ""),
        result.get("style_zh", ""),
    ]

    if not result.get("prompt_en"):
        result["prompt_en"] = ", ".join(p for p in parts_en if p)
    if not result.get("prompt_zh"):
        result["prompt_zh"] = "，".join(p for p in parts_zh if p)

    result["negative_prompt"] = negative_prompt
    return result


# ---------------------------------------------------------------------------
# Prompt Editor — expand & translate
# ---------------------------------------------------------------------------

PROMPT_EXPAND_SYSTEM_PROMPT = """You are an expert AI image prompt specialist, cinematographer, and translator.
The user provides a brief description or incomplete prompt (any language).

Your job:
1. Expand it into a complete, vivid, detailed AI image generation prompt optimised for
   Midjourney, Stable Diffusion, Flux, and ComfyUI.
2. Translate and adapt it into natural, expressive Traditional Chinese.
3. Suggest a negative prompt.
4. Suggest comma-separated style tags.

Return ONLY valid JSON (no extra text):
{
  "prompt_en": "detailed English prompt with photographic/cinematic style, mood, lighting, details...",
  "prompt_zh": "詳細繁體中文提示詞，自然流暢，包含視覺細節與氛圍",
  "negative_prompt": "blurry, low quality, watermark, deformed, ...",
  "style_tags": "cinematic photography, 8K HDR, highly detailed, ..."
}"""


def expand_and_translate_prompt(brief_input: str) -> dict:
    """Expand a brief description into full bilingual image-generation prompts."""
    data = agent.chat(
        system_prompt=PROMPT_EXPAND_SYSTEM_PROMPT,
        user_prompt=f'Input: "{brief_input}"\n\nExpand into a full AI image generation prompt.',
    )
    return {
        "prompt_en":       data.get("prompt_en",       brief_input),
        "prompt_zh":       data.get("prompt_zh",       ""),
        "negative_prompt": data.get("negative_prompt", "blurry, low quality, watermark, deformed"),
        "style_tags":      data.get("style_tags",      "cinematic photography, highly detailed, 8k"),
    }


# ---------------------------------------------------------------------------
# Video Script / Storyboard Generator
# ---------------------------------------------------------------------------

VIDEO_SCRIPT_SYSTEM_PROMPT = """You are a professional film director, screenwriter, and AI video storyboard designer.
You specialise in creating precise, platform-ready shooting scripts for AI video generation tools
(Runway Gen-4, Kling 3.0, Veo 3, Sora 2, Pika, Luma Dream Machine, Hailuo AI).

Given: project name, synopsis, genre, target platform, total duration, scene count, aspect ratio, visual style.

Generate a complete scene-by-scene shooting script as a JSON ARRAY.
Each element is one scene:
[
  {
    "scene_no": 1,
    "title_en": "Opening — The Wasteland",
    "title_zh": "開場：廢土之地",
    "location_en": "EXT. NEON CITY ROOFTOP — NIGHT",
    "location_zh": "外景・霓虹城市屋頂・夜晚",
    "characters": "VERA (late 20s, cyberpunk soldier, chrome arm)",
    "action_en": "VERA stands at the roof edge, drenched trench coat whipping in gale-force wind. She surveys burning towers below, then slowly raises her chrome arm to block a debris gust.",
    "action_zh": "VERA 站在屋頂邊緣，濕透的風衣在強風中翻飛。她俯視下方燃燒的高塔，緩緩舉起義肢手臂擋住碎片衝擊。",
    "camera_movement": "Slow dolly forward → crane boom up to reveal city panorama",
    "camera_angle": "Low angle tracking → aerial wide establish",
    "duration": "5s",
    "mood_en": "Ominous, desolate, cinematic noir",
    "mood_zh": "不祥、荒涼、黑色電影",
    "director_note_en": "EMOTIONAL BEAT: audience feels civilisation's weight collapsing. Her silhouette must be iconic and isolated.",
    "director_note_zh": "核心情感：觀眾感受到文明崩潰的沉重。她的剪影必須孤立且標誌性。",
    "image_prompt_en": "cinematic low angle shot of cyberpunk female soldier on skyscraper rooftop, rain-soaked trench coat, chrome prosthetic arm, burning neon city below, volumetric fog, dramatic rim light, 16:9, photorealistic, Blade Runner aesthetic, 8K HDR",
    "dialogue_vo": ""
  }
]

Rules:
1. Each scene must be a distinct, visually compelling emotional beat.
2. Distribute total_duration proportionally (durations should roughly sum to total).
3. Build a clear narrative arc: setup → rising tension → climax → resolution.
4. camera_movement must be feasible for the target platform.
5. image_prompt_en must be paste-ready with full style/technical tags — suitable for Midjourney or SD.
6. dialogue_vo: max one sentence; leave empty string if scene is silent/visual-only.
7. Return ONLY the JSON array. No markdown fences, no extra prose."""


def generate_video_script(
    project_name: str,
    synopsis: str,
    genre: str = "動作 Action",
    platform: str = "Runway Gen-4",
    total_duration: str = "1min",
    num_scenes: int = 6,
    aspect_ratio: str = "16:9",
    visual_style: str = "Cinematic Blockbuster",
) -> list:
    """Generate a scene-by-scene shooting script / storyboard.

    Returns:
        List of scene dicts (scene_no, title_en/zh, location, action, camera,
        duration, mood, director_note, image_prompt_en, dialogue_vo).
    """
    user_prompt = (
        f"Project: {project_name}\n"
        f"Genre: {genre}\n"
        f"Target platform: {platform}\n"
        f"Visual style: {visual_style}\n"
        f"Aspect ratio: {aspect_ratio}\n"
        f"Total duration: {total_duration}\n"
        f"Number of scenes: {num_scenes}\n"
        f"Synopsis:\n{synopsis}\n\n"
        f"Generate exactly {num_scenes} scenes that cover the full story arc. "
        f"Total clip durations should sum to approximately {total_duration}."
    )

    # agent.chat parses JSON (including arrays); may return list or dict
    result = agent.chat(system_prompt=VIDEO_SCRIPT_SYSTEM_PROMPT, user_prompt=user_prompt)

    # If it returned a list directly
    if isinstance(result, list):
        return result

    # If wrapped in a key
    if isinstance(result, dict):
        for key in ("scenes", "script", "storyboard", "data"):
            if isinstance(result.get(key), list):
                return result[key]

    # Fallback: single error scene
    return [{
        "scene_no": 1, "title_en": "Parse Error", "title_zh": "解析錯誤",
        "location_en": "", "location_zh": "", "characters": "",
        "action_en": f"AI returned unexpected format: {str(result)[:300]}",
        "action_zh": "AI 回傳格式異常，請重試",
        "camera_movement": "", "camera_angle": "", "duration": "",
        "mood_en": "", "mood_zh": "", "director_note_en": "",
        "director_note_zh": "", "image_prompt_en": "", "dialogue_vo": "",
    }]
