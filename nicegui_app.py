"""NiceGUI Desktop App — AI Image & Video Prompt Generator (Director Edition)."""
from __future__ import annotations

import asyncio
import uuid
from typing import Optional

from nicegui import app, ui, run

import json

import config
import image_utils
import logger as applog
import prompt_generator
import recorder
import templates
from models import Character, CinemaSettings, PromptSequence

# ── constants ─────────────────────────────────────────────────────────────────
ASPECT_RATIOS    = ["16:9", "9:16", "1:1", "4:3", "21:9", "2.35:1 Anamorphic", "4:5", "3:2"]
RESOLUTIONS      = ["4K (3840×2160)", "8K (7680×4320)", "2K (2560×1440)", "1080p (1920×1080)"]
CAMERA_ANGLES    = ["Eye Level", "Low Angle", "High Angle", "Bird's Eye View",
                    "Dutch Angle", "Over-the-Shoulder", "POV", "Worm's Eye View"]
CAMERA_LENSES    = ["14mm Ultra Wide", "24mm Wide", "35mm Standard Wide",
                    "50mm Normal", "85mm Portrait", "135mm Telephoto",
                    "200mm Long Telephoto", "Macro"]
LIGHTINGS        = ["Cinematic Natural Light", "Golden Hour", "Blue Hour",
                    "High Key Studio", "Low Key Dramatic", "Rim / Back Light",
                    "Chiaroscuro", "Neon City Light", "Candlelight", "Overcast Soft"]
COLOR_GRADES     = ["Cinematic Warm", "Cool Desaturated", "Teal & Orange",
                    "Black & White", "Vibrant Saturated", "Bleach Bypass", "Kodak Film"]
DOF_OPTIONS      = ["Shallow (f/1.4)", "Shallow (f/1.8)", "Standard (f/2.8)",
                    "Mid (f/5.6)", "Deep (f/8)", "Hyperfocal"]
DURATIONS        = ["3s", "4s", "5s", "6s", "8s", "10s", "15s"]
FPS_OPTIONS      = ["24fps (Cinematic)", "25fps (PAL)", "30fps (Standard)", "60fps (Smooth)"]
CAMERA_MOVEMENTS = [
    "Static", "Slow Pan Left", "Slow Pan Right", "Tilt Up", "Tilt Down",
    "Zoom In (Push)", "Zoom Out (Pull)", "Dolly In", "Dolly Out",
    "Tracking Shot", "Arc Shot (Left)", "Arc Shot (Right)",
    "Crane Up", "Crane Down", "Handheld / Shaky Cam", "360° Orbit",
]
MOTION_INTENSITIES = ["Subtle", "Moderate", "Dynamic", "Extreme"]
DEFAULT_STYLE = "cinematic photography, highly detailed"
DEFAULT_NEG   = "blurry, low quality, watermark, text, deformed, artifacts"
DEFAULT_NEG_V = "static, blurry, low quality, watermark, deformed, flickering, jitter"

CHAR_LABELS  = [t["label"] for t in templates.CHARACTER_TEMPLATES]
STORY_LABELS = [t["label"] for t in templates.STORY_TEMPLATES]
STYLE_LABELS = [t["label"] for t in templates.STYLE_TEMPLATES]

# ── helpers ───────────────────────────────────────────────────────────────────

def _cinema(ar, res, angle, lens, light, grade, dof) -> CinemaSettings:
    return CinemaSettings(
        aspect_ratio=ar,
        resolution=res.split(" ")[0],
        camera_angle=angle,
        camera_lens=lens,
        lighting=light,
        color_grade=grade,
        depth_of_field=dof,
    )


def _level_color(level: str) -> str:
    return {
        "DEBUG":   "text-gray-400",
        "INFO":    "text-blue-300",
        "WARNING": "text-yellow-300",
        "ERROR":   "text-red-400",
        "CRITICAL":"text-red-600",
    }.get(level, "text-white")


def _copy_btn(text_getter, color: str = "bg-amber-600") -> ui.button:
    """Amber copy-to-clipboard button.  text_getter() must return the string to copy."""
    async def _do() -> None:
        await ui.run_javascript(
            f"navigator.clipboard.writeText({json.dumps(text_getter())})"
        )
        ui.notify("已複製 ✓", type="positive")
    return ui.button("複製", icon="content_copy", on_click=_do).classes(
        f"{color} text-white text-xs px-2 py-1 self-end"
    )


# ── Cinema settings widget (shared) ──────────────────────────────────────────

def cinema_inputs() -> dict:
    """Render cinema settings row and return refs."""
    refs = {}
    with ui.row().classes("flex-wrap gap-3 w-full"):
        refs["ar"]    = ui.select(ASPECT_RATIOS,   value="16:9",                       label="比例").classes("w-28")
        refs["res"]   = ui.select(RESOLUTIONS,     value=RESOLUTIONS[0],               label="解析度").classes("w-44")
        refs["angle"] = ui.select(CAMERA_ANGLES,   value="Eye Level",                  label="鏡頭角度").classes("w-40")
        refs["lens"]  = ui.select(CAMERA_LENSES,   value="35mm Standard Wide",         label="焦距").classes("w-44")
        refs["light"] = ui.select(LIGHTINGS,       value="Cinematic Natural Light",    label="燈光").classes("w-44")
        refs["grade"] = ui.select(COLOR_GRADES,    value="Cinematic Warm",             label="調色").classes("w-36")
        refs["dof"]   = ui.select(DOF_OPTIONS,     value="Shallow (f/1.8)",            label="景深").classes("w-36")
    return refs


def character_inputs(include_autocomplete: bool = True) -> dict:
    """Render character name / desc inputs and optional AI autocomplete."""
    refs: dict = {}
    with ui.expansion("👤 角色設定", icon="person", value=True).classes("w-full bg-gray-800"):
        if include_autocomplete:
            with ui.row().classes("items-end gap-2 w-full"):
                refs["short"] = ui.input(label="快速輸入 (e.g. 老武士)", placeholder="輸入簡短描述讓 AI 自動完成").classes("flex-1")
                refs["auto_btn"] = ui.button("✨ AI 自動完成", icon="auto_awesome").classes(
                    "bg-rose-600 text-white")

        with ui.row().classes("flex-wrap gap-3 w-full mt-2"):
            with ui.column().classes("flex-1 min-w-48"):
                refs["name"]     = ui.input(label="角色名稱", value="Hero").classes("w-full")
                refs["desc_en"]  = ui.textarea(label="英文描述").props("rows=3").classes("w-full")
                refs["desc_zh"]  = ui.textarea(label="中文描述").props("rows=3").classes("w-full")
            with ui.column().classes("flex-1 min-w-48"):
                refs["char_tmpl"] = ui.select(CHAR_LABELS, label="套用角色模板",
                                               value=CHAR_LABELS[0]).classes("w-full")
                refs["apply_char"] = ui.button("套用", icon="style").classes(
                    "mt-1 bg-violet-700 text-white")

    return refs


