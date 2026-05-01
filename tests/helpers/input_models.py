from pydantic import BaseModel


class InputModel(BaseModel):
    """Base model for rating calculation input."""

    current_rating: int
    opponent_ratings: list[int]
    score: float


class DwzInputModel(InputModel):
    """Model for DWZ rating calculation input."""

    current_rating: int
    opponent_ratings: list[int]
    score: float
    age: int = 26
    index: int = 30


class EloInputModel(InputModel):
    """Model for Elo rating calculation input."""

    current_rating: int
    opponent_ratings: list[int]
    score: float
    birth_year: int = 2000
    evaluation_year: int | None = None
    games_played: int = 30
    reached_2400: bool = False
