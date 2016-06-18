
class Message:

    def __init__(self, category, content, sender, receiver):
        self.category = category
        self.content = content
        self.sender = sender
        self.reciever = receiver

    def __str__(self):
        return '[{0} to {1}] {2} (category: {3})'.format(self.sender, self.reciever, self.content, self.category)


