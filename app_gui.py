"""Gradio GUI — AI Image & Video Prompt Generator (Director Edition)."""
from __future__ import annotations
import sys
import gradio as gr

import config
import image_utils
import prompt_generator
import recorder
import templates
from models import Character, CinemaSettings

# ── Option lists ──────────────────────────────────────────────────────────────

ASPECT_RATIOS   = ["16:9", "9:16", "1:1", "4:3", "21:9", "2.35:1 Anamorphic", "4:5", "3:2"]
RESOLUTIONS     = ["4K (3840×2160)", "8K (7680×4320)", "2K (2560×1440)", "1080p (1920×1080)"]
CAMERA_ANGLES   = ["Eye Level", "Low Angle", "High Angle", "Bird's Eye View",
                   "Dutch Angle", "Over-the-Shoulder", "POV", "Worm's Eye View"]
CAMERA_LENSES   = ["14mm Ultra Wide", "24mm Wide", "35mm Standard Wide",
                   "50mm Normal", "85mm Portrait", "135mm Telephoto",
                   "200mm Long Telephoto", "Macro"]
LIGHTINGS       = ["Cinematic Natural Light", "Golden Hour", "Blue Hour",
                   "High Key Studio", "Low Key Dramatic", "Rim / Back Light",
                   "Chiaroscuro", "Neon City Light", "Candlelight", "Overcast Soft"]
COLOR_GRADES    = ["Cinematic Warm", "Cool Desaturated", "Teal & Orange",
                   "Black & White", "Vibrant Saturated", "Bleach Bypass", "Kodak Film"]
DOF_OPTIONS     = ["Shallow (f/1.4)", "Shallow (f/1.8)", "Standard (f/2.8)",
                   "Mid (f/5.6)", "Deep (f/8)", "Hyperfocal"]
DURATIONS       = ["3s", "4s", "5s", "6s", "8s", "10s", "15s"]
FPS_OPTIONS     = ["24fps (Cinematic)", "25fps (PAL)", "30fps (Standard)", "60fps (Smooth)"]
CAMERA_MOVEMENTS = [
    "Static", "Slow Pan Left", "Slow Pan Right", "Tilt Up", "Tilt Down",
    "Zoom In (Push)", "Zoom Out (Pull)", "Dolly In", "Dolly Out",
    "Tracking Shot", "Arc Shot (Left)", "Arc Shot (Right)",
    "Crane Up", "Crane Down", "Handheld / Shaky Cam", "360° Orbit"
]
MOTION_INTENSITIES = ["Subtle", "Moderate", "Dynamic", "Extreme"]

DEFAULT_STYLE = "cinematic photography, highly detailed"
DEFAULT_NEG   = "blurry, low quality, watermark, text, deformed, artifacts"
DEFAULT_NEG_V = "static, blurry, low quality, watermark, deformed, flickering, jitter"


# ── Shared helpers ────────────────────────────────────────────────────────────

def _frame_to_display(frame) -> tuple[str, str, str]:
    c = frame.cinema
    specs = f"**{c.resolution}** | **{c.aspect_ratio}** | {c.camera_angle} | {c.camera_lens} | {c.lighting} | {c.color_grade}"
    detail = (
        f"{specs}\n\n"
        f"**動作 / Action:** {frame.action_zh} / {frame.action_en}\n\n"
        f"**表情 / Expression:** {frame.expression_zh} / {frame.expression_en}\n\n"
        f"**場景 / Scene:** {frame.scene_zh} / {frame.scene_en}\n\n"
        f"**連續性:** {frame.continuity_note_zh}"
    )
    return frame.prompt_en, frame.prompt_zh, detail


def _cinema_from_inputs(ar, res, angle, lens, light, grade, dof) -> CinemaSettings:
    return CinemaSettings(
        aspect_ratio=ar, resolution=res.split(" ")[0],
        camera_angle=angle, camera_lens=lens,
        lighting=light, color_grade=grade, depth_of_field=dof,
    )


