from elochess.base import update_rating
from elochess.dwz import DwzCalculator
from helpers.samples import get_dwz_samples


def test_dwz_calculator() -> None:
    """Test DWZ calculation with some sample data."""
    for sample in get_dwz_samples():
        assert sample.output == update_rating(sample.input, DwzCalculator)
