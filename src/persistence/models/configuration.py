from peewee import CharField
from persistence.models import BaseModel


class Configuration(BaseModel):
    """Configuration persistence model"""

    identifier = CharField()
    value = CharField()
    scope = CharField(null=True)
