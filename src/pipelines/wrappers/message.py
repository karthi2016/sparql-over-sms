
class Message:
    """A wrapper for a pipeline-able message"""

    def __init__(self, category, body, sender=None, receiver=None):
        self.category = category
        self.body = body
        self.sender = sender
        self.receiver = receiver

    def __str__(self):
        incoming = self.sender is not None

        if incoming:
            return '{0}: {1} (incoming {2})'.format(self.sender, self.body, self.category)
        else:
            return '{0}: {1} (outgoing {2})'.format(self.receiver, self.body, self.category)
