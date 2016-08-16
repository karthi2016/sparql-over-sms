from persistence.models import BaseModel
from peewee import *

class Agent(BaseModel):
    """description of class"""

    agentid = IntegerField()
    name = CharField(unqiue=True)
    hostname = CharField(unqiue=True)
    phonenumber = CharField(unqiue=True)
    

