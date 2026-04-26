from typing import Protocol

from elochess.base.input_model import InputModel


class RatingCalculator(Protocol):
    """A protocol for calculating ratings."""

    @classmethod
    def update_rating(
        cls, current_rating: int, opponent_ratings: list[int], score: float
    ) -> int:
        """Return the updated rating."""


def update_rating(input_data: InputModel, calculator: type[RatingCalculator]) -> int:
    """Return the updated rating using the provided calculator."""
    extra = input_data.model_dump(
        exclude={"current_rating", "opponent_ratings", "score"}
    )
    return calculator.update_rating(
        input_data.current_rating,
        input_data.opponent_ratings,
        input_data.score,
        **extra,
    )
