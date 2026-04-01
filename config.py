import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── API Provider ─────────────────────────────────────────────────────────────
# "openrouter"  → use OpenRouter cloud API
# "ollama"      → use local Ollama (openai-compatible endpoint)
API_PROVIDER: str = os.getenv("API_PROVIDER", "openrouter")

# ── OpenRouter ────────────────────────────────────────────────────────────────
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL: str = os.getenv("OPENROUTER_MODEL", "qwen/qwen3.6-plus-preview:free")
OPENROUTER_VISION_MODEL: str = os.getenv(
    "OPENROUTER_VISION_MODEL", "bytedance-seed/seed-2.0-mini"
)

# ── Ollama ────────────────────────────────────────────────────────────────────
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_VISION_MODEL: str = os.getenv("OLLAMA_VISION_MODEL", "llava")

# ── Paths ─────────────────────────────────────────────────────────────────────
IMAGES_DIR = Path(os.getenv("IMAGES_DIR", "images"))
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "outputs"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS_JSON = OUTPUT_DIR / "prompts.json"
PROMPTS_MD = OUTPUT_DIR / "prompts.md"
VIDEO_PROMPTS_JSON = OUTPUT_DIR / "video_prompts.json"
VIDEO_PROMPTS_MD = OUTPUT_DIR / "video_prompts.md"

# Path to .env file (same directory as config.py)
_ENV_PATH = Path(__file__).parent / ".env"


def save_settings(
    provider: str,
    openrouter_key: str,
    openrouter_model: str,
    openrouter_vision_model: str,
    ollama_base_url: str,
    ollama_model: str,
    ollama_vision_model: str,
) -> None:
    """Persist settings to .env and update runtime globals."""
    global API_PROVIDER, OPENROUTER_API_KEY, OPENROUTER_MODEL, OPENROUTER_VISION_MODEL
    global OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_VISION_MODEL

    API_PROVIDER = provider
    OPENROUTER_API_KEY = openrouter_key
    OPENROUTER_MODEL = openrouter_model
    OPENROUTER_VISION_MODEL = openrouter_vision_model
    OLLAMA_BASE_URL = ollama_base_url
    OLLAMA_MODEL = ollama_model
    OLLAMA_VISION_MODEL = ollama_vision_model

    # Read existing .env (preserve unknown lines)
    existing: dict[str, str] = {}
    if _ENV_PATH.exists():
        for line in _ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                existing[k.strip()] = v.strip()

    existing.update({
        "API_PROVIDER": provider,
        "OPENROUTER_API_KEY": openrouter_key,
        "OPENROUTER_MODEL": openrouter_model,
        "OPENROUTER_VISION_MODEL": openrouter_vision_model,
        "OLLAMA_BASE_URL": ollama_base_url,
        "OLLAMA_MODEL": ollama_model,
        "OLLAMA_VISION_MODEL": ollama_vision_model,
    })

    lines = [f"{k}={v}" for k, v in existing.items()]
    _ENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_config() -> None:
    if API_PROVIDER == "openrouter" and not OPENROUTER_API_KEY:
        raise EnvironmentError(
            "OPENROUTER_API_KEY 尚未設定。\n"
            "請至「⚙ 設定」頁面輸入 API Key，或切換為 Ollama 本地模式。\n"
            "取得 Key：https://openrouter.ai/keys"
        )