def _build_project_image_choices() -> list[str]:
    return [str(p) for p in image_utils.scan_project_images(config.IMAGES_DIR)]


# ── Template loaders ─────────────────────────────────────────────────────────

def apply_char_template(label: str):
    t = templates.get_char(label)
    if not t:
        return gr.update(), gr.update(), gr.update()
    return t["name"], t["description_en"], t["description_zh"]

def apply_story_template(label: str):
    t = templates.get_story(label)
    if not t:
        return gr.update()
    return t["theme_zh"] + "\n" + t["theme_en"]

def apply_style_template(label: str):
    t = templates.get_style(label)
    if not t:
        return gr.update()
    return t["style"]


# ── Tab 1: Image Text generation ──────────────────────────────────────────────

def autofill_character(short_input: str):
    if not short_input.strip():
        return "", "", "", "", ""
    try:
        config.validate_config()
    except EnvironmentError as e:
        return str(e), "", "", "", ""
    r = prompt_generator.autocomplete_character(short_input.strip())
    return r["name"], r["description_en"], r["description_zh"], \
           r["theme_zh"] + " / " + r["theme_en"], r["style"]


def gen_single_text(name, desc, desc_zh, theme, style,
                    ar, res, angle, lens, light, grade, dof, neg):
    try:
        config.validate_config()
    except EnvironmentError as e:
        return str(e), "", ""
    if not desc.strip():
        return "請填寫角色英文描述 / Please enter character description.", "", ""
    char   = Character(name=name or "Hero", description=desc, description_zh=desc_zh or desc)
    cinema = _cinema_from_inputs(ar, res, angle, lens, light, grade, dof)
    frame  = prompt_generator.generate_frame(
        character=char, theme=theme or "a dramatic moment",
        style=style or DEFAULT_STYLE, cinema=cinema,
    )
    frame.negative_prompt = neg or DEFAULT_NEG
    recorder.save_frame(frame)
    return _frame_to_display(frame)


def gen_sequence_text(name, desc, desc_zh, theme, num_frames, style,
                      ar, res, angle, lens, light, grade, dof, neg):
    try:
        config.validate_config()
    except EnvironmentError as e:
        return "", str(e)
    if not desc.strip():
        return "", "請填寫角色英文描述 / Please enter character description."
    char   = Character(name=name or "Hero", description=desc, description_zh=desc_zh or desc)
    cinema = _cinema_from_inputs(ar, res, angle, lens, light, grade, dof)
    n      = max(2, min(8, int(num_frames)))

    from models import PromptSequence
    import uuid
    sid      = str(uuid.uuid4())[:8]
    sequence = PromptSequence(session_id=sid, character=char)
    previous = None
    for i in range(n):
        f = prompt_generator.generate_frame(
            character=char, theme=theme or "a dramatic scene",
            frame_index=i + 1, previous_frame=previous,
            style=style or DEFAULT_STYLE, cinema=cinema, session_id=sid,
        )
        f.negative_prompt = neg or DEFAULT_NEG
        sequence.frames.append(f)
        previous = f
    recorder.save_sequence(sequence)

    md = [f"## Sequence `{sid}` — {n} frames\n"]
    for f in sequence.frames:
        c = f.cinema
        md.append(
            f"### Frame {f.frame_index}\n"
            f"> **EN:** {f.prompt_en}\n\n"
            f"> **中文:** {f.prompt_zh}\n\n"
            f"*{c.resolution} | {c.aspect_ratio} | {c.camera_angle} | {c.lighting}*\n"
            f"*動作:* {f.action_zh} | *表情:* {f.expression_zh} | *場景:* {f.scene_zh}\n\n---\n"
        )
    return "\n".join(md), f"✓ 已儲存 `{config.PROMPTS_MD}`"


# ── Tab 2: Image from image ───────────────────────────────────────────────────

def refresh_project_images():
    choices = _build_project_image_choices()
    return gr.update(choices=choices, value=choices[0] if choices else None)


