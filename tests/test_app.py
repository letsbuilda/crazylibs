"""Testing the app."""

from typer.testing import CliRunner

from crazylibs.cli import app

runner = CliRunner()


def test_app() -> None:
    """Test that the app can be invoked."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
