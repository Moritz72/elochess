import math


def _get_age_component(age: int) -> float:
    """
    Return the age component used for calculation.

    J = 5  for ages 00-20
    J = 10 for ages 21-25
    J = 15 for ages 26-
    """
    if age <= 20:
        return 5
    if age <= 25:
        return 10
    return 15


def _get_base_coefficient(current_rating: int, age: int) -> float:
    """
    Return the calculated base value ("Grundwert").

    E_0 = (R_0 / 1000) ^ 4 + J

    R_0: Current rating
    J:   Age component
    """
    return math.pow(current_rating / 1000, 4) + _get_age_component(age)


def _get_accelaration_factor(
    current_rating: int, age: int, is_above_expectation: bool
) -> float:
    """
    Return the calculated accelaration factor ("Beschleunigungsfaktor").

    For age up to 20 and performances above expectation:
        f_B = R_0 / 2000,
        where f_B is then capped below to 0.5 and above to 1.0.

    In all other cases:
        f_B = 1

    R_0: Current rating
    """
    if age <= 20 and is_above_expectation:
        return min(max(current_rating / 2000, 0.5), 1.0)
    return 1.0


def _get_deceleration_surcharge(
    current_rating: int, is_below_expectation: bool
) -> float:
    """
    Return the calculated decelaration surcharge ("Bremszuschlag").

    For current rating lower than 1300 and performances below expectation:
        S_Br = exp((1300 - R_0) / 150) - 1

    In all other cases:
        S_Br = 0

    R_0: Current rating
    """
    if current_rating < 1300 and is_below_expectation:
        return math.exp((1300 - current_rating) / 150) - 1
    return 0.0


def get_development_coefficient(
    current_rating: int,
    age: int,
    index: int,
    is_above_expectation: bool,
    is_below_expectation: bool,
) -> int:
    """
    Return the development coefficient ("Entwicklkungskoeffizient").

    E = E_0 * f_B + S_Br,
    where E is then rounded to an integer and capped below to 5.

    For the cap from above the following cases apply

    S_Br == 0:
        For I <= 5:
            E <= 5 * I
        In all other cases:
            E <= 30
    In all other cases:
        E <= 150

    E_0:  Base coefficient
    f_B:  Accelaration factor
    S_Br: Decelaration surcharge
    I:    Index
    """
    base = _get_base_coefficient(current_rating, age)
    accelaration = _get_accelaration_factor(current_rating, age, is_above_expectation)
    decelaration = _get_deceleration_surcharge(current_rating, is_below_expectation)

    coefficient = max(round(base * accelaration + decelaration), 5)

    if decelaration == 0:
        if index <= 5:
            return min(coefficient, 5 * index)
        return min(coefficient, 30)
    return min(coefficient, 150)
