
class MessageRepo:
    """Repository for retreiving and restoring messages"""

    def __init__(self, messagestore, filepath):
        self.messagestore = messagestore
        self.filepath = filepath

    def get_messages(self):
        messageids = self.messagestore.sections()
        return [self.get_message(messageid) for messageid in messageids]

    def get_message(self, messageid):
        messageinfo = self.messagestore[messageid]

        message = {k: messageinfo[k] for k in messageinfo.keys()}
        message['messageid'] = messageid

        return message

    def add_message(self, messageinfo):
        messageid = messageinfo['messageid']

        self.messagestore.add_section(messageid)
        self.messagestore.set(messageid, 'sender', messageinfo['sender'])
        self.messagestore.set(messageid, 'body', messageinfo['body'])

        # persist changes
        self.save()

    def update_message(self, messageid, messageinfo):
        message = self.messagestore[messageid]
        message['sender'] = messageinfo['sender']
        message['body'] = messageinfo['body']

        # persist changes
        self.save()

    def remove_message(self, messageid):
        self.messagestore.remove_section(messageid)

        # persist changes
        self.save()

    def save(self):
        with open(self.filepath, 'w') as file:
            self.messagestore.write(file)



