from pathlib import Path

from pydantic import BaseModel, TypeAdapter

from elochess.base import get_rating
from elochess.dwz import DwzCalculator, DwzInputModel

DATA_DIRECTORY = Path(__file__).parent / "data"


class Entry(BaseModel):
    """Helper model for samples."""

    input: DwzInputModel
    output: int


def test_dwz_calculator() -> None:
    """Test DWZ calculation with some sample data."""
    samples_file = DATA_DIRECTORY / "dwz_samples.json"
    samples = TypeAdapter(list[Entry]).validate_json(samples_file.read_text())

    for sample in samples:
        assert sample.output == get_rating(sample.input, DwzCalculator)
