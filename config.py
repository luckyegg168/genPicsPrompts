import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "qwen/qwen3.6-plus-preview:free")
# Vision model — must support image input (Qwen3 is text-only, keep a vision-capable model here)
OPENROUTER_VISION_MODEL = os.getenv("OPENROUTER_VISION_MODEL", "bytedance-seed/seed-2.0-mini")

# Folder where user can drop reference images
IMAGES_DIR = Path(os.getenv("IMAGES_DIR", "images"))
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "outputs"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS_JSON = OUTPUT_DIR / "prompts.json"
PROMPTS_MD = OUTPUT_DIR / "prompts.md"
VIDEO_PROMPTS_JSON = OUTPUT_DIR / "video_prompts.json"
VIDEO_PROMPTS_MD = OUTPUT_DIR / "video_prompts.md"


def validate_config() -> None:
    if not OPENROUTER_API_KEY:
        raise EnvironmentError(
            "OPENROUTER_API_KEY is not set.\n"
            "Copy .env.example to .env and fill in your API key.\n"
            "Get a key at: https://openrouter.ai/keys"
        )
