from typing import Protocol, runtime_checkable


@runtime_checkable
class RatingCalculator(Protocol):
    """A protocol for calculating ratings."""

    @classmethod
    def update_rating(
        cls, current_rating: int, opponent_ratings: list[int], score: float
    ) -> int:
        """Return the updated rating."""
