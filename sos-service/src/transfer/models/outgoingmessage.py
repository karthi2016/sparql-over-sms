from transfer.models import Message

class OutgoingMessage(Message):

    def __init__(self, category, content, receiver):
        super().__init__(category, content, '~self', receiver)

