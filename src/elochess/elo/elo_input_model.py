from elochess.base import InputModel


class EloInputModel(InputModel):
    """Model for Elo rating calculation input."""

    current_rating: int
    opponent_ratings: list[int]
    score: float
    birth_year: int = 2000
    evaluation_year: int | None = None
    games_played: int = 30
    reached_2400: bool = False
