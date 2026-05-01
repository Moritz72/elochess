import math

from elochess.uscf.performance_rating import get_performance_rating


class UscfCalculator:
    """A class for calculating ratings used by USCF."""

    @staticmethod
    def _get_expected_score(rating_difference: int) -> float:
        """
        Return the expected score.

        W_e = 1 / (1 + 10 ^ (-D / 400))
        """
        return 1.0 / (1.0 + math.pow(10, -rating_difference / 400))

    @staticmethod
    def _get_k_factor(
        current_rating: int,
        games_played: int,
        is_dual_rated: bool,
        games_played_now: int,
    ) -> float:
        """
        Return the K-factor.

        For R_0 < 2355:
            G_e = 50 / sqrt(0.662 + (2569 - R_0) ^ 2 * 0.000007390)
        Otherwise:
            G_e = 50

        Then, set G_e to G_p, if G_e > G_p.

        K = 800 / (G_e + G_pn)

        For dual rated tournaments, additional adjustments are performed:
            - K = K, if R_0 < 2000
            - K = K / 4, if R_0 >= 2500
            - K = (6.5 - 0.0025 * R_0) * K, otherwise

        R_0:  Current rating
        G_p:  Games played before
        G_pn: Games played now
        """
        if current_rating < 2355:
            games_lower_bound = 50.0 / math.sqrt(
                0.662 + math.pow(2569 - current_rating, 2) * 0.000007390
            )
        else:
            games_lower_bound = 50.0

        effective_games = min(float(games_played), games_lower_bound)
        k = 800.0 / (effective_games + games_played_now)

        if not is_dual_rated:
            return k
        if current_rating < 2200:
            return k
        if current_rating >= 2500:
            return k / 4
        return (6.5 - 0.0025 * current_rating) * k

    @staticmethod
    def _get_bonus(
        score: float, score_exp: float, games_played_now: int, k_factor: float
    ) -> float:
        """
        Return the bonus.

        B = K * (W - W_e) - 10 * sqrt(min(4, G_pn)),
        where B is then capped below to 0.

        However, if G_pn < 3, then B = 0.

        R_0:  Current rating
        W:   Score
        W_e: Expected score
        G_pn: Games played now
        """
        if games_played_now < 3:
            return 0
        bonus_games = min(4, games_played_now)

        return max(0, k_factor * (score - score_exp) - 10 * math.sqrt(bonus_games))

    @staticmethod
    def _update_rating_low_game_count(
        current_rating: int,
        games_played: int,
        games_played_now: int,
        performance_rating: int,
    ) -> int:
        """
        Return the updated rating for a low number of games played.

        R_n = (G_p * R_0 + G_pn * R_p) / (G_p + G_pn)

        R_0:  Current rating
        G_p:  Games played before
        G_pn: Games played now
        R_p:  Performance rating
        """
        return round(
            (games_played * current_rating + games_played_now * performance_rating)
            / (games_played + games_played_now)
        )

    @classmethod
    def update_rating(
        cls,
        current_rating: int,
        opponent_ratings: list[int],
        score: float,
        *,
        games_played: int = 50,
        is_dual_rated: bool = False,
    ) -> int:
        """
        Return the updated rating.

        R_n = R_0 + K * (W - W_e) + B

        For rating gains this is then round up to the nearest integer,
        while for rating losses it is rounded down to the nearest integer.

        If the number of games played previously is lower than 8,
        a different formula is used.

        R_0: Current rating
        K:   K-factor
        B:   Bonus
        W:   Score
        W_e: Expected score
        """
        if games_played <= 8:
            performance_rating = get_performance_rating(opponent_ratings, score)
            return cls._update_rating_low_game_count(
                current_rating, games_played, len(opponent_ratings), performance_rating
            )

        score_exp = sum(
            cls._get_expected_score(current_rating - opponent_rating)
            for opponent_rating in opponent_ratings
        )
        k = cls._get_k_factor(
            current_rating, games_played, is_dual_rated, len(opponent_ratings)
        )
        bonus = cls._get_bonus(score, score_exp, len(opponent_ratings), k)

        rating = current_rating + k * (score - score_exp) + bonus

        if current_rating < rating:
            rating += 0.4999
        else:
            rating -= 0.4999

        return round(rating)
