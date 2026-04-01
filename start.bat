@echo off
title AI Image Prompt Generator

:: ============================================================
:: PUT YOUR API KEYS HERE
:: ============================================================
set OPENROUTER_API_KEY=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

:: Text model (prompt generation) — Qwen3.6 Plus Preview
set OPENROUTER_MODEL=qwen/qwen3.6-plus-preview:free

:: Vision model (image analysis) — ByteDance Seed 2.0 Mini
set OPENROUTER_VISION_MODEL=bytedance-seed/seed-2.0-mini

:: Output folders
set OUTPUT_DIR=outputs
set IMAGES_DIR=images
:: ============================================================

echo.
echo  AI Image Prompt Generator
echo  -------------------------
echo  Text model  : %OPENROUTER_MODEL%
echo  Vision model: %OPENROUTER_VISION_MODEL%
echo.

:: Install dependencies if not already installed
python -m pip show nicegui >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    python -m pip install -r requirements.txt
    echo.
)

:: Launch NiceGUI Desktop App
echo Starting Prompt Studio (NiceGUI desktop) ...
echo.
python nicegui_app.py

pause
