
class BaseMessage:

    def __init__(self, category, content, sender, receiver, position=0, correlationid=None):
        self.category = category
        self.content = content
        self.sender = sender
        self.reciever = receiver
        self.position = position

        # generate a correlation id
        self.correlationid = correlationid if correlationid is not None else uuid4().hex[:3]

    def __str__(self):
        return '[{0} to {1}] {2} (category: {3})'.format(self.sender, self.reciever, self.content, self.category)
