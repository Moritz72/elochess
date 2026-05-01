from pathlib import Path
from typing import Generic, TypeVar

from pydantic import BaseModel, TypeAdapter

from tests.helpers.input_models import DwzInputModel, EloInputModel, UscfInputModel

DATA_DIRECTORY = Path(__file__).parent.parent / "data"
T = TypeVar("T", EloInputModel, DwzInputModel, UscfInputModel)


class RatingEntry(BaseModel, Generic[T]):
    """Helper model for samples."""

    input: T
    output: int


def _get_samples(
    filename: str, adapter: TypeAdapter[list[RatingEntry[T]]]
) -> list[RatingEntry[T]]:
    """Return the samples from the given file in the given format."""
    samples_file = DATA_DIRECTORY / filename
    return adapter.validate_json(samples_file.read_text())


def get_elo_samples() -> list[RatingEntry[EloInputModel]]:
    """Return the Elo samples."""
    adapter = TypeAdapter(list[RatingEntry[EloInputModel]])
    return _get_samples("elo_samples.json", adapter)


def get_dwz_samples() -> list[RatingEntry[DwzInputModel]]:
    """Return the DWZ samples."""
    adapter = TypeAdapter(list[RatingEntry[DwzInputModel]])
    return _get_samples("dwz_samples.json", adapter)


def get_uscf_samples() -> list[RatingEntry[UscfInputModel]]:
    """Return the USCF samples."""
    adapter = TypeAdapter(list[RatingEntry[UscfInputModel]])
    return _get_samples("uscf_samples.json", adapter)
