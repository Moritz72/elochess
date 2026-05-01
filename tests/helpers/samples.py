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
    filename: str, entry_type: type[RatingEntry[T]]
) -> list[RatingEntry[T]]:
    """Return the samples from the given file in the given format."""
    samples_file = DATA_DIRECTORY / filename
    adapter = TypeAdapter(list[entry_type])  # type: ignore [valid-type]
    return adapter.validate_json(samples_file.read_text())


def get_elo_samples() -> list[RatingEntry[EloInputModel]]:
    """Return the Elo samples."""
    return _get_samples("elo_samples.json", RatingEntry[EloInputModel])


def get_dwz_samples() -> list[RatingEntry[DwzInputModel]]:
    """Return the DWZ samples."""
    return _get_samples("dwz_samples.json", RatingEntry[DwzInputModel])


def get_uscf_samples() -> list[RatingEntry[UscfInputModel]]:
    """Return the USCF samples."""
    return _get_samples("uscf_samples.json", RatingEntry[UscfInputModel])
