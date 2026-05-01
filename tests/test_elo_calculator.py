from elochess.base import RatingCalculator
from elochess.elo import EloCalculator
from tests.helpers.samples import get_elo_samples


def test_elo_calculator_protocol() -> None:
    """Test whether the protocol is implemented correctly."""
    assert issubclass(EloCalculator, RatingCalculator)


def test_elo_calculator_update_rating() -> None:
    """Test update Elo calculation with some sample data."""
    for sample in get_elo_samples():
        assert sample.output == EloCalculator.update_rating(**sample.input.model_dump())
