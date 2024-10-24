"""CLI app definition."""

import random
from pathlib import Path
from typing import Annotated

import typer

from .stories import do_story

app = typer.Typer()


@app.command(help="A variation of the 'Mad Libs' games.")
def run_story_command(
    story_file_name: Annotated[
        str | None,
        typer.Argument(
            help="The name of the story to run, without the .txt extension",
        ),
    ] = None,
) -> None:
    """Run a story."""
    stories_folder = Path("stories")
    if not stories_folder.exists():
        typer.echo("No stories folder found. Exiting.")
        raise typer.Exit(code=1)

    if story_file_name:
        story_path = stories_folder.joinpath(f"{story_file_name}.txt")
        if not story_path.exists():
            typer.echo(f"Story file {story_file_name} not found. Exiting.")
            raise typer.Exit(code=1)
    else:
        story_path = random.choice(list(stories_folder.glob("*.txt")))  # noqa: S311

    do_story(story_path)
