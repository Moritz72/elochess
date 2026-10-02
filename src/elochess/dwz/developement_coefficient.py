success_bonus_divisor = 30
deceleration_factor_drift = 800
success_bonus_juniors = 4
success_bonus_adults = 4
development_coefficient_max = 80

development_coefficient_base = [
    [60, 60, 48, 46, 44, 42, 40, 38, 36, 34, 32],
    [60, 60, 44, 42, 40, 38, 36, 34, 32, 30, 28],
    [60, 60, 41, 39, 37, 35, 33, 31, 29, 27, 25],
]


def _get_base_coefficient(current_rating: int, age: int, index: int) -> float:
    """
    Return the calculated base value ("Grundwert").

    Index:                              1	2	3	4	5	6	7	8	9	10	>10
    Jugendliche/Junioren unter DWZ 2200	60	60	48	46	44	42	40	38	36	34	32
    Erwachsene unter DWZ 2000	        60	60	44	42	40	38	36	34	32	30	28
    Erwachsene ab DWZ 2000 und          60	60	41	39	37	35	33	31	29	27	25
    Jugendliche/Junioren ab DWZ 2200
    """
    i = min(index - 1, 10)

    if current_rating < 2200 and age <= 25:
        return development_coefficient_base[0][i]
    if current_rating < 2000:
        return development_coefficient_base[1][i]
    return development_coefficient_base[2][i]


def _get_success_bonus(
    current_rating: int, age: int, is_above_expectation: bool
) -> float:
    """
    Return the calculated success bonus ("Erfolgsaufschlag").

    For age up to 20:
        a = (R_0 - 2000) / 30,
        where a is then capped below to 0.

    Otherwise, for R_0 < 1600:
        a = 4

    In all other cases:
        a = 0

    Note, that if the performance is not above expectation, a = 0.

    R_0: Current rating
    """
    if not is_above_expectation:
        return 0
    if age <= 20:
        return max((2000 - current_rating) / success_bonus_divisor, 0)
    if current_rating >= 1600:
        return 0
    if age <= 25:
        return success_bonus_juniors
    return success_bonus_adults


def _get_deceleration_factor(current_rating: int, is_below_expectation: bool) -> float:
    """
    Return the calculated decelaration factor ("Bremsfaktor").

    For current rating lower than 1600 and performances below expectation:
        b = (R_0 + 800) / 2400

    In all other cases:
        b = 1

    R_0: Current rating
    """
    if current_rating < 1600 and is_below_expectation:
        divisor = (1600 + deceleration_factor_drift)
        return (current_rating + deceleration_factor_drift) / divisor
    return 1.0


def get_development_coefficient(
    current_rating: int,
    age: int,
    index: int,
    is_above_expectation: bool,
    is_below_expectation: bool,
) -> float:
    """
    Return the development coefficient ("Entwicklkungskoeffizient").

    K = K_0 * b + a,
    where K is then rounded to one significant digit and capped above to 80.

    K_0: Base coefficient
    a:   Success bonus
    b:   Decelaration factor
    """
    base = _get_base_coefficient(current_rating, age, index)
    success = _get_success_bonus(current_rating, age, is_above_expectation)
    decelaration = _get_deceleration_factor(current_rating, is_below_expectation)

    return min(round(base * decelaration + success, 1), development_coefficient_max)
