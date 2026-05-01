import typer

from elochess.cli.update import update_typer

app = typer.Typer(
    name="elochess",
    help="A CLI tool written in python to calculate chess ratings.",
)

app.add_typer(update_typer)
