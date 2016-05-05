from peewee import CharField, IntegerField, TextField, ForeignKeyField
from persistence.models import BaseModel, Contact


class Message(BaseModel):
    """Message persistence model"""

    identifier = CharField()
    position = IntegerField()
    category = IntegerField()
    sender = ForeignKeyField(Contact, related_name='send_messages', null=True)
    receiver = ForeignKeyField(Contact, related_name='received_messages', null=True)
    body = TextField()

