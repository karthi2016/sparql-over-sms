from persistence.models import Agent, BaseModel
from peewee import *


class Message(BaseModel):
    """description of class"""

    correlationid = CharField()
    category = IntegerField()
    body = CharField(null=True)
    sender = ForeignKeyField(Agent, related_name='send_messages')
    receiver = ForeignKeyField(Agent, related_name='received_messages')
    
    # flags
    complete = BooleanField(default=False)
    processed = BooleanField(default=False)

    # computed
    def get_body(self):
        if self.body is not None:
            return self.body

        if not self.complete:
            return None

        messageparts = sorted(self.parts, key=lambda x: x.position)
        body = ''.join([part.body for part in messageparts])
        return body

    def as_dict(self):
        return {
            'id': self.correlationid,
            'sender': self.sender.name,
            'reciever': self.receiver.name,
            'category': self.category,
            'body': self.get_body()
        }
