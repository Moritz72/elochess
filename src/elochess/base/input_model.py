from pydantic import BaseModel


class InputModel(BaseModel):
    """Base model for rating calculation input."""

    current_rating: int
    opponent_ratings: list[int]
    score: float