def gen_from_upload(image_file, theme, style, ar, res, angle, lens, light, grade, dof, neg):
    try:
        config.validate_config()
    except EnvironmentError as e:
        return str(e), "", ""
    if image_file is None:
        return "請上傳圖片 / Please upload an image.", "", ""
    cinema = _cinema_from_inputs(ar, res, angle, lens, light, grade, dof)
    full_style = f"{style or DEFAULT_STYLE}, {cinema.to_prompt_tags()}"
    frame = prompt_generator.generate_from_image(
        image_source=image_file, theme=theme or "", style=full_style,
    )
    frame.cinema = cinema
    frame.negative_prompt = neg or DEFAULT_NEG
    recorder.save_frame(frame)
    return _frame_to_display(frame)


def gen_from_project_image(image_path, theme, style, ar, res, angle, lens, light, grade, dof, neg):
    try:
        config.validate_config()
    except EnvironmentError as e:
        return str(e), "", ""
    if not image_path:
        return "請選擇圖片 / Please select an image.", "", ""
    cinema = _cinema_from_inputs(ar, res, angle, lens, light, grade, dof)
    full_style = f"{style or DEFAULT_STYLE}, {cinema.to_prompt_tags()}"
    frame = prompt_generator.generate_from_image(
        image_source=image_path, theme=theme or "", style=full_style,
    )
    frame.cinema = cinema
    frame.negative_prompt = neg or DEFAULT_NEG
    recorder.save_frame(frame)
    return _frame_to_display(frame)


# ── Tab 3: Video prompt ───────────────────────────────────────────────────────

def gen_video_prompt(name, desc, desc_zh, theme, style,
                     ar, res, angle, lens, light, grade, dof,
                     duration, fps, cam_move, motion_intensity, neg_v,
                     num_clips):
    try:
        config.validate_config()
    except EnvironmentError as e:
        return "", str(e)
    if not desc.strip():
        return "", "請填寫角色英文描述 / Please enter character description."

    char   = Character(name=name or "Hero", description=desc, description_zh=desc_zh or desc)
    cinema = _cinema_from_inputs(ar, res, angle, lens, light, grade, dof)
    n      = max(1, min(6, int(num_clips)))

    import uuid
    sid      = str(uuid.uuid4())[:8]
    frames   = []
    previous = None

    for i in range(n):
        vf = prompt_generator.generate_video_prompt(
            character=char, theme=theme or "a cinematic scene",
            cinema=cinema, duration=duration, fps=fps.split("fps")[0].strip() + "fps",
            camera_movement=cam_move, motion_intensity=motion_intensity,
            negative_prompt=neg_v or DEFAULT_NEG_V,
            frame_index=i + 1, previous_frame=previous, session_id=sid,
        )
        frames.append(vf)
        recorder.save_video_frame(vf)
        previous = vf

    md = [f"## Video Sequence `{sid}` — {n} clips\n"]
    for vf in frames:
        c = vf.cinema
        md.append(
            f"### Clip {vf.frame_index}  [{vf.duration} | {vf.fps} | {vf.camera_movement}]\n"
            f"> **EN:** {vf.prompt_en}\n\n"
            f"> **中文:** {vf.prompt_zh}\n\n"
            f"*規格: {c.resolution} | {c.aspect_ratio} | {c.camera_angle} | {c.lighting}*\n"
            f"*角色動作:* {vf.subject_motion_zh}\n"
            f"*表情:* {vf.expression_zh} | *場景:* {vf.scene_zh}\n"
            f"*Negative:* `{vf.negative_prompt}`\n"
            f"*連續性:* {vf.continuity_note_zh}\n\n---\n"
        )
    return "\n".join(md), f"✓ 已儲存 `{config.VIDEO_PROMPTS_MD}`"


# ── Tab 4: Prompt Viewer ──────────────────────────────────────────────────────

