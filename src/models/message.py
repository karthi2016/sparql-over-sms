
class Message:
    """Base message model"""

    def __init__(self, identifier, position, category, sender, receiver, body):
        self.identifier = identifier
        self.position = position
        self.category = category
        self.sender = sender
        self.receiver = receiver
        self.body = body
