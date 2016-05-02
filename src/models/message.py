
class Message:
    """Base message model"""

    def __init__(self, identifier, position, category, sender, body):
        self.identifier = identifier
        self.position = position
        self.category = category
        self.sender = sender
        self.body = body
