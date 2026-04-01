"""AI Image Prompt Generator — CLI App using OpenRouter."""
from __future__ import annotations

import sys
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich import box

import config
import prompt_generator
import recorder
from models import Character

app = typer.Typer(help="AI 圖片提示詞生成器 | AI Image Prompt Generator")
console = Console()


def _print_frame(frame, show_full: bool = True) -> None:
    console.print(Panel(
        f"[bold cyan]Frame {frame.frame_index}[/] — Session: [yellow]{frame.session_id}[/]\n\n"
        f"[bold]動作 / Action:[/] {frame.action_zh} / {frame.action_en}\n"
        f"[bold]表情 / Expression:[/] {frame.expression_zh} / {frame.expression_en}\n"
        f"[bold]場景 / Scene:[/] {frame.scene_zh} / {frame.scene_en}\n\n"
        f"[bold green]English Prompt:[/]\n{frame.prompt_en}\n\n"
        f"[bold red]中文提示詞:[/]\n{frame.prompt_zh}\n\n"
        f"[dim]連續性 / Continuity: {frame.continuity_note_zh}[/]",
        title=f"[bold]Prompt Frame {frame.frame_index}[/]",
        border_style="blue",
    ))


@app.command("single")
def cmd_single(
    name: str = typer.Option("", "--name", "-n", help="角色名稱 Character name"),
    desc: str = typer.Option("", "--desc", "-d", help="角色英文描述 Character description (English)"),
    desc_zh: str = typer.Option("", "--desc-zh", help="角色中文描述"),
    theme: str = typer.Option("", "--theme", "-t", help="故事主題 / Story theme"),
    style: str = typer.Option("cinematic photography, highly detailed, 8k", "--style", "-s"),
) -> None:
    """生成單張圖片提示詞 | Generate a single image prompt."""
    config.validate_config()

    if not name:
        name = Prompt.ask("[cyan]角色名稱 Character name[/]", default="Hero")
    if not desc:
        desc = Prompt.ask("[cyan]角色英文描述 (e.g. 'a young woman with long black hair')[/]")
    if not desc_zh:
        desc_zh = Prompt.ask("[cyan]角色中文描述[/]", default=desc)
    if not theme:
        theme = Prompt.ask("[cyan]故事主題 / Theme (e.g. '在雨中奔跑')[/]")

    character = Character(name=name, description=desc, description_zh=desc_zh)

    with console.status("[bold green]AI 生成中... Generating...[/]"):
        frame = prompt_generator.generate_frame(
            character=character,
            theme=theme,
            frame_index=1,
            style=style,
        )

    recorder.save_frame(frame)
    _print_frame(frame)
    console.print(f"\n[green]✓ 已儲存到 Saved to:[/] {config.PROMPTS_MD}")


@app.command("sequence")
def cmd_sequence(
    name: str = typer.Option("", "--name", "-n"),
    desc: str = typer.Option("", "--desc", "-d"),
    desc_zh: str = typer.Option("", "--desc-zh"),
    theme: str = typer.Option("", "--theme", "-t"),
    frames: int = typer.Option(0, "--frames", "-f", help="Number of frames (2-8)"),
    style: str = typer.Option("cinematic photography, highly detailed, 8k", "--style", "-s"),
) -> None:
    """生成連續分鏡提示詞序列 | Generate a sequence with continuity."""
    config.validate_config()

    if not name:
        name = Prompt.ask("[cyan]角色名稱 Character name[/]", default="Hero")
    if not desc:
        desc = Prompt.ask("[cyan]角色英文描述[/]")
    if not desc_zh:
        desc_zh = Prompt.ask("[cyan]角色中文描述[/]", default=desc)
    if not theme:
        theme = Prompt.ask("[cyan]故事主題 / Theme[/]")
    if frames <= 0:
        frames = IntPrompt.ask("[cyan]幾個分鏡 / Number of frames[/]", default=4)
        frames = max(2, min(8, frames))

    character = Character(name=name, description=desc, description_zh=desc_zh)

    console.print(f"\n[bold]生成 {frames} 個連續分鏡提示詞... Generating {frames} frames...[/]\n")

    with console.status("[bold green]Processing...[/]") as status:
        sequence = prompt_generator.generate_sequence(
            character=character,
            theme=theme,
            num_frames=frames,
            style=style,
        )

    recorder.save_sequence(sequence)

    for frame in sequence.frames:
        _print_frame(frame)

    console.print(f"\n[green]✓ 序列已儲存 Sequence saved:[/] {config.PROMPTS_MD}")
    console.print(f"[green]✓ JSON:[/] {config.PROMPTS_JSON}")


@app.command("history")
def cmd_history(
    n: int = typer.Option(10, "--count", "-n", help="顯示幾筆 Number of recent records"),
    keyword: str = typer.Option("", "--search", "-s", help="關鍵字搜尋 Search keyword"),
) -> None:
    """瀏覽已儲存的提示詞 | Browse saved prompts."""
    if keyword:
        records = recorder.search_by_keyword(keyword)
        console.print(f"[cyan]搜尋 '{keyword}' — 找到 {len(records)} 筆[/]\n")
    else:
        records = recorder.list_recent(n)
        console.print(f"[cyan]最近 {len(records)} 筆提示詞:[/]\n")

    if not records:
        console.print("[yellow]尚無記錄 No records found.[/]")
        return

    table = Table(box=box.ROUNDED, show_lines=True)
    table.add_column("Frame", style="cyan", width=6)
    table.add_column("Session", style="yellow", width=10)
    table.add_column("Action 動作", width=20)
    table.add_column("Expression 表情", width=20)
    table.add_column("Scene 場景", width=25)
    table.add_column("時間", width=20)

    for r in records:
        table.add_row(
            str(r.get("frame_index", "")),
            r.get("session_id", ""),
            r.get("action_zh", ""),
            r.get("expression_zh", ""),
            r.get("scene_zh", ""),
            str(r.get("created_at", ""))[:19],
        )

    console.print(table)
    console.print(f"\n[dim]完整提示詞請查看: {config.PROMPTS_MD}[/]")


@app.command("interactive")
def cmd_interactive() -> None:
    """互動模式 — 逐步輸入生成提示詞 | Interactive mode."""
    config.validate_config()

    console.print(Panel(
        "[bold cyan]AI 圖片提示詞生成器[/]\n[bold]AI Image Prompt Generator[/]\n\n"
        "使用 OpenRouter AI 生成雙語圖片提示詞\nPowered by OpenRouter API",
        border_style="cyan",
    ))

    while True:
        console.print("\n[bold]選擇模式 Choose mode:[/]")
        console.print("  [cyan]1[/] — 單張提示詞 Single frame")
        console.print("  [cyan]2[/] — 連續分鏡 Sequence")
        console.print("  [cyan]3[/] — 查看歷史 History")
        console.print("  [cyan]q[/] — 退出 Quit")

        choice = Prompt.ask("\n選擇 Choose", choices=["1", "2", "3", "q"])

        if choice == "q":
            console.print("[yellow]再見 Goodbye![/]")
            break
        elif choice == "1":
            cmd_single(name="", desc="", desc_zh="", theme="", style="cinematic photography, highly detailed, 8k")
        elif choice == "2":
            cmd_sequence(name="", desc="", desc_zh="", theme="", frames=0, style="cinematic photography, highly detailed, 8k")
        elif choice == "3":
            n = IntPrompt.ask("顯示幾筆 How many", default=10)
            cmd_history(n=n, keyword="")


if __name__ == "__main__":
    app()
