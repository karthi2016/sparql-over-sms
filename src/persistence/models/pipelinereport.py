from peewee import IntegerField
from persistence.models import BaseModel


class PipelineReport(BaseModel):
    """Pipeline report persistence model"""

    identifier = IntegerField()
