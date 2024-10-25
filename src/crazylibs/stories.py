"""Story functions."""

from pathlib import Path
import re
import typer


def run_story(story_file: Path) -> None:
    """Run a story."""
    raw_text = Path(story_file).read_text().strip()
    title, story_text = raw_text.split("\n", maxsplit=1)

    typer.echo(f'Welcome to "{title}"')
    typer.echo("")
    typer.echo("Please fill in the following words:")

    context: dict[str, str] = {}

    lines = story_text.split("\n")
    for line in lines:
        print("oneoffs", re.findall(r"\([a-zA-Z]+\)", line))
        print("new contexts", re.findall(r"\([a-zA-Z]+ : \d+\)", line))
        print("existing", re.findall(r"\(\d+\)", line))

    typer.echo("")
    typer.echo("Wow, what a good selection of words!")
    typer.echo("Here is your story:")
    typer.echo("")

    # typer.echo(story_text)
