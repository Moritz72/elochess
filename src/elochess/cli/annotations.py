from typing import Annotated

import typer

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
