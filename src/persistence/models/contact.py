from datetime import datetime
from peewee import CharField, DateTimeField
from persistence import BaseModel


class Contact(BaseModel):
    """Contact persistence model"""

    identifier = CharField()
    name = CharField()
    phonenumber = CharField()
    ip = CharField()
    created_timestamp = DateTimeField(default=datetime.now)
    modified_timestamp = DateTimeField(default=datetime.now)
