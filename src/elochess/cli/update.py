from typing import Annotated

import typer

from elochess.dwz import DwzCalculator
from elochess.elo import EloCalculator

CurrentRating = Annotated[
    int,
    typer.Option(
        "--current",
        "-c",
        min=0,
        help="The rating you have at present.",
    ),
]
OpponentRatings = Annotated[
    list[int],
    typer.Option(
        "--opponent",
        "-o",
        min=0,
        help="The rating(s) of your opponent(s). Repeat in case of multiple.",
    ),
]
Score = Annotated[
    float,
    typer.Option(
        "--score",
        "-s",
        min=0.0,
        help="The total score you achieved (1.0 = win, 0.5 = draw, 0.0 = loss).",
    ),
]
BirthYear = Annotated[
    int,
    typer.Option(
        "--birthyear",
        "-b",
        min=0,
        help="The year of your birth.",
    ),
]
EvaluationYear = Annotated[
    int | None,
    typer.Option(
        "--evalyear",
        "-e",
        min=0,
        help="The year to evaluate at (defaults to the current year).",
    ),
]
GamesPlayed = Annotated[
    int,
    typer.Option(
        "--games",
        "-g",
        min=0,
        help="The number of rated games played previously.",
    ),
]
Reached2400 = Annotated[
    bool,
    typer.Option(
        "--master",
        "-m",
        help="Whether you have ever been rated 2400 or higher.",
    ),
]
Age = Annotated[
    int,
    typer.Option(
        "--age",
        "-a",
        min=0,
        help="The age you are at present.",
    ),
]
Index = Annotated[
    int,
    typer.Option(
        "--index",
        "-i",
        min=0,
        help="The index of your latest previous evaluation if present.",
    ),
]

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