def load_viewer(prompt_type: str, keyword: str, count: int) -> str:
    if keyword.strip():
        if prompt_type == "image":
            records = recorder.search_by_keyword(keyword)
        elif prompt_type == "video":
            records = recorder.search_video_by_keyword(keyword)
        else:
            records = (recorder.search_by_keyword(keyword) +
                       recorder.search_video_by_keyword(keyword))
    else:
        records = recorder.load_all_prompts(prompt_type, int(count))

    if not records:
        return "尚無記錄 No records found."

    lines = []
    for r in records:
        ptype  = r.get("prompt_type", "image")
        badge  = "🎬 VIDEO" if ptype == "video" else "🖼 IMAGE"
        ts     = str(r.get("created_at", ""))[:19]
        sid    = r.get("session_id", "")
        fidx   = r.get("frame_index", "")
        cinema = r.get("cinema", {})
        ar     = cinema.get("aspect_ratio", "")
        res    = cinema.get("resolution", "")
        angle  = cinema.get("camera_angle", "")
        light  = cinema.get("lighting", "")

        specs_line = f"`{res}` `{ar}` `{angle}` `{light}`"

        if ptype == "video":
            extra = (
                f"**運鏡:** {r.get('camera_movement','')} | "
                f"**時長:** {r.get('duration','')} | "
                f"**FPS:** {r.get('fps','')}\n\n"
                f"**角色動作:** {r.get('subject_motion_zh','')}"
            )
        else:
            extra = (
                f"**動作:** {r.get('action_zh','')} | "
                f"**表情:** {r.get('expression_zh','')}"
            )

        lines.append(
            f"### {badge} — Frame {fidx} · Session `{sid}` · {ts}\n"
            f"{specs_line}\n\n"
            f"**EN Prompt:**\n```\n{r.get('prompt_en','')}\n```\n\n"
            f"**中文提示詞:**\n```\n{r.get('prompt_zh','')}\n```\n\n"
            f"{extra}\n\n"
            f"**場景:** {r.get('scene_zh','')}\n\n"
            f"**Negative:** `{r.get('negative_prompt','')}`\n\n"
            f"**連續性:** {r.get('continuity_note_zh','')}\n\n---\n"
        )
    return "\n".join(lines)


# ── Cinema settings block (reusable) ─────────────────────────────────────────

def _cinema_block(prefix: str = ""):
    """Return a list of Gradio components for cinema settings."""
    with gr.Group():
        gr.Markdown("##### 攝影規格 Cinema Settings")
        with gr.Row():
            ar    = gr.Dropdown(ASPECT_RATIOS,   value="16:9",                     label="比例 Aspect Ratio")
            res   = gr.Dropdown(RESOLUTIONS,     value="4K (3840×2160)",            label="解析度 Resolution")
            dof   = gr.Dropdown(DOF_OPTIONS,     value="Shallow (f/1.8)",           label="景深 Depth of Field")
        with gr.Row():
            angle = gr.Dropdown(CAMERA_ANGLES,   value="Eye Level",                label="鏡頭角度 Camera Angle")
            lens  = gr.Dropdown(CAMERA_LENSES,   value="35mm Standard Wide",       label="鏡頭焦距 Lens")
        with gr.Row():
            light = gr.Dropdown(LIGHTINGS,       value="Cinematic Natural Light",  label="燈光 Lighting")
            grade = gr.Dropdown(COLOR_GRADES,    value="Cinematic Warm",           label="調色 Color Grade")
    return ar, res, angle, lens, light, grade, dof


# ── Build app ─────────────────────────────────────────────────────────────────

