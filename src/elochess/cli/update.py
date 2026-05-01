import typer

from elochess.cli.annotations import (
    Age,
    BirthYear,
    CurrentRating,
    EvaluationYear,
    GamesPlayed,
    Index,
    OpponentRatings,
    Reached2400,
    Score,
)
from elochess.dwz import DwzCalculator
from elochess.elo import EloCalculator

update_typer = typer.Typer(
    name="update",
    help="Calculate updated ratings for given current ratings and results.",
)


@update_typer.command("elo")
def get_elo(
    current: CurrentRating,
    opponents: OpponentRatings,
    score: Score,
    *,
    birth_year: BirthYear = 2000,
    evaluation_year: EvaluationYear = None,
    games_played: GamesPlayed = 30,
    reached_2400: Reached2400 = False,
) -> None:
    """Return the updated Elo rating."""
    rating = EloCalculator.update_rating(
        current,
        opponents,
        score,
        birth_year=birth_year,
        evaluation_year=evaluation_year,
        games_played=games_played,
        reached_2400=reached_2400,
    )
    typer.echo(rating)


@update_typer.command("dwz")
def get_dwz(
    current: CurrentRating,
    opponents: OpponentRatings,
    score: Score,
    *,
    age: Age = 26,
    index: Index = 30,
) -> None:
    """Return the updated DWZ rating."""
    rating = DwzCalculator.update_rating(
        current,
        opponents,
        score,
        age=age,
        index=index,
    )
    typer.echo(rating)
