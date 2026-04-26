from elochess.base import InputModel


class DwzInputModel(InputModel):
    """Model for DWZ rating calculation input."""

    current_rating: int
    opponent_ratings: list[int]
    score: float
    age: int = 26
    index: int = 30
