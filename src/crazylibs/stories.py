"""Story functions."""

from pathlib import Path

import typer


def do_story(story_file: Path) -> None:
    """Fun."""
    story_text = Path(story_file).read_text()
    raw_title, questions_block, template = story_text.split("---")

    title = raw_title.strip()

    question_rows = questions_block.strip().split("\n")
    questions = {}
    for row in question_rows:
        index, question = row.split(":")
        questions[index] = question.strip()

    typer.echo(f'Welcome to "{title}"')
    typer.echo("")
    typer.echo("Please fill in the following words:")

    context = {}
    for index, question in questions.items():
        context[index] = typer.prompt(question)

    text = template
    for index, item in context.items():
        text = text.replace(f"({index})", item)

    typer.echo("")
    typer.echo("Wow, what a good selection of words!")
    typer.echo("Here is your story:")
    typer.echo("")

    typer.echo(text)
