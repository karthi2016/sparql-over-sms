from peewee import IntegerField, ForeignKeyField
from persistence.models import BaseModel, PipelineReport


class PipelineTaskLog(BaseModel):
    """Pipeline task log persistence model"""

    identifier = IntegerField()
    report = ForeignKeyField(PipelineReport, related_name='task_logs')

