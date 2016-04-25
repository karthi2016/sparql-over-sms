from uuid import uuid4


class Message:
    """Represents a incoming or outgoing message"""

    def __init__(self, category, body, sender=None, receiver=None, correlationid=None):
        self.category = category
        self.body = body
        self.sender = sender
        self.receiver = receiver

        # generate a correlation id
        self.correlationid = correlationid if correlationid is not None else uuid4().hex[:4]

    def __str__(self):
        incoming = self.sender is not None

        if incoming:
            return '{0}: {1} (incoming {2})'.format(self.sender, self.body, self.category)
        else:
            return '{0}: {1} (outgoing {2})'.format(self.receiver, self.body, self.category)
