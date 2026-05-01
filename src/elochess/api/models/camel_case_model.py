from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelCaseModel(BaseModel):
    """Base model for requests and responses."""

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
