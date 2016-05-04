from datetime import datetime
from peewee import CharField, IntegerField, TextField, DateTimeField
from persistence import BaseModel


class Message(BaseModel):
    """Message persistence model"""

    identifier = CharField()
    position = IntegerField()
    category = IntegerField()
    sender = CharField()
    receiver = CharField()
    body = TextField()
    created_timestamp = DateTimeField(default=datetime.now)
