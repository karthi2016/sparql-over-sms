from datetime import datetime
from peewee import Model, DateTimeField
from persistence import database

class BaseModel(Model):
    """Base class for persistence models"""

    created_timestamp = DateTimeField(default=datetime.now)
    modified_timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = database
