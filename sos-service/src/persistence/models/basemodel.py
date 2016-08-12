from persistence import database
from peewee import *

class BaseModel(Model):
    """description of class"""

    creation_timestamp = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    modification_timestamp = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    
    class Meta:
        database = database

