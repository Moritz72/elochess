import math

from elochess.dwz.developement_coefficient import get_development_coefficient


class DwzCalculator:
    """A class for calculating ratings used by the German chess federation."""

    @staticmethod
    def _get_expected_score(rating_difference: int) -> float:
        """
        Return the expected score ("Gewinnerwartung").

        The distribution is assumed to follow a normal distribution,
        where the standard deviation is set to be 200 * sqrt(2).

        Occasionaly, the following approximation may be used.
        1 / (1 + 10 ^ (-D / 400))

        The result is then rounded to 3 significant digits.
        """
        return round(0.5 * (1.0 + math.erf(rating_difference / 400)), 3)

    @classmethod
    def get_rating(
        cls,
        current_rating: int,
        opponent_ratings: list[int],
        score: float,
        *,
        age: int = 26,
        evaluation_number: int = 30,
    ) -> int:
        """
        Return the updated rating.

        R_n = R_0 + 800 * (W - W_e) / (E + n)

        R_0: Current rating
        W:   Score
        W_e: Exected score
        E:   Development coefficient
        n:   Number of rateable game
        """
        score_exp = sum(
            cls._get_expected_score(current_rating - opponent_rating)
            for opponent_rating in opponent_ratings
        )
        development = get_development_coefficient(
            current_rating, age, evaluation_number, score > score_exp, score < score_exp
        )
        games = len(opponent_ratings)

        rating = current_rating + 800 * (score - score_exp) / (development + games)
        return round(rating)
