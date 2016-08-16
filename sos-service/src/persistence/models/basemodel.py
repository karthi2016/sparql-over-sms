from datetime import datetime
from persistence import database
from peewee import *

class BaseModel(Model):
    """description of class"""

    creation_timestamp = DateTimeField(default=datetime.now)
    modification_timestamp = DateTimeField(default=datetime.now)
    
    class Meta:
        database = database

