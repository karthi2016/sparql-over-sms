from datetime import datetime
from peewee import CharField, DateTimeField
from persistence.models import BaseModel


class Configuration(BaseModel):
    """Configuration persistence model"""

    identifier = CharField()
    value = CharField()
    created_timestamp = DateTimeField(default=datetime.now)
    modified_timestamp = DateTimeField(default=datetime.now)
