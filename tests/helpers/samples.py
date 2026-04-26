from pathlib import Path

from pydantic import BaseModel, TypeAdapter

from elochess.dwz import DwzInputModel
from elochess.elo import EloInputModel

DATA_DIRECTORY = Path(__file__).parent.parent / "data"


class EloEntry(BaseModel):
    """Helper model for Elo samples."""

    input: EloInputModel
    output: int


class DwzEntry(BaseModel):
    """Helper model for DWZ samples."""

    input: DwzInputModel
    output: int


def get_elo_samples() -> list[EloEntry]:
    """Return the Elo samples."""
    samples_file = DATA_DIRECTORY / "elo_samples.json"
    return TypeAdapter(list[EloEntry]).validate_json(samples_file.read_text())


def get_dwz_samples() -> list[DwzEntry]:
    """Return the DWZ samples."""
    samples_file = DATA_DIRECTORY / "dwz_samples.json"
    return TypeAdapter(list[DwzEntry]).validate_json(samples_file.read_text())
