"""CLI app definition."""

from random import choice

import typer

app = typer.Typer()


@app.command()
def run_story() -> None:
    """Fun!"""  # noqa: D400
    from crazylibs.stories import stories

    story = choice(stories)  # noqa: S311

    typer.echo(f'Welcome to "{story.title}"')
    typer.echo("")
    typer.echo("Please fill in the following words:")

    context = {}
    for index, question in story.questions.items():
        context[index] = typer.prompt(question)

    text = story.template
    for index, item in context.items():
        text = text.replace(f"({index})", item)

    typer.echo("")
    typer.echo("Wow, what a good selection of words!")
    typer.echo("Here is your story:")
    typer.echo("")

    typer.echo(text)