def theme_style_inputs() -> dict:
    refs: dict = {}
    with ui.expansion("🎭 主題 & 風格", icon="movie", value=True).classes("w-full bg-gray-800"):
        with ui.row().classes("flex-wrap gap-3 w-full"):
            with ui.column().classes("flex-1 min-w-48"):
                refs["theme"]      = ui.textarea(label="故事主題 / Story theme",
                                                  placeholder="輸入主題或套用模板").props("rows=2").classes("w-full")
                refs["story_tmpl"] = ui.select(STORY_LABELS, label="主題模板",
                                                value=STORY_LABELS[0]).classes("w-full")
                refs["apply_story"] = ui.button("套用故事", icon="style").classes(
                    "bg-violet-700 text-white")
            with ui.column().classes("flex-1 min-w-48"):
                refs["style"]       = ui.input(label="風格 / Style", value=DEFAULT_STYLE).classes("w-full")
                refs["style_tmpl"]  = ui.select(STYLE_LABELS, label="風格模板",
                                                 value=STYLE_LABELS[0]).classes("w-full")
                refs["apply_style"] = ui.button("套用風格", icon="palette").classes(
                    "bg-fuchsia-700 text-white")
                refs["neg"]        = ui.input(label="負面提示詞", value=DEFAULT_NEG).classes("w-full")
    return refs


def _bind_char_template(crefs: dict) -> None:
    def apply():
        t = templates.get_char(crefs["char_tmpl"].value)
        if t:
            crefs["name"].set_value(t["name"])
            crefs["desc_en"].set_value(t["description_en"])
            crefs["desc_zh"].set_value(t["description_zh"])
            crefs["style"].set_value(t["style"]) if "style" in crefs else None
    crefs["apply_char"].on("click", lambda: apply())


def _bind_story_style_templates(trefs: dict) -> None:
    def apply_story():
        t = templates.get_story(trefs["story_tmpl"].value)
        if t:
            trefs["theme"].set_value(f"{t['theme_zh']}\n{t['theme_en']}")
    def apply_style():
        t = templates.get_style(trefs["style_tmpl"].value)
        if t:
            trefs["style"].set_value(t["style"])
    trefs["apply_story"].on("click", lambda: apply_story())
    trefs["apply_style"].on("click", lambda: apply_style())


# ── Page: Single image prompt ─────────────────────────────────────────────────

@ui.page("/")
def page_single():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-5xl mx-auto p-4 gap-4"):
        ui.label("🖼 單張圖片提示詞").classes("text-2xl font-bold text-white")

        crefs = character_inputs()
        trefs = theme_style_inputs()

        _bind_char_template({**crefs, "style": trefs.get("style")})
        _bind_story_style_templates(trefs)

        with ui.expansion("🎬 電影規格", icon="camera", value=True).classes("w-full bg-gray-800"):
            cinrefs = cinema_inputs()

        with ui.row().classes("items-start gap-2 w-full"):
            result_en  = ui.textarea(label="✅ English Prompt").props("rows=5").classes("flex-1 font-mono")
            _copy_btn(lambda: result_en.value)
        with ui.row().classes("items-start gap-2 w-full"):
            result_zh  = ui.textarea(label="✅ 中文提示詞").props("rows=5").classes("flex-1 font-mono")
            _copy_btn(lambda: result_zh.value, color="bg-amber-500")
        result_det = ui.markdown("").classes("w-full text-gray-300")

        async def generate():
            try:
                config.validate_config()
            except EnvironmentError as e:
                ui.notify(str(e), type="negative"); return
            if not crefs["desc_en"].value.strip():
                ui.notify("請填寫角色英文描述", type="warning"); return

            result_en.set_value("⏳ 生成中…")
            result_zh.set_value("⏳ 生成中…")
            char   = Character(name=crefs["name"].value or "Hero",
                                description=crefs["desc_en"].value,
                                description_zh=crefs["desc_zh"].value or crefs["desc_en"].value)
            cin    = _cinema(cinrefs["ar"].value, cinrefs["res"].value,
                              cinrefs["angle"].value, cinrefs["lens"].value,
                              cinrefs["light"].value, cinrefs["grade"].value,
                              cinrefs["dof"].value)
            try:
                frame = await run.io_bound(
                    prompt_generator.generate_frame,
                    character=char,
                    theme=trefs["theme"].value or "a dramatic moment",
                    style=trefs["style"].value or DEFAULT_STYLE,
                    cinema=cin,
                )
                frame.negative_prompt = trefs["neg"].value or DEFAULT_NEG
                await run.io_bound(recorder.save_frame, frame)
                result_en.set_value(frame.prompt_en)
                result_zh.set_value(frame.prompt_zh)
                c = frame.cinema
                result_det.set_content(
                    f"**{c.resolution}** | **{c.aspect_ratio}** | {c.camera_angle} | {c.camera_lens} | {c.lighting}\n\n"
                    f"**動作:** {frame.action_zh} / {frame.action_en}\n\n"
                    f"**表情:** {frame.expression_zh} / {frame.expression_en}\n\n"
                    f"**場景:** {frame.scene_zh} / {frame.scene_en}\n\n"
                    f"**連續性:** {frame.continuity_note_zh}"
                )
                ui.notify("✅ 提示詞已生成並儲存", type="positive")
                applog.log.info(f"Single image prompt generated. Session={frame.session_id}")
            except Exception as exc:
                applog.log.error(f"generate_frame error: {exc}", exc_info=True)
                result_en.set_value(f"❌ 錯誤：{exc}")
                result_zh.set_value("")
                ui.notify(f"生成失敗：{exc}", type="negative")

        # Autocomplete binding
        async def do_autocomplete():
            short = crefs["short"].value.strip()
            if not short:
                ui.notify("請先輸入簡短描述", type="warning"); return
            try:
                config.validate_config()
            except EnvironmentError as e:
                ui.notify(str(e), type="negative"); return
            crefs["auto_btn"].set_text("⏳…")
            try:
                r = await run.io_bound(prompt_generator.autocomplete_character, short)
                crefs["name"].set_value(r.get("name", ""))
                crefs["desc_en"].set_value(r.get("description_en", ""))
                crefs["desc_zh"].set_value(r.get("description_zh", ""))
                trefs["theme"].set_value(
                    r.get("theme_zh", "") + "\n" + r.get("theme_en", "")
                )
                trefs["style"].set_value(r.get("style", DEFAULT_STYLE))
                ui.notify("✅ 角色已自動完成", type="positive")
                applog.log.info(f"Autocomplete: {short} → {r.get('name')}")
            except Exception as exc:
                applog.log.error(f"autocomplete error: {exc}", exc_info=True)
                ui.notify(f"自動完成失敗：{exc}", type="negative")
            finally:
                crefs["auto_btn"].set_text("✨ AI 自動完成")

        crefs["auto_btn"].on("click", do_autocomplete)

        ui.button("🚀 生成提示詞", icon="send", on_click=generate).classes(
            "bg-indigo-600 text-white text-lg px-6 py-3 rounded-xl"
        )


