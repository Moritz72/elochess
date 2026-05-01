from typer.testing import CliRunner

from elochess.cli.app import app

runner = CliRunner()


def test_update_elo() -> None:
    """Test the update Elo CLI command."""
    command = [
        "update",
        "elo",
        "--current",
        "1500",
        "--opponent",
        "1400",
        "--opponent",
        "1600",
        "--score",
        "1.5",
    ]
    result = runner.invoke(app, command)

    assert result.exit_code == 0
    assert result.output == "1510\n"


def test_update_dwz() -> None:
    """Test the update DWZ CLI command."""
    command = [
        "update",
        "dwz",
        "--current",
        "1500",
        "--opponent",
        "1400",
        "--opponent",
        "1600",
        "--score",
        "1.5",
    ]
    result = runner.invoke(app, command)

    assert result.exit_code == 0
    assert result.output == "1518\n"


def test_update_uscf() -> None:
    """Test the update USCF CLI command."""
    command = [
        "update",
        "uscf",
        "--current",
        "1500",
        "--opponent",
        "1400",
        "--opponent",
        "1600",
        "--score",
        "1.5",
    ]
    result = runner.invoke(app, command)

    assert result.exit_code == 0
    assert result.output == "1522\n"
