import repositories


class StoreMessage:
    """Stores a message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        from webapi import app

        messagerepo = app.injector.get(repositories.MessageRepo)
        messageinfo = {
            'messageid': '{0}-{1}'.format(token.message.correlationid, token.message.category),
            'sender': token.message.sender,
            'body': token.message.body
        }

        messagerepo.add_message(messageinfo)

