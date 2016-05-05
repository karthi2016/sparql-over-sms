from peewee import CharField
from persistence.models import BaseModel


class Contact(BaseModel):
    """Contact persistence model"""

    identifier = CharField(unique=True)
    name = CharField()
    phonenumber = CharField(null=True, unique=True)
    ip = CharField(null=True, unique=True)
