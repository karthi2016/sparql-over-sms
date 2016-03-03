import uuid

from repositories import MessageRepo


class StoreMessage:
    """Stores a message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        print('message storing is not yet supported, but here is your message:')
        print(token.message)

