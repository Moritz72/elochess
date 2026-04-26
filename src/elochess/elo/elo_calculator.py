from datetime import UTC, datetime

from elochess.elo.expected_score import get_expected_score


class EloCalculator:
    """A class for calculating ratings used by FIDE."""

    @staticmethod
    def _get_k_factor(
        current_rating: int,
        birth_year: int,
        evaluation_year: int | None,
        games_played: int,
        reached_2400: bool,
    ) -> int:
        """
        Return the K-factor.

        Goes through the following criteria until one is met:
        - K = 10, if a rating of 2400 has ever been reached
        - K = 40, if the year of the 18th birthday has not ended yet
                  and the current rating is below 2300
        - K = 40, if less than 30 rated games have been played previously
        - K = 20

        """
        evaluation_year = evaluation_year or datetime.now(UTC).year

        if reached_2400:
            return 10
        if evaluation_year - birth_year <= 18 and current_rating < 2300:
            return 40
        if games_played < 30:
            return 40
        return 20

    @classmethod
    def update_rating(
        cls,
        current_rating: int,
        opponent_ratings: list[int],
        score: float,
        *,
        birth_year: int = 2000,
        evaluation_year: int | None = None,
        games_played: int = 30,
        reached_2400: bool = False,
    ) -> int:
        """
        Return the updated rating.

        R_n = R_0 + K * (W - W_e)

        R_0: Current rating
        K:   K-factor
        W:   Score
        W_e: Expected score
        """
        below_2650 = current_rating < 2650
        score_exp = sum(
            get_expected_score(current_rating - opponent_rating, below_2650)
            for opponent_rating in opponent_ratings
        )
        k = cls._get_k_factor(
            current_rating, birth_year, evaluation_year, games_played, reached_2400
        )

        rating = current_rating + k * (score - score_exp)
        return round(rating)
