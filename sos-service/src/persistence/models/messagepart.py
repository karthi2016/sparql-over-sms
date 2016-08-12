from persistence.models import BaseModel, Message
from peewee import *


class MessagePart(BaseModel):
    """description of class"""

    message = ForeignKeyField(Message, related_name='parts')
    content = CharField()
    position = IntegerField()
