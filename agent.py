"""OpenRouter AI agent — wraps the OpenAI-compatible API."""
from __future__ import annotations

import json
import time
from typing import Any

from openai import OpenAI

import config


def _build_client() -> OpenAI:
    return OpenAI(
        api_key=config.OPENROUTER_API_KEY,
        base_url=config.OPENROUTER_BASE_URL,
    )


import re

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)


def _strip_thinking(content: str) -> str:
    """Remove Qwen3 <think>...</think> reasoning blocks before parsing."""
    return _THINK_RE.sub("", content).strip()


def _parse_response(content: str, response_format: str) -> dict[str, Any]:
    clean = _strip_thinking(content)
    if response_format == "text":
        return {"text": clean}
    # Strip markdown code fences if present
    if clean.startswith("```"):
        lines = clean.splitlines()
        clean = "\n".join(lines[1:-1]) if lines[-1] == "```" else "\n".join(lines[1:])
    return json.loads(clean.strip())


def chat(
    system_prompt: str,
    user_prompt: str,
    model: str | None = None,
    max_retries: int = 3,
    response_format: str = "json",
) -> dict[str, Any]:
    """Send a text-only chat request to OpenRouter."""
    client = _build_client()
    chosen_model = model or config.OPENROUTER_MODEL
    content = ""

    for attempt in range(1, max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=chosen_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.85,
            )
            content = response.choices[0].message.content or ""
            return _parse_response(content, response_format)

        except json.JSONDecodeError as e:
            if attempt == max_retries:
                raise ValueError(
                    f"AI returned non-JSON after {max_retries} attempts: {e}\nContent: {content}"
                ) from e
            time.sleep(1)

        except Exception:
            if attempt == max_retries:
                raise
            time.sleep(2 ** attempt)

    return {}


def chat_with_image(
    system_prompt: str,
    user_prompt: str,
    image_base64: str,
    image_mime: str = "image/jpeg",
    model: str | None = None,
    max_retries: int = 3,
    response_format: str = "json",
) -> dict[str, Any]:
    """Send a vision request (text + image) to OpenRouter.

    Args:
        system_prompt: System instruction.
        user_prompt: Text instruction alongside the image.
        image_base64: Base64-encoded image bytes.
        image_mime: MIME type, e.g. 'image/jpeg', 'image/png'.
        model: Override model — must support vision (e.g. google/gemini-flash-1.5).
        max_retries: Retry attempts.
        response_format: 'json' or 'text'.
    """
    client = _build_client()
    chosen_model = model or config.OPENROUTER_VISION_MODEL
    content = ""

    user_message = [
        {
            "type": "image_url",
            "image_url": {"url": f"data:{image_mime};base64,{image_base64}"},
        },
        {"type": "text", "text": user_prompt},
    ]

    for attempt in range(1, max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=chosen_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                temperature=0.85,
            )
            content = response.choices[0].message.content or ""
            return _parse_response(content, response_format)

        except json.JSONDecodeError as e:
            if attempt == max_retries:
                raise ValueError(
                    f"Vision AI returned non-JSON after {max_retries} attempts: {e}\nContent: {content}"
                ) from e
            time.sleep(1)

        except Exception:
            if attempt == max_retries:
                raise
            time.sleep(2 ** attempt)

    return {}
