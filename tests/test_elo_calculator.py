from elochess.base import update_rating
from elochess.elo import EloCalculator
from helpers.samples import get_elo_samples


def test_elo_calculator() -> None:
    """Test Elo calculation with some sample data."""
    for sample in get_elo_samples():
        assert sample.output == update_rating(sample.input, EloCalculator)
