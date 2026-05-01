def _get_expected_score(rating_difference: float) -> float:
    """
    Return the expected score.

    W_e = 0.5 + D / 800,
    where W_e is then capped below to 0 and capped above to 1.
    """
    return max(0.0, min(1.0, 0.5 + rating_difference / 800))


def get_performance_rating(opponent_ratings: list[int], score: float) -> int:
    """
    Return the performance rating.

    Finds the rating at which the given score would be expected.
    This is done via binary search.

    Except, in case of perfect scores:
        Highest opponent rating + 400
    And, in case of negative perfect scores:
        Lowest opponent rating - 400
    """
    if score == 0:
        minimum_rating = min(opponent_ratings, default=400)
        return max(100, minimum_rating - 400)

    if score == len(opponent_ratings):
        maximum_rating = max(opponent_ratings, default=-400)
        return min(2700, maximum_rating + 400)

    bound_low = 0.0
    bound_high = 4000.0

    while bound_high - bound_low > 0.1:
        middle = (bound_high + bound_low) / 2.0
        expected_score = sum(
            _get_expected_score(middle - opponent_rating)
            for opponent_rating in opponent_ratings
        )

        if expected_score > score:
            bound_high = middle
        else:
            bound_low = middle

    return round((bound_high + bound_low) / 2.0)
