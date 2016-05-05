from peewee import CharField
from persistence.models import BaseModel


class Contact(BaseModel):
    """Contact persistence model"""

    identifier = CharField()
    name = CharField()
    phonenumber = CharField(null=True)
    ip = CharField(null=True)
