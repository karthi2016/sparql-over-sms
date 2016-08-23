from transfer.models import BaseMessage

class OutgoingMessage(BaseMessage):

    def __init__(self, category, content, receiver):
        super().__init__(category, content, '~self', receiver)

