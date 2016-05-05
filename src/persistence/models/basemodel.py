from datetime import datetime
from peewee import Model, DateTimeField
from persistence import database
from playhouse.shortcuts import model_to_dict

class BaseModel(Model):
    """Base class for persistence models"""

    created_timestamp = DateTimeField(default=datetime.now)
    modified_timestamp = DateTimeField(default=datetime.now)

    def as_dict(self):
        return model_to_dict(self)

    class Meta:
        database = database
