from persistence.models import Agent, BaseModel
from peewee import *

class Message(BaseModel):
    """description of class"""

    messageid = IntegerField()
    correlationid = CharField()
    category = IntegerField()
    sender = ForeignKeyField(Agent, related_name='send_messages')
    receiver = ForeignKeyField(Agent, related_name='received_messages')
    
    # flags
    complete = BooleanField()
    processed = BooleanField()
