from persistence.models import BaseModel
from peewee import *


class Agent(BaseModel):
    """description of class"""

    name = CharField(unique=True, null=True)
    hostname = CharField(unique=True, null=True)
    phonenumber = CharField(unique=True, null=True)

    def as_dict(self):
        c_timestamp = self.creation_timestamp.isoformat()
        m_timestamp = self.modification_timestamp.isoformat()

        return {
            'id': self.get_id(),
            'name': self.name,
            'hostname': self.hostname,
            'phonenumber': self.phonenumber,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }
