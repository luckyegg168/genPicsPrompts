from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Character(BaseModel):
    name: str = "角色"
    description: str = "a person"
    description_zh: str = "一個人物"


class CinemaSettings(BaseModel):
    """Professional cinematic settings shared by image and video prompts."""
    aspect_ratio: str = "16:9"
    resolution: str = "4K"
    camera_angle: str = "Eye Level"
    camera_lens: str = "35mm Standard"
    lighting: str = "Cinematic Natural Light"
    color_grade: str = "Cinematic Warm"
    depth_of_field: str = "Shallow (f/1.8)"

    def to_prompt_tags(self) -> str:
        return (
            f"{self.resolution}, {self.aspect_ratio}, "
            f"{self.camera_angle} shot, {self.camera_lens} lens, "
            f"{self.lighting}, {self.color_grade}, "
            f"{self.depth_of_field} depth of field"
        )

    def to_prompt_tags_zh(self) -> str:
        return (
            f"{self.resolution}解析度, {self.aspect_ratio}畫面比例, "
            f"{self.camera_angle}鏡頭角度, {self.camera_lens}鏡頭, "
            f"{self.lighting}, {self.color_grade}調色, "
            f"{self.depth_of_field}景深"
        )


class PromptFrame(BaseModel):
    """Single image prompt — one frame in a sequence."""

    frame_index: int = 0
    session_id: str = ""
    prompt_type: str = "image"
    created_at: datetime = Field(default_factory=datetime.now)

    character: Character = Field(default_factory=Character)
    cinema: CinemaSettings = Field(default_factory=CinemaSettings)

    action_en: str = ""
    action_zh: str = ""
    expression_en: str = ""
    expression_zh: str = ""
    scene_en: str = ""
    scene_zh: str = ""
    style_en: str = "cinematic photography, highly detailed"
    style_zh: str = "電影攝影，高度細節"

    prompt_en: str = ""
    prompt_zh: str = ""
    negative_prompt: str = "blurry, low quality, watermark, text, deformed"

    continuity_note_en: str = ""
    continuity_note_zh: str = ""

    def to_markdown(self) -> str:
        ts = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"""
## [IMAGE] Frame {self.frame_index} — {ts}
**Session:** {self.session_id}

### English Prompt
> {self.prompt_en}

### 中文提示詞
> {self.prompt_zh}

**規格:** {self.cinema.resolution} | {self.cinema.aspect_ratio} | {self.cinema.camera_angle} | {self.cinema.camera_lens}
**燈光/調色:** {self.cinema.lighting} | {self.cinema.color_grade} | {self.cinema.depth_of_field}
**動作:** {self.action_zh} / {self.action_en}
**表情:** {self.expression_zh} / {self.expression_en}
**場景:** {self.scene_zh} / {self.scene_en}
**Negative:** {self.negative_prompt}
**連續性:** {self.continuity_note_zh}

---
"""


class VideoPromptFrame(BaseModel):
    """Video prompt for AI video generation (Runway, Kling, Pika, Sora, Luma)."""

    frame_index: int = 0
    session_id: str = ""
    prompt_type: str = "video"
    created_at: datetime = Field(default_factory=datetime.now)

    character: Character = Field(default_factory=Character)
    cinema: CinemaSettings = Field(default_factory=CinemaSettings)

    # Video-specific settings
    duration: str = "5s"
    fps: str = "24fps"
    camera_movement: str = "Static"
    motion_intensity: str = "Moderate"

    # Content
    action_en: str = ""
    action_zh: str = ""
    expression_en: str = ""
    expression_zh: str = ""
    scene_en: str = ""
    scene_zh: str = ""
    subject_motion_en: str = ""
    subject_motion_zh: str = ""

    prompt_en: str = ""
    prompt_zh: str = ""
    negative_prompt: str = "static, blurry, low quality, watermark, deformed, flickering"

    continuity_note_en: str = ""
    continuity_note_zh: str = ""

    def to_markdown(self) -> str:
        ts = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"""
## [VIDEO] Frame {self.frame_index} — {ts}
**Session:** {self.session_id}

### English Prompt
> {self.prompt_en}

### 中文提示詞
> {self.prompt_zh}

**規格:** {self.cinema.resolution} | {self.cinema.aspect_ratio} | {self.duration} | {self.fps}
**鏡頭:** {self.cinema.camera_angle} | {self.cinema.camera_lens} | 運鏡: {self.camera_movement}
**燈光/調色:** {self.cinema.lighting} | {self.cinema.color_grade}
**動作:** {self.action_zh} | 運動強度: {self.motion_intensity}
**表情:** {self.expression_zh}
**場景:** {self.scene_zh}
**角色動作:** {self.subject_motion_zh}
**Negative:** {self.negative_prompt}
**連續性:** {self.continuity_note_zh}

---
"""


class PromptSequence(BaseModel):
    """A series of frames with shared character and continuity."""

    session_id: str
    character: Character
    frames: list[PromptFrame] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
