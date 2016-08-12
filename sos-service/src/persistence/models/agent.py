from persistence.models import BaseModel
from peewee import *

class Agent(BaseModel):
    """description of class"""

    agentid = IntegerField()
    name = CharField()
    hostname = CharField()
    phonenumber = CharField()
    