def build_app() -> gr.Blocks:
    with gr.Blocks(
        title="AI 圖片・影片提示詞生成器",
        theme=gr.themes.Soft(),
        css="""
        .prompt-box textarea { font-family: monospace; font-size: 13px; }
        .badge-video { color: #e05; font-weight: bold; }
        """,
    ) as demo:

        gr.Markdown(
            "# AI 圖片・影片提示詞生成器 (Director Edition)\n"
            "Powered by **OpenRouter** · `qwen/qwen3.6-plus-preview` · `bytedance-seed/seed-2.0-mini`"
        )

        with gr.Tabs():

            # ── Tab 1: Image (Text) ──────────────────────────────────────────
            with gr.Tab("🖼 圖片提示詞"):
                gr.Markdown("### 文字生成圖片提示詞")

                with gr.Group():
                    gr.Markdown("#### ⚡ 快速輸入 — AI 自動補完所有欄位")
                    with gr.Row():
                        quick_input = gr.Textbox(
                            placeholder='例如: "A asian woman"、"老武士"、"neon city girl"',
                            label="簡短描述 Short Description", scale=4,
                        )
                        btn_autofill = gr.Button("AI 自動補完", variant="secondary", scale=1)

                gr.Markdown("---")

                with gr.Row():
                    with gr.Column(scale=1):
                        # ── Templates ────────────────────────────────────────
                        with gr.Group():
                            gr.Markdown("##### 🗂 情境模板 Presets")
                            with gr.Row():
                                tpl_char  = gr.Dropdown(templates.char_labels(),
                                    label="角色模板 Character", scale=2)
                                btn_tchar = gr.Button("套用", size="sm", scale=1)
                            with gr.Row():
                                tpl_story  = gr.Dropdown(templates.story_labels(),
                                    label="故事模板 Story", scale=2)
                                btn_tstory = gr.Button("套用", size="sm", scale=1)
                            with gr.Row():
                                tpl_style  = gr.Dropdown(templates.style_labels(),
                                    label="風格模板 Style", scale=2)
                                btn_tstyle = gr.Button("套用", size="sm", scale=1)

                        gr.Markdown("##### 角色設定 Character")
                        t_name    = gr.Textbox(label="名稱 Name", value="Hero")
                        t_desc    = gr.Textbox(label="英文描述 Description (EN)*",
                                               placeholder="a young woman with silver hair...")
                        t_desc_zh = gr.Textbox(label="中文描述 Description (ZH)",
                                               placeholder="銀髮年輕女性...")
                        t_theme   = gr.Textbox(label="故事主題 Theme",
                                               placeholder="在廢墟中尋找希望")
                        t_style   = gr.Textbox(label="風格 Style", value=DEFAULT_STYLE)
                        t_neg     = gr.Textbox(label="Negative Prompt", value=DEFAULT_NEG)

                        t_ar, t_res, t_angle, t_lens, t_light, t_grade, t_dof = _cinema_block("t")

                    with gr.Column(scale=2):
                        gr.Markdown("#### 單張 Single Frame")
                        btn_single = gr.Button("生成單張 Generate", variant="primary")
                        out_en     = gr.Textbox(label="English Prompt", lines=4,
                                                interactive=False, elem_classes="prompt-box")
                        out_zh     = gr.Textbox(label="中文提示詞", lines=4,
                                                interactive=False, elem_classes="prompt-box")
                        out_detail = gr.Markdown()

                        gr.Markdown("---")
                        gr.Markdown("#### 連續分鏡 Sequence")
                        with gr.Row():
                            t_frames = gr.Slider(2, 8, value=4, step=1, label="分鏡數 Frames")
                            btn_seq  = gr.Button("生成序列 Generate Sequence", variant="primary")
                        out_seq      = gr.Markdown()
                        out_seq_info = gr.Markdown()

                btn_autofill.click(autofill_character, [quick_input],
                                   [t_name, t_desc, t_desc_zh, t_theme, t_style])
                btn_tchar.click(apply_char_template,  [tpl_char],  [t_name, t_desc, t_desc_zh])
                btn_tstory.click(apply_story_template, [tpl_story], [t_theme])
                btn_tstyle.click(apply_style_template, [tpl_style], [t_style])
                btn_single.click(gen_single_text,
                    [t_name, t_desc, t_desc_zh, t_theme, t_style,
                     t_ar, t_res, t_angle, t_lens, t_light, t_grade, t_dof, t_neg],
                    [out_en, out_zh, out_detail])
                btn_seq.click(gen_sequence_text,
                    [t_name, t_desc, t_desc_zh, t_theme, t_frames, t_style,
                     t_ar, t_res, t_angle, t_lens, t_light, t_grade, t_dof, t_neg],
                    [out_seq, out_seq_info])

            # ── Tab 2: Image from image ──────────────────────────────────────
            with gr.Tab("📷 圖片分析"):
                gr.Markdown(f"### 上傳或選擇圖片，AI 分析生成提示詞\n圖片資料夾: `{config.IMAGES_DIR}/`")

                with gr.Row():
                    with gr.Column(scale=1):
                        i_theme = gr.Textbox(label="額外主題 Theme (optional)",
                                             placeholder="延伸場景動作")
                        i_style = gr.Textbox(label="風格 Style", value=DEFAULT_STYLE)
                        i_neg   = gr.Textbox(label="Negative Prompt", value=DEFAULT_NEG)
                        i_ar, i_res, i_angle, i_lens, i_light, i_grade, i_dof = _cinema_block("i")

                    with gr.Column(scale=2):
                        with gr.Tabs():
                            with gr.Tab("上傳圖片 Upload"):
                                i_upload  = gr.Image(label="拖拽上傳 Drop / Click",
                                                     type="filepath", height=280)
                                btn_upload = gr.Button("分析上傳圖片", variant="primary")

                            with gr.Tab("專案圖片 Project"):
                                gr.Markdown(f"將圖片放入 `{config.IMAGES_DIR}/` 後點重新整理")
                                btn_refresh = gr.Button("重新整理 Refresh", size="sm")
                                i_project   = gr.Dropdown(choices=_build_project_image_choices(),
                                                          label="選擇圖片", interactive=True)
                                i_preview   = gr.Image(label="預覽", height=220, interactive=False)
                                btn_project = gr.Button("分析選擇圖片", variant="primary")

                with gr.Row():
                    i_out_en     = gr.Textbox(label="English Prompt", lines=4,
                                              interactive=False, elem_classes="prompt-box")
                    i_out_zh     = gr.Textbox(label="中文提示詞", lines=4,
                                              interactive=False, elem_classes="prompt-box")
                i_out_detail = gr.Markdown()

                img_inputs = [i_theme, i_style, i_ar, i_res, i_angle, i_lens, i_light, i_grade, i_dof, i_neg]
                btn_upload.click(gen_from_upload, [i_upload] + img_inputs,
                                 [i_out_en, i_out_zh, i_out_detail])
                btn_refresh.click(refresh_project_images, [], [i_project])
                i_project.change(lambda p: p, [i_project], [i_preview])
                btn_project.click(gen_from_project_image, [i_project] + img_inputs,
                                  [i_out_en, i_out_zh, i_out_detail])

            # ── Tab 3: Video prompt ──────────────────────────────────────────
            with gr.Tab("🎬 影片提示詞"):
                gr.Markdown("### AI 影片提示詞生成器\n適用: Runway Gen-3 · Kling AI · Pika · Sora · Luma")

                with gr.Row():
                    with gr.Column(scale=1):
                        # ── Templates ────────────────────────────────────────
                        with gr.Group():
                            gr.Markdown("##### 🗂 情境模板 Presets")
                            with gr.Row():
                                vtpl_char  = gr.Dropdown(templates.char_labels(),
                                    label="角色模板 Character", scale=2)
                                vbtn_tchar = gr.Button("套用", size="sm", scale=1)
                            with gr.Row():
                                vtpl_story  = gr.Dropdown(templates.story_labels(),
                                    label="故事模板 Story", scale=2)
                                vbtn_tstory = gr.Button("套用", size="sm", scale=1)
                            with gr.Row():
                                vtpl_style  = gr.Dropdown(templates.style_labels(),
                                    label="風格模板 Style", scale=2)
                                vbtn_tstyle = gr.Button("套用", size="sm", scale=1)

                        gr.Markdown("##### 角色設定 Character")
                        v_name    = gr.Textbox(label="名稱 Name", value="Hero")
                        v_desc    = gr.Textbox(label="英文描述 Description (EN)*",
                                               placeholder="a young woman with silver hair...")
                        v_desc_zh = gr.Textbox(label="中文描述 Description (ZH)")
                        v_theme   = gr.Textbox(label="故事主題 Theme",
                                               placeholder="夜雨中的追逐")
                        v_style   = gr.Textbox(label="風格 Style", value=DEFAULT_STYLE)

                        gr.Markdown("##### 影片規格 Video Specs")
                        with gr.Row():
                            v_duration = gr.Dropdown(DURATIONS,          value="5s",       label="時長 Duration")
                            v_fps      = gr.Dropdown(FPS_OPTIONS,         value="24fps (Cinematic)", label="幀率 FPS")
                        v_cam_move    = gr.Dropdown(CAMERA_MOVEMENTS,     value="Static",   label="運鏡 Camera Movement")
                        v_motion_int  = gr.Dropdown(MOTION_INTENSITIES,   value="Moderate", label="運動強度 Motion Intensity")
                        v_neg         = gr.Textbox(label="Negative Prompt", value=DEFAULT_NEG_V)

                        v_ar, v_res, v_angle, v_lens, v_light, v_grade, v_dof = _cinema_block("v")

                    with gr.Column(scale=2):
                        with gr.Row():
                            v_clips  = gr.Slider(1, 6, value=1, step=1, label="生成幾個片段 Clips")
                            btn_vid  = gr.Button("生成影片提示詞 Generate", variant="primary")
                        v_out      = gr.Markdown()
                        v_out_info = gr.Markdown()

                vbtn_tchar.click(apply_char_template,   [vtpl_char],   [v_name, v_desc, v_desc_zh])
                vbtn_tstory.click(apply_story_template, [vtpl_story],  [v_theme])
                vbtn_tstyle.click(apply_style_template, [vtpl_style],  [v_style])
                btn_vid.click(gen_video_prompt,
                    [v_name, v_desc, v_desc_zh, v_theme, v_style,
                     v_ar, v_res, v_angle, v_lens, v_light, v_grade, v_dof,
                     v_duration, v_fps, v_cam_move, v_motion_int, v_neg, v_clips],
                    [v_out, v_out_info])

            # ── Tab 4: Prompt Viewer ─────────────────────────────────────────
            with gr.Tab("📋 提示詞檢視"):
                gr.Markdown("### 所有已生成的提示詞 — 圖片 & 影片")
                with gr.Row():
                    pv_type    = gr.Radio(["all", "image", "video"], value="all",
                                          label="類型 Type")
                    pv_keyword = gr.Textbox(label="關鍵字搜尋 Search", placeholder="雨中 / rain", scale=3)
                    pv_count   = gr.Slider(5, 100, value=20, step=5, label="顯示筆數")
                    btn_view   = gr.Button("載入 Load", variant="primary")
                pv_out = gr.Markdown()

                btn_view.click(load_viewer, [pv_type, pv_keyword, pv_count], [pv_out])
                demo.load(load_viewer, [pv_type, pv_keyword, pv_count], [pv_out])

        gr.Markdown(
            f"---\n"
            f"圖片提示詞: `{config.PROMPTS_MD}` · `{config.PROMPTS_JSON}`  |  "
            f"影片提示詞: `{config.VIDEO_PROMPTS_MD}` · `{config.VIDEO_PROMPTS_JSON}`"
        )

    return demo


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        config.validate_config()
    except EnvironmentError as e:
        print(f"\n[ERROR] {e}\n")
        sys.exit(1)

    app = build_app()
    app.launch(server_name="0.0.0.0", server_port=7860, share=False, inbrowser=True)
