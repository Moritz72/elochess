from bisect import bisect_left

_FIDE_PD_TABLE = [
    (3, 0.50),
    (10, 0.51),
    (17, 0.52),
    (25, 0.53),
    (32, 0.54),
    (39, 0.55),
    (46, 0.56),
    (53, 0.57),
    (61, 0.58),
    (68, 0.59),
    (76, 0.60),
    (83, 0.61),
    (91, 0.62),
    (98, 0.63),
    (106, 0.64),
    (113, 0.65),
    (121, 0.66),
    (129, 0.67),
    (137, 0.68),
    (145, 0.69),
    (153, 0.70),
    (162, 0.71),
    (170, 0.72),
    (179, 0.73),
    (188, 0.74),
    (197, 0.75),
    (206, 0.76),
    (215, 0.77),
    (225, 0.78),
    (235, 0.79),
    (245, 0.80),
    (256, 0.81),
    (267, 0.82),
    (278, 0.83),
    (290, 0.84),
    (302, 0.85),
    (315, 0.86),
    (328, 0.87),
    (344, 0.88),
    (357, 0.89),
    (374, 0.90),
    (391, 0.91),
    (411, 0.92),
    (432, 0.93),
    (456, 0.94),
    (484, 0.95),
    (517, 0.96),
    (559, 0.97),
    (619, 0.98),
    (735, 0.99),
]

_DP_LIMITS = [x[0] for x in _FIDE_PD_TABLE]
_DP_VALUES = [x[1] for x in _FIDE_PD_TABLE]


def get_expected_score(rating_difference: int, below_2650: bool) -> float:
    """
    Return the expected score.

    W_e = 1 / (1 + 10 ^ (-D / 400))

    Instead of the above formula, a precomputed table is used.
    """
    if rating_difference >= 400 and below_2650:
        rating_difference = 400
    if rating_difference <= -400 and below_2650:
        rating_difference = -400

    sign = 1 if rating_difference >= 0 else -1
    absolute_difference = abs(rating_difference)

    i = bisect_left(_DP_LIMITS, absolute_difference)
    pd = _DP_VALUES[i] if i < len(_DP_VALUES) else 1.0

    if sign > 0:
        return pd
    return 1 - pd
