from pathlib import Path

from pydantic import BaseModel, TypeAdapter

from elochess.base import get_rating
from elochess.elo import EloCalculator, EloInputModel

DATA_DIRECTORY = Path(__file__).parent / "data"


class Entry(BaseModel):
    """Helper model for samples."""

    input: EloInputModel
    output: int


def test_elo_calculator() -> None:
    """Test Elo calculation with some sample data."""
    samples_file = DATA_DIRECTORY / "elo_samples.json"
    samples = TypeAdapter(list[Entry]).validate_json(samples_file.read_text())

    for sample in samples:
        assert sample.output == get_rating(sample.input, EloCalculator)
