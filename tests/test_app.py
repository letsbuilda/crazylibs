"""Testing the app."""

from crazylibs.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app() -> None:
    """Test that the app can be invoked."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
