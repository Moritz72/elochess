from typing import Annotated

from pydantic import Field

from elochess.api.models import CamelCaseModel


class UpdateRequest(CamelCaseModel):
    """Base model for rating update requests."""

    current_rating: Annotated[int, Field(ge=0)] = Field(
        ...,
        title="Current Rating",
        description="The rating you have at present.",
        examples=[1500],
    )
    opponent_ratings: list[Annotated[int, Field(ge=0)]] = Field(
        ...,
        title="Opponent Ratings",
        description="The ratings of your opponents.",
        examples=[[1400, 1600]],
    )
    score: Annotated[float, Field(ge=0)] = Field(
        ...,
        title="Score",
        description="The total score you achieved (1.0 = win, 0.5 = draw, 0.0 = loss).",
        examples=[1.5],
    )


class UpdateDwzRequest(UpdateRequest):
    """Model for DWZ update requests."""

    age: Annotated[int, Field(ge=0)] = Field(
        26,
        title="Age",
        description="The age you are at present.",
        examples=[26],
    )
    index: Annotated[int, Field(ge=0)] = Field(
        30,
        title="Index",
        description="The index of your latest previous evaluation if present.",
        examples=[30],
    )


class UpdateEloRequest(UpdateRequest):
    """Model for Elo update requests."""

    birth_year: Annotated[int, Field(ge=0)] = Field(
        2000,
        title="Birth Year",
        description="The year of your birth.",
        examples=[2000],
    )
    evaluation_year: Annotated[int | None, Field(ge=0)] = Field(
        None,
        title="Birth Year",
        description="The year to evaluate at (defaults to the current year).",
        examples=[2026],
    )
    games_played: Annotated[int, Field(ge=0)] = Field(
        30,
        title="Games Played",
        description="The number of rated games played previously.",
        examples=[30],
    )
    reached_2400: bool = Field(
        default=False,
        title="Reached 2400",
        description="Whether you have ever been rated 2400 or higher.",
        examples=[False],
    )


class UpdateUscfRequest(UpdateRequest):
    """Model for USCF rating update requests."""

    games_played: Annotated[int, Field(ge=0)] = Field(
        50,
        title="Games Played",
        description="The number of rated games played previously.",
        examples=[50],
    )
    is_dual_rated: bool = Field(
        default=False,
        title="Is Dual Rated",
        description="Whether games count for Regular and Quick ratings simultaneously.",
        examples=[False],
    )
