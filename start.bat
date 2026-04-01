@echo off
title AI Image Prompt Generator
setlocal

set VENV_PYTHON=.venv\Scripts\python.exe
set VENV_PIP=.venv\Scripts\pip.exe

:: ── Create venv if missing ──────────────────────────────────────────────────
if not exist "%VENV_PYTHON%" (
    echo [setup] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create venv. Make sure Python 3.10+ is installed.
        pause & exit /b 1
    )
)

:: ── Install / upgrade dependencies ─────────────────────────────────────────
"%VENV_PIP%" show nicegui >nul 2>&1
if errorlevel 1 (
    echo [setup] Installing dependencies into .venv ...
    "%VENV_PIP%" install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] pip install failed.
        pause & exit /b 1
    )
    echo.
)

:: ── API keys: load from .env (do NOT hardcode keys here) ───────────────────
:: Copy .env.example to .env and fill in your key if .env is missing
if not exist ".env" (
    echo [WARNING] .env not found. Copying .env.example as template...
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo [WARNING] Please edit .env and set OPENROUTER_API_KEY, then restart.
        notepad .env
        pause & exit /b 0
    ) else (
        echo [WARNING] No .env or .env.example found. Settings page can set the key.
    )
)

echo.
echo  AI Image Prompt Generator  ^|  venv: .venv
echo  ─────────────────────────────────────────
echo  Starting Prompt Studio (NiceGUI) ...
echo.

"%VENV_PYTHON%" nicegui_app.py

pause
