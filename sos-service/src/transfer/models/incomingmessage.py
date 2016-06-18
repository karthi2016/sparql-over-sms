from transfer.models import Message


class IncomingMessage(Message):

    def __init__(self, category, content, sender):
        super().__init__(category, content, sender, '~self')