# ── Page: Sequence ────────────────────────────────────────────────────────────

@ui.page("/sequence")
def page_sequence():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-5xl mx-auto p-4 gap-4"):
        ui.label("🔄 圖片序列生成").classes("text-2xl font-bold text-white")

        crefs = character_inputs()
        trefs = theme_style_inputs()
        _bind_char_template({**crefs, "style": trefs.get("style")})
        _bind_story_style_templates(trefs)

        with ui.expansion("🎬 電影規格", icon="camera", value=True).classes("w-full bg-gray-800"):
            cinrefs = cinema_inputs()

        num_frames = ui.slider(min=2, max=8, value=3, step=1).classes("w-full")
        ui.label().bind_text_from(num_frames, "value",
                                   backward=lambda v: f"幀數：{int(v)} 幀").classes("text-gray-300")

        frames_container = ui.column().classes("w-full gap-3")
        status_label = ui.label("").classes("text-gray-400")

        async def gen_sequence():
            try:
                config.validate_config()
            except EnvironmentError as e:
                ui.notify(str(e), type="negative"); return
            if not crefs["desc_en"].value.strip():
                ui.notify("請填寫角色英文描述", type="warning"); return

            frames_container.clear()
            n      = int(num_frames.value)
            char   = Character(name=crefs["name"].value or "Hero",
                                description=crefs["desc_en"].value,
                                description_zh=crefs["desc_zh"].value or crefs["desc_en"].value)
            cin    = _cinema(cinrefs["ar"].value, cinrefs["res"].value,
                              cinrefs["angle"].value, cinrefs["lens"].value,
                              cinrefs["light"].value, cinrefs["grade"].value,
                              cinrefs["dof"].value)
            sid      = str(uuid.uuid4())[:8]
            sequence = PromptSequence(session_id=sid, character=char)
            previous = None

            for i in range(n):
                status_label.set_text(f"⏳ 生成第 {i+1}/{n} 幀…")
                try:
                    frame = await run.io_bound(
                        prompt_generator.generate_frame,
                        character=char,
                        theme=trefs["theme"].value or "a dramatic scene",
                        frame_index=i + 1,
                        previous_frame=previous,
                        style=trefs["style"].value or DEFAULT_STYLE,
                        cinema=cin,
                        session_id=sid,
                    )
                    frame.negative_prompt = trefs["neg"].value or DEFAULT_NEG
                    sequence.frames.append(frame)
                    previous = frame

                    with frames_container:
                        with ui.card().classes("w-full bg-gray-800 p-3"):
                            ui.label(f"Frame {i+1} — {frame.action_zh}").classes("font-bold text-indigo-300")
                            _en_t = frame.prompt_en
                            _zh_t = frame.prompt_zh
                            with ui.row().classes("items-start gap-2 w-full"):
                                ui.label(_en_t).classes("flex-1 text-sm text-gray-200 font-mono")
                                _copy_btn(lambda t=_en_t: t)
                            with ui.row().classes("items-start gap-2 w-full"):
                                ui.label(_zh_t).classes("flex-1 text-sm text-gray-400")
                                _copy_btn(lambda t=_zh_t: t, color="bg-amber-500")
                except Exception as exc:
                    applog.log.error(f"Sequence frame {i+1} error: {exc}", exc_info=True)
                    with frames_container:
                        ui.label(f"❌ Frame {i+1} 失敗：{exc}").classes("text-red-400")
                    ui.notify(f"第 {i+1} 幀失敗：{exc}", type="negative")

            await run.io_bound(recorder.save_sequence, sequence)
            status_label.set_text(f"✅ 序列 {sid} 已儲存 ({len(sequence.frames)} 幀)")
            ui.notify(f"✅ 序列已儲存 — {len(sequence.frames)} 幀", type="positive")
            applog.log.info(f"Sequence saved: {sid}, {len(sequence.frames)} frames")

        ui.button("🚀 生成序列", icon="burst_mode", on_click=gen_sequence).classes(
            "bg-purple-600 text-white text-lg px-6 py-3 rounded-xl"
        )


# ── Page: Video prompt ────────────────────────────────────────────────────────

