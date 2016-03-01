import uuid

from repositories import MessageRepo


class StoreMessage:
    """Stores a message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        from webapi import app

        messageinfo = {
            'messageid': token.message.correlationid,
            'sender': token.message.sender,
            'body': token.message.body
        }

        messagerepo = MessageRepo(app.config['c_messages'], app.config['f_messages'])
        messagerepo.add_message(messageinfo)

        print('message storing is not yet supported, but here is your message:')
        print(token.message)

