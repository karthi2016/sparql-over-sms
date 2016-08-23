from persistence.models import Agent, BaseModel
from peewee import *


class Message(BaseModel):
    """description of class"""

    correlationid = CharField()
    category = IntegerField()
    sender = ForeignKeyField(Agent, related_name='send_messages')
    receiver = ForeignKeyField(Agent, related_name='received_messages')
    
    # flags
    complete = BooleanField(default=False)
    processed = BooleanField(default=False)

    # computed
    def get_body(self):
        if not self.complete:
            return None

        messageparts = sorted(self.parts, key=lambda x: x.position)
        body = ''.join([part.body for part in messageparts])
        return body