@ui.page("/video")
def page_video():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-5xl mx-auto p-4 gap-4"):
        ui.label("🎬 影片提示詞生成").classes("text-2xl font-bold text-white")

        crefs = character_inputs()
        trefs = theme_style_inputs()
        _bind_char_template({**crefs, "style": trefs.get("style")})
        _bind_story_style_templates(trefs)

        with ui.expansion("🎬 電影規格", icon="camera", value=True).classes("w-full bg-gray-800"):
            cinrefs = cinema_inputs()

        with ui.expansion("🎥 影片設定", icon="videocam", value=True).classes("w-full bg-gray-800"):
            with ui.row().classes("flex-wrap gap-3 w-full"):
                dur_sel    = ui.select(DURATIONS,          value="5s",                   label="時長").classes("w-24")
                fps_sel    = ui.select(FPS_OPTIONS,        value="24fps (Cinematic)",    label="FPS").classes("w-44")
                move_sel   = ui.select(CAMERA_MOVEMENTS,   value="Dolly In",             label="攝影機運動").classes("w-44")
                motion_sel = ui.select(MOTION_INTENSITIES, value="Moderate",             label="動作強度").classes("w-32")
                num_clips  = ui.number(label="片段數", value=2, min=1, max=6, step=1).classes("w-28")
            neg_v = ui.input(label="負面提示詞(影片)", value=DEFAULT_NEG_V).classes("w-full")

        output_area = ui.column().classes("w-full gap-3")
        status_lbl  = ui.label("").classes("text-gray-400")

        async def gen_video():
            try:
                config.validate_config()
            except EnvironmentError as e:
                ui.notify(str(e), type="negative"); return
            if not crefs["desc_en"].value.strip():
                ui.notify("請填寫角色英文描述", type="warning"); return

            output_area.clear()
            n      = int(num_clips.value)
            char   = Character(name=crefs["name"].value or "Hero",
                                description=crefs["desc_en"].value,
                                description_zh=crefs["desc_zh"].value or crefs["desc_en"].value)
            cin    = _cinema(cinrefs["ar"].value, cinrefs["res"].value,
                              cinrefs["angle"].value, cinrefs["lens"].value,
                              cinrefs["light"].value, cinrefs["grade"].value,
                              cinrefs["dof"].value)
            sid      = str(uuid.uuid4())[:8]
            previous = None

            for i in range(n):
                status_lbl.set_text(f"⏳ 生成第 {i+1}/{n} 個片段…")
                try:
                    vf = await run.io_bound(
                        prompt_generator.generate_video_prompt,
                        character=char,
                        theme=trefs["theme"].value or "a cinematic scene",
                        cinema=cin,
                        duration=dur_sel.value,
                        fps=fps_sel.value.split("fps")[0].strip() + "fps",
                        camera_movement=move_sel.value,
                        motion_intensity=motion_sel.value,
                        negative_prompt=neg_v.value or DEFAULT_NEG_V,
                        frame_index=i + 1,
                        previous_frame=previous,
                        session_id=sid,
                    )
                    previous = vf
                    await run.io_bound(recorder.save_video_frame, vf)

                    with output_area:
                        with ui.card().classes("w-full bg-gray-800 p-3"):
                            ui.label(f"Clip {i+1} [{vf.duration} | {vf.fps} | {vf.camera_movement}]").classes(
                                "font-bold text-green-300")
                            _en_t = vf.prompt_en
                            _zh_t = vf.prompt_zh
                            with ui.row().classes("items-start gap-2 w-full"):
                                ui.label(_en_t).classes("flex-1 text-sm text-gray-200 font-mono")
                                _copy_btn(lambda t=_en_t: t)
                            with ui.row().classes("items-start gap-2 w-full"):
                                ui.label(_zh_t).classes("flex-1 text-sm text-gray-400")
                                _copy_btn(lambda t=_zh_t: t, color="bg-amber-500")
                            ui.label(f"角色動作: {vf.subject_motion_zh}").classes("text-xs text-yellow-300")
                except Exception as exc:
                    applog.log.error(f"Video clip {i+1} error: {exc}", exc_info=True)
                    with output_area:
                        ui.label(f"❌ Clip {i+1} 失敗：{exc}").classes("text-red-400")
                    ui.notify(f"Clip {i+1} 失敗：{exc}", type="negative")

            status_lbl.set_text(f"✅ 影片序列 {sid} 已儲存")
            ui.notify(f"✅ 影片序列已儲存 — {n} 片段", type="positive")
            applog.log.info(f"Video sequence saved: {sid}")

        ui.button("🚀 生成影片提示詞", icon="movie", on_click=gen_video).classes(
            "bg-green-600 text-white text-lg px-6 py-3 rounded-xl"
        )


# ── Page: Image-to-prompt ─────────────────────────────────────────────────────

@ui.page("/image2prompt")
def page_image2prompt():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-5xl mx-auto p-4 gap-4"):
        ui.label("📷 以圖生文").classes("text-2xl font-bold text-white")

        with ui.row().classes("flex-wrap gap-4 w-full"):
            uploaded_image: dict = {"path": None}
            upload = ui.upload(
                label="上傳參考圖片",
                auto_upload=True,
                on_upload=lambda e: uploaded_image.update({"path": e.name}),
            ).classes("flex-1")

        theme_input = ui.input(label="附加主題/方向 (可選)").classes("w-full")
        style_input = ui.input(label="風格", value=DEFAULT_STYLE).classes("w-full")
        neg_input   = ui.input(label="負面提示詞", value=DEFAULT_NEG).classes("w-full")

        with ui.expansion("🎬 電影規格", icon="camera", value=False).classes("w-full bg-gray-800"):
            cinrefs = cinema_inputs()

        with ui.row().classes("items-start gap-2 w-full"):
            result_en  = ui.textarea(label="✅ English Prompt").props("rows=5").classes("flex-1 font-mono")
            _copy_btn(lambda: result_en.value)
        with ui.row().classes("items-start gap-2 w-full"):
            result_zh  = ui.textarea(label="✅ 中文提示詞").props("rows=5").classes("flex-1 font-mono")
            _copy_btn(lambda: result_zh.value, color="bg-amber-500")

        async def gen_from_upload():
            try:
                config.validate_config()
            except EnvironmentError as e:
                ui.notify(str(e), type="negative"); return
            if not uploaded_image["path"]:
                ui.notify("請先上傳圖片", type="warning"); return
            cin   = _cinema(cinrefs["ar"].value, cinrefs["res"].value,
                             cinrefs["angle"].value, cinrefs["lens"].value,
                             cinrefs["light"].value, cinrefs["grade"].value,
                             cinrefs["dof"].value)
            full_style = f"{style_input.value or DEFAULT_STYLE}, {cin.to_prompt_tags()}"
            result_en.set_value("⏳ 分析圖片中…"); result_zh.set_value("⏳ …")
            try:
                frame = await run.io_bound(
                    prompt_generator.generate_from_image,
                    image_source=uploaded_image["path"],
                    theme=theme_input.value or "",
                    style=full_style,
                )
                frame.cinema = cin
                frame.negative_prompt = neg_input.value or DEFAULT_NEG
                await run.io_bound(recorder.save_frame, frame)
                result_en.set_value(frame.prompt_en)
                result_zh.set_value(frame.prompt_zh)
                ui.notify("✅ 圖片分析完成", type="positive")
                applog.log.info("Image-to-prompt generated from upload.")
            except Exception as exc:
                applog.log.error(f"image2prompt error: {exc}", exc_info=True)
                result_en.set_value(f"❌ 錯誤：{exc}"); result_zh.set_value("")
                ui.notify(f"失敗：{exc}", type="negative")

        ui.button("🔍 分析圖片生成提示詞", icon="image_search", on_click=gen_from_upload).classes(
            "bg-teal-600 text-white text-lg px-6 py-3 rounded-xl"
        )


# ── Page: Prompt library (view + edit) ───────────────────────────────────────

@ui.page("/library")
def page_library():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-5xl mx-auto p-4 gap-4"):
        ui.label("📋 提示詞庫").classes("text-2xl font-bold text-white")

        # ── Search bar ─────────────────────────
        with ui.row().classes("items-end gap-3 w-full"):
            kw_input   = ui.input(label="搜尋關鍵字").classes("flex-1")
            type_sel   = ui.select(["all", "image", "video"], value="all", label="類型").classes("w-28")
            count_sel  = ui.number(label="顯示筆數", value=30, min=5, max=200, step=5).classes("w-28")
            ui.button("🔍 搜尋", icon="search", on_click=lambda: refresh_list()).classes(
                "bg-blue-600 text-white px-4 py-2 rounded-lg"
            )

        records_state: dict = {"data": [], "type": "all"}
        cards_container = ui.column().classes("w-full gap-3")

        # ── Edit dialog ────────────────────────
        edit_state: dict = {"idx": None, "ptype": None}

        with ui.dialog() as edit_dialog, ui.card().classes("w-full max-w-2xl p-4 gap-3"):
            ui.label("✏️ 編輯提示詞").classes("text-xl font-bold text-white")
            ui.separator().classes("bg-gray-600")

            with ui.column().classes("w-full gap-1"):
                with ui.row().classes("items-center justify-between w-full"):
                    ui.label("English Prompt").classes("text-sm text-gray-400 font-semibold")
                    _dlg_copy_en_btn = _copy_btn(lambda: edit_en.value)
                edit_en  = ui.textarea().props("rows=4").classes("w-full font-mono text-sm")

            with ui.column().classes("w-full gap-1"):
                with ui.row().classes("items-center justify-between w-full"):
                    ui.label("中文提示詞").classes("text-sm text-gray-400 font-semibold")
                    _dlg_copy_zh_btn = _copy_btn(lambda: edit_zh.value, color="bg-amber-500")
                edit_zh  = ui.textarea().props("rows=4").classes("w-full font-mono text-sm")

            with ui.column().classes("w-full gap-1"):
                ui.label("負面提示詞").classes("text-sm text-gray-400 font-semibold")
                edit_neg = ui.input().classes("w-full")

            def save_edit():
                idx   = edit_state["idx"]
                ptype = edit_state["ptype"]
                if idx is None:
                    return
                ok = recorder.update_by_index_in_list(ptype, idx, {
                    "prompt_en": edit_en.value,
                    "prompt_zh": edit_zh.value,
                    "negative_prompt": edit_neg.value,
                })
                if ok:
                    ui.notify("✅ 已儲存", type="positive")
                    applog.log.info(f"Prompt edited: {ptype} index {idx}")
                    edit_dialog.close()
                    refresh_list()
                else:
                    ui.notify("❌ 儲存失敗", type="negative")

            ui.separator().classes("bg-gray-600")
            with ui.row().classes("gap-3"):
                ui.button("💾 儲存", icon="save", on_click=save_edit).classes(
                    "bg-green-600 text-white")
                ui.button("取消", icon="close", on_click=edit_dialog.close).classes(
                    "bg-gray-600 text-white")

        def open_edit(idx: int, record: dict, ptype: str) -> None:
            edit_state["idx"]   = idx
            edit_state["ptype"] = ptype
            edit_en.set_value(record.get("prompt_en", ""))
            edit_zh.set_value(record.get("prompt_zh", ""))
            edit_neg.set_value(record.get("negative_prompt", ""))
            edit_dialog.open()

        def delete_record(idx: int, ptype: str) -> None:
            ok = recorder.delete_by_index_in_list(ptype, idx)
            if ok:
                ui.notify("🗑 已刪除", type="positive")
                applog.log.info(f"Prompt deleted: {ptype} index {idx}")
                refresh_list()
            else:
                ui.notify("❌ 刪除失敗", type="negative")

        def refresh_list() -> None:
            kw    = kw_input.value.strip()
            ptype = type_sel.value
            count = int(count_sel.value)

            if kw:
                if ptype == "image":
                    data = recorder.search_by_keyword(kw)
                elif ptype == "video":
                    data = recorder.search_video_by_keyword(kw)
                else:
                    data = recorder.search_by_keyword(kw) + recorder.search_video_by_keyword(kw)
            else:
                data = recorder.load_all_prompts(ptype, count)

            records_state["data"]  = data
            records_state["type"]  = ptype
            cards_container.clear()

            if not data:
                with cards_container:
                    ui.label("尚無記錄 No records found.").classes("text-gray-400")
                return

            # Track the index into the original JSON files for edit/delete
            # We need to get the absolute JSON index.  For simplicity we pass idx=i
            # relative to the subset returned (works because update/delete_by_index_in_list
            # re-loads the full list).  To avoid confusion, reload fresh indices.
            img_all   = recorder._load_json(config.PROMPTS_JSON)
            vid_all   = recorder._load_json(config.VIDEO_PROMPTS_JSON)

            for record in data:
                rtype = record.get("prompt_type", ptype if ptype != "all" else "image")
                badge  = "🎬 VIDEO" if rtype == "video" else "🖼 IMAGE"
                ts     = str(record.get("created_at", ""))[:19]
                sid    = record.get("session_id", "")
                fi     = record.get("frame_index", "")
                cin    = record.get("cinema", {})
                ar     = cin.get("aspect_ratio", "")
                res    = cin.get("resolution", "")
                angle  = cin.get("camera_angle", "")

                # find absolute index for this record
                pool = vid_all if rtype == "video" else img_all
                try:
                    abs_idx = next(
                        j for j, r in enumerate(pool)
                        if r.get("session_id") == sid and r.get("frame_index") == fi
                    )
                except StopIteration:
                    abs_idx = -1

                with cards_container:
                    with ui.card().classes("w-full bg-gray-800 p-3 gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            ui.label(f"{badge} — {ts}  Session: {sid}  Frame: {fi}").classes(
                                "text-xs text-gray-400"
                            )
                            ui.label(f"{res} {ar} {angle}").classes("text-xs text-indigo-300")

                        _pen = record.get("prompt_en", "")
                        _pzh = record.get("prompt_zh", "")
                        with ui.row().classes("items-start gap-2 w-full"):
                            ui.label(_pen).classes("flex-1 text-sm text-gray-200 font-mono")
                            _copy_btn(lambda t=_pen: t)
                        with ui.row().classes("items-start gap-2 w-full"):
                            ui.label(_pzh).classes("flex-1 text-sm text-gray-400")
                            _copy_btn(lambda t=_pzh: t, color="bg-amber-500")

                        if rtype == "video":
                            ui.label(
                                f"運鏡: {record.get('camera_movement','')} | "
                                f"{record.get('duration','')} | {record.get('fps','')}"
                            ).classes("text-xs text-yellow-300")

                        with ui.row().classes("gap-2 mt-2"):
                            _idx   = abs_idx
                            _rt    = rtype
                            _rec   = dict(record)
                            ui.button("✏️ 編輯", icon="edit",
                                       on_click=lambda _i=_idx, _r=_rec, _t=_rt: open_edit(_i, _r, _t),
                                      ).classes("bg-indigo-600 text-white text-xs px-3 py-1")
                            ui.button("🗑 刪除", icon="delete",
                                       on_click=lambda _i=_idx, _t=_rt: delete_record(_i, _t),
                                      ).classes("bg-red-700 text-white text-xs px-3 py-1")

        # initial load
        refresh_list()


