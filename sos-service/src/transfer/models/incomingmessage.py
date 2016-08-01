from transfer.models import BaseMessage


class IncomingMessage(BaseMessage):

    def __init__(self, category, content, sender):
        super().__init__(category, content, sender, '~self')

