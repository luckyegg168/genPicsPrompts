"""Unified application logger — writes to file and exposes in-memory ring buffer for UI display."""
from __future__ import annotations

import logging
import sys
from collections import deque
from datetime import datetime
from pathlib import Path

import config

_LOG_FILE = config.OUTPUT_DIR / "app.log"
_MAX_ENTRIES = 500  # ring buffer size for UI display

# ── In-memory ring buffer consumed by the Log page ───────────────────────────
_buffer: deque[dict] = deque(maxlen=_MAX_ENTRIES)


class _BufferHandler(logging.Handler):
    """Push records into the in-memory ring buffer."""

    def emit(self, record: logging.LogRecord) -> None:
        _buffer.append(
            {
                "ts": datetime.fromtimestamp(record.created).strftime("%Y-%m-%d %H:%M:%S"),
                "level": record.levelname,
                "msg": self.format(record),
            }
        )


def _setup() -> logging.Logger:
    fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")

    # File handler
    file_handler = logging.FileHandler(_LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(fmt)

    # Stdout handler (visible in terminal)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(fmt)

    # Ring-buffer handler (visible in UI)
    buf_handler = _BufferHandler()
    buf_handler.setFormatter(fmt)

    logger = logging.getLogger("genPicsPrompts")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)
        logger.addHandler(buf_handler)
    return logger


log = _setup()


# ── Public helpers ────────────────────────────────────────────────────────────

def get_log_entries(level_filter: str = "ALL") -> list[dict]:
    """Return buffered log entries, optionally filtered by level."""
    if level_filter == "ALL":
        return list(_buffer)
    return [e for e in _buffer if e["level"] == level_filter]


def clear_buffer() -> None:
    _buffer.clear()


def get_log_file_path() -> Path:
    return _LOG_FILE
