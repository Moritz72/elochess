from typing import Annotated

from pydantic import Field

from elochess.api.models import CamelCaseModel


class UpdateResponse(CamelCaseModel):
    """Model for update responses."""

    rating: Annotated[int, Field(ge=0)] = Field(
        ...,
        title="Rating",
        description="Your updated rating after calculation.",
        examples=[1510],
    )