# ── Page: Log viewer ──────────────────────────────────────────────────────────

@ui.page("/logs")
def page_logs():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-5xl mx-auto p-4 gap-4"):
        ui.label("📜 操作記錄 / Logs").classes("text-2xl font-bold text-white")

        with ui.row().classes("items-center gap-3"):
            level_sel = ui.select(["ALL", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                                   value="ALL", label="篩選等級").classes("w-40")
            ui.button("🔄 刷新", icon="refresh", on_click=lambda: refresh_logs()).classes(
                "bg-blue-600 text-white px-4 py-2 rounded-lg"
            )
            ui.button("🗑 清除記憶體", icon="delete_sweep", on_click=lambda: (
                applog.clear_buffer(), refresh_logs(), ui.notify("已清除 buffer", type="positive")
            )).classes("bg-red-700 text-white px-4 py-2 rounded-lg")

            log_path = applog.get_log_file_path()
            ui.label(f"記錄檔案：{log_path}").classes("text-xs text-gray-500")

        log_container = ui.column().classes(
            "w-full h-96 overflow-y-auto bg-gray-900 rounded-xl p-3 font-mono text-xs gap-1"
        )

        def refresh_logs() -> None:
            entries = applog.get_log_entries(level_sel.value)
            log_container.clear()
            with log_container:
                if not entries:
                    ui.label("— 尚無記錄 —").classes("text-gray-500")
                    return
                for e in reversed(entries):
                    color = _level_color(e["level"])
                    ui.label(f"[{e['ts']}] [{e['level']}] {e['msg']}").classes(color)

        refresh_logs()

        # Auto-refresh every 3 seconds
        ui.timer(3.0, refresh_logs)


# ── Page: AI 補完 (Continuation) ─────────────────────────────────────────────

FIELD_LABELS = {
    "subject_en":    "主體 Subject (EN)",
    "subject_zh":    "主體 Subject (ZH)",
    "action_en":     "動作 Action (EN)",
    "action_zh":     "動作 Action (ZH)",
    "expression_en": "表情 Expression (EN)",
    "expression_zh": "表情 Expression (ZH)",
    "scene_en":      "場景 Scene (EN)",
    "scene_zh":      "場景 Scene (ZH)",
    "style_en":      "風格 Style (EN)",
    "style_zh":      "風格 Style (ZH)",
}
FIELD_KEYS = list(FIELD_LABELS.keys())


@ui.page("/continue")
def page_continue():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-5xl mx-auto p-4 gap-4"):
        ui.label("🤖 AI 補完提示詞").classes("text-2xl font-bold text-white")
        ui.label("鎖定想保留的欄位，讓 AI 補完其餘部分。每個欄位都可個別編輯。").classes(
            "text-gray-400 text-sm"
        )

        # ── Load from library ─────────────────────────────────────────
        with ui.expansion("📂 從提示詞庫載入", icon="folder_open", value=False).classes(
            "w-full bg-gray-800"
        ):
            with ui.row().classes("items-end gap-2 w-full"):
                lib_kw = ui.input(label="搜尋關鍵字").classes("flex-1")
                lib_type = ui.select(["image", "video"], value="image", label="類型").classes("w-24")

                lib_results   = ui.column().classes("w-full gap-2 mt-2")

                def do_lib_search():
                    kw = lib_kw.value.strip()
                    lib_results.clear()
                    data = (recorder.search_by_keyword(kw) if lib_type.value == "image"
                            else recorder.search_video_by_keyword(kw)) if kw else \
                           recorder.load_all_prompts(lib_type.value, 20)
                    with lib_results:
                        if not data:
                            ui.label("無結果").classes("text-gray-500")
                            return
                        for rec in data[:20]:
                            _pen = rec.get("prompt_en", "")
                            _pzh = rec.get("prompt_zh", "")
                            _ae  = rec.get("action_en", "")
                            _az  = rec.get("action_zh", "")
                            _ee  = rec.get("expression_en", "")
                            _ez  = rec.get("expression_zh", "")
                            _se  = rec.get("scene_en", "")
                            _sz  = rec.get("scene_zh", "")

                            def _load(r=rec, pe=_pen, pz=_pzh,
                                      ae=_ae, az=_az, ee=_ee, ez=_ez, se=_se, sz=_sz):
                                field_inputs["subject_en"].set_value(
                                    r.get("character", {}).get("description", pe[:80]) if isinstance(r.get("character"), dict) else pe[:80]
                                )
                                field_inputs["subject_zh"].set_value(
                                    r.get("character", {}).get("description_zh", pz[:80]) if isinstance(r.get("character"), dict) else pz[:80]
                                )
                                field_inputs["action_en"].set_value(ae)
                                field_inputs["action_zh"].set_value(az)
                                field_inputs["expression_en"].set_value(ee)
                                field_inputs["expression_zh"].set_value(ez)
                                field_inputs["scene_en"].set_value(se)
                                field_inputs["scene_zh"].set_value(sz)
                                field_inputs["style_en"].set_value(r.get("style_en", DEFAULT_STYLE))
                                field_inputs["style_zh"].set_value(r.get("style_zh", ""))
                                ui.notify("已載入 ✓", type="positive")

                            with ui.card().classes("w-full bg-gray-900 p-2"):
                                ui.label(_pen[:120] + ("…" if len(_pen) > 120 else "")).classes(
                                    "text-xs text-gray-300 font-mono"
                                )
                                ui.button("載入這筆", icon="download", on_click=_load).classes(
                                    "bg-teal-700 text-white text-xs mt-1"
                                )

                ui.button("🔍 搜尋", icon="search", on_click=do_lib_search).classes(
                    "bg-blue-600 text-white px-3 py-2"
                )

        # ── Field grid with lock toggles ──────────────────────────────
        ui.label("📝 欄位編輯（勾選 = 鎖定，AI 不修改）").classes("font-semibold text-gray-300 mt-2")

        field_inputs: dict[str, ui.textarea] = {}
        field_locks:  dict[str, ui.checkbox] = {}

        # Arrange in pairs (EN / ZH) side by side
        field_pairs = [
            ("subject_en",    "subject_zh"),
            ("action_en",     "action_zh"),
            ("expression_en", "expression_zh"),
            ("scene_en",      "scene_zh"),
            ("style_en",      "style_zh"),
        ]

        for en_key, zh_key in field_pairs:
            with ui.row().classes("w-full gap-2 items-start"):
                for key in (en_key, zh_key):
                    with ui.column().classes("flex-1 gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            field_locks[key] = ui.checkbox("🔒 鎖定").classes(
                                "text-xs text-yellow-400"
                            )
                            ui.label(FIELD_LABELS[key]).classes("text-xs text-gray-400")
                        field_inputs[key] = ui.textarea().props("rows=2").classes(
                            "w-full font-mono text-sm"
                        )
                        _copy_btn(lambda k=key: field_inputs[k].value)

        neg_input = ui.input(label="負面提示詞", value=DEFAULT_NEG).classes("w-full")

        # ── Direction hint ────────────────────────────────────────────
        direction = ui.input(
            label="🎯 補完方向 (可選，e.g. '下一幕在雨中', '改成驚訝表情', 'next tense action')"
        ).classes("w-full")

        # ── Result area ───────────────────────────────────────────────
        ui.separator().classes("bg-gray-700 my-2")
        ui.label("✅ 補完結果").classes("font-semibold text-green-300")

        result_fields: dict[str, ui.textarea] = {}
        result_pairs = list(field_pairs)

        for en_key, zh_key in result_pairs:
            with ui.row().classes("w-full gap-2 items-start"):
                for key in (en_key, zh_key):
                    with ui.column().classes("flex-1 gap-1"):
                        ui.label(FIELD_LABELS[key]).classes("text-xs text-gray-400")
                        result_fields[key] = ui.textarea().props("rows=2").classes(
                            "w-full font-mono text-sm bg-gray-800"
                        )
                        _copy_btn(lambda k=key: result_fields[k].value)

        with ui.row().classes("items-start gap-2 w-full"):
            full_en = ui.textarea(label="📋 完整英文提示詞").props("rows=4").classes(
                "flex-1 font-mono bg-gray-800"
            )
            _copy_btn(lambda: full_en.value)
        with ui.row().classes("items-start gap-2 w-full"):
            full_zh = ui.textarea(label="📋 完整中文提示詞").props("rows=4").classes(
                "flex-1 font-mono bg-gray-800"
            )
            _copy_btn(lambda: full_zh.value, color="bg-amber-500")

        # ── Generate button ───────────────────────────────────────────
        gen_btn = ui.button("🤖 AI 補完", icon="auto_fix_high").classes(
            "bg-rose-600 text-white text-lg px-6 py-3 rounded-xl"
        )

        async def do_continue():
            try:
                config.validate_config()
            except EnvironmentError as e:
                ui.notify(str(e), type="negative"); return

            locked: dict = {}
            unlocked: list = []
            for key in FIELD_KEYS:
                val = field_inputs[key].value.strip()
                if field_locks[key].value and val:
                    locked[key] = val
                else:
                    unlocked.append(key)

            if not locked:
                ui.notify("請至少鎖定一個欄位作為 AI 補完的基礎", type="warning"); return

            gen_btn.set_text("⏳ AI 補完中…")
            try:
                result = await run.io_bound(
                    prompt_generator.generate_continuation,
                    locked_fields=locked,
                    unlock_targets=unlocked,
                    direction_hint=direction.value.strip(),
                    style=field_inputs["style_en"].value.strip() or DEFAULT_STYLE,
                    negative_prompt=neg_input.value,
                )
                for key in FIELD_KEYS:
                    v = result.get(key, "")
                    result_fields[key].set_value(v)
                    # Also propagate back to input fields if unlocked (so user can re-lock and regenerate)
                    if not field_locks[key].value:
                        field_inputs[key].set_value(v)

                full_en.set_value(result.get("prompt_en", ""))
                full_zh.set_value(result.get("prompt_zh", ""))
                ui.notify("✅ 補完完成", type="positive")
                applog.log.info(f"AI continuation generated. locked={list(locked.keys())}")
            except Exception as exc:
                applog.log.error(f"continuation error: {exc}", exc_info=True)
                ui.notify(f"補完失敗：{exc}", type="negative")
            finally:
                gen_btn.set_text("🤖 AI 補完")

        gen_btn.on("click", do_continue)

        # ── Save result to library ───────────────────────────────────
        async def save_result():
            from models import PromptFrame, Character, CinemaSettings
            import uuid
            frame = PromptFrame(
                session_id=str(uuid.uuid4())[:8],
                frame_index=1,
                character=Character(
                    description=result_fields.get("subject_en", ui.textarea()).value or "AI completed",
                    description_zh=result_fields.get("subject_zh", ui.textarea()).value or "",
                ),
                action_en=result_fields["action_en"].value,
                action_zh=result_fields["action_zh"].value,
                expression_en=result_fields["expression_en"].value,
                expression_zh=result_fields["expression_zh"].value,
                scene_en=result_fields["scene_en"].value,
                scene_zh=result_fields["scene_zh"].value,
                prompt_en=full_en.value,
                prompt_zh=full_zh.value,
                negative_prompt=neg_input.value,
                style_en=result_fields["style_en"].value,
                style_zh=result_fields["style_zh"].value,
            )
            await run.io_bound(recorder.save_frame, frame)
            ui.notify("✅ 已儲存至提示詞庫", type="positive")
            applog.log.info(f"Continuation saved to library: {frame.session_id}")

        ui.button("💾 儲存至提示詞庫", icon="save", on_click=save_result).classes(
            "bg-green-600 text-white px-5 py-2 rounded-xl"
        )


# ── Page: Settings ────────────────────────────────────────────────────────────

@ui.page("/settings")
def page_settings():
    _page_setup()
    _sidebar()
    with ui.column().classes("w-full max-w-3xl mx-auto p-4 gap-6"):
        ui.label("⚙ 設定").classes("text-2xl font-bold text-white")

        # ── Provider selector ─────────────────────────────────────────
        with ui.card().classes("w-full bg-gray-800 p-4 gap-3"):
            ui.label("API 來源").classes("text-lg font-semibold text-indigo-300")
            provider_radio = ui.radio(
                {"openrouter": "☁ OpenRouter (雲端)", "ollama": "🖥 Ollama (本機)"},
                value=config.API_PROVIDER,
            ).classes("text-white")

        # ── OpenRouter settings ───────────────────────────────────────
        with ui.card().classes("w-full bg-gray-800 p-4 gap-3") as or_card:
            ui.label("☁ OpenRouter 設定").classes("text-lg font-semibold text-blue-300")
            or_key   = ui.input(label="API Key", value=config.OPENROUTER_API_KEY,
                                 password=True, password_toggle_button=True).classes("w-full")
            or_model = ui.input(label="文字模型", value=config.OPENROUTER_MODEL).classes("w-full")
            or_vis   = ui.input(label="視覺模型", value=config.OPENROUTER_VISION_MODEL).classes("w-full")
            ui.link("取得 API Key → openrouter.ai/keys",
                    "https://openrouter.ai/keys", new_tab=True).classes("text-xs text-blue-400")

        # ── Ollama settings ───────────────────────────────────────────
        with ui.card().classes("w-full bg-gray-800 p-4 gap-3") as ol_card:
            ui.label("🖥 Ollama 本機設定").classes("text-lg font-semibold text-green-300")
            ol_url   = ui.input(label="Ollama Base URL", value=config.OLLAMA_BASE_URL).classes("w-full")
            ol_model = ui.input(label="文字模型 (e.g. llama3, mistral)", value=config.OLLAMA_MODEL).classes("w-full")
            ol_vis   = ui.input(label="視覺模型 (e.g. llava)", value=config.OLLAMA_VISION_MODEL).classes("w-full")
            ui.label("確保 Ollama 已在本機執行：ollama serve").classes("text-xs text-gray-400")

        # ── Think Mode ────────────────────────────────────────────────
        with ui.card().classes("w-full bg-gray-800 p-4 gap-2"):
            ui.label("🧠 Think Mode（推理模式）").classes("text-lg font-semibold text-purple-300")
            think_toggle = ui.switch(
                "啟用 Think Mode（Qwen3 等模型支援深度推理，更準確但較慢）",
                value=config.THINK_MODE,
            ).classes("text-white")
            ui.label(
                "關閉後會在提示詞前加入 /no-think，讓模型跳過思考鏈直接回答（速度較快）。"
            ).classes("text-xs text-gray-400")

        # Show/hide cards based on selection
        def _update_cards():
            is_or = provider_radio.value == "openrouter"
            or_card.set_visibility(is_or)
            ol_card.set_visibility(not is_or)

        provider_radio.on("update:model-value", lambda: _update_cards())
        _update_cards()

        # ── Save ──────────────────────────────────────────────────────
        def do_save():
            config.save_settings(
                provider=provider_radio.value,
                openrouter_key=or_key.value.strip(),
                openrouter_model=or_model.value.strip() or config.OPENROUTER_MODEL,
                openrouter_vision_model=or_vis.value.strip() or config.OPENROUTER_VISION_MODEL,
                ollama_base_url=ol_url.value.strip() or "http://localhost:11434/v1",
                ollama_model=ol_model.value.strip() or "llama3",
                ollama_vision_model=ol_vis.value.strip() or "llava",
                think_mode=think_toggle.value,
            )
            applog.log.info(f"Settings saved. provider={config.API_PROVIDER}, think_mode={config.THINK_MODE}")
            ui.notify(f"✅ 設定已儲存（{config.API_PROVIDER}）", type="positive")

        async def do_test():
            try:
                config.validate_config()
            except EnvironmentError as e:
                ui.notify(str(e), type="negative"); return
            try:
                r = await run.io_bound(
                    prompt_generator.autocomplete_character, "test connection"
                )
                ui.notify(f"✅ 連線成功 — model responded: {r.get('name','OK')}", type="positive")
            except Exception as exc:
                ui.notify(f"❌ 連線失敗：{exc}", type="negative")

        with ui.row().classes("gap-3"):
            ui.button("💾 儲存設定", icon="save", on_click=do_save).classes(
                "bg-green-600 text-white px-6 py-3 rounded-xl"
            )
            ui.button("🔌 測試連線", icon="electrical_services", on_click=do_test).classes(
                "bg-blue-600 text-white px-6 py-3 rounded-xl"
            )

        # ── Current config display ────────────────────────────────────
        def show_info():
            prov = config.API_PROVIDER
            think_str = "🧠 Think ON" if config.THINK_MODE else "⚡ Think OFF"
            if prov == "ollama":
                return f"**目前使用**：Ollama 本機 — `{config.OLLAMA_BASE_URL}` 模型：`{config.OLLAMA_MODEL}` | {think_str}"
            key_hint = ("*" * 8 + config.OPENROUTER_API_KEY[-4:]) if len(config.OPENROUTER_API_KEY) > 4 else "(未設定)"
            return f"**目前使用**：OpenRouter — 模型：`{config.OPENROUTER_MODEL}` Key：`{key_hint}` | {think_str}"

        info_md = ui.markdown(show_info()).classes("text-gray-300 text-sm")
        ui.timer(2.0, lambda: info_md.set_content(show_info()))


# ── Sidebar navigation ────────────────────────────────────────────────────────

def _sidebar() -> None:
    with ui.left_drawer(top_corner=True, bottom_corner=True).classes(
        "bg-gray-900 text-white w-52 pt-4"
    ):
        ui.label("🎬 Prompt Studio").classes("text-xl font-bold px-4 pb-4 text-indigo-300")
        ui.separator().classes("bg-gray-700")
        _nav_btn("🏠 單張圖片",    "/",            "image")
        _nav_btn("🔄 圖片序列",    "/sequence",    "burst_mode")
        _nav_btn("🎬 影片提示詞",  "/video",       "movie")
        _nav_btn("📷 以圖生文",    "/image2prompt","image_search")
        _nav_btn("🤖 AI 補完",     "/continue",    "auto_fix_high")
        _nav_btn("📋 提示詞庫",    "/library",     "library_books")
        _nav_btn("📜 操作記錄",    "/logs",        "history")
        _nav_btn("⚙ 設定",        "/settings",    "settings")
        ui.separator().classes("bg-gray-700 mt-auto")
        ui.label("v2.1 NiceGUI").classes("text-xs text-gray-600 px-4 py-2")


def _nav_btn(label: str, path: str, icon: str) -> None:
    ui.button(label, icon=icon,
               on_click=lambda p=path: ui.navigate.to(p)).classes(
        "w-full text-left text-white bg-transparent hover:bg-gray-700 rounded-none px-4 py-2"
    )


# ── Per-page setup ───────────────────────────────────────────────────────────

def _page_setup() -> None:
    """Apply global dark theme — must be called inside every @ui.page function."""
    ui.query("body").classes("bg-gray-950 text-white")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ in {"__main__", "__mp_main__"}:
    applog.log.info("Prompt Studio starting — NiceGUI mode")
    try:
        config.validate_config()
        applog.log.info("API key validated ✓")
    except EnvironmentError as e:
        applog.log.warning(f"Config warning: {e}")

    ui.run(
        title="🎬 Prompt Studio — AI Image & Video Generator",
        host="127.0.0.1",
        port=8080,
        native=True,
        window_size=(1280, 860),
        dark=True,
        favicon="🎬",
        reload=False,
    )
