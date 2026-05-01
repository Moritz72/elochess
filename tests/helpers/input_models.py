from pydantic import BaseModel


class InputModel(BaseModel):
    """Base model for rating update calculation input."""

    current_rating: int
    opponent_ratings: list[int]
    score: float


class DwzInputModel(InputModel):
    """Model for DWZ update calculation input."""

    age: int = 26
    index: int = 30


class EloInputModel(InputModel):
    """Model for Elo update calculation input."""

    birth_year: int = 2000
    evaluation_year: int | None = None
    games_played: int = 30
    reached_2400: bool = False
