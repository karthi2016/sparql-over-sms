from persistence.models import BaseModel
from peewee import *


class Agent(BaseModel):
    """description of class"""

    name = CharField(unique=True, null=True)
    hostname = CharField(unique=True, null=True)
    phonenumber = CharField(unique=True, null=True)
    

