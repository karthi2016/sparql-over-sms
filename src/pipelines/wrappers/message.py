
class Message:
    """A wrapper for a pipeline-able message"""

    def __init__(self, category, body, sender=None, receiver=None):
        self.category = category
        self.body = body
        self.sender = sender
        self.receiver = receiver
