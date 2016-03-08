import repositories


class StoreMessage:
    """Stores a message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        from webapi import app

        messagerepo = repositories.MessageRepo(app.config['c_messages'], app.config['f_messages'])
        messageinfo = {
            'messageid': '{0}-{1}'.format(token.message.correlationid, token.message.category),
            'sender': token.message.sender,
            'body': token.message.body
        }

        messagerepo.add_message(messageinfo)

