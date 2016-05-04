from peewee import Model
from persistence import database

class BaseModel(Model):
    """Base class for persistence models"""

    class Meta:
        database = database
