from elochess.base import RatingCalculator
from elochess.uscf import UscfCalculator
from tests.helpers.samples import get_uscf_samples


def test_elo_calculator_protocol() -> None:
    """Test whether the protocol is implemented correctly."""
    assert issubclass(UscfCalculator, RatingCalculator)


def test_elo_calculator_update_rating() -> None:
    """Test update USCF rating calculation with some sample data."""
    for sample in get_uscf_samples():
        assert sample.output == UscfCalculator.update_rating(
            **sample.input.model_dump()
        )
