"""Utilities for loading and encoding images for vision API."""
from __future__ import annotations

import base64
import mimetypes
from pathlib import Path

SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def load_image_as_base64(path: str | Path) -> tuple[str, str]:
    """Read an image file and return (base64_string, mime_type).

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file extension is not supported.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Image not found: {p}")

    ext = p.suffix.lower()
    if ext not in SUPPORTED_EXTS:
        raise ValueError(f"Unsupported image format '{ext}'. Supported: {SUPPORTED_EXTS}")

    mime = mimetypes.types_map.get(ext, "image/jpeg")
    # Normalize common aliases
    if ext in (".jpg", ".jpeg"):
        mime = "image/jpeg"
    elif ext == ".png":
        mime = "image/png"
    elif ext == ".webp":
        mime = "image/webp"
    elif ext == ".gif":
        mime = "image/gif"

    with open(p, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")

    return b64, mime


def scan_project_images(images_dir: str | Path = "images") -> list[Path]:
    """Return sorted list of image files in the project images folder."""
    d = Path(images_dir)
    if not d.exists():
        return []
    return sorted(
        p for p in d.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS
    )


def bytes_to_base64(image_bytes: bytes, mime: str = "image/jpeg") -> tuple[str, str]:
    """Convert raw bytes (e.g. from Gradio upload) to (base64_string, mime_type)."""
    return base64.b64encode(image_bytes).decode("utf-8"), mime
