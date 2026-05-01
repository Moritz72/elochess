from elochess.base import RatingCalculator
from elochess.dwz import DwzCalculator
from tests.helpers.samples import get_dwz_samples


def test_dwz_calculator_protocol() -> None:
    """Test whether the protocol is implemented correctly."""
    assert issubclass(DwzCalculator, RatingCalculator)


def test_dwz_calculator_update_rating() -> None:
    """Test update DWZ calculation with some sample data."""
    for sample in get_dwz_samples():
        assert sample.output == DwzCalculator.update_rating(**sample.input.model_dump())
