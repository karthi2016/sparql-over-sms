from models import Model


class Message(Model):
    """Representas a message"""

    def __init__(self, identifier, position, category, sender, body):
        self.identifier = identifier
        self.position = position
        self.category = category
        self.sender = sender
        self.body = body
