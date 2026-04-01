"""Persist and retrieve generated prompts."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from models import PromptFrame, PromptSequence, VideoPromptFrame
import config

# ── helpers ───────────────────────────────────────────────────────────────────

def _load_json(path: Path) -> list[dict]:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_json(records: list[dict], path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2, default=str)


def _append_markdown(content: str, path: Path) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


# ── Image prompts ─────────────────────────────────────────────────────────────

def save_frame(frame: PromptFrame) -> None:
    records = _load_json(config.PROMPTS_JSON)
    records.append(frame.model_dump(mode="json"))
    _save_json(records, config.PROMPTS_JSON)
    _append_markdown(frame.to_markdown(), config.PROMPTS_MD)


def save_sequence(sequence: PromptSequence) -> None:
    header = (
        f"\n# Sequence: {sequence.session_id} — {sequence.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"**Character:** {sequence.character.description_zh} ({sequence.character.description})\n"
    )
    _append_markdown(header, config.PROMPTS_MD)
    for frame in sequence.frames:
        save_frame(frame)


def list_recent(n: int = 10) -> list[dict]:
    return _load_json(config.PROMPTS_JSON)[-n:]


def search_by_keyword(keyword: str) -> list[dict]:
    kw = keyword.lower()
    return [
        r for r in _load_json(config.PROMPTS_JSON)
        if kw in r.get("prompt_en", "").lower()
        or kw in r.get("prompt_zh", "").lower()
        or kw in r.get("action_zh", "").lower()
        or kw in r.get("scene_zh", "").lower()
    ]


# ── Video prompts ─────────────────────────────────────────────────────────────

def save_video_frame(frame: VideoPromptFrame) -> None:
    records = _load_json(config.VIDEO_PROMPTS_JSON)
    records.append(frame.model_dump(mode="json"))
    _save_json(records, config.VIDEO_PROMPTS_JSON)
    _append_markdown(frame.to_markdown(), config.VIDEO_PROMPTS_MD)


def list_recent_video(n: int = 10) -> list[dict]:
    return _load_json(config.VIDEO_PROMPTS_JSON)[-n:]


def search_video_by_keyword(keyword: str) -> list[dict]:
    kw = keyword.lower()
    return [
        r for r in _load_json(config.VIDEO_PROMPTS_JSON)
        if kw in r.get("prompt_en", "").lower()
        or kw in r.get("prompt_zh", "").lower()
        or kw in r.get("scene_zh", "").lower()
    ]


# ── Combined viewer ───────────────────────────────────────────────────────────

def load_all_prompts(prompt_type: str = "all", n: int = 50) -> list[dict]:
    """Load recent prompts of given type: 'image', 'video', or 'all'."""
    results = []
    if prompt_type in ("image", "all"):
        for r in _load_json(config.PROMPTS_JSON)[-n:]:
            r.setdefault("prompt_type", "image")
            results.append(r)
    if prompt_type in ("video", "all"):
        for r in _load_json(config.VIDEO_PROMPTS_JSON)[-n:]:
            r.setdefault("prompt_type", "video")
            results.append(r)
    results.sort(key=lambda r: r.get("created_at", ""), reverse=True)
    return results[:n]


# ── Edit / Delete ─────────────────────────────────────────────────────────────

def _find_record(records: list[dict], session_id: str, frame_index: int) -> Optional[int]:
    """Return list index of a record matching session_id + frame_index, or None."""
    for i, r in enumerate(records):
        if r.get("session_id") == session_id and r.get("frame_index") == frame_index:
            return i
    return None


def update_frame(session_id: str, frame_index: int, updates: dict) -> bool:
    """Patch an existing image prompt record in-place. Returns True on success."""
    records = _load_json(config.PROMPTS_JSON)
    idx = _find_record(records, session_id, frame_index)
    if idx is None:
        return False
    records[idx].update(updates)
    _save_json(records, config.PROMPTS_JSON)
    return True


def delete_frame(session_id: str, frame_index: int) -> bool:
    """Delete an image prompt record. Returns True on success."""
    records = _load_json(config.PROMPTS_JSON)
    idx = _find_record(records, session_id, frame_index)
    if idx is None:
        return False
    records.pop(idx)
    _save_json(records, config.PROMPTS_JSON)
    return True


def update_video_frame(session_id: str, frame_index: int, updates: dict) -> bool:
    """Patch an existing video prompt record in-place. Returns True on success."""
    records = _load_json(config.VIDEO_PROMPTS_JSON)
    idx = _find_record(records, session_id, frame_index)
    if idx is None:
        return False
    records[idx].update(updates)
    _save_json(records, config.VIDEO_PROMPTS_JSON)
    return True


def delete_video_frame(session_id: str, frame_index: int) -> bool:
    """Delete a video prompt record. Returns True on success."""
    records = _load_json(config.VIDEO_PROMPTS_JSON)
    idx = _find_record(records, session_id, frame_index)
    if idx is None:
        return False
    records.pop(idx)
    _save_json(records, config.VIDEO_PROMPTS_JSON)
    return True


def delete_by_index_in_list(prompt_type: str, list_index: int) -> bool:
    """Delete a record by its absolute position in the JSON list (0-based). Used by UI."""
    path = config.PROMPTS_JSON if prompt_type == "image" else config.VIDEO_PROMPTS_JSON
    records = _load_json(path)
    if list_index < 0 or list_index >= len(records):
        return False
    records.pop(list_index)
    _save_json(records, path)
    return True


def update_by_index_in_list(prompt_type: str, list_index: int, updates: dict) -> bool:
    """Update a record by its absolute position in the JSON list (0-based). Used by UI."""
    path = config.PROMPTS_JSON if prompt_type == "image" else config.VIDEO_PROMPTS_JSON
    records = _load_json(path)
    if list_index < 0 or list_index >= len(records):
        return False
    records[list_index].update(updates)
    _save_json(records, path)
    return True
