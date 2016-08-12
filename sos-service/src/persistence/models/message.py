from persistence.models import BaseModel
from peewee import *

class Message(BaseModel):
    """description of class"""

    messageid = IntegerField()
    correlationid = CharField()
    category = IntegerField()
    senderid = IntegerField()
    receiverid = IntegerField()
    
    # flags
    complete = BooleanField()
    processed = BooleanField()
